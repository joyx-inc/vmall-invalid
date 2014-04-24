vmall
=====


微商场接口文档!	{#welcome}
=====================
----------
#签名算法
blablabla...

----------
#基础接口部分


初始化接口
---------

> 接口地址：api/<商场编号>/init?v=`<app版本号>`&uid=`<用户id>`
> 请求方式：GET
> 请求头：无

    //JSON结构
    {
        "mallId":"<商场id>",
        "mallCode":"<商场编号>",
        "mallName":"<商场名称>",
        "mallMapId":"<商场地图id>",
        "interfaceVersion":"<接口版本号>",
        "appName":"<app内部显示的名称>",    //待定！！
        "date":"<服务器当前时间>",          //主要用于秒杀活动等，客户端比较本地时间
        "isNewUser":<是否为新用户>,
        "secretKey":"<私钥>"                //如果isNewUser==true,则返回secretKey，否则secretKey为空
    }
    
免费WIFI接口？？
---------

> 接口地址：api/<商场编号>/wifi?v=`<app版本号>`&uid=`<用户id>`
> 请求方式：GET
> 请求头：Authorization:<签名串>


    //JSON结构
    {
        ??
    }

----------
#主页部分

主页面接口
---------
主页导航部分暂时写死，不通过接口返回！

> 接口地址：api/<商场编号>/main?v=`<app版本号>`&uid=`<用户id>`
> 请求方式：GET
> 请求头：Authorization:<签名串>

    //JSON结构
    {
        "slideShow":[                       //轮播
            {
                "itemType":"对象类型",      //  #1:优惠; 2:商户; 3: 商品; 4: 网页
                "itemId":"对象id",
                "picUrl":"图片地址"
                "link":"链接地址"           // itemType为4的时候才有值
            }
        ],
        "models":[                          //主页下方model部分
            {
                "modelType":"模块类型",     //模块类型必须是预先定好的！
                "modelTitle":"模块标题",     
                "modelItems":[              //不同模块对应不同对象结构
                    {？？},
                    {？？},
                    ...
                ]
            }
        ],
        date":"<服务器当前时间>"
    }

搜索接口
---------
**暂时只搜索优惠**
主要用于搜索接口，同时其他接口也可能重用，如：二维码、。。。

> 接口地址：api/<商场编号>/search?v=`<app版本号>`&uid=`<用户id>`&`<查询条件>`
> 请求方式：GET
> 请求头：Authorization:<签名串>

**查询条件：**


| key       |    类型   | required  | 描述  |
| :-------- | --------:| :--: | :-- |
| keyword  | string |  Y   |  关键字 或 一、二维码  |
| type     |   int |  Y   |  查询类型：0：关键字查询 ，1：一、二维码查询  |
| order      |    string | N  | 排序？？  |
| amount     |   int |  Y   |  每页条数  |
| page     |   int |  Y   |  请求的页数  |


    //JSON结构
    {
        "totalCount":<总页数>,
        "currentPage":<当前页>,
        "coupons":[                         //优惠列表
            {store:                         // 优惠对应的商户信息
                {
                title: '商户名称',
                logo: '商户LOGO',
                id: '商户ID',
                category: '商户类型'
                },
             id: '优惠ID',
             title: '优惠标题',
             type: '优惠类型',              // 1: 优惠活动; 2: 优惠券; 3: 团购;
             tag: '优惠标签',
             image: '优惠图',
             collectCount: '下载数',
             commentCount: '评论数',
             startTime: '开始时间',
             endTime: '结束时间'
             }

        ]
    }

----------

#优惠页面

优惠接口
---------

> 接口地址：api/<商场编号>/coupon?v=`<app版本号>`&uid=`<用户id>`&like=`<0：默认，1：关注的商户对应的优惠劵>`&`<查询参数>`
> 请求方式：GET
> 请求头：Authorization:<签名串>

**查询参数：**


| key       |    类型   | required  | 描述  |
| :-------- | --------:| :--: | :-- |
| cid  | string |  N   |  分类id  |
| order      |    string | N  | 排序  value:优惠、楼层、人气、名称
| amount     |   int |  Y   |  每页条数  |
| page     |   int |  Y   |  请求的页数  |


    //JSON结构
    {
        "totalCount":<总页数>,
        "currentPage":<当前页>,
        "coupons":[                         //优惠列表
            {store:                         // 优惠对应的商户信息
                {
                title: '商户名称',
                logo: '商户LOGO',
                id: '商户ID',
                category: '商户类型'
                },
             id: '优惠ID',
             title: '优惠标题',
             type: '优惠类型',              // 1: 优惠活动; 2: 优惠券; 3: 团购;
             tag: '优惠标签',
             image: '优惠图',
             collectCount: '下载数',
             commentCount: '评论数',
             startTime: '开始时间',
             endTime: '结束时间'
             }
        ]                    
    }


优惠详细信息接口
---------

> 接口地址：api/<商场编号>/coupon_detail?v=`<app版本号>`&uid=`<用户id>`&couponid=`<优惠id>`
> 请求方式：GET
> 请求头：Authorization:<签名串>


    //JSON结构
    {store:                         // 优惠对应的商户信息
        {
        title: '商户名称',
        logo: '商户LOGO',
        id: '商户ID',
        category: '商户类型',
        address: '商户地址',
        floor: '楼层',
        storeNo: '房间号',
        tel: '商户电话',
        mapid: '商户地址ID'
        },
     id: '优惠ID',
     title: '优惠标题',
     type: '优惠类型',              // 1: 优惠活动; 2: 优惠券; 3: 团购;
     tag: '优惠标签',
     images: ['优惠图'...],
     description: '详情',
     downloadLimit: '下载限制'      // 0: 不限制; 1: 限一次; -N: 一天N次,
     downloadCount: '下载次数',     // limit为0或1时,返回所有下载次数; limit为-N时,返回当天下载次数
     collectCount: '下载数',
     commentCount: '评论数',
     startTime: '开始时间',
     endTime: '结束时间',
     date":"<服务器当前时间>"
     }


#服务

服务列表接口
---------

> 接口地址：api/<商场编号>/services?v=`<app版本号>`&uid=`<用户id>`
> 请求方式：GET
> 请求头：Authorization:<签名串>

    //JSON结构
    [
        {服务对象},{服务对象},{服务对象},...
        {
            "itemType":"对象类型",      //  #1:内置功能; 0: 网页
            "itemId":"对象id",
            "picUrl":"图片地址"
            "link":"链接地址"           // itemType为0的时候才有值
        }
    ]

#商户

商户列表接口
---------

> 接口地址：api/<商场编号>/shop?v=`<app版本号>`&uid=`<用户id>`&like=`<0：默认，1：关注的商户>`&`<查询参数>`
> 请求方式：GET
> 请求头：Authorization:<签名串>

**查询参数：**


| key       |    类型   | required  | 描述  |
| :-------- | --------:| :--: | :-- |
| floor  | string |  N   |  楼层  |
| cid  | string |  N   |  分类id  |
| order      |    string | N  | 排序  value:优惠、楼层、人气、名称
| amount     |   int |  Y   |  每页条数  |
| page     |   int |  Y   |  请求的页数  |


    //JSON结构
    {
        "totalCount":<总页数>,
        "currentPage":<当前页>,
        "list":[                         //优惠列表
            {
            title: '商户名称',
            logo: '商户LOGO',
            id: '商户ID',
            category: '商户类型',
            floor: '楼层',
            storeNo: '商户房间号',
            followerCount: '关注人数'
            }...
        ]                    
    }

商户详细信息接口
---------

> 接口地址：api/<商场编号>/shop_detail?v=`<app版本号>`&uid=`<用户id>`&shopid=`<商户id>`
> 请求方式：GET
> 请求头：Authorization:<签名串>


    //JSON结构
    {                                       //商户对象
        <商户对象基本信息>,
        "coupons":[{商户发布的优惠劵},{商户发布的优惠劵},{商户发布的优惠劵},...],
        "comments"[{商户的评论信息},{商户的评论信息},{商户的评论信息},...]
    }

#我的信息

用户基本信息接口
---------

> 接口地址：api/<商场编号>/myinfo?v=`<app版本号>`&uid=`<用户id>`
> 请求方式：GET
> 请求头：Authorization:<签名串>


    //JSON结构
    [
        <用户基本信息>
    ]

修改用户基本信息接口
---------

> 接口地址：api/<商场编号>/myinfo?**update**&v=`<app版本号>`&uid=`<用户id>`
> 请求方式：**PUT**
> 请求头：Authorization:<签名串>
> 请求体：`{用户基本信息}`
> 
> **响应：**
response code:200 OK




我的优惠劵接口
---------


消费记录接口
---------


我关注的商家接口
---------

我关注的商品接口？？？
---------

我关注的优惠接口
---------

绑定手机接口
---------

绑定会员卡接口
---------

