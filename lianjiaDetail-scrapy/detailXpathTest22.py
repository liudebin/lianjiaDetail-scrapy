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
	<meta name="description" content="贝壳上海租房网,提供整租 · 三林苑 3室1厅出租房源信息,此房源位于上海浦东三林的三林苑,3室86㎡5000元.找租房房源,就来上海贝壳租房!">
	<meta name="keywords" content="整租 · 三林苑 3室1厅,三林苑租房信息,上海浦东三林房屋出租">
	<meta http-equiv="Cache-Control" content="no-transform " />
	<title>整租 · 三林苑 3室1厅-三林苑租房信息-上海三林苑三林房屋出租【上海贝壳租房】</title>
	<link href="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/img/favicon.ico?_v=20181211213832d80" type="image/x-icon" rel="icon">
		<link rel="stylesheet" href="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/common/css/common.css?_v=20181211213832d80">
	  <script>
    var g_conf = {};
  </script>
    <link rel="stylesheet" href="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/page/detail/index.css?_v=20181211213832d80">
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
      <p class="content__title">整租 · 三林苑 3室1厅</p>

      <!-- 房源副标题 -->
      <div class="content__subtitle">
          <i class="hide">4人浏览 </i>房源上架时间 2018-11-05          <i class="house_code">房源编号：SH2118758042790002688</i>
          <!-- 发布人、发布机构入口 -->
                    <span class="content-right" data-el="showReportBox" data-event_id="10804" data-event_action="house_code=SH2118758042790002688">举报与反馈</span>
      </div>

      <!-- 房源左侧内容 -->
      <div class="content__article fl">

        <!-- 房源图片轮播图 -->
        <div class="content__article__slide" id="mySwipe">

          <!-- 房源大图 -->
          <ul class="content__article__slide__wrapper">
                                  <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="整租 · 三林苑 3室1厅" src="https://image1.ljcdn.com/rent-user-avatar/1338308e-2a3c-4dbf-a06e-50c3bbab288f.780x439.jpg" data-el="lazy-img" data-src="https://image1.ljcdn.com/rent-user-avatar/1338308e-2a3c-4dbf-a06e-50c3bbab288f.780x439.jpg" />
                          </div>
                        <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="整租 · 三林苑 3室1厅" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/780-439.png?_v=20181211213832d80" data-el="lazy-img" data-src="https://image1.ljcdn.com/rent-user-avatar/779b9d91-f911-4d98-9508-97b5a6b73631.780x439.jpg" />
                          </div>
                        <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="整租 · 三林苑 3室1厅" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/780-439.png?_v=20181211213832d80" data-el="lazy-img" data-src="https://image1.ljcdn.com/rent-user-avatar/780bfff6-e8a9-4715-933a-d7634d48e3ea.780x439.jpg" />
                          </div>
                        <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="整租 · 三林苑 3室1厅" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/780-439.png?_v=20181211213832d80" data-el="lazy-img" data-src="https://image1.ljcdn.com/rent-user-avatar/80bbbcea-8118-4167-aaa1-80c0dc2eb96f.780x439.jpg" />
                          </div>
                        <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="整租 · 三林苑 3室1厅" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/780-439.png?_v=20181211213832d80" data-el="lazy-img" data-src="https://image1.ljcdn.com/rent-user-avatar/bc2bb57e-6f10-4c5e-b567-02c0beecd42e.780x439.jpg" />
                          </div>
                        <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="整租 · 三林苑 3室1厅" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/780-439.png?_v=20181211213832d80" data-el="lazy-img" data-src="https://image1.ljcdn.com/rent-user-avatar/6ec30ec8-e0dd-4ed2-9002-b6c4b701fe1b.780x439.jpg" />
                          </div>
                        <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="整租 · 三林苑 3室1厅" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/780-439.png?_v=20181211213832d80" data-el="lazy-img" data-src="https://image1.ljcdn.com/rent-user-avatar/3d9552ae-b5a7-4a70-8448-d3b75fc0d578.780x439.jpg" />
                          </div>
                        <div class="content__article__slide__item" data-el="slideItem">
                              <img alt="整租 · 三林苑 3室1厅" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/780-439.png?_v=20181211213832d80" data-el="lazy-img" data-src="https://image1.ljcdn.com/rent-user-avatar/557ab322-fb45-4abd-8e3a-81511e989301.780x439.jpg" />
                          </div>
                                </ul>

          <!-- 房源缩略图 -->
          <div class="content__thumb--box">
            <ul class="content__article__slide--small content__article__slide_dot" data-el="prefix" id="prefix">
                                                <li class="active" data-index="0">
                    <img src="https://image1.ljcdn.com/rent-user-avatar/1338308e-2a3c-4dbf-a06e-50c3bbab288f.126x86.jpg">
                  </li>
                                  <li class="" data-index="1">
                    <img src="https://image1.ljcdn.com/rent-user-avatar/779b9d91-f911-4d98-9508-97b5a6b73631.126x86.jpg">
                  </li>
                                  <li class="" data-index="2">
                    <img src="https://image1.ljcdn.com/rent-user-avatar/780bfff6-e8a9-4715-933a-d7634d48e3ea.126x86.jpg">
                  </li>
                                  <li class="" data-index="3">
                    <img src="https://image1.ljcdn.com/rent-user-avatar/80bbbcea-8118-4167-aaa1-80c0dc2eb96f.126x86.jpg">
                  </li>
                                  <li class="" data-index="4">
                    <img src="https://image1.ljcdn.com/rent-user-avatar/bc2bb57e-6f10-4c5e-b567-02c0beecd42e.126x86.jpg">
                  </li>
                                  <li class="" data-index="5">
                    <img src="https://image1.ljcdn.com/rent-user-avatar/6ec30ec8-e0dd-4ed2-9002-b6c4b701fe1b.126x86.jpg">
                  </li>
                                  <li class="" data-index="6">
                    <img src="https://image1.ljcdn.com/rent-user-avatar/3d9552ae-b5a7-4a70-8448-d3b75fc0d578.126x86.jpg">
                  </li>
                                  <li class="" data-index="7">
                    <img src="https://image1.ljcdn.com/rent-user-avatar/557ab322-fb45-4abd-8e3a-81511e989301.126x86.jpg">
                  </li>
                                          </ul>
          </div>

          <!-- 图片切换按钮 -->
          <span class="content__article__slide--prev" data-el="prev"></span>
          <span class="content__article__slide--next" data-el="next"></span>

          <!-- 房源关注入口及hover浮层 -->
          <span class="content__article__slide--tips hide" data-el="getApp">关注的房源请在链家APP中查看</span>
          <span class="content__article__slide--button" data-type="house" data-id="SH2118758042790002688" data-el="checkWatch"><i class="heart"></i><span>关注房源</span></span>
        </div>

        <!-- 房源基本信息 -->
        <div class="content__article__info">
          <h3 id="info">房屋信息</h3>
          <ul>
            <li class="fl oneline">基本信息</li>
                          <li class="fl oneline">发布：1个月前</li>
                                        <li class="fl oneline">入住：随时入住</li>
                              <li class="fl oneline">&nbsp;</li>
                                        <li class="fl oneline">租期：1~2年</li>
                                        <li class="fl oneline">看房：随时可看</li>
                              <li class="fl oneline">&nbsp;</li>
                                        <li class="fl oneline">楼层：6/6层</li>
                                        <li class="fl oneline">电梯：无</li>
                              <li class="fl oneline">&nbsp;</li>
                                        <li class="fl oneline">车位：租用车位</li>
                                        <li class="fl oneline">用水：民水</li>
                              <li class="fl oneline">&nbsp;</li>
                                        <li class="fl oneline">用电：民电</li>
                                        <li class="fl oneline">燃气：有</li>
                              <li class="fl oneline">&nbsp;</li>
                                        <li class="fl oneline">采暖：自采暖</li>
                                    </ul>
        </div>

        <!-- 房源分割标识线，js里用到，勿删 -->
        <div class="info__line line"></div>

        <!-- 配套设施列表 -->
        <ul class="content__article__info2">
          <li class="fl oneline">配套设施</li>
                      <li class="fl oneline television "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/03401a4eddd82179ae3774b43e382238.1524906085686_abc8a9ce-3748-4317-9955-2452322f07d9);"></i>电视</li>
                      <li class="fl oneline refrigerator "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/f01e63a2d0b36d2b6b92269dac7210a8.1524905973505_6a9e4bde-4acb-4699-ba93-32f4dc13304a);"></i>冰箱</li>
                      <li class="fl oneline washing_machine "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/b45b25b8cbdbcbf1393999d1140d6729.1524906592660_dfa64012-e42c-4b11-a874-e2888e6dce4c);"></i>洗衣机</li>
                      <li class="fl oneline air_conditioner "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/2c5080db6cb434413d39fe816faddafe.1524906138308_77f21b82-5983-4448-8348-ef9346263338);"></i>空调</li>
                      <li class="fl oneline water_heater "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/82e5b44b21844b608071ac426a5eb7e6.1524906411157_ae925a22-d95e-48bf-975c-447a27dd4ce9);"></i>热水器</li>
                      <li class="fl oneline bed "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/c40aee40a80ebcaa8d716a2c9ae14391.1524906024762_ac4fb64e-8467-46de-b6f5-7f9ba1ce2622);"></i>床</li>
                      <li class="fl oneline heating_no "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/ce93a6cec4a601367fbd8f5d8760ecc8.1525926673137_fa39878e-9033-4494-9912-13c176c060ca);"></i>暖气</li>
                      <li class="fl oneline wifi "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/b2abaa59759a7f4ae327ed67c6fbc6d8.1524906246773_6b435b4a-03d6-4292-acd8-6d3af96a791d);"></i>宽带</li>
                      <li class="fl oneline wardrobe "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/b024f9fdd5797563ead74f237105fd5a.1524906626107_4b1c45fe-0266-40af-b39c-6311887b0aaa);"></i>衣柜</li>
                      <li class="fl oneline natural_gas "><i style="background-image: url(https://image1.ljcdn.com/rent-front-image/aa2df480d8496d0851febe38022b1da2.1524906515169_c731df5b-234f-4716-ba42-0058f833204c);"></i>天然气</li>
                  </ul>

        <!-- 房源描述数据 -->
                
        <!-- 描述展示 -->
                <div class="content__article__info3" id="desc">
          <h3>房源描述</h3>
          <ul>
                        
              <li class="">
                <!--im参数配置2. port 参数中判断 “lianjia / qita” 时，判断条件：1）若UCID为100开头，则传值 “lianjia” 2) 若UCID不为100开头，则传值 “qita”-->
                
                <!-- 判断show_booth是否为1 为1或未返回则显示，否则不显示-->
                                  <div>
                                          <i data-el="updateAvatar" data-houseCode="SH2118758042790002688" class="info3__icon"></i>
                                        <!-- <i class="info3__icon" style="background-image: url(https://image1.ljcdn.com/rent-user-avatar/cd7f63a5-198e-492c-9230-4bf5cbc65b8b)"></i> -->
                    <div>
                      <span data-el="updateName" data-houseCode="SH2118758042790002688">
                      </span>

                      <!-- 判断信息卡的房源，是否显示icon-->
                      <div class="duty-pic" data-el="updatePic" data-show_booth="1">
                        <!-- 显示icon-->
                        <span class="duty-icon" data-el="dutyCard"><!-- <img src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/detail/duty-com@2x.png?_v=20181211213832d80"> --></span>
                        <!-- hover时显示经纪人卡片-->
                        <div class="duty-pop" data-el="picList">
                        </div>
                      </div>

                      <!-- 显示im-->
                                              <span class="agent__im" data-el="callIM"  data-im_id="2400000000060228" data-id="SH2118758042790002688" data-type="house" data-info="2400000000060228" data-port="pc_qita_zufangplat_detail_house" data-brand="200306000002" data-title="[房源]3室1厅1卫，南 西南 北，86m²，5000元"></span>
                      
                    </div>

                    <p>
                       职业房东管家                      <span data-el="updatePhone" data-houseCode="SH2118758042790002688">10109666</span>
                    </p>
                  </div>
                
                <p data-el="houseComment" data-desc="11号线三林东站 旁边  三房一厅  看房方便 打电话联系 " class="threeline">11号线三林东站 旁边  三房一厅  看房方便 打电话联系 </p>
                <p class="detail__info--more" data-el="commentShowMore">查看更多<i class="more__icon up"></i></p>
              </li>
                                    </ul>
        </div>
        
      </div>

      <!-- 右侧黄金展位 -->
      <div class="content__aside fr" id="aside">

        <!-- 租金及支付方式 -->
        <p class="content__aside--title"><span>5000</span>元/月 (季付价)</p>
        
        <!-- 房源标签列表 -->
        <p class="content__aside--tags">
                  <i class="content__item__tag--is_subway_house" data-class="is_subway_house">近地铁</i>
                  <i class="content__item__tag--decoration" data-class="decoration">精装</i>
                  <i class="content__item__tag--free_brokerage_fee" data-class="free_brokerage_fee">免中介费</i>
                  <i class="content__item__tag--is_key" data-class="is_key">随时看房</i>
                </p>

        <!-- 房源户型、朝向、面积、租赁方式 -->
        <ul class="content__aside__list">
          <p class="content__article__table">
            <span><i class="house"></i>整租</span>
            <span><i class="typ"></i>3室1厅1卫</span>
            <span><i class="area"></i>86㎡</span>
            <span><i class="orient"></i>朝南 西南 北</span>
          </p>
        </ul>
        <!-- 经纪人信息，目前只展示一条信息 -->
                <ul class="content__aside__list">
                    <!-- 判断数据源 是否展示icon等信息-->
                                                        <li>
                  <!--im参数配置2. port 参数中判断 “lianjia / qita” 时，判断条件：1）若UCID为100开头，则传值 “lianjia” 2) 若UCID不为100开头，则传值 “qita”-->
                                    <span data-el="updateAvatar" data-houseCode="SH2118758042790002688" class="content__aside__list--icon"></span>
                  <div class="content__aside__list--title oneline">
                    <span class="contact_name" data-el="updateName" data-houseCode="SH2118758042790002688" title="房东"></span>
                      <!-- 判断信息卡的房源，是否显示icon-->
                      <div class="duty-pic" data-el="updatePic" data-show_booth="1">
                        <!-- 显示icon-->
                        <span class="duty-icon" data-el="dutyCard"></span>
                        <!-- hover时显示经纪人卡片-->
                        <div class="duty-pop" data-el="picList">
                        </div>
                      </div>

                                              <span class="contact__im" data-el="callIM" data-im_id="2400000000060228" data-info="2400000000060228" data-port="pc_qita_zufangplat_detail_house" data-brand="200306000002" data-id="SH2118758042790002688" data-type="house" data-title="[房源]3室1厅1卫，南 西南 北，86m²，5000元"></span>
                                        </div>
                  <p class="content__aside__list--subtitle oneline">
                    职业房东管家                  </p> 
                                  <p class="content__aside__list--bottom oneline" data-el="updatePhone" data-houseCode="SH2118758042790002688">10109666</p>
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
            <span>6号线 - 华夏西路</span>
            <span>1191m</span>
          </li>
                  <li>
            距离
            <span>11号线(迪士尼-花桥) - 三林</span>
            <span>934m</span>
          </li>
                  <li>
            距离
            <span>11号线(迪士尼-花桥) - 三林东</span>
            <span>150m</span>
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
        <a href="/zufang/SH2142415753440673792.html" target="_blank" data-event_id="10805" data-event_action="house_code=SH2142415753440673792&position=1"><img alt="/zufang/SH2142415753440673792.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=20181211213832d80" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/rent-house-1/c0280c9bffd89bccbeeede9cebbec8c5-1544230829349/d2bf2a3dc57ca5ed89ea0e2ed6e8aee9.jpg.250x182.jpg"></a>
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
        <a href="/zufang/SH2138234578861826048.html" target="_blank" data-event_id="10805" data-event_action="house_code=SH2138234578861826048&position=2"><img alt="/zufang/SH2138234578861826048.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=20181211213832d80" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/rent-user-avatar/fdab7ba1-5bff-44a1-a5a2-ef90d7d6b65d.250x182.jpg"></a>
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
        <a href="/zufang/SH2120928048827613184.html" target="_blank" data-event_id="10805" data-event_action="house_code=SH2120928048827613184&position=3"><img alt="/zufang/SH2120928048827613184.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=20181211213832d80" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/rent-user-avatar/9c0f6ef7-36b1-42d5-8531-48ea6d6c9d3b.250x182.jpg"></a>
        <p class="bottom__list--item__des">
          <span>
            <a href="/zufang/pudong" target="_blank">浦东</a> 
            - 
            <a href="/zufang/sanlin" target="_blank">三林</a>  
            三林苑          </span>
          <span class="bottom__list--item--hl fr">2300元/月</span> 
        </p>
        <p class="bottom__list--item__btm">
          3室1厅1卫 25㎡
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
        <a href="/zufang/SH2060055308939829248.html" target="_blank" data-event_id="10806" data-event_action="house_code=SH2060055308939829248&position=1"><img alt="/zufang/SH2060055308939829248.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=20181211213832d80" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/shfdfs-image/20160619/0dfaf917-9808-475c-8db1-97d64c54ff7e.jpg.250x182.jpg"></a>
        <p class="bottom__list--item__des">
          <span>
            <a href="/zufang/pudong" target="_blank">浦东</a> 
            - 
            <a href="/zufang/sanlin" target="_blank">三林</a>  
            恒大翰城瀚林苑          </span>
          <span class="bottom__list--item--hl fr">9800元/月</span> 
        </p>
        <p class="bottom__list--item__btm">
          4室2厅2卫 144㎡
        </p>
      </div>
          <div class="bottom__list--item">
        <a href="/zufang/SH2114948358857555968.html" target="_blank" data-event_id="10806" data-event_action="house_code=SH2114948358857555968&position=2"><img alt="/zufang/SH2114948358857555968.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=20181211213832d80" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/shfdfs-image/20160815/5dde636c-381f-4f49-b7ed-92cd8fe2bc40.jpg.250x182.jpg"></a>
        <p class="bottom__list--item__des">
          <span>
            <a href="/zufang/pudong" target="_blank">浦东</a> 
            - 
            <a href="/zufang/sanlin" target="_blank">三林</a>  
            金地湾流域(别墅)          </span>
          <span class="bottom__list--item--hl fr">25000元/月</span> 
        </p>
        <p class="bottom__list--item__btm">
          6室3厅4卫 309㎡
        </p>
      </div>
          <div class="bottom__list--item">
        <a href="/zufang/SH1917832630246842368.html" target="_blank" data-event_id="10806" data-event_action="house_code=SH1917832630246842368&position=3"><img alt="/zufang/SH1917832630246842368.html" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/363-274.png?_v=20181211213832d80" data-el="lazy-img" class="lazyload" data-src="https://image1.ljcdn.com/shfdfs-image/20161023/4819e7e3-08d3-4667-8341-2016ecc4d9e3.jpg.250x182.jpg"></a>
        <p class="bottom__list--item__des">
          <span>
            <a href="/zufang/pudong" target="_blank">浦东</a> 
            - 
            <a href="/zufang/sanlin" target="_blank">三林</a>  
            环球翡翠湾花园(公寓)          </span>
          <span class="bottom__list--item--hl fr">8600元/月</span> 
        </p>
        <p class="bottom__list--item__btm">
          3室2厅2卫 132㎡
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
                <li data-el="fixedNavItem" data-href="desc">房源描述</li>
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
            <span class="global__list--icon icon--200306000002"></span>
            <p class="global__list--title"><i data-el="updateName" data-houseCode="SH2118758042790002688"></i>（职业房东）<span class="fr" data-el="updatePhone" data-houseCode="SH2118758042790002688">&nbsp;</span></p>
            <p class="global__list--subtitle oneline"><span>5000</span>/月  押一付三</p>
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
    longitude: '121.5288861',
    latitude: '31.15013281'
  };
  g_conf.subway = [{"distance":1191,"lines":["6\u53f7\u7ebf"],"name":"\u534e\u590f\u897f\u8def","point_lat":31.154894,"point_lng":121.521457},{"distance":934,"lines":["11\u53f7\u7ebf(\u8fea\u58eb\u5c3c-\u82b1\u6865)"],"name":"\u4e09\u6797","point_lat":31.149017,"point_lng":121.517781},{"distance":150,"lines":["11\u53f7\u7ebf(\u8fea\u58eb\u5c3c-\u82b1\u6865)"],"name":"\u4e09\u6797\u4e1c","point_lat":31.153007,"point_lng":121.529401}];
  g_conf.name = '三林苑';
  g_conf.houseCode = 'SH2118758042790002688';
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
                <i></i><img src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/img/wxapp.jpg?_v=20181211213832d80" alt="下载掌上链家" width="94">
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
                      <li><a href="https://sy.lianjia.com/zufang/">沈阳租房</a></li>
                      <li><a href="https://cd.lianjia.com/zufang/">成都租房</a></li>
                      <li><a href="https://sx.lianjia.com/zufang/">绍兴租房</a></li>
                      <li><a href="https://cq.lianjia.com/zufang/">重庆租房</a></li>
                      <li><a href="https://nj.lianjia.com/zufang/">南京租房</a></li>
                      <li><a href="https://zh.lianjia.com/zufang/">珠海租房</a></li>
                      <li><a href="https://taizhou.lianjia.com/zufang/">台州租房</a></li>
                      <li><a href="https://nb.lianjia.com/zufang/">宁波租房</a></li>
                      <li><a href="https://hk.lianjia.com/zufang/">海口租房</a></li>
                      <li><a href="https://jx.lianjia.com/zufang/">嘉兴租房</a></li>
                      <li><a href="https://ty.lianjia.com/zufang/">太原租房</a></li>
                      <li><a href="https://xan.lianjia.com/zufang/">雄安新区租房</a></li>
                      <li><a href="https://zz.lianjia.com/zufang/">郑州租房</a></li>
                      <li><a href="https://cc.lianjia.com/zufang/">长春租房</a></li>
                      <li><a href="https://qd.lianjia.com/zufang/">青岛租房</a></li>
                      <li><a href="https://sjz.lianjia.com/zufang/">石家庄租房</a></li>
                      <li><a href="https://liangshan.lianjia.com/zufang/">凉山租房</a></li>
                      <li><a href="https://kf.lianjia.com/zufang/">开封租房</a></li>
                      <li><a href="https://km.lianjia.com/zufang/">昆明租房</a></li>
                      <li><a href="https://xm.lianjia.com/zufang/">厦门租房</a></li>
                      <li><a href="https://hui.lianjia.com/zufang/">惠州租房</a></li>
                      <li><a href="https://jn.lianjia.com/zufang/">济南租房</a></li>
                      <li><a href="https://bj.lianjia.com/zufang/">北京租房</a></li>
                      <li><a href="https://wh.lianjia.com/zufang/">武汉租房</a></li>
                      <li><a href="https://ganzhou.lianjia.com/zufang/">赣州租房</a></li>
                      <li><a href="https://cs.lianjia.com/zufang/">长沙租房</a></li>
                      <li><a href="https://wx.lianjia.com/zufang/">无锡租房</a></li>
                      <li><a href="https://fs.lianjia.com/zufang/">佛山租房</a></li>
                      <li><a href="https://gz.lianjia.com/zufang/">广州租房</a></li>
                      <li><a href="https://changzhou.lianjia.com/zufang/">常州租房</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                      <li><a href="https://sh.lianjia.com/zufang/xintiandi/">新天地租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/xuanqiao/">宣桥租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/caojiadu/">曹家渡租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/malu/">马陆租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/chongmingxincheng/">崇明新城租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/chongmingqita/">崇明其它租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/nanjingxilu/">南京西路租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/mangu/">曼谷租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/riben/">日本租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/maqiao/">马桥租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/gaojing/">高境租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/tangzhen/">唐镇租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/chenjiazhen/">陈家镇租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/xuxing/">徐行租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/gaohang/">高行租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/kunshan1/">昆山租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/jinganxincheng/">静安新城租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/jiuting/">九亭租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/lianyang/">联洋租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/hongqiao1/">虹桥租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/yangdong/">杨东租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/renminguangchang/">人民广场租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/zhuanghang/">庄行租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/jinhui/">金汇租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/xianghuaqiao/">香花桥租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/xietulu/">斜土路租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/haiwan/">海湾租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/jiadingxincheng/">嘉定新城租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/xinjiangwancheng/">新江湾城租房</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/zhenguang/">真光租房</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                      <li><a href="https://sh.lianjia.com/zufang/c5011000017738/">仓库静安区</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000017869/">天吉小区</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000016294/">中房华东大厦</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000018276/">福海公寓</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000015351/">凯旋公寓</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000014545/">马桥公寓</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000016434/">大木桥路456号</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000018549/">桂景苑</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000017646/">云台大厦</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000017628/">元和投资大厦</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000016231/">华升公寓</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000016666/">鼎邦丽池(公寓)</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000017636/">亭园大厦</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000017630/">宝莲城</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000016667/">建德坊</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000014173/">蓝村小区</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000015023/">银城大厦</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000016607/">欣怡小区</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000014700/">俞二小区</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000017366/">赵家宅小区</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000016177/">贵人大厦</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000018263/">联洋花园(一期)</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000014187/">上虹新村</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011102207375/">长青企业广场</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000020399/">平顺路721弄</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000014515/">华庭雅居</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000016575/">中二小区</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000017863/">涵养村</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000013726/">浦坊大楼</a></li>
                      <li><a href="https://sh.lianjia.com/zufang/c5011000018703/">淮海西路346弄</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                      <li><a href="https://xm.fang.lianjia.com/">厦门楼盘</a></li>
                      <li><a href="https://san.fang.lianjia.com/">三亚楼盘</a></li>
                      <li><a href="https://wuhu.fang.lianjia.com/">芜湖楼盘</a></li>
                      <li><a href="https://ganzhou.fang.lianjia.com/">赣州楼盘</a></li>
                      <li><a href="https://zh.fang.lianjia.com/">珠海楼盘</a></li>
                      <li><a href="https://sz.fang.lianjia.com/">深圳楼盘</a></li>
                      <li><a href="https://cq.fang.lianjia.com/">重庆楼盘</a></li>
                      <li><a href="https://ty.fang.lianjia.com/">太原楼盘</a></li>
                      <li><a href="https://qd.fang.lianjia.com/">青岛楼盘</a></li>
                      <li><a href="https://lf.fang.lianjia.com/">廊坊楼盘</a></li>
                      <li><a href="https://liangshan.fang.lianjia.com/">凉山楼盘</a></li>
                      <li><a href="https://taizhou.fang.lianjia.com/">台州楼盘</a></li>
                      <li><a href="https://zz.fang.lianjia.com/">郑州楼盘</a></li>
                      <li><a href="https://cd.fang.lianjia.com/">成都楼盘</a></li>
                      <li><a href="https://zs.fang.lianjia.com/">中山楼盘</a></li>
                      <li><a href="https://zj.fang.lianjia.com/">镇江楼盘</a></li>
                      <li><a href="https://jian.fang.lianjia.com/">吉安楼盘</a></li>
                      <li><a href="https://cc.fang.lianjia.com/">长春楼盘</a></li>
                      <li><a href="https://bj.fang.lianjia.com/">北京楼盘</a></li>
                      <li><a href="https://sjz.fang.lianjia.com/">石家庄楼盘</a></li>
                      <li><a href="https://wx.fang.lianjia.com/">无锡楼盘</a></li>
                      <li><a href="https://xan.fang.lianjia.com/">雄安新区楼盘</a></li>
                      <li><a href="https://cs.fang.lianjia.com/">长沙楼盘</a></li>
                      <li><a href="https://yt.fang.lianjia.com/">烟台楼盘</a></li>
                      <li><a href="https://dg.fang.lianjia.com/">东莞楼盘</a></li>
                      <li><a href="https://gy.fang.lianjia.com/">贵阳楼盘</a></li>
                      <li><a href="https://hui.fang.lianjia.com/">惠州楼盘</a></li>
                      <li><a href="https://kf.fang.lianjia.com/">开封楼盘</a></li>
                      <li><a href="https://sy.fang.lianjia.com/">沈阳楼盘</a></li>
                      <li><a href="https://sh.fang.lianjia.com/">上海楼盘</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                      <li><a href="https://yt.ke.com/ershoufang/">烟台二手房</a></li>
                      <li><a href="https://km.ke.com/ershoufang/">昆明二手房</a></li>
                      <li><a href="https://wh.ke.com/ershoufang/">武汉二手房</a></li>
                      <li><a href="https://jx.ke.com/ershoufang/">嘉兴二手房</a></li>
                      <li><a href="https://xm.ke.com/ershoufang/">厦门二手房</a></li>
                      <li><a href="https://taizhou.ke.com/ershoufang/">台州二手房</a></li>
                      <li><a href="https://zs.ke.com/ershoufang/">中山二手房</a></li>
                      <li><a href="https://zj.ke.com/ershoufang/">镇江二手房</a></li>
                      <li><a href="https://jl.ke.com/ershoufang/">吉林二手房</a></li>
                      <li><a href="https://xa.ke.com/ershoufang/">西安二手房</a></li>
                      <li><a href="https://hz.ke.com/ershoufang/">杭州二手房</a></li>
                      <li><a href="https://tj.ke.com/ershoufang/">天津二手房</a></li>
                      <li><a href="https://dg.ke.com/ershoufang/">东莞二手房</a></li>
                      <li><a href="https://dl.ke.com/ershoufang/">大连二手房</a></li>
                      <li><a href="https://wuhu.ke.com/ershoufang/">芜湖二手房</a></li>
                      <li><a href="https://hui.ke.com/ershoufang/">惠州二手房</a></li>
                      <li><a href="https://bj.ke.com/ershoufang/">北京二手房</a></li>
                      <li><a href="https://cs.ke.com/ershoufang/">长沙二手房</a></li>
                      <li><a href="https://jian.ke.com/ershoufang/">吉安二手房</a></li>
                      <li><a href="https://lf.ke.com/ershoufang/">廊坊二手房</a></li>
                      <li><a href="https://liangshan.ke.com/ershoufang/">凉山二手房</a></li>
                      <li><a href="https://jn.ke.com/ershoufang/">济南二手房</a></li>
                      <li><a href="https://sh.ke.com/ershoufang/">上海二手房</a></li>
                      <li><a href="https://changzhou.ke.com/ershoufang/">常州二手房</a></li>
                      <li><a href="https://xan.ke.com/ershoufang/">雄安新区二手房</a></li>
                      <li><a href="https://cd.ke.com/ershoufang/">成都二手房</a></li>
                      <li><a href="https://gz.ke.com/ershoufang/">广州二手房</a></li>
                      <li><a href="https://sz.ke.com/ershoufang/">深圳二手房</a></li>
                      <li><a href="https://ty.ke.com/ershoufang/">太原二手房</a></li>
                      <li><a href="https://ganzhou.ke.com/ershoufang/">赣州二手房</a></li>
                  </ul>
               <ul data-el="childrenList"  >
                  </ul>
           </div>

    <div class="footer__bottom">
      <p>链家网（北京）科技有限公司 | 网络经营许可证 京ICP备16057509号-2 | &copy; Copyright&copy;2010-2018 链家网Lianjia.com版权所有</p>
      <a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010802024019" style="display:inline-block;text-decoration:none;height:20px;line-height:20px;"><img style="margin-right: 5px;" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/img/beian.png?_v=20181211213832d80">京公网安备 11010802024019号</a>
    </div>

  </div>
