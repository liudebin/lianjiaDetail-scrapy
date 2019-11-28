# coding=utf-8
import scrapy

from msysqlDb import mysqlHadler

baseUrl = 'https://sh.lianjia.com'


def getList(a):
    print a
    if a:
        if a[0].extract().isdigit():
            return a[0].extract()
        return a[0].extract().strip()
    else:
        return ""


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'lianjiaDetail'
    dbObject = mysqlHadler().dbHandle()
    cursor = dbObject.cursor()
    cursor.execute("USE test")
    # sql = "INSERT INTO articles(author,title,times,url,admire,likes) VALUES(%s,%s,%s,%s,%s,%s)"
    sql = "select link from rent_detail_lianjia where community_code is null ;"
    cursor.execute(sql)
    results = cursor.fetchall()
    box = []
    for row in results:
        box.append(row[0])
    # start_urls = [
    #     'https://sh.lianjia.com/zufang/SH2135972204813492224.html'
    # ]
    start_urls = box

    def parse(self, response):
        # print response
        subtitile = response.xpath('//div[@class="content__subtitle"]')[0].xpath('string(.)').extract()[0].strip()
        upload_date = subtitile[12:22]
        code = response.xpath('//div[@class="content__subtitle"]')[0].xpath(".//i[position()=2]/text()")[0].extract()
        house_code = code[5:]

        content__aside = response.xpath('.//div[@class="content__aside fr"]')[0]
        price_content = content__aside.xpath('.//div[@class="content__aside--title"]')[0].xpath('string(.)').extract()
        price = int(content__aside.xpath('.//div[@class="content__aside--title"]/span/text()')[0].extract())

        tags = ""
        for quote in content__aside.xpath('.//p[@class="content__aside--tags"]/i'):
            tags = tags + "/" + quote.xpath('string(.)').extract()[0]

        content__article__table = \
            content__aside.xpath('//ul[@class="content__aside__list"]')[0]

        house_type_content_span = content__article__table.xpath('.//li[position()=2]/span')[0].xpath('string(.)').extract_first()
        house_type_content = content__article__table.xpath('.//li[position()=2]')[0].xpath('string(.)').extract_first()
        house_type_content1 = house_type_content.replace(house_type_content_span, "")
        house_type = house_type_content1.split()[0]

        square = house_type_content1.split()[1]

        direct = content__article__table.xpath('.//li[position()=3]')[0].xpath('string(.)').extract()

        base_info = response.xpath('.//div[@class="content__article__info"]')[0]
        base_info_str = ""
        for quote in base_info.xpath('.//ul/li[@class="fl oneline"]'):
            base_info_str = base_info_str + quote.xpath("string(.)").extract()[0] + "\n"

        houseComment = response.xpath('.//p[@data-el="houseComment"]/attribute::data-desc')
        house_comment = ""
        if houseComment:
            house_comment = houseComment[0].extract()

        sub_way = ""
        for quote in response.xpath('.//div[@class="content__article__info4"]/ul/li'):
            sub_way = sub_way + quote.xpath('.//span[position()=1]/text()')[0].extract()
            sub_way = sub_way + "- " + quote.xpath('.//span[position()=2]/text()')[0].extract() + "\n"

        community_link = baseUrl + response.xpath('//div[@class="bread__nav w1150 bread__nav--bottom"]/h1/a/@href')[0].extract()
        community_code = response.xpath('//div[@class="bread__nav w1150 bread__nav--bottom"]/h1/a/@href')[0].extract()[8:-1]
        community = response.xpath('//div[@class="bread__nav w1150 bread__nav--bottom"]/h1/a/text()')[0].extract()[:-2]

        yield {
            'house_code': house_code,
            'price_content': price_content,
            'tags': tags,
            'house_type': house_type,
            'sub_way': sub_way,
            'house_comment': house_comment,
            'upload_date': upload_date,
            'square': square,
            'direct': direct,
            'base_info_str': base_info_str,
            'community_code': community_code,
            'community': community,
            'community_link': community_link
        }

    # next_page_url = response.css("li.next > a::attr(href)").extract_first()
    # if next_page_url is not None:
    #     yield scrapy.Request(response.urljoin(next_page_url))
