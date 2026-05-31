from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Post, Banner, Visitor, ProductCategory
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .models import ContactMessage

def home(request):
    banners = Banner.objects.all()  
    visitor, created = Visitor.objects.get_or_create(id=1)
    visitor.count += 1
    visitor.save()
    return render(request, 'main/home.html', {
        'banners': banners,      
        'visitor_count': visitor.count
    })

def product_list(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    return render(request, 'main/product_list.html', {
        'categories': categories,
        'products': products
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'main/product_detail.html', {'product': product})

def about(request):
    return render(request, 'main/about.html')

def news(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    return render(request, 'main/news.html', {
        'categories': categories,
        'posts': posts
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'main/post_detail.html', {'post': post})

def contact(request):
    return render(request, 'main/contact.html')

@csrf_protect
def contact(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ContactMessage.objects.create(
            fname   = data.get('fname', ''),
            email   = data.get('email', ''),
            phone   = data.get('phone', ''),
            subject = data.get('subject', ''),
            message = data.get('message', ''),
        )
        return JsonResponse({'status': 'ok'})
    return render(request, 'main/contact.html')