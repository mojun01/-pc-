#coding utf-8
#mojun

from django.conf.urls import url

from.import views
urlpatterns = [
    url(r'^sign/',views.userSign,name="sign"), #注册会员
    url(r'^signdo/',views.userSigndo,name='signdo'),#注册的数据写进说一句库

    #email验证部分
    url(r'^UserEmail/',views.UserEmails,name='UserEmail'),

    url(r'^chakan_email/',views.chakan_email,name='chakan_email'),
    url(r'jihuo/',views.jihuo,name='jihuo'),
    url(r'^email_active/',views.email_active,name='email_active'),

    url(r'^login/',views.userLogin,name='login'),    #登入
    url(r'^logindo/',views.userLogindo,name='logindo'),
    url(r'^loginout/',views.loginout,name='loginout'),

    url(r'^main/',views.userMainPage,name='main'),   #登入成功的首页主页面


    # url(r'^carts/',views.userCart,name='carts'),   #购物车
    # url(r'^cartsdo',views.userCartsdo,name='cartsdo'),  #用户下单页面

    #商品详情页
    # url(r'^goods_introduce/',views.goods_introduce,name='goods_introduce'),

    #把数据传入商品详情页   一对一！
    # /(?P<seller_id>[0-9]+)这里加这个是为了对应index 加参数，seller_id 对应def goods_introduce(request,pk):
    #(request,pk,seller_id)  对应方法1
    url(r'^goods_introduce/(?P<pk>[0-9]+)',views.goods_introduce,name='goods_introduce'),

    url(r'^user_order/',views.user_order,name='user_order'),

    url(r'^user_base/',views.user_base,name='user_base'),


    url(r'users_orderdetails/(?P<pk>[0-9]+)/(?P<adress_id>[0-9]+)',views.users_orderdetails,name='users_orderdetails'),

    #收货
    url(r'^shouhuo/(?P<pk>[0-9]+)',views.shouhuo,name='shouhuo'),

    #个人资料修改
    url(r'^modifymessages/',views.modifymessages,name='modifymessages'),
    url(r'^modifymessagedo/',views.modifymessagedo,name='modifymessagedo'),

    #评论
    url(r'^commentgoodsadd/(?P<goods_id>[0-9]+)/(?P<seller_id>[0-9]+)',views.commentgoodsadd,name='commentgoodsadd'),
    
    url(r'^commentgoodsadddo/',views.commentgoodsadddo,name='commentgoodsadddo'),
    url(r'^get_valid_img/',views.get_valid_img,name='get_valid_img')



]



