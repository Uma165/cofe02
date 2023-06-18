from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from products.models import ProductCategory, Product, Basket
from  django.core.paginator import Paginator


# функции= контроллеры= вьюхи = обработчики запросов

def index(request):
    context={ 'title': 'Латте',}
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page_namber = 1):
    products=Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_namber)

    context = {'title': 'Латте - Каталог',
                'categories': ProductCategory.objects.all(),
               'products':products_paginator,
                }
    return render(request, 'products/products.html', context)


@login_required     #(login_url='/users/login/')
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(reguest, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(reguest.META['HTTP_REFERER'])

