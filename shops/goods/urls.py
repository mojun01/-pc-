#coding utf-8
#mojun

from django.conf.urls import url
from.import views

urlpatterns =[
    url(r'^goodsadd/$',views.goodsadd,name='goodsadd'),
    url(r'^goodstypeadd/',views.goodstypeadd,name='goodstypeadd'),
    url(r'^goodstypeaddDo/',views.goodstypeaddDo,name='goodstypeaddDo'),

    url(r'^goodsShow/$',views.goodsShow,name='goodsShow'),
    url(r'^delettype/(?P<pk>[0-9]+)',views.delettype,name='delettype'),
    url(r'^modlytype/(?P<pk>[0-9]+)',views.modlytype,name='modlytype'),
    url(r'^goodsmodlyDo/',views.goodsmodlyDo,name='goodsmodlyDo'),

    #商品进数据库
    url(r'^goodsadddo/',views.goodsadddo,name='goodsadddo'),


    url(r'^goodslist_show/',views.goodslist_show,name='goodslist_show'),

    url(r'^deletgoods/(?P<pk>[0-9]+)',views.deletgoods,name='deletgoods'),
    url(r'^modlygoods/(?P<pk>[0-9]+)',views.modlygoods,name='modlygoods'),

    url(r'^updatagoodsadddo/',views.updatagoodsadddo,name='updatagoodsadddo'),

    #鲜果列表
    url(r'^goodslist/',views.goodslist,name='goodslist'),
    url(r'^goodslist1/(?P<pk>[0-9]+)',views.goodslist1,name='goodslist1'),
    url(r'^goodslistss/(?P<type_id>[0-9]+)',views.goodslistss,name='goodslistss'),
    
    #商品下架
    url(r'^ishowx/(?P<pk>[0-9]+)',views.ishowx,name='ishowx'),
    #商品上架
    url(r'^ishows/(?P<pk>[0-9]+)',views.ishows,name='ishows'),




]