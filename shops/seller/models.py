from django.db import models


# Create your models here.


# 权限表
class power(models.Model):
    name = models.CharField(max_length=30, default='')
    url_name = models.CharField(max_length=100)
    namespase = models.CharField(max_length=50)


# 角色表  role为角色
class role(models.Model):
    name = models.CharField(max_length=30)
    add_time = models.DateTimeField(auto_now_add=True)
    power = models.ManyToManyField('power')
    add_user = models.CharField(max_length=30)
    status = models.SmallIntegerField(default=0)


# 一定要把表先迁移，再加外键，以为外键不能为空

#卖家登入数据
class sellerData(models.Model):
    seller_id=models.AutoField(auto_created=True,primary_key=True,db_column='seller_id')
    seller_name=models.CharField(max_length=30,null=False,db_column='seller_name')
    seller_pass=models.CharField(max_length=30,null=False,db_column='seller_pass')
    role=models.ForeignKey('role',default=1)

#邮箱验证，发邮箱
class sendemail(models.Model):
    sendemail_id=models.AutoField(auto_created=True,primary_key=True,db_column='sendemail_id')
    email_title=models.CharField(max_length=50,null=False,db_column='email_title')
    email_info=models.TextField(null=False,db_column='email_info')
    email_time=models.DateTimeField(null=True,db_column='email_time')
    user_id=models.CharField(max_length=100,null=False,db_column='user_id')




