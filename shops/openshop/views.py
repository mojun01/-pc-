from django.shortcuts import render
from shops import settings
from datetime import  datetime
from openshop.models import openshopdata
from seller.models import sellerData
from django.http import HttpResponseRedirect,HttpResponse


# Create your views here.
def openshop(request):
    return render(request,'openshop/openshop.html')


def openshopdo(request):
    seller_name=request.POST['seller_name']
    seller_pass=request.POST['seller_pass']
    sellerData.objects.create(
        seller_name=seller_name,
        seller_pass=seller_pass
    )
    seller=sellerData.objects.last()
    seller_id=seller.seller_id
    shop_count=openshopdata.objects.filter(seller_id=seller_id).count()
    if shop_count >5 :
        #其实这句话没有，型用户开店，不会走到这儿
        return HttpResponse('每个商家不能开超过5家的店铺！')
    else:
        shop_name = request.POST['shop_name']
        seller_name = request.POST['seller_name']
        seller_email = request.POST['seller_email']
        shop_adress=request.POST['shop_adress']
        user_sex = request.POST['user_sex']
        shop_info = request.POST['shop_info']
        shop_logo = request.FILES['shop_logo']
        add_time = datetime.now()

        save_path = '%s/media/shoplogo/%s' % (settings.MEDIA_ROOT, shop_logo.name)
        # 写入文件
        with open(save_path, 'wb')as f:
            for content in shop_logo.chunks():
                f.write(content)

        res=openshopdata.objects.create(

            shop_name=shop_name,
            seller_name=seller_name,
            seller_email=seller_email,
            shop_adress=shop_adress,
            user_sex=user_sex,
            shop_info=shop_info,
            add_time=add_time,
            shop_logo = 'media/shoplogo/%s' % shop_logo.name,
            seller_id = seller_id

        )
        if res:
            # return HttpResponse('secceful！')
            return HttpResponseRedirect('/seller/sellerLogin/')
        else:
            return HttpResponse('失败')



