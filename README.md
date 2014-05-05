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
http://www.wise-mall.com
测试商场编号: bj001
>http://www.wise-mall.com/api/bj001/coupon
>http://www.wise-mall.com/init/bj001?userid=1234

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

      md5：将secret 拼接到参数字符串头、将mall_code拼接到串尾进行md5加密后，再转化成大写，格式是：base64(md5(secretkey1value1key2value2...{mall_code}))

      注：JAVA中MD5是对字节数组加密，加密结果是16字节，我们需要的是32位的大写字符串，图片参数不用加入签名中


校验规则算法：

		签名算法采用Hmac-md5，hmac（secret+"app_key"+app_key+"timestamp"+timestamp+...+{mall_code}, secret）
		原始字符串：secret+"app_key"+app_key+"timestamp"+timestamp+...+secret，加密串是secret，
		其中timestamp(时间戳格式为13位数字类型，例如：1333275943000,位数不够可使用“0”补足)这部分工作必须在服务端处理。


###3.3[错误消息](id:anchor_init_errmsg)
接口调用出错时统一返回如下消息体:

>
    //JSON结构
    {
        "errorCode":"<错误编号>",       // 发生错误时,errorCode非空
        "errorMsg":"<错误消息>"
    }
>

####错误消息定义<待完善>
|编号		|描述		|
| :--------: | :-- |
|1001 		|	非法调用
|1001 		|	版本太低啦~~~~~~~~~

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


> 接口地址：init/<商场编号>?`<系统参数>`
> 请求方式：GET
> 响应体：
> 
    //JSON结构
    {
        "mallId":"<商场id>",
        "mallCode":"<商场编号>",
        "mallName":"<商场名称>",
        "mallMapId":"<商场地图id>",
        "mallLogo":"<商场Logo>",               // logo地址
        "appName":"<app内部显示的名称>",       //待定！！
        "date":"<服务器当前时间>",             //主要用于秒杀活动等，客户端比较本地时间
        "isNewUser":<是否为新用户>,
        "secretKey":"<私钥>"                   //如果isNewUser==true,则返回secretKey，否则secretKey为空
    }
    
>
> 参考：
>  
> 1. [系统参数](#系统参数)

    
免费WIFI接口？？
---------

**小蔡来定吧**

> 接口地址：api/<商场编号>/wifi?`<系统参数>`
> 请求方式：GET
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

```json

    //JSON结构
    {'store':                         // 优惠对应的商户信息
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
     collectType: '下载方式'            // 0: 免费下, 1: 分享后下载
     collectLimit: '限量'              // 0: 不限制; N: 限制下载N次,
     collectRole: '下载规则'            // 待定, 目前返回空串,统一处理为每人限下载一次
     userCollectCount: '我的下载次数',       // 根据role不同会有不同的处理情况,目前总是返回1.
     collectCount: '下载数',            // 已下载总量
     commentCount: '评论数',
     startTime: '开始时间',
     endTime: '结束时间',
     date:"<服务器当前时间>"
     }
```

优惠券下载接口
---------

> 接口地址：api/<商场编号>/coupon_download?`<系统参数>`&couponid=`<优惠id>`
> 请求方式：GET


    //JSON结构
    {
     status: '下载结果',            // 1: 成功; 2: X; 3: 失败-已下载过; 4: 失败-不符合参与条件
     msg: '提示信息',               // 失败的提示信息
     coupon_code: '优惠代码',              // 1: 优惠活动; 2: 优惠券; 3: 团购;
     date":"<服务器当前时间>"
     }




#服务

服务列表接口
---------

> 接口地址：api/<商场编号>/services?`<系统参数>`
> 请求方式：GET

    //JSON结构
    {
        totalCount: "总数"
        services:[
        {服务对象},{服务对象},{服务对象},...
        {
            "name":"对象名称",
            "itemType":"对象类型",      //  #1:内置功能; 0: 网页
            "itemId":"对象id",
            "picUrl":"图片地址"
            "link":"链接地址"           // itemType为0的时候才有值
        }
    ]
    }


#商户

商户列表接口
---------

> 接口地址：api/<商场编号>/shop?`<系统参数>`&like=`<0：默认，1：关注的商户>`&`<查询参数>`
> 请求方式：GET

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


    //JSON结构
    {
        name: "姓名",
        gender: "性别",
        nick_name: "昵称",
        mobile: "手机号",
        club_card: "会员卡号",
    }


修改用户基本信息接口
---------

> 接口地址：api/<商场编号>/myinfo?**update**&`<系统参数>`
> 请求方式：**PUT**
> 请求体：`{用户基本信息}`
> 
> **响应：**
response code:200 OK




我的优惠劵接口
---------
> 接口地址：api/<商场编号>/myinfo/coupons_download?`<系统参数>`
> 请求方式：GET


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
             coupon_code: '优惠券代码',
             coupon_status: '优惠券状态',  // ('0', '未消费'), ('1', '已消费')
             startTime: '开始时间',
             endTime: '结束时间'
             }
        ]
    }



消费记录接口
---------



我关注的商家接口
---------

> 接口地址：api/<商场编号>/myinfo/shop?`<系统参数>`&`<查询参数>`
> 请求方式：GET

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


我关注的商品接口？？？
---------

我关注的优惠接口
---------
> 接口地址：api/<商场编号>/myinfo/coupons_focus?`<系统参数>`&`<查询参数>`
> 请求方式：GET


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
             ...
        ]
    }


绑定手机接口-发送短信
---------


绑定手机接口-保存手机号
---------



绑定会员卡接口
---------
> 接口地址：api/<商场编号>/myinfo/club_card?`<系统参数>`
> 请求方式：GET

    //JSON结构
    {
        "club_card":<会员卡号>,
    }


> 接口地址：api/<商场编号>/myinfo/club_card?`<系统参数>`&club_card=<卡号>
> 请求方式：PUT

    //JSON结构
    {
        "result":<发送结果>,
    }

绑定银行卡接口
---------
取银行列表
> 接口地址：api/<商场编号>/myinfo/bank_list?`<系统参数>`
> 请求方式：GET

    //JSON结构
    [
        {
        bank_id..<银行ID>
        bank_name..<银行名称>
        }
        ...
    ]

取我的卡列表
> 接口地址：api/<商场编号>/myinfo/bank_card?`<系统参数>`
> 请求方式：GET

    //JSON结构
    [
        {
            id: <卡ID>,
            bank_id: <银行Id>,
            bank_name: <银行名称>,
            card_num: <卡号>,
        }
    ]

删除卡
> 接口地址：api/<商场编号>/myinfo/bank_card?`<系统参数>`&card_id=<卡id>&card_id=<卡id>&card_id=<卡id>
> 请求方式：DELETE

    //JSON结构
    {
        "result":<发送结果>,
    }

新增卡
> 接口地址：api/<商场编号>/myinfo/bank_card?`<系统参数>`&club_card=<卡号>&bank_id=<银行ID>
> 请求方式：PUT

    //JSON结构
    {
        "result":<发送结果>,
    }


消息推送/提示接口
---------
先确定有几种消息
> 接口地址：api/<商场编号>/push/?`<系统参数>`
> 请求方式：GET

    //JSON结构
