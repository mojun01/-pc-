from django.shortcuts import render
from.models import cartdata,orderadress,ordertatus,userDatas,orderdata
from datetime import datetime
from django.utils import timezone
import random
from django.db.models import Sum

from django.http import HttpResponseRedirect,HttpResponse
from utils.pay import AliPay


#购物车已经导入到订单详情页
def ordershow(request):


    useruid=request.session.get('uid')
    #  cartlist  是为了把商品传入到订单页
    cartlist=cartdata.objects.filter(user_id=useruid).all()
    # sum  是为了计算订单页的总计价格！
    sum=cartdata.objects.filter(user_id=useruid).aggregate(Total=Sum("goods_xiaoji"))
    addresslist = orderadress.objects.filter(user_id=useruid).all()
    return render(request,'order/order.html',{"cartlist":cartlist,"sum":sum,"addresslist":addresslist})

#这个是收货地址
def order_adress(request):
    useruid = request.session.get('uid')
    adress = orderadress.objects.filter(user_id=useruid).all()
    return render(request,'order/orderadress.html',{"adress":adress})

# 这是把添加的地址写入数据库
def order_adressdo(request):
    userid = request.session.get('uid')
    if userid == None:
        return HttpResponseRedirect('/User/login')
    else:
        adress_name=request.POST['adress_name']
        phone_user=request.POST['phone_user']
        adress_username=request.POST['adress_username']
        ord=orderadress.objects.create(adress_name=adress_name,
                                   phone_user=phone_user,
                                   adress_username=adress_username,
                                   user_id=userid
                                   )
    if ord:
        return HttpResponseRedirect('/order/ordershow')
    else:
        return HttpResponse('no no no!')

def addto(request):
    uid = request.session.get('uid')
    seller_id=request.session.get('seller_id')
    openshop_id=request.session.get('openshop_id')
    if uid == None:
        return HttpResponseRedirect('/User/login')
    else:
        count=orderadress.objects.filter(user_id=uid).count()
        if count==0:
            return HttpResponse('请先添加收货地址')
        else:
            adress_id=request.POST['adress_id']
            order_price=request.POST['total']

            order_time=datetime.now()
            order_status=0
            order_num=timezone.now().strftime("%Y%m%d%H%M%S")+str(random.randint(10000,99999))
            ress=ordertatus.objects.create(
                user_id=uid,
                adress_id=adress_id,
                order_time=order_time,
                order_status=order_status,
                order_num=order_num,
                order_price=order_price,
                seller_id=seller_id,
                openshop_id=openshop_id
            )
            if ress:
                 # return HttpResponse('111')
                return HttpResponseRedirect('/order/comitdo')
            else:
                return HttpResponse('失败')
            

            







#把下单表加入数据库
def comitdo(request):
    uid=request.session.get('uid')
    openshop_id=request.session.get('openshop_id')
    if uid==None:
        return HttpResponseRedirect('/User/login')
    else:
        order=ordertatus.objects.filter(user_id=uid).last()
        order_id=order.mass_id
        carts=cartdata.objects.raw("select * from cart_cartdata join goods_goods on cart_cartdata.goods_id=goods_goods.goods_id where cart_cartdata.user_id="+str(uid))

        for i in carts:
            deles=orderdata.objects.create(

                goods_name=i.goods_name,
                goods_pic=i.goods_pic,
                goods_xprice=i.goods_xprice,
                goods_count=i.goods_count,
                goods_xiaoji=i.goods_xiaoji,
                goods_id=i.goods_id,
                seller_id=i.seller_id,
                mess_id =order_id,
                user_id=uid,
                openshop_id=openshop_id
            )
        if deles:
            cartdata.objects.filter(user_id=uid).all().delete()
            return HttpResponseRedirect('/order/chakan_order')
            # return HttpResponse('ok')
        else:
            return HttpResponse('失败')


def chakan_order(request):
    uid=request.session.get('uid')
    messager=ordertatus.objects.filter(user_id=uid).last()
    return render(request,'order/chakan_order.html',{"messager":messager})

            
#查看订单的带参数路由
def chakan_ordertit(request):
    return HttpResponseRedirect('/User/user_order')



def get_ali_object():
    #沙箱环境地址：
    app_id="2016092400585223" #APPID应用
    #支付完成后，支付向这个地址发送一个POST请求
    notify_url="http://127.0.0.1:8000/page2/"
    #支付完成后，跳转的地址
    return_url="http://127.0.0.1:8000/User/user_order/"

    merchant_private_key_path="paykey/app_private_2048.txt" #应用私钥
    alipay_public_key_path = "paykey/alipay_public_2048.txt" #支付宝公钥

    alipay=AliPay(
        appid=app_id,
        app_notify_url=notify_url,
        return_url=return_url,
        app_private_key_path=merchant_private_key_path,
        alipay_public_key_path=alipay_public_key_path,
    )
    return alipay

def page2(request):
    alipay=get_ali_object()
    if request.method=="POST":
        #检测是否成功
        #去请求体中获取所有返回的数据：状态/订单号
        from urllib.parse import parse_qs
        #
        body_str=request.body.decode('utf-8')
        post_data=parse_qs(body_str)
        
        post_dict={}
        for k,v in post_data.items():
            post_dict[k] = v[0]
         #
        sign=post_dict.pop('sign',None)
        status=alipay.verify(post_dict,sign)
        print('------开始-------')
        print('POST验证',status)
        print(post_dict)
        out_trade_no=post_dict['out_trade_no']
        #修改订单状态
        # models.order.objects.filter(trade_no=out_trade_no).updata(status=2)
        print('--------结束---------')
        return HttpResponse('POST返回')
    else:
        params=request.GET.dict()
        sign=params.pop('sign',None)
        status=alipay.verify(params,sign)
        print('=======开始========')
        print('GET验证',status)
        print('=========结束========')
        return HttpResponse('支付成功')

    

def payorder(request):
    #根据当前用户的配置，生成url，并跳转。
    money=float(request.POST.get('order_price'))
    alipay=get_ali_object()
    #生成支付的url
    query_params=alipay.direct_pay(
        subject="343434", #简单描述商品
        out_trade_no=request.POST['order_id'],
        total_amount=money,


    )
    pay_url="https://openapi.alipaydev.com/gateway.do?{0}".format(query_params) #支付宝网管地址（沙箱应用）
    return HttpResponseRedirect(pay_url)





