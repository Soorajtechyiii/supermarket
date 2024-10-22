from django.shortcuts import render #type:ignore
from django.template import loader  #type:ignore
from django.http import HttpResponse #type:ignore
from.models import Items
def pagehtml(request):
    Id=loader.get_template('demo1html.html')
    return HttpResponse(Id.render())

def items(request):
    if request.method=='POST':
        ProductID=request.POST.get('ID')
        url=request.POST.get('img')
        ProductName=request.POST.get('NAME')
        productPrice=request.POST.get('PRICE')
        DiscountPrice=request.POST.get('DISCOUNT')
        I=Items(ProductID=ProductID,url=url,ProductName=ProductName,productPrice=productPrice,
                DiscountPrice=DiscountPrice)
        I.save()
        return HttpResponse('datasave')
    else:
        return HttpResponse('data not saved')

def dataread(request):
    data=Items.objects.all()
    return render(request,'displaydata.html',{'data':data})

def setcookie(request):
    response=HttpResponse('cookieset')
    response.set_cookie('java-tutorial','javapoint')
    return response
def getcookie(request):
    tutorial=request.COOKIES['java-tutorial']
    return HttpResponse('java tutorials @:'+tutorial);

        


