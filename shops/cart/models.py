from django.db import models
from users.models import userDatas
from seller.models import sellerData
from goods.models import goods
from openshop.models import openshopdata
# Create your models here.

class cartdata(models.Model):
    cart_id=models.AutoField(primary_key=True,auto_created=True,db_column='cart_id')
    user=models.ForeignKey(userDatas,db_column='user_id')
    seller=models.ForeignKey(sellerData,db_column='seller_id')
    goods=models.ForeignKey(goods,db_column='goods_id')
    
    goods_name=models.CharField(max_length=50,null=False,db_column='goods_name')
    goods_pic=models.CharField(max_length=100,null=False,db_column='goods_pic')
    goods_xprice=models.FloatField(null=False,db_column='goods_xprice')
    goods_count=models.IntegerField(null=False,db_column='goods_count')
    goods_xiaoji=models.FloatField(null=False,db_column='goods_xiaoji')
    #购物车需要店铺id
    openshop=models.ForeignKey(openshopdata,db_column='openshop_id',default="")



    




