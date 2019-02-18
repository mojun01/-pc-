"""shops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from.upload import upload_image
from django.conf.urls.static import static
from django.conf import settings
# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^User/',include('users.urls',namespace='users')),
    url(r'^Goods/',include('goods.urls',namespace='goods')),

    #商家登入
    url(r'^seller/',include('seller.urls',namespace='seller')),

    url(r'^cart/',include('cart.urls',namespace='cart')), #购物车总路由

    url(r'^order/',include('order.urls',namespace='order')),
    url(r'^openshop/',include('openshop.urls',namespace='openshop')),
    url(r'^store/',include('store.urls',namespace='store')),
    url(r'^admin/uploads/(?P<dir_name>[^/]+)$',upload_image,name="upload_image"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



