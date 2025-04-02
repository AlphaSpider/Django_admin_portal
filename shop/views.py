from django.shortcuts import render, redirect
from .models import Category, Product

# Create your views here.
def home(request):
    all_products=Product.objects.all()
    return render(request, "index.html", {"data":all_products})
    print()

def add_product(request):
    cat_data=Category.objects.all()
    if request.method=="POST":
        id=request.POST.get("category")
        categoty_obj=Category.objects.get(cat_id=id)
        product_obj=Product()
        product_obj.name=request.POST.get("name")
        product_obj.price=request.POST.get("price")
        product_obj.stock=request.POST.get("stock")
        product_obj.category=categoty_obj
        print(request.FILES.get("product_image"))
        product_obj.product_image=request.FILES.get("product_image")
        print("Image recieved")
        product_obj.save()
        return redirect('/')
    return render(request, "add_product.html", {"data":cat_data})