#coding utf-8
#mojun

from django.conf.urls import url

from.import views

urlpatterns=[
    url(r'^ordershow',views.ordershow,name='ordershow'),
    # url(r'^orderadd/',views.orderadd,name='orderadd')
    url(r'^order_adress/',views.order_adress,name='order_adress'),
    url(r'^order_adressdo/',views.order_adressdo,name='order_adressdo'),
    url(r'^addto',views.addto,name='addto'),

    url(r'^comitdo/',views.comitdo,name='comitdo'),
    #下单成功后的路由
    url(r'^chakan_order/',views.chakan_order,name='chakan_order'),

    #查看订单的带参数路由
    url(r'^chakan_ordertit/(?P<pk>[0-9]+)',views.chakan_ordertit,name='chakan_ordertit'),



    # 订单的状态路径
    # url(r'^ordertatus/',views.ordertatus,name='ordertatus'),

    url(r'^payorder/',views.payorder,name='payorder'),

    
]