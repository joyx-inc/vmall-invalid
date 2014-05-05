#!python
#encoding:utf-8
import datetime
from django.db import models

# Create your models here.


dict_type = {0: '待审核', 1: '正常', -1: '删除'}
dict_subject_type = {1: '优惠', 2: '商户', 3: '商品', 4: '网页'}
choices_subject_type = ((1, '优惠'), (2, '商户'), (3, '商品'), (4, '网页'))
choices_promotion_type = ((1, '优惠活动'), (2, '优惠券'), (3, '团购'))
choices_gender = ((1, '男'), (2, '女'))
choices_yes_or_no = ((True, '是'), (False, '否'))


class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    modified_date = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    #    ext = models.CharField(null=True, blank=True, max_length=1024, verbose_name=u'Ext')


    class Meta:
        abstract = True


class Mall(BaseModel):
    name = models.CharField(max_length=50, verbose_name=u'商场名称', )
    logo = models.CharField(max_length=50, verbose_name=u'商场LOGO', )
    mall_code = models.CharField(max_length=50, verbose_name=u'商场编号', )
    mall_map_id = models.CharField(max_length=50, verbose_name=u'商场地图ID', )
    app_name = models.CharField(max_length=50, verbose_name=u'商场APP名称', )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '商场'
        verbose_name_plural = '商场列表'
        db_table='t_mall'

# 标签
class Tag(BaseModel):
    name = models.CharField(max_length=20, verbose_name=u'标签名称', )
    type = models.IntegerField(verbose_name=u"标签类型", default=1, choices=choices_subject_type)
    group = models.CharField(verbose_name=u'分组', max_length=20, null=True, blank=True)
    description = models.CharField(verbose_name=u'备注', max_length=100, null=True, blank=True)
    mall = models.ForeignKey(Mall, verbose_name=u'所属商场')


    def __str__(self):
        return "%s (%s)" % (self.name, dict_type[self.type])

    def __unicode__(self):
        return self.name

    def type_desc(self):
        return dict_type[self.type]

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签列表'
        db_table='t_tag'


# 主题
class Subject(BaseModel):
    title = models.CharField(max_length=50, verbose_name=u'标题')
    type = models.IntegerField(verbose_name="主题类型", default=1, choices=choices_subject_type)
    item_count = models.IntegerField(default=0, verbose_name=u'子类数量')
    image = models.CharField(max_length=150, verbose_name=u'图片地址', null=True, blank=True)
    url = models.CharField(max_length=150, verbose_name=u'链接地址', null=True, blank=True)
    start_time = models.DateTimeField(verbose_name=u'开始时间')
    end_time = models.DateTimeField(verbose_name=u'结束时间')
    description = models.CharField(verbose_name=u'描述', max_length=1000, null=True, blank=True)
    order = models.IntegerField(verbose_name=u'排序', default=100)
    mall = models.ForeignKey(Mall, verbose_name=u'所属商场')


    def __str__(self):
        return self.title

    def type_desc(self):
        return dict_type[self.type]

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '主题'
        verbose_name_plural = '主题列表'
        db_table='t_subject'


# 首页轮播图
class SlideShow(BaseModel):
    title = models.CharField(max_length=50)
    type = models.IntegerField(verbose_name=u"类型", default=1, choices=choices_subject_type)  #1:优惠; 2:商户; 3: 商品; 4: 网页
    image = models.CharField(max_length=150, verbose_name=u'图片地址')
    url = models.CharField(max_length=150, verbose_name=u'链接地址', null=True, blank=True)
    item_id = models.IntegerField(verbose_name=u'对象ID', null=True, blank=True)
    order = models.IntegerField(verbose_name=u'排序', default=100)
    mall = models.ForeignKey(Mall, verbose_name=u'所属商场')

    def __str__(self):
        return self.title

    def type_desc(self):
        return dict_type[self.type]
    class Meta:
        verbose_name = '首页轮播图'
        verbose_name_plural = '首页轮播图列表'
        db_table='t_slide_show'


# 用户
class User(BaseModel):
    name = models.CharField(verbose_name=u'姓名', max_length=20)
    gender = models.IntegerField(verbose_name=u'性别', choices=choices_gender, default=1)
    deviceId = models.CharField(verbose_name=u'设备编码', max_length=50)
    app_secret = models.CharField(verbose_name=u'app_secret', max_length=20, null=True, blank=True)
    nick_name = models.CharField(verbose_name=u'昵称', max_length=20, null=True, blank=True)
    mobile = models.CharField(verbose_name=u'手机号', max_length=20, null=True, blank=True)
    club_card = models.CharField(verbose_name=u'会员卡号', max_length=50, null=True, blank=True)
    login_name = models.CharField(verbose_name=u'登录名', max_length=20, null=True, blank=True)
    login_password = models.CharField(verbose_name=u'登录密码', max_length=50, null=True, blank=True)
    mall = models.ForeignKey(Mall, verbose_name=u'所属商场')


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户列表'
        db_table='t_user'


