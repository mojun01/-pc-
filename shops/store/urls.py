#coding utf-8
#mojun

from django.conf.urls import url
from.import views
urlpatterns=[
    url(r'^allstore/',views.allstore,name='allstore'),
    url(r'^store_page/(?P<openshop_id>[0-9]+)',views.store_page,name='store_page')

]




