from django.db import models

from users.models import userDatas
from seller.models import sellerData
from goods.models import goods
from openshop.models import openshopdata
# from order.models import orderadress

# Create your models here.
from cart.models import cartdata


# 地址表
class orderadress(models.Model):
    adress_id = models.AutoField(auto_created=True, primary_key=True, db_column='adress_id')
    adress_name = models.CharField(max_length=100, null=False, db_column='adress_name')
    adress_username = models.CharField(max_length=100, null=False, db_column='adress_username')
    phone_user = models.CharField(max_length=20, null=False, db_column='phone_user')
    user = models.ForeignKey(userDatas, db_column='user_id')


#订单状态表
class ordertatus(models.Model):
    mass_id=models.AutoField(auto_created=True,primary_key=True,db_column='mass_id')
    user = models.ForeignKey(userDatas, db_column='user_id')
    adress=models.ForeignKey(orderadress,db_column='adress_id')
    order_time=models.DateTimeField(null=False,db_column='order_time')
    order_status=models.IntegerField(null=False,db_column='order_status')
    order_price=models.FloatField(null=False,db_column='order_price')
    order_num=models.CharField(max_length=100,null=False,db_column='order_num')
    seller=models.ForeignKey(sellerData,db_column='seller_id',default='')
    # 购物车需要店铺id
    openshop = models.ForeignKey(openshopdata, db_column='openshop_id', default='')



#订单详情表
class orderdata(models.Model):
    order_id = models.AutoField(primary_key=True, auto_created=True, db_column='order_id')
    user = models.ForeignKey(userDatas, db_column='user_id')
    seller = models.ForeignKey(sellerData, db_column='seller_id')
    goods = models.ForeignKey(goods, db_column='goods_id')
    goods_name = models.CharField(max_length=50, null=False, db_column='goods_name')
    goods_pic = models.CharField(max_length=100, null=False, db_column='goods_pic')
    goods_xprice = models.FloatField(null=False, db_column='goods_xprice')
    goods_count = models.IntegerField(null=False, db_column='goods_count')
    goods_xiaoji = models.FloatField(null=False, db_column='goods_xiaoji')
    mess=models.ForeignKey(ordertatus,db_column='mess_id')
    # 购物车需要店铺id
    openshop = models.ForeignKey(openshopdata, db_column='openshop_id',default='')
    






    
