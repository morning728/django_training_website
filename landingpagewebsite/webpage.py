from django.shortcuts import render
from crm import models

def first_webpage(request):
    orders_list = models.Order.objects.all()
    return render(request, './index.html', {'orders_list':orders_list})

def thank_page(request):
    name = request.POST["name"]
    num = request.POST["phone"]
    new = models.Order(order_name = name, order_phone = num)
    new.save()
    return render(request, './thank_page.html',{"name":name, 'num':num})