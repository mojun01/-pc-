from django.db import models
from seller.models import sellerData

# Create your models here.

class openshopdata(models.Model):
    openshop_id=models.AutoField(auto_created=True,primary_key=True,db_column='openshop_id')
    shop_name=models.CharField(max_length=30,null=False,db_column='shop_name')
    seller_name=models.CharField(max_length=30,null=True,db_column='seller_name')
    seller_email=models.CharField(max_length=30,null=False,db_column='seller_email')
    shop_adress=models.CharField(max_length=50,null=False,db_column='shop_adress')
    user_sex=models.IntegerField(null=True,db_column='user_sex')
    shop_logo=models.ImageField(default="",upload_to="media/shoplogo")
    shop_info=models.TextField(null=False,db_column='shop_info')
    add_time = models.DateTimeField(null=True, db_column='add_time')
    #谁开的店，需要卖家id
    seller=models.ForeignKey(sellerData,db_column='seller_id',default="")
    


    