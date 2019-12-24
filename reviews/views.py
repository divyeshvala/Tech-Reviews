from django.shortcuts import render, redirect
from .models import Review, Product
from django.contrib import messages
from django.db import models
from datetime import date
from datetime import datetime

def products_view(request):
    products = Product.objects.all()
    user = request.user
    return render(request, 'products.html', {'products':products, "user":user})

def display_view(request, p_id):
    product = Product.objects.get(id=p_id)
    reviews = product.reviews.all()
    user = request.user
    s = sum( review.stars for review in reviews)
    count = reviews.count()
    avg_rating = s/count 
    avg_rating = format(avg_rating, '.2f')
    return render(request, 'display_reviews.html', {"reviews" : reviews, "user":user, "p_id":p_id, "avg_rating": avg_rating})

def write_view(request, p_id):
    user = request.user
    if request.method == "POST":
        text = request.POST["text"]
        stars = request.POST["stars"]
        user = request.user

        if user.is_authenticated :
            author = user.first_name
            today = str(date.today())
            time = str(datetime.now())
            r_id = Review.objects.create(text=text, stars=stars, author=author, time=time)
            Product.objects.get(id=p_id).reviews.add(r_id)
            messages.info(request, 'review submited')
        else:
            # ask user to login first
            messages.info(request, 'Please login first')

    return redirect('display_view_url', p_id)