# 银行列表
class Bank(BaseModel):
    name = models.CharField(max_length=20, verbose_name=u'银行名称')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '银行'
        verbose_name_plural = '银行列表'
        db_table='t_bank'


# 商户
class Store(BaseModel):
    title = models.CharField(verbose_name=u'商户名称', max_length=50)
    alias = models.CharField(verbose_name=u'别名', max_length=200, null=True, blank=True)
    follower_count = models.IntegerField(verbose_name=u'关注人数', default=0)
    comment_count = models.IntegerField(verbose_name=u'评论人数', default=0)
    logo = models.CharField(verbose_name=u'LOGO', max_length=150, null=True, blank=True)
    tel = models.CharField(verbose_name=u'电话', max_length=30, null=True, blank=True)
    address = models.CharField(verbose_name=u'地址', max_length=50, null=True, blank=True)
    homepage = models.CharField(verbose_name=u'WEB主页', max_length=50, null=True, blank=True)
    description = models.CharField(verbose_name=u'简介', max_length=500, null=True, blank=True)
    floor = models.CharField(verbose_name=u'楼层', max_length=50, null=True, blank=True)
    storeNo = models.CharField(verbose_name=u'房间号', max_length=50, null=True, blank=True)
    order = models.IntegerField(verbose_name=u'排序', default=100)
    mall = models.ForeignKey(Mall, verbose_name=u'所属商场')


    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '商户'
        verbose_name_plural = '商户列表'
        db_table='t_store'

    @staticmethod
    def serialize(obj):
        return {
            "id": obj.id,
            "title": obj.title,
            "create_date": obj.create_date.strftime('%Y-%m-%d %H:%M:%S') if isinstance(obj.create_date,
                                                                                       datetime.datetime) else None,
            "follower_count": obj.follower_count,
            "comment_count": obj.comment_count,
        }


# 商品
class Goods(BaseModel):
    title = models.CharField(verbose_name=u'商品名称', max_length=50)
    store = models.ForeignKey(Store, verbose_name=u'所属商户')
    market_price = models.CharField(max_length=150, verbose_name=u'市场价', null=True, blank=True)
    mall_price = models.CharField(max_length=150, verbose_name=u'商场价', null=True, blank=True)
    #promotion_price = models.CharField(max_length=150, verbose_name=u'促销价', null=True, blank=True)
    brand_name = models.CharField(max_length=150, verbose_name=u'品牌', null=True, blank=True)
    place = models.CharField(max_length=150, verbose_name=u'产地', null=True, blank=True)
    description = models.TextField(max_length=2048, verbose_name=u'描述', null=True, blank=True)
    cover_img = models.CharField(max_length=150, verbose_name=u'封面图', null=True, blank=True)
    order = models.IntegerField(verbose_name=u'排序', default=100)
    mall = models.ForeignKey(Mall, verbose_name=u'所属商场')


    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品列表'
        db_table='t_goods'


# 优惠促销
class Promotion(BaseModel):
    title = models.CharField(max_length=50)
    type = models.IntegerField(verbose_name=u'优惠类型', default=1,
                               choices=choices_promotion_type)  #,1: 优惠活动; 2: 优惠券; 3: 团购;
    store = models.ForeignKey(Store, verbose_name=u'所属商户', null=True)
    sub_type = models.IntegerField(verbose_name='下级分类', null=True, blank=True)  #用于细分优惠券类型
    is_bank_special = models.BooleanField(default=False, verbose_name=u'是否银行卡专享', choices=choices_yes_or_no)
    start_time = models.DateTimeField(verbose_name=u'开始时间')
    end_time = models.DateTimeField(verbose_name=u'结束时间')
    description = models.TextField(max_length=2048, verbose_name=u'描述', null=True, blank=True)
    cover_img = models.CharField(max_length=150, verbose_name=u'封面图', null=True, blank=True)
    collect_count = models.IntegerField(verbose_name=u'下载人数', default=0)
    comment_count = models.IntegerField(verbose_name=u'评论人数', default=0)
    order = models.IntegerField(verbose_name=u'排序', default=100)
    mall = models.ForeignKey(Mall, verbose_name=u'所属商场')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = '优惠'
        verbose_name_plural = '优惠列表'
        db_table='t_promotion'


