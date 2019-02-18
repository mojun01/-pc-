from django.shortcuts import render
from.models import userDatas,modifymessage,goodscomment
from goods.models import goods   #导入商品的数据库
# from.models import userOerderDatas #订单
from django.http import HttpResponseRedirect,HttpResponse
from order.models import ordertatus,orderdata,orderadress
from shops import settings
from datetime import  datetime
from django.core.mail import send_mail
from.models import UserEmail
#导入验证码模块
from PIL import Image,ImageDraw,ImageFont
import random
from io import BytesIO
# Create your views here.


def userSign(request):
    return render(request, 'users/signin.html')  #注册会员
def userSigndo(request):
    username=request.POST['username']
    password=request.POST['password']
    email=request.POST['email']
    res=userDatas.objects.create(username=username,userpassword=password,user_email=email,email_status=0)
    if res:
        return HttpResponseRedirect('/User/UserEmail/')
    else:
        return HttpResponse("注册失败，请再次注册！")

#邮箱验证部分
def UserEmails(request):
    user=userDatas.objects.last()
    email=user.user_email
    username=user.username
    id=user.userid
    time=datetime.now()
    path = "会员"+username+"你好!请尽快激活账号 <a href='http://127.0.0.1:8000/User/email_active/'>激活邮箱</a>"
    res=send_mail("全球生鲜欢迎你！"," ",settings.EMAIL_FROM,[email],html_message=path,fail_silently=True)
    if res:
        UserEmail.objects.create(
            user_id=id,
            email_time=time,
            email_title='全球生鲜欢迎您',
            email_body='会员你好 欢迎注册全球生鲜商城'
        )
    return HttpResponseRedirect('/User/chakan_email/')
# 查看email
def chakan_email(request):
    return render(request,'users/chakan_email.html')
#激活邮箱
def jihuo(request):
    return render(request,'users/jihuo.html')
#执行邮箱功能
def email_active(request):
    user=userDatas.objects.last()
    id=user.userid
    res=userDatas.objects.filter(userid=id).update(email_status=1)
    if res:
        return HttpResponseRedirect('/User/login/')
    else:
        return HttpResponse('激活失败')
#     用户登入
def userLogin(request):
    return render(request,'users/login.html')

# 用户数据写进数据库
def userLogindo(request):
    username = request.POST['username']
    password = request.POST['password']
    res=userDatas.objects.filter(username=username,userpassword=password)
    if res:
        status=userDatas.objects.get(username=username,userpassword=password).email_status
        if status==1:
            userid=userDatas.objects.get(
                username=username,
                userpassword=password).userid
            request.session['uname']=username
            request.session['uid'] = userid
            return HttpResponseRedirect('/User/main/')
        else:
            return HttpResponseRedirect('/User/jihuo/')
    else:
        return HttpResponse('登入失败，重新登入！')
#     注销账号
def loginout(request):
    del request.session['uname']
    return HttpResponseRedirect('/User/main/')
 #首页面》主页面  添加商品展示限制功能
def userMainPage(request):        #引入数据库的商品数据到首页
    seller_id=request.session['seller_id']
    goodlist = goods.objects.filter(goods_ishow=1).order_by('-goods_id')[0:10]
    return render(request,'users/index.html',{"goodlist":goodlist})




 #  把数据传入商品详情页   一对一！
def goods_introduce(request,pk):
    #(request,pk,seller_id)  对应方法1
    #(request,pk) 对应方法2
    #pk 等于goods_id
    ingoods=goods.objects.get(pk=pk)
    # ingoods.seller_id  对应 (request,pk) 但可以获得seller_id
    p=ingoods.seller_id

    #数据库在goods表里面
    goodslist=goods.objects.exclude(goods_id=pk).all()[0:4] #limit 从数据库里拿数据
    #print(ingoods)
    # sql = "select * from  goods_goods join users_goodscomment  on goods_goods.goods_id = goods_goodscomment.goods_id " \
    #       "join users_userDatas on goods_goodscomment.user_id = users_userDatas.user_id " \
    #       "where goods_goods.goods_id=" + str(pk)
    # return HttpResponse(sql)

    # 方法1 评论表关联用户表 users_userdatas
    # sql = "SELECT * FROM users_goodscomment a LEFT JOIN users_userdatas b ON a.user_id=b.user_id WHERE a.seller_id = "+str(seller_id)+" AND a.goods_id = "+pk+""
    sqlone="SELECT * FROM goods_goods a LEFT JOIN users_goodscomment b ON a.goods_id=b.goods_id WHERE a.seller_id = "+str(p)+" AND a.goods_id = "+pk+""
    com=goods.objects.raw(sqlone)

    #方法2 评论表关联个人资料更新表
    sql="SELECT * FROM users_goodscomment a LEFT JOIN users_userDatas b ON a.user_id=b.usermodify_id WHERE a.goods_id = "+pk+""
    commentlist=goodscomment.objects.raw(sql)
    # a=commentlist.user_photo

    tou="SELECT * FROM users_userDatas"
    aa=userDatas.objects.raw(tou)
    
    # return HttpResponse(aa)
    return render(request,'users/goods_introduce.html',{"ingoods":ingoods,"goodslist":goodslist,"commentlist":commentlist,"com":com,"aa":aa})


