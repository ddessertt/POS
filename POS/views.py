from urllib import request

from astroid import objects
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from POS.models import Product, Type

from . import models

# Create your views here.


def my_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('index')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'รหัสผ่านไม่ถูกต้อง'

    return render(request, template_name='login.html', context=context)

def my_logout(request):
    logout(request)
    return redirect('login')

def Home(request):
    
    search_product = request.GET.get('search_product', '')
    select_type = request.GET.get('select_type', '')

    po_type = Type.objects.all().order_by('id')
    pos = Product.objects.all()

    if request.method == 'GET':
        if search_product != '' and select_type != '':
            pos = Product.objects.filter(name__icontains=search_product, Type=select_type)
        elif search_product != '':
            pos = Product.objects.filter(name__icontains=search_product)
    
    return render(request, 'POS/index.html', context ={
        'search_product': search_product,
        'pos': pos,
        'po_type': po_type
    })

def management(request):
    search_product = request.GET.get('search_product', '')


    pos = Product.objects.all()

    if request.method == 'GET':
        if search_product != '':
            pos = Product.objects.filter(name__icontains=search_product)
    
    return render(request, 'POS/management.html', context ={
        'search_product': search_product,
        'pos': pos,
    })


def add_product(request):
    message = ''
    po_type = Type.objects.all().order_by('id')

    if request.method == 'POST':
        product = Product.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            Type_id=request.POST.get('Type'),
            price=request.POST.get('price'),
        )
        message = 'สร้างสินค้าใหม่แล้ว: %s' % (product.name)
    else:
        product = Product.objects.none()

    context = {
        'po_type': po_type,
        'product': product,
        'message': message
    }
    return render(request, 'POS/add_product.html', context=context)

def add_type(request):
    message = ''

    if request.method == 'POST':
        product_type = Type.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description')
        )
        message = 'สร้างประเภทใหม่แล้ว: %s' %(product_type.name)
    else:
        product_type = Type.objects.none()

    context = {
        'product_type': product_type,
        'message': message
    }
    return render(request, 'POS/add_type.html', context=context)

def product_edit(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        product_type = Type.objects.all()
        message = ''
    except Product.DoesNotExist:
        return redirect('management')
    
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.Type_id = request.POST.get('Type')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.save()
        message = 'แก้ไขสำเร็จแล้ว'
    
    context = {
        'message': message,
        'product': product,
        'po_type': product_type
    }

    return render(request, 'POS/add_product.html', context=context)

def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()

    return redirect(to='management')
