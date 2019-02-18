#coding utf-8
#mojun

from django.conf.urls import url
from.import views

urlpatterns=[

    url(r'^cartadd/',views.cartadd,name='cartadd'),
    url(r'^cartshow/',views.cartshow,name='cartshow'),
    # url(r'^deletcart/(?P<pk>[0-9]+)',views.deletcart,name='deletcart'),
    #ajaxc
    url(r'^delcar/',views.delcar,name='delcar'),
    url(r'^changenum/',views.changenum,name='changenum'),
    url(r'^jiannum/',views.jiannum,name='jiannum'),



    url(r'^clearcart/',views.clearcart,name='clearcart'),

    #购物车的商品数量的加减，商品小计 ，商品总计
    url(r'^decgoodsnum/(?P<pk>[0-9]+)',views.decgoodsnum,name='decgoodsnum'),
    url(r'^addgoodsnum/(?P<pk>[0-9]+)',views.addgoodsnum,name='addgoodsnum'),


]
