from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from . models import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.



def home(request,c_slug=None):#c_slug is for calling the category
    c_page=None#declare the variable as none to call them later in looping
    prodt=None#declare the variable as none to call them later in looping

    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)#get the object called in category to c_slug
        prodt=product.objects.filter(catname=c_page,avail=True)#filtering the products as category and checking the availability,always check you cannot give any varibale names it should be specified keywords.
    else:
        prodt=product.objects.all().filter(avail=True)#if not just show the all products
    cat=Category.objects.all()

    #PAGINATOR
    paginator=Paginator(prodt,4)#how many product in 1 page this needs to be query set not model set
    try:#this try gives 1 firt page
        page=request.GET.get('page','1')
    except:#if even 1 page is not availble this should show its in first only page
        page=None

    try:
        pro=paginator.page(page)
        #in case empty pages occurs this return over all number of pages available
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)#this shows overall pages number available

    return render(request,'index.html',{'pr':prodt,'ct':cat,'pg':pro})##'ct':c_page## for category calling






def prod_det(request,c_slug,product_slug):#to call both product and category slugs
    try:#in case error occurs try and except is better option
        prod=product.objects.get(catname__slug=c_slug,slug=product_slug)#category__slug is for category slug means c_slug,ordinary product slug is slug(2 args)
    except Exception as e:#in case error occurs what to do
        raise e #raise the error
    # pr=product.objects.all()
    return render(request,'product.html',{'pr':prod})#CALL THE BOTH PARAMETER GIVEN (C_SLUG AND PRODUCT SLUG) TO URL


def searching(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=product.objects.all().filter(Q(name__contains=query)|(Q(dsc__contains=query)))#Q MEANS COMPLEX DATABAS QUERY
    return render(request,'search.html',{'qr':query,'pr':products})