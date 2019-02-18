#coding utf-8
#mojun
from django.conf.urls import url

from.import views

urlpatterns = [
    # 商家登入
    url(r'^sellerLogin/$', views.sellerLogin, name='sellerLogin'),
    url(r'^sellerLogindo/$', views.sellerLogindo, name='sellerLogindo'),
    url(r'^sellerout/',views.sellerout,name='sellerout'),

    url(r'^sellerMina/(?P<pk>[0-9]+)',views.sellerMina,name='sellerMina'),
    url(r'^showorder/',views.showorder,name='showorder'),

    #会员中心的会员列表
    url(r'^huiyuan/',views.huiyuan,name='huiyuan'),

    url(r'^show_xiangqing/(?P<pk>[0-9]+)/(?P<adress_id>[0-9]+)',views.show_xiangqing,name='show_xiangqing'),
    # url(r'^show_xiangqing/',views.show_xiangqing,name='show_xiangqing')

#收货
    url(r'^fahuo/(?P<pk>[0-9]+)',views.fahuo,name='fahuo'),

    url(r'^seller_chakan_comment/(?P<pk>[0-9]+)',views.seller_chakan_comment,name='seller_chakan_comment'),

    #卖家店铺
    url(r'^store_list/',views.store_list,name='store_list'),


    #已有店铺的卖家开店
    url(r'^store/',views.store,name='store'),

    #卖家再开店的数据写进openshopdata数据库
    url(r'^storedo',views.storedo,name='storedo'),

    #邮件的发送
    url(r'^sendemail/(?P<pk>[0-9]+)',views.sendemail,name='sendemail'),
    url(r'^sendemaildo/',views.sendemaildo,name='sendemaildo'),



    #后台权限分配
    url(r'^management/',views.management,name='management'),
    url(r'^poweradd/',views.poweradd,name='poweradd'),
    url(r'^dopower/',views.dopower,name='dopower'),
    url(r'^delpower/',views.delpower,name='delpower'),



    # 后台角色分配
    url(r'^roles/', views.roles, name='roles'),
    url(r'^roleadd/', views.roleadd, name='roleadd'),
    url(r'^dorole/', views.dorole, name='dorole'),
    url(r'^delrole/', views.delrole, name='delrole')





]


