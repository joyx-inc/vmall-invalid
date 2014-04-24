vmall
=====


微商场接口文档!
=====================
----------
#http调用方式说明

1. 调用介绍
2. 调用入口
3. 调用参数

##1. 调用介绍
略

##2. 调用入口
小蔡

##3. 调用参数
调用API ，必须传入系统参数和应用参数。系统参数详细介绍如下：

###3.1参数

####系统参数

|名称		|类型		|是否必须 	|描述		|
| :--------: | --------:| :--: 		| :-- |
|timestamp 		|string	|Y	|	时间戳，服务端允许客户端请求时间误差为6分钟。
|userid 		|string	|Y	|	用户uuid
|v 		|string	|Y	|	客户端版本号
|sign	|string	|Y	|对 API 输入参数进行 md5 加密获得，详细参考如下 [签名sign](#32签名sign)

####应用参数
|名称		|类型		|是否必须 	|描述		|
| :--------: | --------:| :--: 		| :-- |
|fields 		|string	|Y	|	请求参数，对应不同接口的相应参数。


###3.2[签名sign](id:anchor_init_sign)

除获取资源外，任何接口调用前都必须将**系统参数**填入到当前请求的url中，因为每一次提交请求都会用来验证用户的身份。

####签名
调用API 时需要对请求参数进行签名验证，服务器也会对该请求参数进行验证是否合法的。

**方法如下：**
> 根据参数名称（除签名和图片）将所有请求参数按照字母先后顺序排序:key + value .... key + value
> 
      例如：将foo=1,bar=2,baz=3 排序为bar=2,baz=3,foo=1，参数名和参数值链接后，得到拼装字符串bar2baz3foo1

系统支持MD5加密方式:

      md5：将secret 拼接到参数字符串头、尾进行md5加密后，再转化成大写，格式是：base64(md5(secretkey1value1key2value2...secret))

      注：JAVA中MD5是对字节数组加密，加密结果是16字节，我们需要的是32位的大写字符串，图片参数不用加入签名中


校验规则算法：

		签名算法采用Hmac-md5，hmac（secret+"app_key"+app_key+"timestamp"+timestamp+secret, secret）
		原始字符串：secret+"app_key"+app_key+"timestamp"+timestamp+secret，加密串是secret，
		其中timestamp(时间戳格式为13位数字类型，例如：1333275943000,位数不够可使用“0”补足)这部分工作必须在服务端处理。


----------
#基础接口部分


[初始化接口](id:anchor_init)
---------

客户端启动时的初始化接口，主要用于：

* 获取客户端基本信息
* 用户注册、登录
* ...

####用户注册登录：
访问接口时，客户端提交生成的用户唯一标示uuid，服务器端判断该uuid是否存在

> *  uuid存在:isNewUser:false,secretKey:null
> *  uuid不存在:isNewUser:true,secretKey:<服务器端生成的对应秘钥>


####接口：


> 接口地址：api/<商场编号>/init?`<系统参数>`
> 
> 请求方式：GET
> 
> 响应体：
> 
    //JSON结构
    {
        "mallId":"<商场id>",
        "mallCode":"<商场编号>",
        "mallName":"<商场名称>",
        "mallMapId":"<商场地图id>",
        "appName":"<app内部显示的名称>",    //待定！！
        "date":"<服务器当前时间>",          //主要用于秒杀活动等，客户端比较本地时间
        "isNewUser":<是否为新用户>,
        "secretKey":"<私钥>"                  //如果isNewUser==true,则返回secretKey，否则secretKey为空
    }
    
>
> 参考：
>  
> 1. [系统参数](#系统参数)

    
免费WIFI接口？？
---------

**小蔡来定吧**

> 接口地址：api/<商场编号>/wifi?`<系统参数>`
> 
> 请求方式：GET
> 
> 请求头：Authorization:<签名串>
> 
> 响应体：
> 
	//JSON结构
	{
	   ??
	}

----------
#主页部分

主页面接口
---------
主页导航部分暂时写死，不通过接口返回！

> 接口地址：api/<商场编号>/main?`<系统参数>`
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

> 接口地址：api/<商场编号>/search?`<系统参数>`&`<查询条件>`
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

> 接口地址：api/<商场编号>/coupon?`<系统参数>`&like=`<0：默认，1：关注的商户对应的优惠劵>`&`<查询参数>`
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

> 接口地址：api/<商场编号>/coupon_detail?`<系统参数>`&couponid=`<优惠id>`
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

> 接口地址：api/<商场编号>/services?`<系统参数>`
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

> 接口地址：api/<商场编号>/shop?`<系统参数>`&like=`<0：默认，1：关注的商户>`&`<查询参数>`
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

> 接口地址：api/<商场编号>/shop_detail?`<系统参数>`&shopid=`<商户id>`
> 请求方式：GET
> 请求头：Authorization:<签名串>


    //JSON结构
    {                                       //商户对象
        <商户对象基本信息>,
        "coupons":[{商户发布的优惠劵},{商户发布的优惠劵},{商户发布的优惠劵},...],
        "comments"[{商户的评论信息},{商户的评论信息},{商户的评论信息},...]

        title: '商户名称',
        logo: '商户LOGO',
        id: '商户ID',
        category: '商户类型',
        floor: '楼层',
        storeNo: '商户房间号',
        description: '介绍',
        followerCount: '关注人数',
        特殊属性: '特殊属性',
        特殊属性: '特殊属性',
        特殊属性: '特殊属性',
        特殊属性: '特殊属性',
        coupons:[                           // 商户的优惠劵
            {
             id: '优惠ID',
             title: '优惠标题',
             type: '优惠类型',              // 1: 优惠活动; 2: 优惠券; 3: 团购;
             tag: '优惠标签',
             image: '优惠图',
            }...
        ],
        comments:[                          // 商户的评论
            {
            author: "发布人名字",
            content: "内容",
            createTime: "发布时间"
            },...
        ]
    }

#我的信息

用户基本信息接口
---------

> 接口地址：api/<商场编号>/myinfo?`<系统参数>`
> 请求方式：GET
> 请求头：Authorization:<签名串>


    //JSON结构
    [
        <用户基本信息>
    ]

修改用户基本信息接口
---------

> 接口地址：api/<商场编号>/myinfo?**update**&`<系统参数>`
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

