from django.shortcuts import render
from goods.models import goods

# Create your views here.
from openshop.models import openshopdata

def allstore(request):
    store_list=openshopdata.objects.all()
    return render(request,'seller/store/allstore.html',{"store_list":store_list})
    
def store_page(request,openshop_id):
    page=goods.objects.filter(openshop_id=openshop_id).all()
    return render(request,'store/store_page.html',{"page":page})

