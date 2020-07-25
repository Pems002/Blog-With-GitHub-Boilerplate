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
    "type": "git",
    "url": "https://github.com/Pems002/Maverick-Theme-Galileo.git",
    "branch": "latest"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "Pems002/Blog@gh-pages"
}

# 站点设置
site_name = "Sean's Blog"
site_logo = "https://cdn.jsdelivr.net/gh/Pems002/Blog@source/src/static/logo.JPG"
site_build_date = "2019-07-30T09:00+08:00"
author = "Sean"
email = "admin@imsean.cn"
author_homepage = "https://www.imsean.cn"
description = "乘风破浪"
key_words = ['Blog', 'Sean', 'Maverick']
language = 'zh-CN'
external_links = [
    {
        "name": "个人主页",
        "url": "https://www.imsean.cn",
        "brief": "Sean is here!"
    },
    {
        "name": "Notion页",
        "url": "https://home.imsean.cn",
        "brief": "Notion Work Space."
    },
    {
        "name": "Blog项目仓库",
        "url": "https://github.com/Pems002/Blog",
        "brief": "托管在Github上的项目。"
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
        "name": "关于我",
        "url": "${site_prefix}who-im-i/",
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
    }
]

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "MW3rej0gI05buDtSpAN15yi2-gzGzoHsz",
    "appKey": "g8BYYF25hHDXLNaTpptqumwL",
    "visitor": True,
    "recordIP": True
}

head_addon = r'''
<link rel="icon" href="https://cdn.jsdelivr.net/gh/Pems002/Blog@source/src/static/favicon.ico" type="image/x-icon" />
<link rel="shortcut icon" href="https://cdn.jsdelivr.net/gh/Pems002/Blog@source/src/static/favicon.ico" type="image/x-icon" />
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
