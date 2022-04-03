from django.shortcuts import render,redirect,get_object_or_404
from proj1.models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def cart_det(request,tot=0,count=0,cart_items=None,vat=0,total=0):
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
        cart_items=items.objects.filter(cart=ct,active=True)
        for i in cart_items:
            tot +=(i.prodt.price*i.quant)
            count+=i.quant
            vat=tot*(5/100)
            total=vat+tot
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',{'tot':tot,'c_items':cart_items,'count':count,'vat':vat,'totts':total})

def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id

def add_cart(request,product_id):
    prod=product.objects.get(id=product_id)
    #this try is to get the session key created in function c_id()
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
    #if the session key is not created then create a session key and save
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    # calling products from the models to try if the items already available then increment the items
    try:
        c_items=items.objects.get(prodt=prod,cart=ct)
        if c_items.quant < c_items.prodt.stock:
            c_items.quant +=1
            c_items.save()
    # if not available create the items into the cart
    except items.DoesNotExist:
        c_items=items.objects.create(prodt=prod,quant=1,cart=ct)
        c_items.save()
    return redirect('cartdet')

def min_cart(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(product,id=product_id)
    c_items=items.objects.get(prodt=prod,cart=ct)
    if c_items.quant > 1:
        c_items.quant-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartdet')


def del_cartitems(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(product,id=product_id)
    c_items=items.objects.get(prodt=prod,cart=ct)
    c_items.delete()
    return redirect('cartdet')


