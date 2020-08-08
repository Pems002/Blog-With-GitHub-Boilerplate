---
layout: post
cid: 172
title: 基于Chromium的新版Edge体验报告
slug: 172
date: 2020/03/08 21:04:00
updated: 2020/04/17 21:14:06
status: publish
author: Sean
categories: 
  - 学记
tags: 
  - 体验
  - 新尝试
  - Browser
  - Microsoft
  - Edge
banner: https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/am/imageFileData/RE4ntrO
bannerascover: 1
bannerStyle: 0
excerpt: 抱紧微软爸爸的大腿，抛弃Chrome！
posttype: 0
showfullcontent: 0
showTOC: 0
---


从去年开始，由于占有率下滑，就一直听说微软已经开发了基于Chromium的新版Edge浏览器。据说当时放出消息时就可以下载Preview版本来试用了。

当时的我可能嫌麻烦（也有极大的可能就是懒 :@(害羞) ），没有下载使用。因为当时Chrome已经占据我PC、手机端。

>同步功能下的历史记录、收藏夹；我在电脑上未看完的内容可以进而推送到手机端继续查看；UI的简洁美观....

虽然绝大多数浏览器都能做到，但我也不晓得到底为什么这么喜欢Chrome，导致我自打全平台同步用了Chrome后，几乎不宠信我的『二儿子』**Firefox**了，只是偶尔在Firefox迭代了新的功能后，可能才会用一下它，不然Chrome必定作为首选。这次新版Edge的推出，也不难看出，未来微软想通过Windows版本迭代来取代之前的旧版Edge，以提高其占有率的决心，从而将流向Chrome的那一大部分用户拉回来。

不出意外，我也在1月份接触到了正式放出的Edge。当天的我正在刷着某小蓝软件<del>没想到吧，就是以“人在美国，刚下飞机”而著称的知乎</del>就看到某位专栏作家写到有关基于Chromium的Edge。在这之前的某些日子，可能Chrome感知到了新版Edge即将要发布了，就慌了神，开始变得异常卡顿 :@(尴尬) 当时的我好奇劲一下爆棚，想着见一见这脱胎换骨的新少侠。于是我就下载了新版的Edge在我的PC上。

打开[Edge的官网][1]『介绍新版Edge』褚在中央，同时也提供各个Windows版本以及其他操作系统的下载。定睛一看我发现，他居然是英文官网，emmm :@(想一想) 看来微软的决心还不够大阿，中文官网都不提供，这难道是不打算抢“蛋糕”了？
>截至写稿的今天，微软官方的Edge页面依旧是没有提供中文，微软中文的Support页也只提供了一篇指南：[下载基于 Chromium 的新版 Microsoft Edge][2]

![Edge官网.png][3]

不仅换了新的Logo，同时也摒弃了原先的UI风格，更换成类似Chrome的风格，但不同的是Chrome在版本跟新后就变得圆润了，而Edge的设计还是那么直，方正。这对刚从Chrome转来的我有了点震惊，我居然有些喜欢这个风格？ :@(小眼睛) 

跑偏了，体验浏览器居然被官网给带跑了，不过这个设计我还是喜欢的。 ::(真棒) 下载安装完后，可以选择直接从旧版的Edge导入信息，也可以从电脑内现已安装的浏览器（Chrome、Firefox导入数据）。仔细看你可以发现，其实他还是支持中文的，而且翻译工作也做得很充分，基本用户上手就可以使用。默认页集成了微软的每日聚焦，还有竖屏信息流。

![默认页信息.png][4]

怎么说呢，这点其实因人而异，有些人可能不太喜欢这种导航页，比如我一般打开浏览器习惯就是搜索，所以我将首页设置成了Bing，这个导航页我基本不用；但有些人就很需要这种链接+信息的导航页，因人而异，你也可以设置关闭这点微软还是很良心的。

再者，和Chrome不相上下的同步功能也是不错的，但目前只能同步收藏夹、设置、地址、密码等，历史记录、扩展及集锦（貌似是微软开发的新功能）即将上线。这时我大概理解了为什么连中文官网都没有，同步功能也不完善，可能是一个『公开抢先体验版』，未来应该就会上线了。

![同步.png][5]

![扩展.png][6]

由于采用Chromium作为内核，扩展插件上也是可以在Chrome的商店下载且直接安装在Edge内的，虽然微软暂时还没有开设属于Edge的官方商店，但相信未来肯定会完善这一块的。

虽然现在已经2020年了，但个别顽固倔强地网站还是选择使用FlashPlayer。这时，由于Edge没有完全优化好的缘故，在个别网站使用FlashPlayer时可能会显示如下问题

![Flash.png][7]

关于这个问题我也在CSDN上看到了解决方法，详细的解决方法可以前往CSDN页查看：[Win10 新版Edge浏览器Flash Player不兼容][8]

>原因可能为：微软使用的是谷歌浏览器内核内置的都是专门适用于 Chromium 浏览器的 NPAPI Adobe Flash Player 播放插件。而非谷歌浏览器即便调用相同的插件也会遭到流氓公司的劫持，导致出现地区不兼容提示再强迫用户安装广告版。

从这也可以看出，其实这次的Edge大概可以理解为微软放出的『正式体验版』，优化没有到位，个别问题还是存在。但我还是说一下这近2个月的使用体验，我这2个月以来一直在使用Edge，从原本的重度Chrome用户转变为Edge用户其实还是挺难的，主要是Chrome就那么巧的在Edge刚发布的那段时间抽风。体验不错，问题尚待解决，不过前期支持还是可以的，让我有新鲜感从Chrome转来，最后深深植根，可以看出微软还是可以做好的，毕竟从升级到Win10开始有Edge这个浏览器时，我从没有用过这么长时间，主要也可能是原来真的是很垃圾，被Chrome踩在地上摩擦，不过现在一看，未来局势大好，只要勤更新，加上Windows的版本更新，Edge的占有率未来还是很客观的。

最后推荐一下少数派的这篇文章：[微软全新 Edge 浏览器正式上线，尝鲜前你应该了解这些事][9]写的也不错，很多点我都没有写到，但我只是一个体验，不像人家细细的品啦 ::(勉强) 


  [1]: https://www.microsoft.com/en-us/edge
  [2]: https://support.microsoft.com/zh-cn/help/4501095/download-the-new-microsoft-edge-based-on-chromium
  [3]: https://www.imsean.cn/usr/uploads/2020/03/1493692009.png#vwid=1583&vhei=754
  [4]: https://www.imsean.cn/usr/uploads/2020/03/1201631825.png#vwid=1349&vhei=739
  [5]: https://www.imsean.cn/usr/uploads/2020/03/763491518.png#vwid=854&vhei=498
  [6]: https://www.imsean.cn/usr/uploads/2020/03/3704572937.png#vwid=608&vhei=44
  [7]: https://www.imsean.cn/usr/uploads/2020/03/2116615433.png#vwid=371&vhei=180
  [8]: https://blog.csdn.net/qq_45295475/article/details/104116575
  [9]: https://sspai.com/post/58490