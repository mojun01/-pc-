from django.shortcuts import render
from.models import goods_type ,goods,sellerData
from django.http import HttpResponseRedirect,HttpResponse
import datetime
from django.conf import settings
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

def goodsadd(request):

    list=goods_type.objects.order_by('-type_id')
    return render(request,'goods/goodsAdd.html',{"list":list})


def goodstypeadd(request):
    type = goods_type.objects.all()
    return render(request,'goods/goodstypeadd.html',{"type":type})

def goodstypeaddDo(request):
    type_name=request.POST['type_name']
    openshop_id = request.session.get('openshop_id')
    add_time=datetime.datetime.now()

    type=goods_type.objects.create(
        type_name=type_name,
        openshop_id=openshop_id,
        add_time=add_time,
    )
    if type:
       # return HttpResponse('ok')
        return HttpResponseRedirect('/Goods/goodsShow')
    else:
        return HttpResponse('erro')


def goodsShow(request):
    seller_id=request.session['seller_id']
    openshop_id=request.session['openshop_id']
    list=goods_type.objects.order_by('-type_id')
    return render(request,'goods/goodsshow.html',{"list":list})


def delettype(request,pk):
    list=goods_type.objects.get(pk=pk)
    list.delete()
    return HttpResponseRedirect("/Goods/goodsShow")

def modlytype(request,pk):
    list=goods_type.objects.get(pk=pk)
    return render(request,'goods/goodsmodly.html',{'list':list})


def goodsmodlyDo(request):
    type_name = request.POST['type_name']
    type_id=request.POST['type_id']
    ret=goods_type.objects.filter(type_id=type_id).update(type_name=type_name)
    if ret:
        return HttpResponseRedirect('/Goods/goodsShow')
    else:
        return HttpResponse('erro!')

    
def goodsadddo(request):
    openshop_id = request.session.get('openshop_id')
    goods_num=request.POST['goods_num']
    goods_name=request.POST['goods_name']
    # type=goods.seller.seller_id
    type_id=request.POST['type_id']
    goods_oprice=request.POST['goods_oprice']
    goods_xprice=request.POST['goods_xprice']
    goods_count=request.POST['goods_count']
    goods_method=request.POST['goods_method']
    goods_infro=request.POST['goods_infro']

    goods_ishow=request.POST['goods_ishow']

    goods_address=request.POST['goods_address']
    goods_body=request.POST['goods_content']
    up_time=datetime.datetime.now()
    seller_id=request.session.get('seller_id')
    goods_pic = request.FILES['goods_pic']


    save_path = '%s/media/uploads/%s' % (settings.MEDIA_ROOT,goods_pic.name)
    with open(save_path,'wb')as f:
        for content in goods_pic.chunks():
            f.write(content)

    ress=goods.objects.create(

                              goods_num=goods_num,
                              goods_name=goods_name,
                              type_id=type_id,
                              goods_oprice=goods_oprice,
                              goods_xprice=goods_xprice,
                              goods_count=goods_count,
                              goods_method=goods_method,
                              goods_infro=goods_infro,
                              goods_ishow=goods_ishow,
                              goods_address=goods_address,
                              goods_body=goods_body,
                              seller_id=seller_id,
                              up_time=up_time,
                              goods_pic='media/uploads/%s' % goods_pic.name,
        openshop_id=openshop_id
                              )
    if ress:
        return HttpResponseRedirect('/Goods/goodslist_show')
        # return HttpResponse('1231')
    else:
        return HttpResponse('添加失败！')

#商品列表
def goodslist_show(request):
    seller_id=request.session['seller_id']
    openshop_id=request.session['openshop_id']
    list=goods.objects.filter(seller_id=seller_id,openshop_id=openshop_id).order_by('-pk')

    # django的分布器
    # 1.分页器 分谁 一页显示几条数据，如果没有获取默认值是1
    paginator = Paginator(list, 3)
    page = request.GET.get("page", 1)
    # 吧当前页变成整数
    Current = int(page)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果输入的页码不是整数
    except EmptyPage:
        # 如果输入的页码是一个空页 最大页
        list = paginator.page(paginator.num_pages)

    return render(request,'goods/goodslist_show.html',locals())




