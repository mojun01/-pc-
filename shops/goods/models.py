from django.db import models
from seller.models import sellerData
from openshop.models import openshopdata
# Create your models here.

class goods_type(models.Model):
    type_id=models.AutoField(auto_created=True,primary_key=True,db_column='type_id')
    type_name=models.CharField(max_length=30,null=False,db_column='type_name')
    openshop = models.ForeignKey(openshopdata, db_column='openshop_id', default='')
    seller = models.ForeignKey(sellerData, db_column='seller_id',default='')
    add_time = models.DateTimeField(null=True, db_column='add_time')



class goods(models.Model):
    goods_id = models.AutoField(auto_created=True,primary_key=True,db_column='goods_id')
    goods_num = models.CharField(max_length=30,null=False,db_column='goods_num')
    goods_name = models.CharField(max_length=100,null=False,db_column='goods_name')

    type = models.ForeignKey(goods_type,db_column='type_id')

    goods_oprice = models.FloatField(null=False,db_column='goods_oprice')
    goods_xprice = models.FloatField(null=False,db_column='goods_xprice')
    goods_count = models.IntegerField(null=False,db_column='goods_count')
    goods_method = models.CharField(null=False,db_column='goods_method',max_length=100)
    goods_infro = models.CharField(null=False,max_length=200,db_column='goods_infro')
    goods_ishow = models.IntegerField(null=False,db_column='goods_ishow')

    goods_pic = models.ImageField(default="",upload_to="media/uploads")
    
    goods_address = models.CharField(max_length=50,null=False,db_column='goods_address')
    goods_body = models.TextField(null=False,db_column='goods_body')

    seller = models.ForeignKey(sellerData,db_column='seller_id')

    up_time = models.DateTimeField(null=False,db_column='up_time')
    down_time = models.DateTimeField(null=True,db_column='down_time')

    # 购物车需要店铺id
    openshop = models.ForeignKey(openshopdata, db_column='openshop_id',default='')



