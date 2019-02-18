from django.shortcuts import render
from cart.models import cartdata
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from.models import cartdata
from.models import goods
from django.db.models import Sum

def cartadd(request):
    openshop_id=request.session['openshop_id']
    # 判断用户是否登入成功 ，如果没登入就让客户去等。
    userid = request.session.get('uid')
    if userid == None:
        return HttpResponseRedirect('/User/login')
    else:
        #正常添加数据
        seller_id=request.POST['seller_id']
        goods_id=request.POST['goods_id']
        goods_name=request.POST['goods_name']
        goods_pic=request.POST['goods_pic']
        goods_price=request.POST['goods_xprice']
        goods_count=request.POST['goods_count']
        goods_xj=float(goods_count)*float(goods_price)
        #判断购物车里有没有已经添加过得商品，有的话，数量和小计，总计也有变化。
        gw=cartdata.objects.filter(goods_id=goods_id).count()
        if gw>0:
            #已经有同个商品了
            cart= cartdata.objects.get(goods_id=goods_id)
            cart.goods_count=int(goods_count)+int(cart.goods_count)
            cart.goods_xiaoji=cart.goods_count*cart.goods_xprice
            cart.save()
        else:
            cartdata.objects.create(seller_id=seller_id,
                                    goods_id=goods_id,
                                    user_id=userid,
                                    goods_name=goods_name,
                                    goods_pic=goods_pic,
                                    goods_xprice=goods_price,
                                    goods_count=goods_count,
                                    goods_xiaoji= goods_xj,
                                    openshop_id=openshop_id
                                    )
            #modelshi 外检不能加id，这里必须加id
    print(type(goods_count))
    return HttpResponseRedirect('/cart/cartshow')
#购物车展示
def cartshow(request):
    userid = request.session.get('uid')
    cart_user=cartdata.objects.filter(user_id=userid).all()
    sunprice=cartdata.objects.filter(user_id=userid).aggregate(Total=Sum("goods_xiaoji"))
 #购物车的总计
    return render(request,'cart/cart.html',{"cart_user":cart_user,"sunprice":sunprice})


def deletcart(request,pk):
    userid = request.session.get('uid')
    decar=cartdata.objects.filter(goods_id=pk,user_id=userid).get()
    decar.delete()
    return HttpResponseRedirect('/cart/cartshow')



def clearcart(request):
    userid = request.session.get('uid')
    decar = cartdata.objects.filter(user_id=userid).all()
    decar.delete()
    return HttpResponse(1)



    
def decgoodsnum(request,pk):
    userid = request.session.get('uid')
    deccargoods = cartdata.objects.get(goods_id=pk,user_id=userid)
    if deccargoods.goods_count==1:
        deccargoods.goods_count=1
    else:
        deccargoods.goods_count=deccargoods.goods_count-1
        deccargoods.goods_xiaoji=deccargoods.goods_count*deccargoods.goods_xprice
        deccargoods.save()
    return HttpResponseRedirect('/cart/cartshow')


def addgoodsnum(request,pk):
    userid = request.session.get('uid')
    addcargoods = cartdata.objects.get(goods_id=pk, user_id=userid)
    goodslist=goods.objects.get(goods_id=pk)
    addcargoods.goods_count = addcargoods.goods_count + 1
    goods_kc=goodslist.goods_count
    if addcargoods.goods_count > goods_kc:
        addcargoods.goods_count=goods_kc
    else:
        addcargoods.goods_xiaoji = addcargoods.goods_count * addcargoods.goods_xprice
        addcargoods.save()
    return HttpResponseRedirect('/cart/cartshow')
        
    
def delcar(request):
    #给个相应
    id=request.GET.get('carid',0)
    #删除数据库里的值
    cartdata.objects.get(cart_id=id).delete()

    return HttpResponse('ok')


    
#用ajax来写购物车的加减
def changenum(request):
    id=request.GET.get('id')
    new_num=request.GET.get('new_num')
    c=cartdata.objects.filter(cart_id=id).first()
    goods_id=c.goods_id
    b=goods.objects.filter(pk=goods_id).first()
    if int(new_num)>b.goods_count:
        new_num=b.goods_count
    else:
        cartdata.objects.filter(cart_id=id).update(goods_count=new_num)
        return HttpResponse(1)

def jiannum(request):
    id = request.GET.get('id')
    new_num = request.GET.get('new_num')
    cartdata.objects.filter(cart_id=id).update(goods_count=new_num)
    return HttpResponse(1)
    

    
    
    