def deletgoods(request,pk):
    list=goods.objects.get(pk=pk)
    list.delete()
    return HttpResponseRedirect("/Goods/goodslist_show")

def modlygoods(request,pk):
    signle =goods.objects.get(pk=pk)
    typelist = goods_type.objects.all()
    # picimg=goods.objects.all()
    return render(request,'goods/uptadagoodsAdd.html',{'signle':signle,"typelist":typelist})


def updatagoodsadddo(request):
    goods_id=request.POST['goods_id']
    goods_num=request.POST['goods_num']
    goods_name=request.POST['goods_name']
    # type=goods.seller.seller_id
    type_id=request.POST['type_id']
    goods_oprice=request.POST['goods_oprice']
    goods_xprice=request.POST['goods_xprice']
    goods_count=request.POST['goods_count']
    goods_method=request.POST['goods_method']
    goods_infro=request.POST['goods_infro']
    goods_ishow=request.POST['goods_ishow']
    goods_address=request.POST['goods_address']
    goods_body=request.POST['goods_content']
    up_time=datetime.datetime.now()
    seller_id=request.session.get('seller_id')
    goods_pic = request.FILES['goods_pic']
    save_path = '%s/media/uploads/%s' % (settings.MEDIA_ROOT,goods_pic.name)
    with open(save_path,'wb')as f:
        for content in goods_pic.chunks():
            f.write(content)
    ress=goods.objects.filter(goods_id=goods_id).update(

                              goods_num=goods_num,
                              goods_name=goods_name,
                              type_id=type_id,
                              goods_oprice=goods_oprice,
                              goods_xprice=goods_xprice,
                              goods_count=goods_count,
                              goods_method=goods_method,
                              goods_infro=goods_infro,
                              goods_ishow=goods_ishow,
                              goods_address=goods_address,
                              goods_body=goods_body,
                              seller_id=seller_id,
                              up_time=up_time,
                              goods_pic='media/uploads/%s' % goods_pic.name,
                              )
    if ress:
        return HttpResponseRedirect('/Goods/goodslist_show')
        # return HttpResponse('1231')
    else:
        return HttpResponse('修改失败！')


# 鲜果列表的逻辑代码
def goodslist(request):
#直接把goods表的数据倒过来就可以啦
    list1=goods_type.objects.all() #包括了type_id 
    list=goods.objects.filter(goods_ishow=1).order_by('-goods_id').all()



# django的分布器
    # 1.分页器 分谁 一页显示几条数据，如果没有获取默认值是1
    paginator = Paginator(list,10)
    page = request.GET.get("page",1)
    # 吧当前页变成整数
    Current = int(page)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果输入的页码不是整数
    except EmptyPage:
        # 如果输入的页码是一个空页 最大页
        list = paginator.page(paginator.num_pages)

    return render(request,'goods/allindex.html',locals(),{"list1":list1})

def goodslistss(request,type_id) :
    list = goods.objects.filter(goods_ishow=1,type_id=type_id).order_by('-goods_id').all()
    return render(request, 'goods/allindex.html', locals(), {"list": list})

def goodslist1(request,pk):
    list1 = goods_type.objects.all()
    list = goods.objects.filter(goods_ishow=1,type_id=pk).order_by('-goods_id').all()
    # list=goods.objects.filter(type_id=pk).all()
    # django的分布器
    # 1.分页器 分谁 一页显示几条数据，如果没有获取默认值是1
    paginator = Paginator(list, 10)
    page = request.GET.get("page", 1)
    # 吧当前页变成整数
    Current = int(page)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果输入的页码不是整数
    except EmptyPage:
        # 如果输入的页码是一个空页 最大页
        list = paginator.page(paginator.num_pages)

    return render(request, 'goods/allindex.html', locals(), {"list1": list1})


#商品上下架
def ishowx(request,pk):
    down_time = datetime.datetime.now()
    res=goods.objects.filter(pk=pk).update(goods_ishow=0,down_time=down_time)
    if res:
        return HttpResponseRedirect('/Goods/goodslist_show/')
def ishows(request,pk):
    up_time=datetime.datetime.now()
    res = goods.objects.filter(pk=pk).update(goods_ishow=1,up_time=up_time)
    if res:
        return HttpResponseRedirect('/Goods/goodslist_show/')
    
        




