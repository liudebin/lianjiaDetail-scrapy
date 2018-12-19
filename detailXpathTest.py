# coding=utf-8
from lxml import etree

def getList(a):
    # print a
    if a:
        if a[0].isdigit():
            return a[0]
        return a[0].strip().encode('utf8')
    else:
        return ""


wb_data = """


<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta http-equiv="Cache-Control" content="no-transform" />
  <meta http-equiv="Cache-Control" content="no-siteapp" />
  <meta http-equiv="Content-language" content="zh-CN" />
  <meta name="format-detection" content="telephone=no" />
  <meta name="applicable-device" content="pc">
	<meta name="description" content="贝壳上海租房网,提供三林苑 1室1厅 4500元出租房源信息,此房源位于上海浦东三林的三林苑,1室66㎡4500元.找租房房源,就来上海贝壳租房!">
	<meta name="keywords" content="三林苑 1室1厅 4500元,三林苑租房信息,上海浦东三林房屋出租">
	<meta http-equiv="Cache-Control" content="no-transform " />
	<title>三林苑 1室1厅 4500元-三林苑租房信息-上海三林苑三林房屋出租【上海贝壳租房】</title>
	<link href="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/img/favicon.ico?_v=20181213213506e97" type="image/x-icon" rel="icon">
		<link rel="stylesheet" href="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/common/css/common.css?_v=20181213213506e97">
	  <script>
    var g_conf = {};
  </script>
    <link rel="stylesheet" href="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/page/detail/index.css?_v=20181213213506e97">
    <link href='//s1.ljcdn.com/feroot/pc/asset/lianjiaIM/css/lianjiaim.css?v=15212312340214' property='stylesheet' rel="stylesheet">
  <style>
    .browser__low {
      height: 100%;
      overflow: hidden;
    }
    .browser__low--wrapper,
    .browser__low--inner {
      display: none;
    }
    .browser__low .browser__low--wrapper {
      position: absolute;
      left: 0;
      right: 0;
      top: 0;
      bottom: 0;
      z-index: 199999;
      background: #000;
      opacity: 0.5;
      filter: alpha(opacity=50);
      display: block;
    }
    .browser__low .browser__low--inner {
      background: #fff;
      position: absolute;
      left: 50%;
      top: 50%;
      z-index: 19999999;
      width: 360px;
      height: 100px;
      margin-top: -90px;
      margin-left: -200px;
      padding: 40px 20px;
      display: block;
    }
    .browser__low .browser__low--inner p {
      font-size: 20px;
      padding-bottom: 40px;
    }
    .browser__low .browser__low--inner a {
      display: inline-block;
      color: #fff;
      background: #2ab78e;
      padding: 10px 6px;
    }
  </style>
  </head>

<body>
<div class="browser__low--wrapper"></div>
<div class="browser__low--inner">
<p>您的浏览器版本过低，请升级：</p>
<a href="https://www.baidu.com/s?wd=chrome" target="_blank">谷歌 Chrome浏览器</a>
</div>

<script>
;;(function() {
  if(!([].forEach)) {
    document.body.className += ' browser__low';
  }
})();
</script>
<div class="wrapper">
   <!--<link href="--><?//=APP_MODE === 'prod' ? '//s1.ljcdn.com/feroot/pc/asset/lianjiaIM/css/lianjiaim.css?v=15212312340214' : '//s1.pc56.lj-web-56.lianjia.com/feroot/pc/asset/lianjiaIM/css/lianjiaim.css'?><!--" property='stylesheet' rel="stylesheet">-->


<div>

  <!-- 引入公用的头、导航、搜索栏 -->
  <div class="header ">
  <ul class="header__wrapper w1150 clear typeUserInfo" id="top">
                      <li class="header__item fl "><a href="//sh.lianjia.com" target="_blank">首页</a></li>
                        <li class="header__item fl "><a href="//sh.lianjia.com/ershoufang/" target="_blank">二手房</a></li>
                        <li class="header__item fl "><a href="//sh.fang.lianjia.com/loupan/" target="_blank">新房</a></li>
                        <li class="header__item fl cur"><a href="/zufang/" target="_blank">租房</a></li>
                        <li class="header__item fl "><a href="//us.lianjia.com" target="_blank">海外</a></li>
                        <li class="header__item fl "><a href="//sh.lianjia.com/xiaoqu/" target="_blank">小区</a></li>
                        <li class="header__item fl "><a href="//sh.lianjia.com/jingjiren/" target="_blank">经纪人</a></li>
                        <li class="header__item fl "><a href="//sh.lianjia.com/wenda/" target="_blank">指南</a></li>
                        <li class="header__item fl "><a href="//sh.lianjia.com/tool.html" target="_blank">工具</a></li>
                        <li class="header__item fl "><a href="//sh.lianjia.com/yezhu/" target="_blank">发布房源</a></li>
                  <li class="header__aside fr pointer typeShowUser" data-el="login" data-event_id="10794" data-event_action="target=login">
      <span data-el="login_box">
        <span data-el="btn_login" data-id="dialog_tel" class="btn-login">登录</span>/<span class="btn-resgiter" data-el="register" data-id="dialog_reg">注册</span>
      </span>
    </li>
    <li class="top__aside fr hide" data-el="user_box">
      <a href="" data-el="userName"></a>
      <a data-el="logout_btn">退出</a>
    </li>

  </ul>

</div>
  <div class="search__area">
  <div class="beike__nav">
  <a class="beike__nav--logo" href="/zufang/"></a>
  
  <ul class="beike__nav--tab">
    <li>
      <a class="cur" href="/zufang/">首页</a>
    </li>

    <li>      
      <a class="" href="/zufang/rt200600000001/">整租</a>
    </li>

    <li><a class="" href="/zufang/rt200600000002/">合租</a></li>
            <li class="beike__nav--code">
      下载APP
      <div class="nav-list beike__nav--qrcode">
        <img src="https://ajax.api.lianjia.com/qr/getDownloadQr?location=nav&amp;ljweb_channel_key=zufang_search" alt="下载贝壳APP" class="QRcode-img">
      </div> 
    </li>
    
  </ul>
</div>  <div class="search w1150" id="search">
  <!-- <a class="search__logo" href="/"></a> -->
  <div class="search__wrap">
    <input class="search__input fl" type="text" data-el="input" placeholder="请输入区域、商圈或小区名开始找房" autocomplete="off" value="" data-value="">
    <span class="search__button fl" data-el="button"></span>
  </div>

</div>  </div>

  <!-- 房源有效时 -->
      <div class="content clear w1150">

      <!-- 房源标题 -->
      <p class="content__title">三林苑 1室1厅 4500元</p>

      <!-- 房源副标题 -->
      <div class="content__subtitle">
          <i class="hide">4人浏览 </i>房源上架时间 2018-10-08          <i class="house_code">房源编号：SH2098450264460894208</i>
          <!-- 发布人、发布机构入口 -->
                    <span class="content-right" data-el="showReportBox" data-event_id="10804" data-event_action="house_code=SH2098450264460894208">举报与反馈</span>
      </div>

      <!-- 房源左侧内容 -->
      <div class="content__article fl">

        <!-- 房源图片轮播图 -->
        <div class="content__article__slide" id="mySwipe">

          <!-- 房源大图 -->
          <ul class="content__article__slide__wrapper">
                                  <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="三林苑 1室1厅 4500元" src="https://image1.ljcdn.com/310000-inspection/test-499bd9bc-9e87-4ffb-9775-1cd2b102992e.png.780x439.jpg" data-el="lazy-img" data-src="https://image1.ljcdn.com/310000-inspection/test-499bd9bc-9e87-4ffb-9775-1cd2b102992e.png.780x439.jpg" />
                          </div>
                        <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="三林苑 1室1厅 4500元" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/780-439.png?_v=20181213213506e97" data-el="lazy-img" data-src="https://image1.ljcdn.com/310000-inspection/test-f3aa0f84-a1a2-4431-8ba3-07f09a2a2086.png.780x439.jpg" />
                          </div>
                        <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="三林苑 1室1厅 4500元" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/780-439.png?_v=20181213213506e97" data-el="lazy-img" data-src="https://image1.ljcdn.com/hdic-frame/test-cd9890c7-3227-4083-92b0-5623adc0cfef.png.780x439.jpg" />
                          </div>
                        <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="三林苑 1室1厅 4500元" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/780-439.png?_v=20181213213506e97" data-el="lazy-img" data-src="https://image1.ljcdn.com/310000-inspection/test-55e60db4-9db0-4e14-b9e3-fa22d4cd2e39.png.780x439.jpg" />
                          </div>
                        <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="三林苑 1室1厅 4500元" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/780-439.png?_v=20181213213506e97" data-el="lazy-img" data-src="https://image1.ljcdn.com/310000-inspection/test-d2bb42a3-22f5-46ad-883c-a9378e482cd3.png.780x439.jpg" />
                          </div>
                        <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="三林苑 1室1厅 4500元" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/780-439.png?_v=20181213213506e97" data-el="lazy-img" data-src="https://image1.ljcdn.com/310000-inspection/test-2d8bab61-7f24-4ea9-9f9c-6da083c82841.png.780x439.jpg" />
                          </div>
                        <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="三林苑 1室1厅 4500元" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/780-439.png?_v=20181213213506e97" data-el="lazy-img" data-src="https://image1.ljcdn.com/310000-inspection/test-cf83ca51-94b1-4e3b-afca-272bb516e29c.png.780x439.jpg" />
                          </div>
                                </ul>

          <!-- 房源缩略图 -->
          <div class="content__thumb--box">
            <ul class="content__article__slide--small content__article__slide_dot" data-el="prefix" id="prefix">
                                                <li class="active" data-index="0">
                    <img src="https://image1.ljcdn.com/310000-inspection/test-499bd9bc-9e87-4ffb-9775-1cd2b102992e.png.126x86.jpg">
                  </li>
                                  <li class="" data-index="1">
                    <img src="https://image1.ljcdn.com/310000-inspection/test-f3aa0f84-a1a2-4431-8ba3-07f09a2a2086.png.126x86.jpg">
                  </li>
                                  <li class="" data-index="2">
                    <img src="https://image1.ljcdn.com/hdic-frame/test-cd9890c7-3227-4083-92b0-5623adc0cfef.png.126x86.jpg">
                  </li>
                                  <li class="" data-index="3">
                    <img src="https://image1.ljcdn.com/310000-inspection/test-55e60db4-9db0-4e14-b9e3-fa22d4cd2e39.png.126x86.jpg">
                  </li>
                                  <li class="" data-index="4">
                    <img src="https://image1.ljcdn.com/310000-inspection/test-d2bb42a3-22f5-46ad-883c-a9378e482cd3.png.126x86.jpg">
                  </li>
                                  <li class="" data-index="5">
                    <img src="https://image1.ljcdn.com/310000-inspection/test-2d8bab61-7f24-4ea9-9f9c-6da083c82841.png.126x86.jpg">
                  </li>
                                  <li class="" data-index="6">
                    <img src="https://image1.ljcdn.com/310000-inspection/test-cf83ca51-94b1-4e3b-afca-272bb516e29c.png.126x86.jpg">
                  </li>
                                          </ul>
          </div>

          <!-- 图片切换按钮 -->
          <span class="content__article__slide--prev" data-el="prev"></span>
          <span class="content__article__slide--next" data-el="next"></span>

          <!-- 房源关注入口及hover浮层 -->
          <span class="content__article__slide--tips hide" data-el="getApp">关注的房源请在链家APP中查看</span>
          <span class="content__article__slide--button" data-type="house" data-id="SH2098450264460894208" data-el="checkWatch"><i class="heart"></i><span>关注房源</span></span>
        </div>

        <!-- 房源基本信息 -->
        <div class="content__article__info">
          <h3 id="info">房屋信息</h3>
          <ul>
            <li class="fl oneline">基本信息</li>
                          <li class="fl oneline">发布：2个月前</li>
                                        <li class="fl oneline">入住：随时入住</li>
                              <li class="fl oneline">&nbsp;</li>
                                        <li class="fl oneline">租期：暂无数据</li>
                                        <li class="fl oneline">看房：需提前预约</li>
                              <li class="fl oneline">&nbsp;</li>
                                        <li class="fl oneline">楼层：中楼层/6层</li>
                                        <li class="fl oneline">电梯：无</li>
                              <li class="fl oneline">&nbsp;</li>
                                        <li class="fl oneline">车位：暂无数据</li>
                                        <li class="fl oneline">用水：民水</li>
                              <li class="fl oneline">&nbsp;</li>
                                        <li class="fl oneline">用电：民电</li>
                                        <li class="fl oneline">燃气：有</li>
                              <li class="fl oneline">&nbsp;</li>
                                        <li class="fl oneline">采暖：暂无数据</li>
                                    </ul>
        </div>

        <!-- 房源分割标识线，js里用到，勿删 -->
        <div class="info__line line"></div>

        <!-- 配套设施列表 -->
        <ul class="content__article__info2">
          <li class="fl oneline">配套设施</li>
                      <li class="fl oneline television_no "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/8705ff7fb13cf9fabdc2aed4ca0052c0.1524906061250_49197f72-e296-4eb7-b9c0-78e443675cfa);"></i>电视</li>
                      <li class="fl oneline refrigerator_no "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/97908a9f37935c43d110762d1ad996f2.1524905937598_92b7500a-1c6c-4569-91b2-9c32cb27c295);"></i>冰箱</li>
                      <li class="fl oneline washing_machine_no "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/ff28f17d82337aaa2cbdcd44ad1bda4c.1524906571057_0c1a2541-7e92-4557-92d0-7588846918d1);"></i>洗衣机</li>
                      <li class="fl oneline air_conditioner_no "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/01018daa3c64d5249dc6b5f90b14ecb7.1524906116550_8f0a3e47-0dd1-4888-9f67-31ff52842545);"></i>空调</li>
                      <li class="fl oneline water_heater_no "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/730ed905f7575d8752520fa858428b06.1524906267640_ef46af19-b1b0-4fe1-8a2d-5d663c000442);"></i>热水器</li>
                      <li class="fl oneline bed_no "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/ca13bd1b4ecd7104f7df71e40643291a.1524905997899_d5dd7ec6-b9ca-442e-9d3b-c9c85a841076);"></i>床</li>
                      <li class="fl oneline heating_no "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/ce93a6cec4a601367fbd8f5d8760ecc8.1525926673137_fa39878e-9033-4494-9912-13c176c060ca);"></i>暖气</li>
                      <li class="fl oneline wifi_no "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/c2e2d43d75f2158cf08fae1c4d2f433f.1524906202377_004ba35e-ce03-480f-bb0c-0acd46ebb1ce);"></i>宽带</li>
                      <li class="fl oneline wardrobe_no "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/da33d5ca764547cc5ed574d10868f2e5.1524906607735_85ecfcc4-6a05-454d-84a5-63e92bec1e83);"></i>衣柜</li>
                      <li class="fl oneline natural_gas_no "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/f0e67d57b15b3c47c4ee77847eef5b97.1524906489358_60a401ee-ee85-42eb-aaf3-5caaa5efc0a6);"></i>天然气</li>
                  </ul>

        <!-- 房源描述数据 -->
                
        <!-- 描述展示 -->
        
      </div>

      <!-- 右侧黄金展位 -->
      <div class="content__aside fr" id="aside">

        <!-- 租金及支付方式 -->
        <p class="content__aside--title"><span>4500</span>元/月 </p>
        
        <!-- 房源标签列表 -->
        <p class="content__aside--tags">
                  <i class="content__item__tag--is_subway_house" data-class="is_subway_house">近地铁</i>
                  <i class="content__item__tag--is_key" data-class="is_key">随时看房</i>
                </p>

        <!-- 房源户型、朝向、面积、租赁方式 -->
        <ul class="content__aside__list">
          <p class="content__article__table">
            <span><i class="house"></i>租赁方式未知</span>
            <span><i class="typ"></i>1室1厅1卫</span>
            <span><i class="area"></i>66㎡</span>
            <span><i class="orient"></i>朝南</span>
          </p>
        </ul>
        <!-- 经纪人信息，目前只展示一条信息 -->
                <ul class="content__aside__list">
                    <!-- 判断数据源 是否展示icon等信息-->
                                                        <li>
                  <!--im参数配置2. port 参数中判断 “lianjia / qita” 时，判断条件：1）若UCID为100开头，则传值 “lianjia” 2) 若UCID不为100开头，则传值 “qita”-->
                                    <span data-el="updateAvatar" data-houseCode="SH2098450264460894208" class="content__aside__list--icon"></span>
                  <div class="content__aside__list--title oneline">
                    <span class="contact_name" data-el="updateName" data-houseCode="SH2098450264460894208" title="韩云龙"></span>
                      <!-- 判断信息卡的房源，是否显示icon-->
                      <div class="duty-pic" data-el="updatePic" data-show_booth="1">
                        <!-- 显示icon-->
                        <span class="duty-icon" data-el="dutyCard"></span>
                        <!-- hover时显示经纪人卡片-->
                        <div class="duty-pop" data-el="picList">
                        </div>
                      </div>

                                              <span class="contact__im" data-el="callIM" data-im_id="1000000022276082" data-info="1000000022276082" data-port="pc_lianjia_zufangplat_detail_house" data-brand="200301001000" data-id="SH2098450264460894208" data-type="house" data-title="[房源]1室1厅1卫，南，66m²，4500元"></span>
                                        </div>
                  <p class="content__aside__list--subtitle oneline">
                                          链家                                        经纪人                  </p> 
                                  <p class="content__aside__list--bottom oneline" data-el="updatePhone" data-houseCode="SH2098450264460894208">10109666</p>
                </li>
                                            </ul>
              </div>
    </div>


    <!-- 地图及推荐房源 -->
    <div class="content--flat w1150" id="mapDetail">

      <!-- 推荐经纪人 -->
            <!-- 地址信息 -->
      <div class="content__article__info4" id="around">
        <h3>地址和交通</h3>
        <ul>
                  <li>
            距离
            <span>11号线(迪士尼-花桥) - 三林东</span>
            <span>474m</span>
          </li>
                </ul>
      </div>
      <!-- 地图插件显示 -->
      <div class="content__map">
        <div id="map" class="content__map--container">
        </div>
      </div>

      <!-- 小区成交列表，最多显示3条 -->
            <div class="content__table" id="deal">
        <h3>小区最新成交</h3>
        <div class="table">
          <div class="tr">
            <div class="th">成交日期</div>
            <div class="th">居室</div>
            <div class="th">面积</div>
            <div class="th">租赁方式</div>
            <div class="th">出租价格</div>
            <div class="th">数据来源</div>
          </div>
                      <div class="tr">
              <div class="td">2018-03-21</div>
              <div class="td">2室1厅1卫</div>
              <div class="td">72㎡</div>
              <div class="td">整租</div>
              <div class="td">4660/月</div>
              <div class="td">自如</div>
            </div>
                      <div class="tr">
              <div class="td">2018-03-19</div>
              <div class="td">1室1厅1卫</div>
              <div class="td">20㎡</div>
              <div class="td">整租</div>
              <div class="td">2800/月</div>
              <div class="td">链家</div>
            </div>
                      <div class="tr">
              <div class="td">2018-03-07</div>
              <div class="td">3室1厅1卫</div>
              <div class="td">7㎡</div>
              <div class="td">合租</div>
              <div class="td">1830/月</div>
              <div class="td">自如</div>
            </div>
                  </div>
      </div>
      
      <!-- 推荐房源分割线 -->
      <p style="height: 1px;" id="recom"></p>
      
      <!-- 同小区在租房源 -->
              <div class="bottom w1150" style="">
  <div class="bottom__list">

    
        <p class="bottom__list--title">同小区在租房源</p>
    
    <div class="bottom__list--wrapper">
          <div class="bottom__list--item">
        <a href="/zufang/SH2138234578861826048.html" target="_blank" data-event_id="10805" data-event_action="house_code=SH2138234578861826048&position=1"><img alt="/zufang/SH2138234578861826048.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=20181213213506e97" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/rent-user-avatar/fdab7ba1-5bff-44a1-a5a2-ef90d7d6b65d.250x182.jpg"></a>
        <p class="bottom__list--item__des">
          <span>
            <a href="/zufang/pudong" target="_blank">浦东</a> 
            - 
            <a href="/zufang/sanlin" target="_blank">三林</a>  
            三林苑          </span>
          <span class="bottom__list--item--hl fr">4800元/月</span> 
        </p>
        <p class="bottom__list--item__btm">
          2室1厅1卫 7㎡
        </p>
      </div>
          <div class="bottom__list--item">
        <a href="/zufang/SH2142415753440673792.html" target="_blank" data-event_id="10805" data-event_action="house_code=SH2142415753440673792&position=2"><img alt="/zufang/SH2142415753440673792.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=20181213213506e97" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/rent-house-1/c0280c9bffd89bccbeeede9cebbec8c5-1544230829349/d2bf2a3dc57ca5ed89ea0e2ed6e8aee9.jpg.250x182.jpg"></a>
        <p class="bottom__list--item__des">
          <span>
            <a href="/zufang/pudong" target="_blank">浦东</a> 
            - 
            <a href="/zufang/sanlin" target="_blank">三林</a>  
            三林苑          </span>
          <span class="bottom__list--item--hl fr">3490元/月</span> 
        </p>
        <p class="bottom__list--item__btm">
          1室1厅1卫 20㎡
        </p>
      </div>
          <div class="bottom__list--item">
        <a href="/zufang/SH2126662538132733952.html" target="_blank" data-event_id="10805" data-event_action="house_code=SH2126662538132733952&position=3"><img alt="/zufang/SH2126662538132733952.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=20181213213506e97" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/rent-user-avatar/a702d5c1-cd79-4e44-a4e0-d501321c7441.250x182.jpg"></a>
        <p class="bottom__list--item__des">
          <span>
            <a href="/zufang/pudong" target="_blank">浦东</a> 
            - 
            <a href="/zufang/sanlin" target="_blank">三林</a>  
            三林苑          </span>
          <span class="bottom__list--item--hl fr">2400元/月</span> 
        </p>
        <p class="bottom__list--item__btm">
          4室0厅4卫 30㎡
        </p>
      </div>
        </div>
  </div>
</div>
      
      <!-- 商圈在租房源 -->
              <div class="bottom w1150" style="margin-top: -62px">
  <div class="bottom__list">

    
        <p class="bottom__list--title"><a href="/zufang/sanlin" target="_blank" title="三林在租房源">三林在租房源</a></p>
    
    <div class="bottom__list--wrapper">
          <div class="bottom__list--item">
        <a href="/zufang/SH2142663995185184768.html" target="_blank" data-event_id="10806" data-event_action="house_code=SH2142663995185184768&position=1"><img alt="/zufang/SH2142663995185184768.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=20181213213506e97" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/rent-user-avatar/d31f7b1d-e96d-404b-a299-1428fa5b6b20.250x182.jpg"></a>
        <p class="bottom__list--item__des">
          <span>
            <a href="/zufang/pudong" target="_blank">浦东</a> 
            - 
            <a href="/zufang/sanlin" target="_blank">三林</a>  
            香樟苑(浦东)          </span>
          <span class="bottom__list--item--hl fr">1600元/月</span> 
        </p>
        <p class="bottom__list--item__btm">
          4室1厅1卫 12㎡
        </p>
      </div>
          <div class="bottom__list--item">
        <a href="/zufang/SH2146335764899184640.html" target="_blank" data-event_id="10806" data-event_action="house_code=SH2146335764899184640&position=2"><img alt="/zufang/SH2146335764899184640.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=20181213213506e97" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/rent-user-avatar/12af79fc-584f-47af-8b98-2901d1f47230.250x182.jpg"></a>
        <p class="bottom__list--item__des">
          <span>
            <a href="/zufang/pudong" target="_blank">浦东</a> 
            - 
            <a href="/zufang/sanlin" target="_blank">三林</a>  
            浦发绿城          </span>
          <span class="bottom__list--item--hl fr">2000元/月</span> 
        </p>
        <p class="bottom__list--item__btm">
          3室1厅1卫 15㎡
        </p>
      </div>
          <div class="bottom__list--item">
        <a href="/zufang/SH2146337302119718912.html" target="_blank" data-event_id="10806" data-event_action="house_code=SH2146337302119718912&position=3"><img alt="/zufang/SH2146337302119718912.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=20181213213506e97" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/rent-user-avatar/a12d163b-6460-402c-bd22-f76dc3ba9397.250x182.jpg"></a>
        <p class="bottom__list--item__des">
          <span>
            <a href="/zufang/pudong" target="_blank">浦东</a> 
            - 
            <a href="/zufang/sanlin" target="_blank">三林</a>  
            浦发绿城          </span>
          <span class="bottom__list--item--hl fr">1700元/月</span> 
        </p>
        <p class="bottom__list--item__btm">
          3室1厅1卫 12㎡
        </p>
      </div>
        </div>
  </div>
</div>
          </div>

    <!-- 跟动快捷导航 -->
    <div class="fixednav hide" id="fixed">
      <ul class="w1150">
        <li data-el="fixedNavItem" data-href="info">房源信息</li>
                <li data-el="fixedNavItem" data-href="around">交通周边</li>
                <li data-el="fixedNavItem" data-href="deal">小区成交</li>
                <li data-el="fixedNavItem" data-href="recom">推荐房源</li>
      </ul>
    </div>

    <!-- 全部经纪人信息，目前已被隐藏 -->
    <div class="global__list hide" id="globalList">
      <div class="global__list--bg" data-el="shadow"></div>
      <div class="global__list__container">
        <span class="global__list--close" data-el="close"></span>
        <ul>
                    <li>
            <span class="global__list--icon icon--200301001000"></span>
            <p class="global__list--title"><i data-el="updateName" data-houseCode="SH2098450264460894208"></i>（链家）<span class="fr" data-el="updatePhone" data-houseCode="SH2098450264460894208">&nbsp;</span></p>
            <p class="global__list--subtitle oneline"><span>4500</span>/月  </p>
          </li>
                  </ul>
      </div>
    </div>

  <!-- 房源失效时兜底处理 -->
  
  <!-- 底部面包屑链接 -->
  <div class="bread__nav w1150" style="">
  <p class="bread__nav__wrapper oneline">
                  <a href="/zufang/">上海租房网</a>&nbsp;&gt;&nbsp;
                        <a href="/zufang/pudong/">浦东租房</a>&nbsp;&gt;&nbsp;
                        <a href="/zufang/sanlin/">三林租房</a>&nbsp;&gt;&nbsp;
                      <h1>
        <a href="/zufang/c5011000014480/">三林苑租房</a>
      </h1>
            </p>
</div>
</div>

<input type="hidden" data-el="showBooth" value="1">
<!--登录-->
<div class="loninContaner">
    <!--mask-->
    <div class="overlay_bg" style="display: none;"></div>
    <!--账号密码登录-->
    <div id="dialog" class="panel_login animated">
        <div class="panel_info"><i class="close_login">×</i>
            <div class="panel_tab">
                <div class="title">
                    <div class="fl">账号密码登录</div>
                </div>
                <div class="clear"></div>
                <div id="con_login_user">
                    <form action="" method="post">
                        <ul>
                            <li class="item border-t userName">
                                <input type="text" class="the_input topSpecial users" placeholder="请输入手机号" maxlength="11">
                            </li>
                            <li class="item border-b pwd">
                                <input type="password" class="the_input password" maxlength="20" placeholder="请输入登录密码"><em class="password-view"></em>
                            </li>
                            <li class="item checkVerimg" style="display:none;">
                                <input type="text" class="the_input ver-img" maxlength="6" placeholder="请输入验证码">
                                <img class="verImg">
                            </li>
                            <li class="item drag" style="display:none;">
                                <div id="drag"></div>
                            </li>
                            <li class="show-error">
                                <dd>用户名或密码错误</dd>
                            </li>
                            <li class="li_01">
                                <label class="checkbox-btn"><span class="active"><input type="checkbox" name="remember" value="1" class="mind-login" checked=""></span>7天内免登录</label><a href="javascript:;" rel="nofollow" class="toforget">忘记密码</a>
                            </li>
                            <li class="li_btn"><a class="login-user-btn">登录</a>
                            </li>
                            <li class="footer-link"><a href="javascript:;" rel="nofollow" class="totellogin">手机快捷登录</a>
                            </li>
                        </ul>
                    </form>
                </div>
                <div id="con_login_agent" class="undis">
                    <form action="" method="post">
                        <ul>
                            <li class="item">
                                <dd></dd>
                                <input type="text" class="the_input users" placeholder="输入经纪人ID号码">
                            </li>
                            <li class="item">
                                <input type="password" class="the_input password" placeholder="登录密码">
                            </li>
                            <li class="li_01">
                                <label class="checkbox-btn"><span class="active"><input type="checkbox" name="remember" value="1" class="mind-login" checked=""></span>7天内免登录</label><a href="https://passport.lianjDia.com/register/resources/lianjia/forget.html?service=http://bj.lianjia.com/" rel="nofollow">忘记密码</a>
                            </li>
                            <li>
                                <input class="login-agent-btn" value="立即登录">
                            </li>
                        </ul>
                    </form>
                </div>
            </div>
        </div>
        <div class="registered"></div>
    </div>
    <!--手机快捷登录-->
    <div id="dialog_tel" class="panel_login animated btn-login bounceIn actLoginBtn" style="display: none;">
        <div class="panel_info"><i class="close_login">×</i>
            <div class="panel_tab">
                <div class="title">
                    <div class="fl">手机快捷登录</div>
                    <div class="register_text_tel">别担心，无账号自动注册不会导致手机号被泄露</div>
                </div>
                <div class="clear"></div>
                <div id="con_login_user_tel">
                    <form action="" method="post">
                        <ul>
                            <li class="item border-t userName">
                                <input type="text" class="the_input topSpecial users_tel" maxlength="11" placeholder="请输入手机号">
                            </li>
                            <!-- <li class="item pwd"><input type="password" class="the_input password_tel"  placeholder="请输入短信验证码"/></li> -->
                            <li class="item checkVerimg" style="">
                                <input type="text" class="the_input ver-img" maxlength="6" placeholder="请输入验证码">
                                <img class="verImg" src="https://upassport.lianjia.com/freshCaptch?t=1517466208641">
                            </li>
                            <li class="item border-b Verify">
                                <input type="text" class="the_input verifycode" maxlength="6" placeholder="请输入短信验证码"><a class="send_verify_code" id="send_verify_code_tel" href="javascript:;" rel="nofollow"><em>获取验证码</em></a>
                            </li>
                            <li class="send_verify_code_s" id="send_verify_code_tel_s" href="javascript:;" rel="nofollow"><em>没有收到验证码？</em><a class="voice_a">发送语音验证码</a>
                            </li>
                            <li class="show-error">
                                <dd>用户名或密码错误</dd>
                            </li>
                            <li class="li_01">
                                <label class="checkbox-btn"><span class="active"><input type="checkbox" name="remember" value="1" class="mind-login" checked=""></span>7天内免登录</label>
                            </li>
                            <li class="li_btn"><a class="login-user-tel-btn">登录</a>
                            </li>
                            <li class="footer-link"><a href="javascript:;" rel="nofollow" class="tologin">账号密码登录</a>
                            </li>
                        </ul>
                    </form>
                </div>
            </div>
        </div>
        <div class="registered"></div>
    </div>
    <!--手机号码注册-->
    <div id="dialog_reg" class="panel_login animated">
        <div class="panel_info"><i class="close_login">×</i>
            <div class="panel_tab">
                <div class="title">
                    <div class="fl">手机号码注册</div>
                    <label class="fr register_text">已有账号？<a href="javascript:;" rel="nofollow" class="tologin">去登录</a>
                    </label>
                </div>
                <div class="clear"></div>
                <div id="con_login_user_reg">
                    <form action="" method="post">
                        <ul>
                            <li class="item border-t userName">
                                <input type="text" class="the_input topSpecial users_reg" maxlength="11" placeholder="请输入手机号">
                            </li>
                            <li class="item checkVerimg" style="">
                                <input type="text" class="the_input ver-img" maxlength="6" placeholder="请输入验证码">
                                <img class="verImg">
                            </li>
                            <li class="item border-c Verify">
                                <input type="text" class="the_input verifycode" maxlength="6" placeholder="请输入短信验证码"><a class="send_verify_code" id="send_verify_code_reg" href="javascript:;" rel="nofollow"><em>获取验证码</em></a>
                            </li>
                            <li class="item border-b pwd">
                                <input type="password" class="the_input password_reg" maxlength="20" placeholder="请输入密码（最少8位，数字+字母）"><em class="password-view"></em>
                            </li>
                            <li class="send_verify_code_s" id="send_verify_code_reg_s" href="javascript:;" rel="nofollow"><em>没有收到验证码？</em><a class="voice_a">发送语音验证码</a>
                            </li>
                            <li class="show-error">
                                <dd>用户名或密码错误</dd>
                            </li>
                            <li class="li_01">
                                <label class="checkbox-btn"><span class="active"><input type="checkbox" name="read" value="1" class="read-protocol" checked=""></span>我已阅读并同意</label>
                                <a class="toprotocol" href="//www.ke.com/zhuanti/protocol" target="_blank">《贝壳用户使用协议》</a>
                                及
                                <a class="toprotocol" href="//www.ke.com/zhuanti/serviceProtocol" target="_blank">《贝壳用户服务协议》</a>
                            </li>
                            <li class="li_btn"><a class="register-user-btn">注册</a>
                            </li>
                        </ul>
                    </form>
                </div>
            </div>
        </div>
        <div class="registered"></div>
    </div>
    <!--找回密码-->
    <div id="dialog_forget" class="panel_login animated">
        <div class="panel_info"><i class="close_login">×</i>
            <div class="panel_tab">
                <div class="title">
                    <div class="fl">找回密码</div>
                </div>
                <div class="clear"></div>
                <div id="con_forget_user_tel" class="con_forget_user_tel">
                    <form action="" method="post">
                        <ul>
                            <li class="item border-t userName">
                                <input type="text" class="the_input topSpecial user_forget_phone" placeholder="请输入手机号" maxlength="11">
                            </li>
                            <li class="item checkVerimg" style="">
                                <input type="text" class="the_input ver-img" maxlength="6" placeholder="请输入验证码">
                                <img class="verImg">
                            </li>
                            <li class="item border-b Verify">
                                <input type="text" class="the_input verifycode" maxlength="6" placeholder="请输入短信验证码"><a class="send_verify_code" id="send_verify_code_forget" href="javascript:;" rel="nofollow"><em>获取验证码</em></a>
                            </li>
                            <li class="item border-t pwd" style="margin-top:-1px;">
                                <input type="password" class="the_input password_reg" maxlength="20" placeholder="请输入密码（最少8位，数字+字母）"><em class="password-view"></em>
                            </li>
                            <li class="send_verify_code_s" id="send_verify_code_forget_s"><em>没有收到验证码？</em><a class="voice_a">发送语音验证码</a>
                            </li>
                            <li class="show-error">
                                <dd>用户名或密码错误</dd>
                            </li>
                            <li class="li_btn"><a class="user-forget">修改密码</a>
                            </li>
                        </ul>
                    </form>
                </div>
                <div id="con_forget_user_pw" class="con_forget_user_pw">
                    <form action="" method="post">
                        <ul>
                            <li class="item border-t pwd">
                                <input type="password" class="the_input password_reg" maxlength="20" placeholder="请输入密码（最少8位，数字+字母）"><em class="password-view"></em>
                            </li>
                            <li class="show-error">
                                <dd>用户名或密码错误</dd>
                            </li>
                            <li class="li_btn"><a class="modify-user-pswd">修改密码</a>
                            </li>
                        </ul>
                    </form>
                </div>
            </div>
        </div>
        <div class="registered"></div>
    </div>
</div>
<script>
  g_conf.coord = {
    longitude: '121.530564',
    latitude: '31.149539'
  };
  g_conf.subway = [{"distance":474,"lines":["11\u53f7\u7ebf(\u8fea\u58eb\u5c3c-\u82b1\u6865)"],"name":"\u4e09\u6797\u4e1c","point_lat":31.152327,"point_lng":121.528866}];
  g_conf.name = '三林苑';
  g_conf.houseCode = 'SH2098450264460894208';
  g_conf.offline = '';

  g_conf.pageId = 'rentalDetail';
  var __requireList = ['page/detail/index'];
</script>
</div>

<div class="fix-right-v3" id="back-top" log-mod="sidebar">
  <table>
    <tbody>
      <tr>
        <td>
          <ul>
            <li class="myfav sidebar-item">
              <a title="我关注的房源" data-url="//user.lianjia.com/site/favorHouse/" data-bl="myfav">我关注的房源</a>
              <span class="popup"><i></i>我关注的房源</span>
            </li>
            <li class="sell sidebar-item">
              <a title="在线卖房" href="//sh.lianjia.com/yezhu/" target="_blank" data-bl="sell">在线卖房</a>
              <span class="popup"><i></i>在线卖房</span>
            </li>
            <li class="baodan sidebar-item">
              <a href="//sh.lianjia.com/anxinchengnuo" title="安心保单" target="_blank" data-bl="baodan">安心保单</a>
              <span class="popup">
                <i></i>安心保单
              </span>
            </li>
            <li class="download sidebar-item">
              <a href="//www.lianjia.com/client/" title="" target="_blank" data-bl="client">下载掌上链家</a>
              <span class="popup popup-qr">
                <i></i><img src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/img/wxapp.jpg?_v=20181213213506e97" alt="下载掌上链家" width="94">
                <em class="qr-title">链家微信小程序</em>
              </span>
            </li>
            <li class="phone sidebar-item">
              <a title="官方客服">官方客服</a>
              <span class="popup"><i></i>官方客服</span>
            </li>

                        <li class="feedback sidebar-item">
              <a href="https://helper.lianjia.com/it/index2#/feedbackForC?channel=lj-pc&city=310000" title="反馈/投诉" data-bl="feedback"></a>
              <span class="popup"><i></i>反馈/投诉</span>
            </li>
          </ul>
        </td>
      </tr>
    </tbody>
  </table>
  <ul>
    <li class="gotop sidebar-item" id="gotop" style="display: none;"><a title="返回顶部">返回顶部</a><span class="popup"><i></i>返回顶部</span></li>
  </ul>
</div>
<div class="footer">
  <div class="footer__wrapper w1150">

    <div class="footer__top">
      <ul class="footer__light">
                <li><a href="/zufang/wzdt/">网站地图</a></li>
              </ul>
      <a class="footer__aside" href="tel:10109666">客服电话<span>10109666</span></a>
    </div>

    <div class="footer__middle">
      <ul data-el="parentList">
                  <li><a class="cur" data-index="0">租房城市</a></li>
                  <li><a class="" data-index="1">热门商圈</a></li>
                  <li><a class="" data-index="2">推荐小区</a></li>
                  <li><a class="" data-index="3">城市新房</a></li>
                  <li><a class="" data-index="4">城市二手房</a></li>
                  <li><a class="" data-index="5">友情链接</a></li>
              </ul>
              <ul data-el="childrenList"  style="display:block">
                      <li><a href="https://hz.lianjia.com/zufang/">杭州租房</a></li>
                      <li><a href="https://cd.lianjia.com/zufang/">成都租房</a></li>
                      <li><a href="https://zh.lianjia.com/zufang/">珠海租房</a></li>
                      <li><a href="https://liangshan.lianjia.com/zufang/">凉山租房</a></li>
                      <li><a href="https://hk.lianjia.com/zufang/">海口租房</a></li>
                      <li><a href="https://sz.lianjia.com/zufang/">深圳租房</a></li>
                      <li><a href="https://nb.lianjia.com/zufang/">宁波租房</a></li>
                      <li><a href="https://wx.lianjia.com/zufang/">无锡租房</a></li>
                      <li><a href="https://zs.lianjia.com/zufang/">中山租房</a></li>
                      <li><a href="https://jian.lianjia.com/zufang/">吉安租房</a></li>
                      <li><a href="https://ts.lianjia.com/zufang/">唐山租房</a></li>
                      <li><a href="https://baoding.lianjia.com/zufang/">保定租房</a></li>
                      <li><a href="https://taizhou.lianjia.com/zufang/">台州租房</a></li>
                      <li><a href="https://yt.lianjia.com/zufang/">烟台租房</a></li>
                      <li><a href="https://qd.lianjia.com/zufang/">青岛租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/">上海租房</a></li>
                      <li><a href="https://hui.lianjia.com/zufang/">惠州租房</a></li>
                      <li><a href="https://ganzhou.lianjia.com/zufang/">赣州租房</a></li>
                      <li><a href="https://hf.lianjia.com/zufang/">合肥租房</a></li>
                      <li><a href="https://kf.lianjia.com/zufang/">开封租房</a></li>
                      <li><a href="https://wuhu.lianjia.com/zufang/">芜湖租房</a></li>
                      <li><a href="https://jn.lianjia.com/zufang/">济南租房</a></li>
                      <li><a href="https://san.lianjia.com/zufang/">三亚租房</a></li>
                      <li><a href="https://dg.lianjia.com/zufang/">东莞租房</a></li>
                      <li><a href="https://nn.lianjia.com/zufang/">南宁租房</a></li>
                      <li><a href="https://xm.lianjia.com/zufang/">厦门租房</a></li>
                      <li><a href="https://cc.lianjia.com/zufang/">长春租房</a></li>
                      <li><a href="https://baoji.lianjia.com/zufang/">宝鸡租房</a></li>
                      <li><a href="https://gz.lianjia.com/zufang/">广州租房</a></li>
                      <li><a href="https://gy.lianjia.com/zufang/">贵阳租房</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                      <li><a href="https://sh.lianjia.com/zufang/waigaoqiao/">外高桥租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/xinxilan/">新西兰租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/nichengzhen/">泥城镇租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/xianghuaqiao/">香花桥租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/hanghua/">航华租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/taopu/">桃浦租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/huajing/">华泾租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/zhoujiazuilu/">周家嘴路租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/luojing/">罗泾租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/changqiao/">长桥租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/shibobinjiang/">世博滨江租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/sichuanbeilu/">四川北路租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/weifang/">潍坊租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/wuxishi/">无锡市租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/lujiazui/">陆家嘴租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/fengjing/">枫泾租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/kunshan1/">昆山租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/zhelin/">柘林租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/nanjingdonglu/">南京东路租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/jiangqiao/">江桥租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/penglaigongyuan/">蓬莱公园租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/gaojing/">高境租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/zhenguang/">真光租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/zhujiajiao/">朱家角租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/dachangzhen/">大场镇租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/dongjing/">东京租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/tangzhen/">唐镇租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/gongfu/">共富租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/gubei/">古北租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/kongjianglu/">控江路租房</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                      <li><a href="https://sh.lianjia.com/zufang/c5016641490955276/">康杉路622号</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000932/">敦化路4弄</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000001942/">荣成路41弄</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000001918/">乔家路258弄8支弄</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000441/">愚园路1283弄</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000792/">新凯城锦昌苑</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000002115/">沪太路1118弄</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000204/">欧美亚商务办公楼</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000001443/">中瑞府前嘉苑</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000029/">滨海二村</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5020026413757163/">衡水路216号</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000001790/">南洋瑞都剑桥府邸(别墅)</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5016612386442467/">控江路300号</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000002366/">龙门邨</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5020035235913134/">招商·依云四季</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5020034608668617/">衡源西岸壹号</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000002511/">紫云路61号</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000928/">常德路444号</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000003089/">金荣公寓</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000494/">明珠小区(川沙)</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5020031764721032/">东宝兴路777号</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000002168/">安高东方御府</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5016753661587023/">牡丹路147号</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000061/">高行银杏苑</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000000450/">八方大酒店</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5020026693926241/">西门路105号(崇明)</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000003032/">宝启花园(别墅)</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5020028559026160/">华志路901号</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000002636/">昆港公路1639号</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5016884171550353/">林林产业园</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                      <li><a href="https://changzhou.fang.lianjia.com/">常州楼盘</a></li>
                      <li><a href="https://xan.fang.lianjia.com/">雄安新区楼盘</a></li>
                      <li><a href="https://xm.fang.lianjia.com/">厦门楼盘</a></li>
                      <li><a href="https://gz.fang.lianjia.com/">广州楼盘</a></li>
                      <li><a href="https://bj.fang.lianjia.com/">北京楼盘</a></li>
                      <li><a href="https://jian.fang.lianjia.com/">吉安楼盘</a></li>
                      <li><a href="https://dg.fang.lianjia.com/">东莞楼盘</a></li>
                      <li><a href="https://gy.fang.lianjia.com/">贵阳楼盘</a></li>
                      <li><a href="https://hk.fang.lianjia.com/">海口楼盘</a></li>
                      <li><a href="https://nn.fang.lianjia.com/">南宁楼盘</a></li>
                      <li><a href="https://jx.fang.lianjia.com/">嘉兴楼盘</a></li>
                      <li><a href="https://zjk.fang.lianjia.com/">张家口楼盘</a></li>
                      <li><a href="https://cs.fang.lianjia.com/">长沙楼盘</a></li>
                      <li><a href="https://sx.fang.lianjia.com/">绍兴楼盘</a></li>
                      <li><a href="https://sh.fang.lianjia.com/">上海楼盘</a></li>
                      <li><a href="https://jiujiang.fang.lianjia.com/">九江楼盘</a></li>
                      <li><a href="https://hui.fang.lianjia.com/">惠州楼盘</a></li>
                      <li><a href="https://baoji.fang.lianjia.com/">宝鸡楼盘</a></li>
                      <li><a href="https://sjz.fang.lianjia.com/">石家庄楼盘</a></li>
                      <li><a href="https://zj.fang.lianjia.com/">镇江楼盘</a></li>
                      <li><a href="https://hz.fang.lianjia.com/">杭州楼盘</a></li>
                      <li><a href="https://fs.fang.lianjia.com/">佛山楼盘</a></li>
                      <li><a href="https://wh.fang.lianjia.com/">武汉楼盘</a></li>
                      <li><a href="https://zs.fang.lianjia.com/">中山楼盘</a></li>
                      <li><a href="https://jl.fang.lianjia.com/">吉林楼盘</a></li>
                      <li><a href="https://jn.fang.lianjia.com/">济南楼盘</a></li>
                      <li><a href="https://sz.fang.lianjia.com/">深圳楼盘</a></li>
                      <li><a href="https://wx.fang.lianjia.com/">无锡楼盘</a></li>
                      <li><a href="https://kf.fang.lianjia.com/">开封楼盘</a></li>
                      <li><a href="https://liangshan.fang.lianjia.com/">凉山楼盘</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                      <li><a href="https://hk.ke.com/ershoufang/">海口二手房</a></li>
                      <li><a href="https://jn.ke.com/ershoufang/">济南二手房</a></li>
                      <li><a href="https://wuhu.ke.com/ershoufang/">芜湖二手房</a></li>
                      <li><a href="https://changzhou.ke.com/ershoufang/">常州二手房</a></li>
                      <li><a href="https://jl.ke.com/ershoufang/">吉林二手房</a></li>
                      <li><a href="https://kf.ke.com/ershoufang/">开封二手房</a></li>
                      <li><a href="https://sjz.ke.com/ershoufang/">石家庄二手房</a></li>
                      <li><a href="https://liangshan.ke.com/ershoufang/">凉山二手房</a></li>
                      <li><a href="https://zz.ke.com/ershoufang/">郑州二手房</a></li>
                      <li><a href="https://zjk.ke.com/ershoufang/">张家口二手房</a></li>
                      <li><a href="https://fs.ke.com/ershoufang/">佛山二手房</a></li>
                      <li><a href="https://zh.ke.com/ershoufang/">珠海二手房</a></li>
                      <li><a href="https://wh.ke.com/ershoufang/">武汉二手房</a></li>
                      <li><a href="https://dg.ke.com/ershoufang/">东莞二手房</a></li>
                      <li><a href="https://xm.ke.com/ershoufang/">厦门二手房</a></li>
                      <li><a href="https://san.ke.com/ershoufang/">三亚二手房</a></li>
                      <li><a href="https://gz.ke.com/ershoufang/">广州二手房</a></li>
                      <li><a href="https://baoji.ke.com/ershoufang/">宝鸡二手房</a></li>
                      <li><a href="https://ty.ke.com/ershoufang/">太原二手房</a></li>
                      <li><a href="https://nb.ke.com/ershoufang/">宁波二手房</a></li>
                      <li><a href="https://qd.ke.com/ershoufang/">青岛二手房</a></li>
                      <li><a href="https://lf.ke.com/ershoufang/">廊坊二手房</a></li>
                      <li><a href="https://jiujiang.ke.com/ershoufang/">九江二手房</a></li>
                      <li><a href="https://sy.ke.com/ershoufang/">沈阳二手房</a></li>
                      <li><a href="https://taizhou.ke.com/ershoufang/">台州二手房</a></li>
                      <li><a href="https://wx.ke.com/ershoufang/">无锡二手房</a></li>
                      <li><a href="https://cs.ke.com/ershoufang/">长沙二手房</a></li>
                      <li><a href="https://cc.ke.com/ershoufang/">长春二手房</a></li>
                      <li><a href="https://baoding.ke.com/ershoufang/">保定二手房</a></li>
                      <li><a href="https://sx.ke.com/ershoufang/">绍兴二手房</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                  </ul>
           </div>

    <div class="footer__bottom">
      <p>链家网（北京）科技有限公司 | 网络经营许可证 京ICP备16057509号-2 | &copy; Copyright&copy;2010-2018 链家网Lianjia.com版权所有</p>
      <a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010802024019" style="display:inline-block;text-decoration:none;height:20px;line-height:20px;"><img style="margin-right: 5px;" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/img/beian.png?_v=20181213213506e97">京公网安备 11010802024019号</a>
    </div>

  </div>
</div>

<script type="text/javascript">
  var footerList = JSON.parse(JSON.stringify([{"abbr":"zfcs","expire":"2018-12-22 23:00:02","city_id":"310000","children":[{"url":"https:\/\/hz.lianjia.com\/zufang\/","title":"\u676d\u5dde\u79df\u623f"},{"url":"https:\/\/cd.lianjia.com\/zufang\/","title":"\u6210\u90fd\u79df\u623f"},{"url":"https:\/\/zh.lianjia.com\/zufang\/","title":"\u73e0\u6d77\u79df\u623f"},{"url":"https:\/\/liangshan.lianjia.com\/zufang\/","title":"\u51c9\u5c71\u79df\u623f"},{"url":"https:\/\/hk.lianjia.com\/zufang\/","title":"\u6d77\u53e3\u79df\u623f"},{"url":"https:\/\/sz.lianjia.com\/zufang\/","title":"\u6df1\u5733\u79df\u623f"},{"url":"https:\/\/nb.lianjia.com\/zufang\/","title":"\u5b81\u6ce2\u79df\u623f"},{"url":"https:\/\/wx.lianjia.com\/zufang\/","title":"\u65e0\u9521\u79df\u623f"},{"url":"https:\/\/zs.lianjia.com\/zufang\/","title":"\u4e2d\u5c71\u79df\u623f"},{"url":"https:\/\/jian.lianjia.com\/zufang\/","title":"\u5409\u5b89\u79df\u623f"},{"url":"https:\/\/ts.lianjia.com\/zufang\/","title":"\u5510\u5c71\u79df\u623f"},{"url":"https:\/\/baoding.lianjia.com\/zufang\/","title":"\u4fdd\u5b9a\u79df\u623f"},{"url":"https:\/\/taizhou.lianjia.com\/zufang\/","title":"\u53f0\u5dde\u79df\u623f"},{"url":"https:\/\/yt.lianjia.com\/zufang\/","title":"\u70df\u53f0\u79df\u623f"},{"url":"https:\/\/qd.lianjia.com\/zufang\/","title":"\u9752\u5c9b\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/","title":"\u4e0a\u6d77\u79df\u623f"},{"url":"https:\/\/hui.lianjia.com\/zufang\/","title":"\u60e0\u5dde\u79df\u623f"},{"url":"https:\/\/ganzhou.lianjia.com\/zufang\/","title":"\u8d63\u5dde\u79df\u623f"},{"url":"https:\/\/hf.lianjia.com\/zufang\/","title":"\u5408\u80a5\u79df\u623f"},{"url":"https:\/\/kf.lianjia.com\/zufang\/","title":"\u5f00\u5c01\u79df\u623f"},{"url":"https:\/\/wuhu.lianjia.com\/zufang\/","title":"\u829c\u6e56\u79df\u623f"},{"url":"https:\/\/jn.lianjia.com\/zufang\/","title":"\u6d4e\u5357\u79df\u623f"},{"url":"https:\/\/san.lianjia.com\/zufang\/","title":"\u4e09\u4e9a\u79df\u623f"},{"url":"https:\/\/dg.lianjia.com\/zufang\/","title":"\u4e1c\u839e\u79df\u623f"},{"url":"https:\/\/nn.lianjia.com\/zufang\/","title":"\u5357\u5b81\u79df\u623f"},{"url":"https:\/\/xm.lianjia.com\/zufang\/","title":"\u53a6\u95e8\u79df\u623f"},{"url":"https:\/\/cc.lianjia.com\/zufang\/","title":"\u957f\u6625\u79df\u623f"},{"url":"https:\/\/baoji.lianjia.com\/zufang\/","title":"\u5b9d\u9e21\u79df\u623f"},{"url":"https:\/\/gz.lianjia.com\/zufang\/","title":"\u5e7f\u5dde\u79df\u623f"},{"url":"https:\/\/gy.lianjia.com\/zufang\/","title":"\u8d35\u9633\u79df\u623f"}],"title":"\u79df\u623f\u57ce\u5e02","class":""},{"abbr":"rmsq","expire":"2018-12-22 23:00:02","city_id":"310000","children":[{"url":"https:\/\/sh.lianjia.com\/zufang\/waigaoqiao\/","title":"\u5916\u9ad8\u6865\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/xinxilan\/","title":"\u65b0\u897f\u5170\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/nichengzhen\/","title":"\u6ce5\u57ce\u9547\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/xianghuaqiao\/","title":"\u9999\u82b1\u6865\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/hanghua\/","title":"\u822a\u534e\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/taopu\/","title":"\u6843\u6d66\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/huajing\/","title":"\u534e\u6cfe\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/zhoujiazuilu\/","title":"\u5468\u5bb6\u5634\u8def\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/luojing\/","title":"\u7f57\u6cfe\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/changqiao\/","title":"\u957f\u6865\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/shibobinjiang\/","title":"\u4e16\u535a\u6ee8\u6c5f\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/sichuanbeilu\/","title":"\u56db\u5ddd\u5317\u8def\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/weifang\/","title":"\u6f4d\u574a\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/wuxishi\/","title":"\u65e0\u9521\u5e02\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/lujiazui\/","title":"\u9646\u5bb6\u5634\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/fengjing\/","title":"\u67ab\u6cfe\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/kunshan1\/","title":"\u6606\u5c71\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/zhelin\/","title":"\u67d8\u6797\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/nanjingdonglu\/","title":"\u5357\u4eac\u4e1c\u8def\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/jiangqiao\/","title":"\u6c5f\u6865\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/penglaigongyuan\/","title":"\u84ec\u83b1\u516c\u56ed\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/gaojing\/","title":"\u9ad8\u5883\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/zhenguang\/","title":"\u771f\u5149\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/zhujiajiao\/","title":"\u6731\u5bb6\u89d2\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/dachangzhen\/","title":"\u5927\u573a\u9547\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/dongjing\/","title":"\u4e1c\u4eac\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/tangzhen\/","title":"\u5510\u9547\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/gongfu\/","title":"\u5171\u5bcc\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/gubei\/","title":"\u53e4\u5317\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/kongjianglu\/","title":"\u63a7\u6c5f\u8def\u79df\u623f"}],"title":"\u70ed\u95e8\u5546\u5708","class":""},{"abbr":"tjxq","expire":"2018-12-22 23:00:03","city_id":"310000","children":[{"url":"https:\/\/sh.lianjia.com\/zufang\/c5016641490955276\/","title":"\u5eb7\u6749\u8def622\u53f7"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000932\/","title":"\u6566\u5316\u8def4\u5f04"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000001942\/","title":"\u8363\u6210\u8def41\u5f04"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000001918\/","title":"\u4e54\u5bb6\u8def258\u5f048\u652f\u5f04"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000441\/","title":"\u611a\u56ed\u8def1283\u5f04"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000792\/","title":"\u65b0\u51ef\u57ce\u9526\u660c\u82d1"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000002115\/","title":"\u6caa\u592a\u8def1118\u5f04"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000204\/","title":"\u6b27\u7f8e\u4e9a\u5546\u52a1\u529e\u516c\u697c"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000001443\/","title":"\u4e2d\u745e\u5e9c\u524d\u5609\u82d1"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000029\/","title":"\u6ee8\u6d77\u4e8c\u6751"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5020026413757163\/","title":"\u8861\u6c34\u8def216\u53f7"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000001790\/","title":"\u5357\u6d0b\u745e\u90fd\u5251\u6865\u5e9c\u90b8(\u522b\u5885)"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5016612386442467\/","title":"\u63a7\u6c5f\u8def300\u53f7"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000002366\/","title":"\u9f99\u95e8\u90a8"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5020035235913134\/","title":"\u62db\u5546\u00b7\u4f9d\u4e91\u56db\u5b63"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5020034608668617\/","title":"\u8861\u6e90\u897f\u5cb8\u58f9\u53f7"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000002511\/","title":"\u7d2b\u4e91\u8def61\u53f7"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000928\/","title":"\u5e38\u5fb7\u8def444\u53f7"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000003089\/","title":"\u91d1\u8363\u516c\u5bd3"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000494\/","title":"\u660e\u73e0\u5c0f\u533a(\u5ddd\u6c99)"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5020031764721032\/","title":"\u4e1c\u5b9d\u5174\u8def777\u53f7"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000002168\/","title":"\u5b89\u9ad8\u4e1c\u65b9\u5fa1\u5e9c"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5016753661587023\/","title":"\u7261\u4e39\u8def147\u53f7"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000061\/","title":"\u9ad8\u884c\u94f6\u674f\u82d1"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000000450\/","title":"\u516b\u65b9\u5927\u9152\u5e97"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5020026693926241\/","title":"\u897f\u95e8\u8def105\u53f7(\u5d07\u660e)"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000003032\/","title":"\u5b9d\u542f\u82b1\u56ed(\u522b\u5885)"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5020028559026160\/","title":"\u534e\u5fd7\u8def901\u53f7"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000002636\/","title":"\u6606\u6e2f\u516c\u8def1639\u53f7"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5016884171550353\/","title":"\u6797\u6797\u4ea7\u4e1a\u56ed"}],"title":"\u63a8\u8350\u5c0f\u533a","class":""},{"abbr":"csxf","expire":"2018-12-22 23:00:03","city_id":"310000","children":[{"url":"https:\/\/changzhou.fang.lianjia.com\/","title":"\u5e38\u5dde\u697c\u76d8"},{"url":"https:\/\/xan.fang.lianjia.com\/","title":"\u96c4\u5b89\u65b0\u533a\u697c\u76d8"},{"url":"https:\/\/xm.fang.lianjia.com\/","title":"\u53a6\u95e8\u697c\u76d8"},{"url":"https:\/\/gz.fang.lianjia.com\/","title":"\u5e7f\u5dde\u697c\u76d8"},{"url":"https:\/\/bj.fang.lianjia.com\/","title":"\u5317\u4eac\u697c\u76d8"},{"url":"https:\/\/jian.fang.lianjia.com\/","title":"\u5409\u5b89\u697c\u76d8"},{"url":"https:\/\/dg.fang.lianjia.com\/","title":"\u4e1c\u839e\u697c\u76d8"},{"url":"https:\/\/gy.fang.lianjia.com\/","title":"\u8d35\u9633\u697c\u76d8"},{"url":"https:\/\/hk.fang.lianjia.com\/","title":"\u6d77\u53e3\u697c\u76d8"},{"url":"https:\/\/nn.fang.lianjia.com\/","title":"\u5357\u5b81\u697c\u76d8"},{"url":"https:\/\/jx.fang.lianjia.com\/","title":"\u5609\u5174\u697c\u76d8"},{"url":"https:\/\/zjk.fang.lianjia.com\/","title":"\u5f20\u5bb6\u53e3\u697c\u76d8"},{"url":"https:\/\/cs.fang.lianjia.com\/","title":"\u957f\u6c99\u697c\u76d8"},{"url":"https:\/\/sx.fang.lianjia.com\/","title":"\u7ecd\u5174\u697c\u76d8"},{"url":"https:\/\/sh.fang.lianjia.com\/","title":"\u4e0a\u6d77\u697c\u76d8"},{"url":"https:\/\/jiujiang.fang.lianjia.com\/","title":"\u4e5d\u6c5f\u697c\u76d8"},{"url":"https:\/\/hui.fang.lianjia.com\/","title":"\u60e0\u5dde\u697c\u76d8"},{"url":"https:\/\/baoji.fang.lianjia.com\/","title":"\u5b9d\u9e21\u697c\u76d8"},{"url":"https:\/\/sjz.fang.lianjia.com\/","title":"\u77f3\u5bb6\u5e84\u697c\u76d8"},{"url":"https:\/\/zj.fang.lianjia.com\/","title":"\u9547\u6c5f\u697c\u76d8"},{"url":"https:\/\/hz.fang.lianjia.com\/","title":"\u676d\u5dde\u697c\u76d8"},{"url":"https:\/\/fs.fang.lianjia.com\/","title":"\u4f5b\u5c71\u697c\u76d8"},{"url":"https:\/\/wh.fang.lianjia.com\/","title":"\u6b66\u6c49\u697c\u76d8"},{"url":"https:\/\/zs.fang.lianjia.com\/","title":"\u4e2d\u5c71\u697c\u76d8"},{"url":"https:\/\/jl.fang.lianjia.com\/","title":"\u5409\u6797\u697c\u76d8"},{"url":"https:\/\/jn.fang.lianjia.com\/","title":"\u6d4e\u5357\u697c\u76d8"},{"url":"https:\/\/sz.fang.lianjia.com\/","title":"\u6df1\u5733\u697c\u76d8"},{"url":"https:\/\/wx.fang.lianjia.com\/","title":"\u65e0\u9521\u697c\u76d8"},{"url":"https:\/\/kf.fang.lianjia.com\/","title":"\u5f00\u5c01\u697c\u76d8"},{"url":"https:\/\/liangshan.fang.lianjia.com\/","title":"\u51c9\u5c71\u697c\u76d8"}],"title":"\u57ce\u5e02\u65b0\u623f","class":""},{"abbr":"csesf","expire":"2018-12-22 23:00:03","city_id":"310000","children":[{"url":"https:\/\/hk.ke.com\/ershoufang\/","title":"\u6d77\u53e3\u4e8c\u624b\u623f"},{"url":"https:\/\/jn.ke.com\/ershoufang\/","title":"\u6d4e\u5357\u4e8c\u624b\u623f"},{"url":"https:\/\/wuhu.ke.com\/ershoufang\/","title":"\u829c\u6e56\u4e8c\u624b\u623f"},{"url":"https:\/\/changzhou.ke.com\/ershoufang\/","title":"\u5e38\u5dde\u4e8c\u624b\u623f"},{"url":"https:\/\/jl.ke.com\/ershoufang\/","title":"\u5409\u6797\u4e8c\u624b\u623f"},{"url":"https:\/\/kf.ke.com\/ershoufang\/","title":"\u5f00\u5c01\u4e8c\u624b\u623f"},{"url":"https:\/\/sjz.ke.com\/ershoufang\/","title":"\u77f3\u5bb6\u5e84\u4e8c\u624b\u623f"},{"url":"https:\/\/liangshan.ke.com\/ershoufang\/","title":"\u51c9\u5c71\u4e8c\u624b\u623f"},{"url":"https:\/\/zz.ke.com\/ershoufang\/","title":"\u90d1\u5dde\u4e8c\u624b\u623f"},{"url":"https:\/\/zjk.ke.com\/ershoufang\/","title":"\u5f20\u5bb6\u53e3\u4e8c\u624b\u623f"},{"url":"https:\/\/fs.ke.com\/ershoufang\/","title":"\u4f5b\u5c71\u4e8c\u624b\u623f"},{"url":"https:\/\/zh.ke.com\/ershoufang\/","title":"\u73e0\u6d77\u4e8c\u624b\u623f"},{"url":"https:\/\/wh.ke.com\/ershoufang\/","title":"\u6b66\u6c49\u4e8c\u624b\u623f"},{"url":"https:\/\/dg.ke.com\/ershoufang\/","title":"\u4e1c\u839e\u4e8c\u624b\u623f"},{"url":"https:\/\/xm.ke.com\/ershoufang\/","title":"\u53a6\u95e8\u4e8c\u624b\u623f"},{"url":"https:\/\/san.ke.com\/ershoufang\/","title":"\u4e09\u4e9a\u4e8c\u624b\u623f"},{"url":"https:\/\/gz.ke.com\/ershoufang\/","title":"\u5e7f\u5dde\u4e8c\u624b\u623f"},{"url":"https:\/\/baoji.ke.com\/ershoufang\/","title":"\u5b9d\u9e21\u4e8c\u624b\u623f"},{"url":"https:\/\/ty.ke.com\/ershoufang\/","title":"\u592a\u539f\u4e8c\u624b\u623f"},{"url":"https:\/\/nb.ke.com\/ershoufang\/","title":"\u5b81\u6ce2\u4e8c\u624b\u623f"},{"url":"https:\/\/qd.ke.com\/ershoufang\/","title":"\u9752\u5c9b\u4e8c\u624b\u623f"},{"url":"https:\/\/lf.ke.com\/ershoufang\/","title":"\u5eca\u574a\u4e8c\u624b\u623f"},{"url":"https:\/\/jiujiang.ke.com\/ershoufang\/","title":"\u4e5d\u6c5f\u4e8c\u624b\u623f"},{"url":"https:\/\/sy.ke.com\/ershoufang\/","title":"\u6c88\u9633\u4e8c\u624b\u623f"},{"url":"https:\/\/taizhou.ke.com\/ershoufang\/","title":"\u53f0\u5dde\u4e8c\u624b\u623f"},{"url":"https:\/\/wx.ke.com\/ershoufang\/","title":"\u65e0\u9521\u4e8c\u624b\u623f"},{"url":"https:\/\/cs.ke.com\/ershoufang\/","title":"\u957f\u6c99\u4e8c\u624b\u623f"},{"url":"https:\/\/cc.ke.com\/ershoufang\/","title":"\u957f\u6625\u4e8c\u624b\u623f"},{"url":"https:\/\/baoding.ke.com\/ershoufang\/","title":"\u4fdd\u5b9a\u4e8c\u624b\u623f"},{"url":"https:\/\/sx.ke.com\/ershoufang\/","title":"\u7ecd\u5174\u4e8c\u624b\u623f"}],"title":"\u57ce\u5e02\u4e8c\u624b\u623f","class":""},{"abbr":"yqlj","title":"\u53cb\u60c5\u94fe\u63a5","city_id":"310000","expire":"2018-12-17","children":[]}]))

</script></body>


<!-- 自动推送代码 -->
<script>
  (function(){
  var canonicalURL, curProtocol;
  //Get the <link> tag
  var x=document.getElementsByTagName("link");
  //Find the last canonical URL
  if(x.length > 0){
  for (i=0;i<x.length;i++){
  if(x[i].rel.toLowerCase() == 'canonical' && x[i].href){
  canonicalURL=x[i].href;
  }
  }
  }
  //Get protocol
  if (!canonicalURL){
  curProtocol = window.location.protocol.split(':')[0];
  }
  else{
  curProtocol = canonicalURL.split(':')[0];
  }
  //Get current URL if the canonical URL does not exist
  if (!canonicalURL) canonicalURL = window.location.href;
  //Assign script content. Replace current URL with the canonical URL
  !function(){var e=/([http|https]:\/\/[a-zA-Z0-9\_\.]+\.baidu\.com)/gi,r=canonicalURL,t=document.referrer;if(!e.test(r)){var n=(String(curProtocol).toLowerCase() === 'https')?"https://sp0.baidu.com/9_Q4simg2RQJ8t7jm9iCKT-xh_/s.gif":"//api.share.baidu.com/s.gif";t?(n+="?r="+encodeURIComponent(document.referrer),r&&(n+="&l="+r)):r&&(n+="?l="+r);var i=new Image;i.src=n}}(window);})();
</script>

<script type="text/javascript" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/common/js/common.js?_v=20181213213506e97"></script>

<script type="text/javascript">
  //引入脚本后
  var imConf = {
          "ajaxroot": "\/\/ajax.api.ke.com\/",
          "imAppid": "ZULIN_WEB_20181122",
          "imAppkey": "0a4e8669fc2a50cbbeeb969726a7ab46"
      };
</script>
<script>
var __basePath = 'https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src?_v=20181213213506e97'.split("?");
require.config({
  baseUrl: __basePath[0],
  paths: {
  },
  urlArgs:  __basePath[1]
});
var config = {"fe_root":"https:\/\/s1.ljcdn.com\/matrix_lianjia_pc\/dist\/pc","version":"20181213213506e97","js_ns":"m_pages_zufangDetail","cur_city_id":"310000","cur_city_name":"\u4e0a\u6d77","cur_city_short":"sh"};
</script>
<script>
;;(function() {
  for(var i = 0, len = __requireList.length; i < len; i++) {
    require([__requireList[i]], function(engine) {
      engine.init();
    });
  }
})();
</script>
<!--动态脚本内容-->
<div style="display: none">
  <script src="https://s19.cnzz.com/z_stat.php?id=1273627291&web_id=1273627291" language="JavaScript"></script>
</div>
<script>
  window.ljConf = {
    city_abbr: 'sh',
    city_id: '310000',
    city_name: '上海',
  }
window.__UDL_CONFIG = window.__UDL_CONFIG || {};
window.__UDL_CONFIG.pid = window.__UDL_CONFIG.pid || (document.domain.search('ke.com')>-1 ? 'bigc_pc_rent':'matrixpc');
window.__UDL_CONFIG.env = ('prod' === 'prod' ? (document.domain.search('ke.com')>-1 ? 'dac' : 'lianjia') : 'test');
window.__UDL_CONFIG[document.domain.search('ke.com') > -1?'uicode':'ljweb_channel_key'] = g_conf.pageId || '';
with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='//s1.ljcdn.com/matrix_pc/dist/pc/third/dig.js?'+__basePath[1]]
</script>

</html>
"""
response = etree.HTML(wb_data)
print response.xpath('//p[@class="content__title"]/text()')[0]
subtitile = response.xpath('//div[@class="content__subtitle"]')[0]
print subtitile.xpath('string(.)').strip()
print subtitile.xpath(".//i[position()=2]/text()")[0]

