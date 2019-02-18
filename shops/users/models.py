from django.db import models
from seller.models import sellerData
from goods.models import goods
from openshop.models import openshopdata

# Create your models here.

class userDatas(models.Model):
    userid=models.AutoField(auto_created=True,primary_key=True,db_column='user_id')
    #用户姓名
    username=models.CharField(max_length=10,null=False,db_column="user_name")
    #用户密码
    userpassword=models.CharField(max_length=16,null=False,db_column="user_password")
    #用户邮箱
    user_email = models.CharField(max_length=100, null=False, db_column='user_email')
    #用户性别
    user_sex = models.IntegerField(null=False, db_column='user_sex')
    #用户年龄
    user_age = models.IntegerField(null=True, db_column='user_age')
    #用户简介
    user_intro = models.TextField(null=True, db_column='user_intro')
    #用户头像
    user_photo = models.ImageField(default="", upload_to="media/img")
    #用户注册时间
    add_time = models.DateTimeField(null=True, db_column='add_time')
    #邮箱状态
    email_status=models.IntegerField(null=True,db_column='email_status')


class UserEmail(models.Model):
    email_id=models.AutoField(auto_created=True,primary_key=True,db_column='email_id')
    user=models.ForeignKey(userDatas,db_column='user_id')
    email_time=models.DateTimeField(null=False,db_column='email_time')
    email_body=models.TextField(null=True,db_column='email_body')
    email_title=models.CharField(max_length=100,null=False,db_column='email_title')



#个人资料修改的数据库models模型
class modifymessage(models.Model):
    usermodify_id=models.AutoField(auto_created=True,primary_key=True,db_column='usermodify_id')
    user_name=models.CharField(max_length=30,null=False,db_column='user_name')
    user_email=models.CharField(max_length=100,null=False,db_column='user_email')
    user_sex=models.IntegerField(null=False,db_column='user_sex')
    user_age=models.IntegerField(null=True,db_column='user_age')
    user_photo=models.ImageField(default="",upload_to="media/img")
    user_intro=models.TextField(null=True,db_column='user_intro')
    add_time = models.DateTimeField(null=True, db_column='add_time')


#评论models模型
class goodscomment(models.Model):
    goodscomment_id=models.AutoField(auto_created=True,primary_key=True,db_column='goodscomment_id')
    #用户id
    user=models.ForeignKey(userDatas,db_column='user_id')
    #卖家id做外建
    seller=models.ForeignKey(sellerData,db_column='seller_id')
    #商品id
    goods=models.ForeignKey(goods,db_column='goods_id')
    #评论时间
    comment_time=models.DateTimeField(null=False,db_column='comment_time')
    #评论内容
    comment_content=models.TextField(null=True,db_column='comment_content')
        # 购物车需要店铺id
    openshop = models.ForeignKey(openshopdata, db_column='openshop_id',default='')