def user_order(request):
    uid=request.session.get('uid')
    if uid==None:
        return HttpResponseRedirect('/User/login')
    else:
        #订单状态表
        ordertatuslist = ordertatus.objects.filter(user_id=uid).order_by('-mass_id')
        #订单详情表
        orderdatalist = orderdata.objects.all()

        return render(request, 'users/user_order.html',
                      {"ordertatuslist": ordertatuslist, "orderdatalist": orderdatalist})

    # return render(request,'users/user_order.html')


#这个没问题
def user_base(request):
    return render(request,'user_base/user_base.html')



def users_orderdetails(request,pk,adress_id):
    uid = request.session.get('uid')
    # 订单地址。
    adress = orderadress.objects.get(adress_id=adress_id,user_id=uid)

    # order 订单状态
    order_tatus = ordertatus.objects.filter(mass_id=pk,user_id=uid).get()
    #order_detail详情页的数据   订单状态的mass_id=订单详情里的mess_id

    order_data = orderdata.objects.filter(mess_id=pk).all()
    return render(request, "users/users_orderdetails.html", {"adresslist": adress,"order_tatus":order_tatus,"order_data":order_data})


#收货功能
def shouhuo(request,pk):
    #为了获取用户id
    uid=request.session.get('uid')
    #为了订单状态的信息
    ress=ordertatus.objects.filter(mass_id=pk,user_id=uid).update(order_status=2)
    if ress:
        return HttpResponseRedirect('/User/user_order')
    else:
        return HttpResponseRedirect(0)
    
#个人资料的修改
def modifymessages(request):
    return render(request,'users/modifymessage.html')

def modifymessagedo(request):
    user_id = request.session.get('uid')
    user_email=request.POST['user_email']
    user_sex=request.POST['user_sex']
    user_age=request.POST['user_age']
    user_photo=request.FILES['user_photo']
    user_intro=request.POST['user_intro']
    add_time = datetime.now()
    # print(user_photo)
    save_path = '%s/media/img/%s' % (settings.MEDIA_ROOT,user_photo.name)
    # 写入文件
    with open(save_path,'wb')as f:
        for content in user_photo.chunks():
            f.write(content)
    #    这里的userID不是外键
    mod=userDatas.objects.filter(
        userid=user_id).update(
        user_email=user_email,
        user_sex=user_sex,
        user_age=user_age,
        add_time=add_time,
        user_intro=user_intro,
        user_photo='media/img/%s' % user_photo.name
                                 )
    if mod:
        # return HttpResponse('ok')
        # request.session['userphoto']=user_photo
        return HttpResponseRedirect('/User/main/')
    else:
        return HttpResponse('个人资料修改失败！')



    # return HttpResponse('ok')
#评价功能
def commentgoodsadd(request,goods_id,seller_id):
    return render(request,'users/commentgoodsadd.html',{"goods_id":goods_id,"seller_id":seller_id})

def commentgoodsadddo(request):
    openshop_id = request.session.get('openshop_id')
    uid = request.session.get('uid')
    goods_id=request.POST['goods_id']
    seller_id=request.POST['seller_id']
    comment_content=request.POST['comment_content']
    comment_time = datetime.now()

    ress= goodscomment.objects.create(
        user_id=uid,
        goods_id=goods_id,
        seller_id=seller_id,
        comment_content=comment_content,
        comment_time=comment_time,
        openshop_id=openshop_id
    )

    if ress:
        # return HttpResponse('评论失败了！')
        return HttpResponseRedirect('/User/user_order/')
    else:
        return HttpResponse('评论失败了！')


#获取验证码图片的视图
def get_valid_img(request):
    #获取随机颜色的函数
    def get_random_color():
        return random.randint(0,255),random.randint(0,255),random.randint(0,255)
    #生成一个图片对象
    img_obj=Image.new(
        'RGB',
        (170,35),
         get_random_color()
    )
    #在生成的图片上写字符
    #生成一个图片画笔对象
    draw_obj=ImageDraw.Draw(img_obj)
    #加载字体文件，得到一个字体对象
    font_obj=ImageFont.truetype("static/font/timesi.ttf",28)
    #开始生成随机字符串并且写到图片上
    tmp_list=[]
    for i in range(4):
        U=chr(random.randint(65,90)) #生成大写字母
        I=chr(random.randint(97,122)) #生成小写字母
        n=str(random.randint(0,9)) #生成数字，注意要换成字符串

        tmp=random.choice([U,I,n])
        tmp_list.append(tmp)
        draw_obj.text((20+40*i,0),tmp,fill=get_random_color(),font=font_obj)
    #保存到session
    request.session["valid_code"] = "".join(tmp_list)
     #加干扰线啊
    width = 220 #防止越界
    height = 35
    for i in range(5):
        x1=random.randint(0,width)
        x2 = random.randint(0, width)
        y1 = random.randint(0,height)
        y2 = random.randint(0, height)
        draw_obj.line((x1,y1,x2,y2),fill=get_random_color())

    #加干扰点
    for i in range(40):
        draw_obj.point((random.randint(0,width),random.randint(0,height)),fill=get_random_color())
        x = random.randint(0,width)
        y=random.randint(0,height)
        draw_obj.arc((x,y,x+4,y+4),0,90,fill=get_random_color())
    #不要在硬盘上保存文件，直接在内存中加载
    io_obj=BytesIO()
    #把生成的图片数据保存到io里
    img_obj.save(io_obj,"png")
    #从io对象里面取上一步保存的数据
    data=io_obj.getvalue()
    return HttpResponse(data)