content__aside = response.xpath('.//div[@class="content__aside fr"]')[0]
print content__aside.xpath('.//p[@class="content__aside--title"]')[0].xpath('string(.)')
print int(content__aside.xpath('.//p[@class="content__aside--title"]/span/text()')[0])

sss = ""
for quote in content__aside.xpath('.//p[@class="content__aside--tags"]/i'):
    sss = sss + "/" +quote.xpath('string(.)')
print sss
content__article__table = content__aside.xpath('//ul[@class="content__aside__list"]/p[@class="content__article__table"]')[0]
pos1 = content__article__table.xpath('.//span[position()=1]')[0]
print pos1.xpath('concat(.//i/attribute::class, " ", string(.))')
print content__article__table.xpath('.//span[position()=2]/i/attribute::class')[0]
print content__article__table.xpath('.//span[position()=2]')[0].xpath('string(.)')
print content__article__table.xpath('.//span[position()=3]/i/attribute::class')[0]
print content__article__table.xpath('.//span[position()=3]')[0].xpath('string(.)')
print content__article__table.xpath('.//span[position()=4]/i/attribute::class')[0]
print content__article__table.xpath('.//span[position()=4]')[0].xpath('string(.)')


base_info = response.xpath('.//div[@class="content__article__info"]')[0]

for quote in base_info.xpath('.//ul/li[@class="fl oneline"]'):
    print quote.xpath("string(.)")


houseComment = response.xpath('.//p[@data-el="houseComment"]/attribute::data-desc')
if houseComment:
    print houseComment[0]

content__table = response.xpath('.//div[@id="deal"]')[0]
print content__table.xpath(".//h3/text()")[0]
for quote in content__table.xpath('.//div[@class="table"]/div'):
    print quote.xpath('string(.)')

for quote in response.xpath('.//div[@class="content__article__info4"]/ul/li'):
    print quote.xpath('.//span[position()=1]/text()')[0]
    print quote.xpath('.//span[position()=2]/text()')[0]

print response.xpath('//div[@class="bread__nav w1150"]/h1/a/@href')[0]
print response.xpath('//div[@class="bread__nav w1150"]/h1/a/text()')[0][:-2]
print response.xpath('//div[@class="bread__nav w1150"]/h1/a/@href')[0][8:-1]

