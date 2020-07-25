# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "Pems002/Blog@gh-pages"
}

# 站点设置
site_name = "Sean's Blog"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-07-30T09:00+08:00"
author = "Sean"
email = "admin@imsean.cn"
author_homepage = "https://www.imsean.cn"
description = "乘风破浪"
key_words = ['Blog', 'Sean', 'Maverick']
language = 'zh-CN'
external_links = [
    {
        "name": "Home Page",
        "url": "https://www.imsean.cn",
        "brief": "我的个人主页。"
    },
    {
        "name": "Notion页",
        "url": "https://home.imsean.cn",
        "brief": "Notion Work Space."
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Weibo",
        "url": "https://https://weibo.com/u/3225834177",
        "icon": "gi gi-weibo"
    },
    {
        "name": "Twitter",
        "url": "https://twitter.com/pems002",
        "icon": "gi gi-twitter"
    },
    {
        "name": "instagram",
        "url": "https://www.instagram.com/pems002",
        "icon": "gi gi-instagram"
    },
    {
        "name": "Github",
        "url": "https://github.com/pems002",
        "icon": "gi gi-github"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
