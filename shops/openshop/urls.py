#coding utf-8
#mojun
from django.conf.urls import url
from.import views
urlpatterns=[
    url(r'^openshop/',views.openshop,name='openshop'),
    url(r'^openshopdo/',views.openshopdo,name='openshopdo'),
]