</div>

<script type="text/javascript">
  var footerList = JSON.parse(JSON.stringify([{"abbr":"zfcs","expire":"2018-12-15 23:00:01","city_id":"310000","children":[{"url":"https:\/\/sy.lianjia.com\/zufang\/","title":"\u6c88\u9633\u79df\u623f"},{"url":"https:\/\/cd.lianjia.com\/zufang\/","title":"\u6210\u90fd\u79df\u623f"},{"url":"https:\/\/sx.lianjia.com\/zufang\/","title":"\u7ecd\u5174\u79df\u623f"},{"url":"https:\/\/cq.lianjia.com\/zufang\/","title":"\u91cd\u5e86\u79df\u623f"},{"url":"https:\/\/nj.lianjia.com\/zufang\/","title":"\u5357\u4eac\u79df\u623f"},{"url":"https:\/\/zh.lianjia.com\/zufang\/","title":"\u73e0\u6d77\u79df\u623f"},{"url":"https:\/\/taizhou.lianjia.com\/zufang\/","title":"\u53f0\u5dde\u79df\u623f"},{"url":"https:\/\/nb.lianjia.com\/zufang\/","title":"\u5b81\u6ce2\u79df\u623f"},{"url":"https:\/\/hk.lianjia.com\/zufang\/","title":"\u6d77\u53e3\u79df\u623f"},{"url":"https:\/\/jx.lianjia.com\/zufang\/","title":"\u5609\u5174\u79df\u623f"},{"url":"https:\/\/ty.lianjia.com\/zufang\/","title":"\u592a\u539f\u79df\u623f"},{"url":"https:\/\/xan.lianjia.com\/zufang\/","title":"\u96c4\u5b89\u65b0\u533a\u79df\u623f"},{"url":"https:\/\/zz.lianjia.com\/zufang\/","title":"\u90d1\u5dde\u79df\u623f"},{"url":"https:\/\/cc.lianjia.com\/zufang\/","title":"\u957f\u6625\u79df\u623f"},{"url":"https:\/\/qd.lianjia.com\/zufang\/","title":"\u9752\u5c9b\u79df\u623f"},{"url":"https:\/\/sjz.lianjia.com\/zufang\/","title":"\u77f3\u5bb6\u5e84\u79df\u623f"},{"url":"https:\/\/liangshan.lianjia.com\/zufang\/","title":"\u51c9\u5c71\u79df\u623f"},{"url":"https:\/\/kf.lianjia.com\/zufang\/","title":"\u5f00\u5c01\u79df\u623f"},{"url":"https:\/\/km.lianjia.com\/zufang\/","title":"\u6606\u660e\u79df\u623f"},{"url":"https:\/\/xm.lianjia.com\/zufang\/","title":"\u53a6\u95e8\u79df\u623f"},{"url":"https:\/\/hui.lianjia.com\/zufang\/","title":"\u60e0\u5dde\u79df\u623f"},{"url":"https:\/\/jn.lianjia.com\/zufang\/","title":"\u6d4e\u5357\u79df\u623f"},{"url":"https:\/\/bj.lianjia.com\/zufang\/","title":"\u5317\u4eac\u79df\u623f"},{"url":"https:\/\/wh.lianjia.com\/zufang\/","title":"\u6b66\u6c49\u79df\u623f"},{"url":"https:\/\/ganzhou.lianjia.com\/zufang\/","title":"\u8d63\u5dde\u79df\u623f"},{"url":"https:\/\/cs.lianjia.com\/zufang\/","title":"\u957f\u6c99\u79df\u623f"},{"url":"https:\/\/wx.lianjia.com\/zufang\/","title":"\u65e0\u9521\u79df\u623f"},{"url":"https:\/\/fs.lianjia.com\/zufang\/","title":"\u4f5b\u5c71\u79df\u623f"},{"url":"https:\/\/gz.lianjia.com\/zufang\/","title":"\u5e7f\u5dde\u79df\u623f"},{"url":"https:\/\/changzhou.lianjia.com\/zufang\/","title":"\u5e38\u5dde\u79df\u623f"}],"title":"\u79df\u623f\u57ce\u5e02","class":""},{"abbr":"rmsq","expire":"2018-12-15 23:00:01","city_id":"310000","children":[{"url":"https:\/\/sh.lianjia.com\/zufang\/xintiandi\/","title":"\u65b0\u5929\u5730\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/xuanqiao\/","title":"\u5ba3\u6865\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/caojiadu\/","title":"\u66f9\u5bb6\u6e21\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/malu\/","title":"\u9a6c\u9646\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/chongmingxincheng\/","title":"\u5d07\u660e\u65b0\u57ce\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/chongmingqita\/","title":"\u5d07\u660e\u5176\u5b83\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/nanjingxilu\/","title":"\u5357\u4eac\u897f\u8def\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/mangu\/","title":"\u66fc\u8c37\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/riben\/","title":"\u65e5\u672c\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/maqiao\/","title":"\u9a6c\u6865\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/gaojing\/","title":"\u9ad8\u5883\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/tangzhen\/","title":"\u5510\u9547\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/chenjiazhen\/","title":"\u9648\u5bb6\u9547\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/xuxing\/","title":"\u5f90\u884c\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/gaohang\/","title":"\u9ad8\u884c\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/kunshan1\/","title":"\u6606\u5c71\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/jinganxincheng\/","title":"\u9759\u5b89\u65b0\u57ce\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/jiuting\/","title":"\u4e5d\u4ead\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/lianyang\/","title":"\u8054\u6d0b\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/hongqiao1\/","title":"\u8679\u6865\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/yangdong\/","title":"\u6768\u4e1c\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/renminguangchang\/","title":"\u4eba\u6c11\u5e7f\u573a\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/zhuanghang\/","title":"\u5e84\u884c\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/jinhui\/","title":"\u91d1\u6c47\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/xianghuaqiao\/","title":"\u9999\u82b1\u6865\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/xietulu\/","title":"\u659c\u571f\u8def\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/haiwan\/","title":"\u6d77\u6e7e\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/jiadingxincheng\/","title":"\u5609\u5b9a\u65b0\u57ce\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/xinjiangwancheng\/","title":"\u65b0\u6c5f\u6e7e\u57ce\u79df\u623f"},{"url":"https:\/\/sh.lianjia.com\/zufang\/zhenguang\/","title":"\u771f\u5149\u79df\u623f"}],"title":"\u70ed\u95e8\u5546\u5708","class":""},{"abbr":"tjxq","expire":"2018-12-15 23:00:01","city_id":"310000","children":[{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000017738\/","title":"\u4ed3\u5e93\u9759\u5b89\u533a"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000017869\/","title":"\u5929\u5409\u5c0f\u533a"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000016294\/","title":"\u4e2d\u623f\u534e\u4e1c\u5927\u53a6"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000018276\/","title":"\u798f\u6d77\u516c\u5bd3"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000015351\/","title":"\u51ef\u65cb\u516c\u5bd3"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000014545\/","title":"\u9a6c\u6865\u516c\u5bd3"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000016434\/","title":"\u5927\u6728\u6865\u8def456\u53f7"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000018549\/","title":"\u6842\u666f\u82d1"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000017646\/","title":"\u4e91\u53f0\u5927\u53a6"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000017628\/","title":"\u5143\u548c\u6295\u8d44\u5927\u53a6"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000016231\/","title":"\u534e\u5347\u516c\u5bd3"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000016666\/","title":"\u9f0e\u90a6\u4e3d\u6c60(\u516c\u5bd3)"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000017636\/","title":"\u4ead\u56ed\u5927\u53a6"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000017630\/","title":"\u5b9d\u83b2\u57ce"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000016667\/","title":"\u5efa\u5fb7\u574a"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000014173\/","title":"\u84dd\u6751\u5c0f\u533a"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000015023\/","title":"\u94f6\u57ce\u5927\u53a6"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000016607\/","title":"\u6b23\u6021\u5c0f\u533a"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000014700\/","title":"\u4fde\u4e8c\u5c0f\u533a"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000017366\/","title":"\u8d75\u5bb6\u5b85\u5c0f\u533a"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000016177\/","title":"\u8d35\u4eba\u5927\u53a6"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000018263\/","title":"\u8054\u6d0b\u82b1\u56ed(\u4e00\u671f)"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000014187\/","title":"\u4e0a\u8679\u65b0\u6751"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011102207375\/","title":"\u957f\u9752\u4f01\u4e1a\u5e7f\u573a"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000020399\/","title":"\u5e73\u987a\u8def721\u5f04"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000014515\/","title":"\u534e\u5ead\u96c5\u5c45"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000016575\/","title":"\u4e2d\u4e8c\u5c0f\u533a"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000017863\/","title":"\u6db5\u517b\u6751"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000013726\/","title":"\u6d66\u574a\u5927\u697c"},{"url":"https:\/\/sh.lianjia.com\/zufang\/c5011000018703\/","title":"\u6dee\u6d77\u897f\u8def346\u5f04"}],"title":"\u63a8\u8350\u5c0f\u533a","class":""},{"abbr":"csxf","expire":"2018-12-15 23:00:01","city_id":"310000","children":[{"url":"https:\/\/xm.fang.lianjia.com\/","title":"\u53a6\u95e8\u697c\u76d8"},{"url":"https:\/\/san.fang.lianjia.com\/","title":"\u4e09\u4e9a\u697c\u76d8"},{"url":"https:\/\/wuhu.fang.lianjia.com\/","title":"\u829c\u6e56\u697c\u76d8"},{"url":"https:\/\/ganzhou.fang.lianjia.com\/","title":"\u8d63\u5dde\u697c\u76d8"},{"url":"https:\/\/zh.fang.lianjia.com\/","title":"\u73e0\u6d77\u697c\u76d8"},{"url":"https:\/\/sz.fang.lianjia.com\/","title":"\u6df1\u5733\u697c\u76d8"},{"url":"https:\/\/cq.fang.lianjia.com\/","title":"\u91cd\u5e86\u697c\u76d8"},{"url":"https:\/\/ty.fang.lianjia.com\/","title":"\u592a\u539f\u697c\u76d8"},{"url":"https:\/\/qd.fang.lianjia.com\/","title":"\u9752\u5c9b\u697c\u76d8"},{"url":"https:\/\/lf.fang.lianjia.com\/","title":"\u5eca\u574a\u697c\u76d8"},{"url":"https:\/\/liangshan.fang.lianjia.com\/","title":"\u51c9\u5c71\u697c\u76d8"},{"url":"https:\/\/taizhou.fang.lianjia.com\/","title":"\u53f0\u5dde\u697c\u76d8"},{"url":"https:\/\/zz.fang.lianjia.com\/","title":"\u90d1\u5dde\u697c\u76d8"},{"url":"https:\/\/cd.fang.lianjia.com\/","title":"\u6210\u90fd\u697c\u76d8"},{"url":"https:\/\/zs.fang.lianjia.com\/","title":"\u4e2d\u5c71\u697c\u76d8"},{"url":"https:\/\/zj.fang.lianjia.com\/","title":"\u9547\u6c5f\u697c\u76d8"},{"url":"https:\/\/jian.fang.lianjia.com\/","title":"\u5409\u5b89\u697c\u76d8"},{"url":"https:\/\/cc.fang.lianjia.com\/","title":"\u957f\u6625\u697c\u76d8"},{"url":"https:\/\/bj.fang.lianjia.com\/","title":"\u5317\u4eac\u697c\u76d8"},{"url":"https:\/\/sjz.fang.lianjia.com\/","title":"\u77f3\u5bb6\u5e84\u697c\u76d8"},{"url":"https:\/\/wx.fang.lianjia.com\/","title":"\u65e0\u9521\u697c\u76d8"},{"url":"https:\/\/xan.fang.lianjia.com\/","title":"\u96c4\u5b89\u65b0\u533a\u697c\u76d8"},{"url":"https:\/\/cs.fang.lianjia.com\/","title":"\u957f\u6c99\u697c\u76d8"},{"url":"https:\/\/yt.fang.lianjia.com\/","title":"\u70df\u53f0\u697c\u76d8"},{"url":"https:\/\/dg.fang.lianjia.com\/","title":"\u4e1c\u839e\u697c\u76d8"},{"url":"https:\/\/gy.fang.lianjia.com\/","title":"\u8d35\u9633\u697c\u76d8"},{"url":"https:\/\/hui.fang.lianjia.com\/","title":"\u60e0\u5dde\u697c\u76d8"},{"url":"https:\/\/kf.fang.lianjia.com\/","title":"\u5f00\u5c01\u697c\u76d8"},{"url":"https:\/\/sy.fang.lianjia.com\/","title":"\u6c88\u9633\u697c\u76d8"},{"url":"https:\/\/sh.fang.lianjia.com\/","title":"\u4e0a\u6d77\u697c\u76d8"}],"title":"\u57ce\u5e02\u65b0\u623f","class":""},{"abbr":"csesf","expire":"2018-12-15 23:00:01","city_id":"310000","children":[{"url":"https:\/\/yt.ke.com\/ershoufang\/","title":"\u70df\u53f0\u4e8c\u624b\u623f"},{"url":"https:\/\/km.ke.com\/ershoufang\/","title":"\u6606\u660e\u4e8c\u624b\u623f"},{"url":"https:\/\/wh.ke.com\/ershoufang\/","title":"\u6b66\u6c49\u4e8c\u624b\u623f"},{"url":"https:\/\/jx.ke.com\/ershoufang\/","title":"\u5609\u5174\u4e8c\u624b\u623f"},{"url":"https:\/\/xm.ke.com\/ershoufang\/","title":"\u53a6\u95e8\u4e8c\u624b\u623f"},{"url":"https:\/\/taizhou.ke.com\/ershoufang\/","title":"\u53f0\u5dde\u4e8c\u624b\u623f"},{"url":"https:\/\/zs.ke.com\/ershoufang\/","title":"\u4e2d\u5c71\u4e8c\u624b\u623f"},{"url":"https:\/\/zj.ke.com\/ershoufang\/","title":"\u9547\u6c5f\u4e8c\u624b\u623f"},{"url":"https:\/\/jl.ke.com\/ershoufang\/","title":"\u5409\u6797\u4e8c\u624b\u623f"},{"url":"https:\/\/xa.ke.com\/ershoufang\/","title":"\u897f\u5b89\u4e8c\u624b\u623f"},{"url":"https:\/\/hz.ke.com\/ershoufang\/","title":"\u676d\u5dde\u4e8c\u624b\u623f"},{"url":"https:\/\/tj.ke.com\/ershoufang\/","title":"\u5929\u6d25\u4e8c\u624b\u623f"},{"url":"https:\/\/dg.ke.com\/ershoufang\/","title":"\u4e1c\u839e\u4e8c\u624b\u623f"},{"url":"https:\/\/dl.ke.com\/ershoufang\/","title":"\u5927\u8fde\u4e8c\u624b\u623f"},{"url":"https:\/\/wuhu.ke.com\/ershoufang\/","title":"\u829c\u6e56\u4e8c\u624b\u623f"},{"url":"https:\/\/hui.ke.com\/ershoufang\/","title":"\u60e0\u5dde\u4e8c\u624b\u623f"},{"url":"https:\/\/bj.ke.com\/ershoufang\/","title":"\u5317\u4eac\u4e8c\u624b\u623f"},{"url":"https:\/\/cs.ke.com\/ershoufang\/","title":"\u957f\u6c99\u4e8c\u624b\u623f"},{"url":"https:\/\/jian.ke.com\/ershoufang\/","title":"\u5409\u5b89\u4e8c\u624b\u623f"},{"url":"https:\/\/lf.ke.com\/ershoufang\/","title":"\u5eca\u574a\u4e8c\u624b\u623f"},{"url":"https:\/\/liangshan.ke.com\/ershoufang\/","title":"\u51c9\u5c71\u4e8c\u624b\u623f"},{"url":"https:\/\/jn.ke.com\/ershoufang\/","title":"\u6d4e\u5357\u4e8c\u624b\u623f"},{"url":"https:\/\/sh.ke.com\/ershoufang\/","title":"\u4e0a\u6d77\u4e8c\u624b\u623f"},{"url":"https:\/\/changzhou.ke.com\/ershoufang\/","title":"\u5e38\u5dde\u4e8c\u624b\u623f"},{"url":"https:\/\/xan.ke.com\/ershoufang\/","title":"\u96c4\u5b89\u65b0\u533a\u4e8c\u624b\u623f"},{"url":"https:\/\/cd.ke.com\/ershoufang\/","title":"\u6210\u90fd\u4e8c\u624b\u623f"},{"url":"https:\/\/gz.ke.com\/ershoufang\/","title":"\u5e7f\u5dde\u4e8c\u624b\u623f"},{"url":"https:\/\/sz.ke.com\/ershoufang\/","title":"\u6df1\u5733\u4e8c\u624b\u623f"},{"url":"https:\/\/ty.ke.com\/ershoufang\/","title":"\u592a\u539f\u4e8c\u624b\u623f"},{"url":"https:\/\/ganzhou.ke.com\/ershoufang\/","title":"\u8d63\u5dde\u4e8c\u624b\u623f"}],"title":"\u57ce\u5e02\u4e8c\u624b\u623f","class":""},{"abbr":"yqlj","title":"\u53cb\u60c5\u94fe\u63a5","city_id":"310000","expire":"2018-12-12","children":[]}]))

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

<script type="text/javascript" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/common/js/common.js?_v=20181211213832d80"></script>

<script type="text/javascript">
  //引入脚本后
  var imConf = {
          "ajaxroot": "\/\/ajax.api.ke.com\/",
          "imAppid": "ZULIN_WEB_20181122",
          "imAppkey": "0a4e8669fc2a50cbbeeb969726a7ab46"
      };
</script>
<script>
var __basePath = 'https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src?_v=20181211213832d80'.split("?");
require.config({
  baseUrl: __basePath[0],
  paths: {
  },
  urlArgs:  __basePath[1]
});
var config = {"fe_root":"https:\/\/s1.ljcdn.com\/matrix_lianjia_pc\/dist\/pc","version":"20181211213832d80","js_ns":"m_pages_zufangDetail","cur_city_id":"310000","cur_city_name":"\u4e0a\u6d77","cur_city_short":"sh"};
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


content__aside = response.xpath('.//div[@class="content__aside fr"]')[0]
print content__aside.xpath('.//p[@class="content__aside--title"]')[0].xpath('string(.)')
print content__aside.xpath('.//p[@class="content__aside--title"]/span/text()')[0]

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