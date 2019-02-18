from django.shortcuts import render
from .models import sellerData,power,role
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
# Create your views here.
from order.models import ordertatus, orderdata, orderadress
from users.models import goodscomment,userDatas,UserEmail
from shops import settings
from django.db.utils import settings
from datetime import datetime
from openshop.models import openshopdata
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json


def sellerLogin(request):
    return render(request, 'seller/seller.html')


def sellerLogindo(request):
    sellername = request.POST['username']
    sellerpass = request.POST['password']
    seller = sellerData.objects.filter(
        seller_name=sellername,
        seller_pass=sellerpass)
    if seller:
        seller_id = sellerData.objects.get(
            seller_name=sellername,
            seller_pass=sellerpass).seller_id

        request.session['sename'] = sellername
        request.session['seller_id'] = seller_id
        return HttpResponseRedirect('/seller/store_list/')
        # return HttpResponse('ok')
    else:
        return HttpResponse("erro")

def sellerout(request):
    del request.session['sename']
    return HttpResponseRedirect('/seller/sellerLogin/')
def sellerMina(request, pk):
    seller_id = request.session.get('seller_id')
    request.session['openshop_id'] = pk
    return render(request, 'seller/mina.html')


# 为了卖家的订单状态能看到

def showorder(request):
    openshop_id = request.session.get('openshop_id')
    # 为了获取卖家的id
    seller_id = request.session.get('seller_id')
    # print(seller_id)
    # 获取数据的订单情况来看订单
    # sql = "select distinct tu.mass_id,tu.order_time,tu.order_status,tu.order_num from order_ordertatus tu left join order_orderdata da on tu.mass_id=da.mess_id where da.seller_id=" + str(
    #     seller_id)

    sql="SELECT * FROM order_ordertatus a WHERE a.mass_id IN (SELECT DISTINCT(mess_id) from order_orderdata WHERE openshop_id="+str(openshop_id)+")"

    # 详情表的seller_id要等于当前登入的seller_id  切记！
    tatus = ordertatus.objects.filter(seller_id=seller_id).raw(sql)
    # if sql:
    #     return HttpResponse(sql)
    return render(request, 'seller/order/showorder.html', locals())
#会员列表
def huiyuan(request):
    openshop_id=request.session.get('openshop_id')
    sql="select distinct a.user_id,a.user_name,a.user_email,a.user_sex,a.user_age,a.user_intro,a.user_photo from users_userdatas a left JOIN order_orderdata b on a.user_id=b.user_id where b.openshop_id="+str(openshop_id)

    huiyuan=userDatas.objects.raw(sql)
    
    return render(request,'seller/huiyuan.html',{"huiyuan":huiyuan})
# 卖家的订单详情
def show_xiangqing(request, pk, adress_id):
    # openshop_id = request.session.get('openshop_id')
    seller_id = request.session.get('seller_id')
    # 获取相同订单地址。
    # 用pk所有表的主键统称 用mess_id主键 的所有的东西找到adress_id 对应的消息
    order_data = orderdata.objects.filter(seller_id=seller_id, mess_id=pk).all()
    adress = orderadress.objects.filter(adress_id=adress_id).get()
    # order 订单状态
    # order_tatus = ordertatus.objects.filter(mass_id=mass_id).get()
    # order_detail详情页的数据   订单状态的mass_id=订单详情里的mess_id
    return render(request, "seller/show_xiangqing.html",
                  {"adresslist": adress, "order_data": order_data})


# 发货功能
def fahuo(request, pk):
    # 为了获取用户id
    uid = request.session.get('uid')
    # 为了订单状态的信息
    ress = ordertatus.objects.filter(mass_id=pk, user_id=uid).update(order_status=1)
    if ress:
        return HttpResponseRedirect('/seller/showorder')
    else:
        return HttpResponseRedirect(0)


# 卖家查看评价
def seller_chakan_comment(request, pk):
    seller_id = request.session.get('seller_id')
    comment = goodscomment.objects.filter(seller_id=seller_id, goodscomment_id=pk).all()
    # return HttpResponse(comment)
    return render(request, "seller/seller_chakan_comment.html", {"comment": comment})


# 店铺列表
def store_list(request):
    seller_id = request.session.get('seller_id')
    storelist = openshopdata.objects.filter(seller_id=seller_id).all()
    return render(request, 'seller/store/store_list.html', {"storelist": storelist})


# 店铺
def store(request):
    return render(request, 'seller/store/store.html')


