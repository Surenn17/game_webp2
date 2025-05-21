from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request,'main/index.html',context={
        
    })

def Contact(request):
    return render(request,'main/contact.html',context={
        
    })

def Product(request):
    return render(request,'main/product-details.html',context={
        
    })

def Shop(request):
    return render(request,'main/shop.html',context={
        
    })

