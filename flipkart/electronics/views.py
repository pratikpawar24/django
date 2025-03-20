from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
def home(request):
    return render(request, 'electronics/home.html')

def product_details(request):
    prod = Product.objects.all()
    form = ProductForm()
    
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductForm()
    return render(request,'electronics/product_details.html',{"prod":prod,'form':form})

def update_product(request,id):
    prod = get_object_or_404(Product,id=id)

    if request.method == "POST":
        form = ProductForm(request.POST,instance=prod)
        if form.is_valid():
            form.save()
            return redirect('product_detail')
    else:
        form = ProductForm(instance=prod)
    return render(request,'electronics/update_product.html',{'form':form,'prod':prod})

    

def delete_product(request,id):
    prod = get_object_or_404(Product,id=id)
    prod.delete()
    return redirect('product_detail')