# 把数据写进数据库
def storedo(request):
    seller_id = request.session.get('seller_id')
    shop_count = openshopdata.objects.filter(seller_id=seller_id).count()
    if shop_count > 5:
        return HttpResponse('每个商家不能开超过5家的店铺！')
    else:
        shop_name = request.POST['shop_name']
        seller_name = request.POST['seller_name']
        seller_email = request.POST['seller_email']
        shop_adress = request.POST['shop_adress']
        user_sex = request.POST['user_sex']
        # shop_info = request.POST['shop_info']
        shop_logo = request.FILES['shop_logo']
        add_time = datetime.now()
        seller_id = request.session.get('seller_id')
        save_path = '%s/media/shoplogo/%s' % (settings.MEDIA_ROOT, shop_logo.name)
        # 写入文件
        with open(save_path, 'wb')as f:
            for content in shop_logo.chunks():
                f.write(content)
        res = openshopdata.objects.create(
            shop_name=shop_name,
            seller_name=seller_name,
            seller_email=seller_email,
            shop_adress=shop_adress,
            user_sex=user_sex,
            add_time=add_time,
            shop_logo='media/shoplogo/%s' % shop_logo.name,
            seller_id=seller_id
        )
        if res:
            return HttpResponseRedirect('/seller/sellerMina/')
        else:
            return HttpResponse('失败')

#卖家给会员发邮件
def sendemail(request,pk):
    email=request.session.get('user_email')
    # return HttpResponse(pk)
    return render(request,'seller/sendemail.html',{"user_id":pk,"email":email})

def sendemaildo(request):
    user_id=request.POST['user_id']
    u=userDatas.objects.get(userid=user_id)
    user_name=u.username    #为了获取用户姓名
    email=u.user_email   #为了获取用户的邮箱地址
    email_time=datetime.now()
    email_title=request.POST['send_title']
    email_body=request.POST['send_info']
    # res=send_mail(email_title,'',settings.EMAIL_FROM,[user_email],html_message=email_body,fail_silently=True)
    res = send_mail(email_title,email_body,settings.EMAIL_FROM, [email], fail_silently=True) #发送邮件给客户，要提供有效的邮箱
    # return HttpResponse(res)
    if res:
        ress=UserEmail.objects.create(
            email_title=email_title,
            email_body=email_body,
            user_id= user_id,
            email_time=email_time,
        )
        if ress:
            return HttpResponseRedirect('/seller/huiyuan/')
        else:
            return HttpResponse(0)
    else:
        return HttpResponse('发送邮件失败！')


#后台权限管理  management 是权限列表
def management(request):
    list=power.objects.filter()
    print(list)
    #分液器
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

    return render(request,'powerlist/management.html',{'list':list})

#为了响应添加的返回路由
def poweradd(request):
    return render(request,'powerlist/addpower.html')


def dopower(request):
    powerobj=power()
    powerobj.name=request.POST.get('name')
    powerobj.url_name=request.POST.get('url_name')
    powerobj.namespase=request.POST.get('namespace')
    powerobj.save()
    # print(powerobj)
    #定义一个空字典
    data={}
    if powerobj.id:
        data['msg'] = '添加成功'
        data['status']= 1
    else:
        data['msg'] = '添加失败'
        data['status'] = 0

    return JsonResponse(data)

def delpower(request):
    id=request.GET.get('id')
    res=power.objects.filter(id=id).first()
    res.delete()
    return HttpResponse(1)



#后台角色管理  role 是权限列表
def roles(request):
    list1=role.objects.filter()
    print(list1)
    #分液器
    # django的分布器
    # 1.分页器 分谁 一页显示几条数据，如果没有获取默认值是1
    paginator = Paginator(list1, 3)
    page = request.GET.get("page", 1)
    # 吧当前页变成整数
    Current = int(page)
    try:
        list1 = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list1 = paginator.page(1)  # 如果输入的页码不是整数
    except EmptyPage:
        # 如果输入的页码是一个空页 最大页
        list1 = paginator.page(paginator.num_pages)

    return render(request,'powerlist/role.html',{'list':list1})

#为了响应添加的返回路由
def roleadd(request):
    return render(request,'powerlist/roleadd.html')


def dorole(request):
    roleobj=role()
    roleobj.name=request.POST.get('uname')
    # roleobj.url_name=request.POST.get('rolestatus')
    roleobj.add_user=request.POST.get('username')
    roleobj.add_time=datetime.now()
    roleobj.status=1
    roleobj.save()
    # print(powerobj)
    #定义一个空字典
    data={}
    if roleobj.id:
        data['msg'] = '添加成功'
        data['status']= 1
    else:
        data['msg'] = '添加失败'
        data['status'] = 0

    return JsonResponse(data)

def delrole(request):
    id=request.GET.get('id')
    res=role.objects.filter(id=id).first()
    res.delete()
    return HttpResponse(1)