# 优惠信息图片
class PromotionImage(BaseModel):
    promotion = models.ForeignKey(Promotion, verbose_name=u'所属优惠')
    image = models.CharField(max_length=150, verbose_name=u'图片地址')
    order = models.IntegerField(verbose_name=u'排序', default=100)
    class Meta:
        db_table='t_promotion_image'


# 优惠银行
class PromotionBank(BaseModel):
    promotion = models.ForeignKey(Promotion, verbose_name=u'所属优惠')
    bank = models.ForeignKey(Bank, verbose_name=u'银行卡')
    class Meta:
        db_table='t_promotion_bank'


# 优惠分享
class PromotionShare(BaseModel):
    promotion = models.ForeignKey(Promotion, verbose_name=u'优惠')
    share_type = models.CharField(max_length=10, verbose_name=u'分享平台')
    user = models.ForeignKey(User, verbose_name=u'用户')
    class Meta:
        db_table='t_promotion_share'


# 用户下载/关注的优惠券
class UserPromotion(BaseModel):
    user = models.ForeignKey(User, verbose_name=u'用户')
    promotion = models.ForeignKey(Promotion, verbose_name=u'优惠')
    type = models.IntegerField(default=1, verbose_name=u'类型,0: 关注; 1: 下载', choices=(('0', '关注'), ('1', '下载')))
    coupon_code = models.CharField(max_length=20, null=True, blank=True)
    coupon_status = models.IntegerField(verbose_name="优惠券消费状态", default=0)  # ('0', '未消费'), ('1', '已消费')
    check_time = models.DateTimeField(verbose_name=u'消费时间',null=True, blank=True)
    class Meta:
        db_table='t_user_promotion'


# 用户拥有的银行卡
class UserBankCard(BaseModel):
    user = models.ForeignKey(User, verbose_name=u'用户')
    bank = models.ForeignKey(Bank, verbose_name=u'银行卡')
    card_num = models.CharField(max_length=20, verbose_name=u'卡号')
    class Meta:
        db_table='t_user_bank_card'


class StoreFollower(BaseModel):
    store = models.ForeignKey(Store, verbose_name=u'商户')
    user = models.ForeignKey(User, verbose_name=u'用户')

    class Meta:
        db_table='t_store_follower'

class Comment(BaseModel):
    title = models.CharField(max_length=50)
    type = models.IntegerField(default=1, verbose_name=u'评论类型,1: 商品评论; 2: 商户评论', choices=(('1', '商品评论'), ('2', '商户评论')))
    store = models.ForeignKey(Store, verbose_name=u'商户')
    goods = models.ForeignKey(Goods, verbose_name=u'商品', null=True, )
    user = models.ForeignKey(User, verbose_name=u'用户')
    user_name = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    mall = models.ForeignKey(Mall, verbose_name=u'所属商场')


    def __str__(self):
        return "(%s) %s" % (self.user_name, self.content)

    class Meta:
        db_table='t_comment'

class SubjectPromotion(BaseModel):
    item = models.ForeignKey(Promotion, verbose_name=u'优惠')
    subject = models.ForeignKey(Subject, verbose_name=u'所属主题')

    class Meta:
        db_table='t_subject_promotion'

class SubjectStore(BaseModel):
    item = models.ForeignKey(Store, verbose_name=u'商户')
    subject = models.ForeignKey(Subject, verbose_name=u'所属主题')
    class Meta:
        db_table='t_subject_store'


class SubjectGoods(BaseModel):
    item = models.ForeignKey(Goods, verbose_name=u'商品')
    subject = models.ForeignKey(Subject, verbose_name=u'所属主题')
    class Meta:
        db_table='t_subject_goods'


class Category(BaseModel):
    name = models.CharField(max_length=50)
    parentId = models.IntegerField(verbose_name=u'父级节点', default=0)
    description = models.TextField(max_length=100, verbose_name=u'描述', null=True, blank=True)
    mall = models.ForeignKey(Mall, verbose_name=u'所属商场')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类列表'
        db_table='t_category'


class StoreCategory(BaseModel):
    store = models.ForeignKey(Store, verbose_name=u'商户')
    category = models.ForeignKey(Category, verbose_name=u'分类')
    class Meta:
        db_table='t_store_category'


class SearchKeyword(BaseModel):
    keyword = models.CharField(max_length=50)
    mall = models.ForeignKey(Mall, verbose_name=u'所属商场')

    def __unicode__(self):
        return self.keyword

    class Meta:
        verbose_name = '搜索关键字'
        verbose_name_plural = '关键字列表'
        db_table='t_search_keyword'


'''
initStore = Store.objects.create()
initStore.id = 0
initStore.title = u'商场'
initStore.save()
'''