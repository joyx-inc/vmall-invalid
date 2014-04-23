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

> 接口地址：api/init?v=`<app版本号>`&mid=`<商场id>`&uid=`<用户id>`
> 请求方式：GET
> 请求头：无

    //JSON结构
    {
        "mallId":"<商场id>",
        "mallMapId":"<商场地图id>",
        "interfaceVersion":"<接口版本号>",
        "appName":"<app内部显示的名称>",    //待定！！
        "date":"<服务器当前时间>",          //主要用于秒杀活动等，客户端比较本地时间
        "isNewUser":<是否为新用户>,
        "secretKey":"<私钥>"                //如果isNewUser==true,则返回secretKey，否则secretKey为空
    }
    
免费WIFI接口？？
---------

> 接口地址：api/wifi?v=`<app版本号>`&mid=`<商场id>`&uid=`<用户id>`
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

> 接口地址：api/main?v=`<app版本号>`&mid=`<商场id>`&uid=`<用户id>`
> 请求方式：GET
> 请求头：Authorization:<签名串>

    //JSON结构
    {
        "slideShow":[                       //轮播
            {
                "itemType":"对象类型",      //可以是多种对象，优惠、商铺、商品等
                "itemId":"对象id",
                "picUrl":"图片地址"
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
        ]
    }

搜索接口
---------
**暂时只搜索优惠**
主要用于搜索接口，同时其他接口也可能重用，如：二维码、。。。

> 接口地址：api/search?v=`<app版本号>`&mid=`<商场id>`&uid=`<用户id>`&`<查询条件>`
> 请求方式：GET
> 请求头：Authorization:<签名串>

**查询条件：**
| key       |    类型   | required  | 描述  |
| :-------- | --------:| :--: | :-- |
| keyword  | string |  Y   |  关键字 或 一、二维码  |
| type     |   int |  Y   |  查询类型：0：关键字查询 ，1：一、二维码查询  |
| order      |    string | N  | 排序？？  
| amount     |   int |  Y   |  每页条数  |
| page     |   int |  Y   |  请求的页数  |


    //JSON结构
    {
        "totalCount":<总页数>,
        "currentPage":<当前页>,
        "coupons":[                         //优惠列表
            {优惠对象,优惠对象,优惠对象,优惠对象,...}
        ]                    
    }

----------

#优惠页面

优惠接口
---------

> 接口地址：api/coupon?v=`<app版本号>`&mid=`<商场id>`&uid=`<用户id>`&like=`<0：默认，1：关注的商户对应的优惠劵>`&`<查询参数>`
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
            {优惠对象,优惠对象,优惠对象,优惠对象,...}
        ]                    
    }


优惠详细信息接口
---------

> 接口地址：api/coupon_detail?v=`<app版本号>`&mid=`<商场id>`&uid=`<用户id>`&couponid=`<优惠id>`
> 请求方式：GET
> 请求头：Authorization:<签名串>


    //JSON结构
    {
        优惠对象                 
    }


#服务

服务列表接口
---------

> 接口地址：api/services?v=`<app版本号>`&mid=`<商场id>`&uid=`<用户id>`
> 请求方式：GET
> 请求头：Authorization:<签名串>

    //JSON结构
    [
        {服务对象},{服务对象},{服务对象},...
    ]

#商户

商户列表接口
---------

> 接口地址：api/shop?v=`<app版本号>`&mid=`<商场id>`&uid=`<用户id>`&like=`<0：默认，1：关注的商户>`&`<查询参数>`
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
        "coupons":[                         //优惠列表
            {{商户对象},{商户对象},{商户对象},{商户对象},...}
        ]                    
    }

商户详细信息接口
---------

> 接口地址：api/shop_detail?v=`<app版本号>`&mid=`<商场id>`&uid=`<用户id>`&shopid=`<商户id>`
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

> 接口地址：api/myinfo?v=`<app版本号>`&mid=`<商场id>`&uid=`<用户id>`
> 请求方式：GET
> 请求头：Authorization:<签名串>


    //JSON结构
    [
        <用户基本信息>
    ]

修改用户基本信息接口
---------

> 接口地址：api/myinfo?**update**&v=`<app版本号>`&mid=`<商场id>`&uid=`<用户id>`
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

