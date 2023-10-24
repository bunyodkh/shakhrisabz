from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

from .models import Category, Hotel, POI, Guide, Restaurant, Tour, Organization, Post
from helpers.utils import email_valid

from .models import Subscription


def index(request):
    context = {
        'categories': Category.objects.all(),
        'poi': POI.objects.first(),
        'hotels': Hotel.objects.all(),
        'guides': Guide.objects.all(),
        'restaurants': Restaurant.objects.all()
    }
    return render(request, 'index.html', context)


def get_hotels(request):
    context = {'hotels': Hotel.objects.all()}
    return render(request, 'hotels.html', context)


def get_hotel(request, *args, **kwargs):
    hotel_id = kwargs['pk']
    context = {'hotel': Hotel.objects.get(id=hotel_id)}
    return render(request, 'hotel.html', context)


def get_restaurants(request):
    context = {'restaurants': Restaurant.objects.all()}
    return render(request, 'restaurants.html', context)


def get_restaurant(request, *args, **kwargs):
    restaurant_id = kwargs['pk']
    context = {'restaurant': Restaurant.objects.get(id=restaurant_id)}
    return render(request, 'restaurant.html', context)


def get_pois(request):
    context = {'pois': POI.objects.all()}
    return render(request, 'index.html', context)


def get_guide(request, *args, **kwargs):
    guide_id = kwargs['pk']
    context = {'guide': Guide.objects.get(id=guide_id)}
    return render(request, 'guide.html', context)


def get_tours(request):
    context = {'tours': Tour.objects.all()}
    return render(request, 'tours.html', context)


def get_organizations(request):
    context = {'organizations': Organization.objects.all()}
    return render(request, 'organizations.html', context)


def get_organization(request, *args, **kwargs):
    organization_id = kwargs['pk']
    context = {'organization': Organization.objects.get(id=organization_id)}
    return render(request, 'organization.html', context)


def get_posts(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'posts.html', context)


def get_post(request, *args, **kwargs):
    post_id = kwargs['pk']
    context = {'post': Post.objects.get(pk=post_id)}
    return render(request, 'post.html', context)

def subscribe(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        validation_result = email_valid(data['email'])  # return type - boolean
        if validation_result:
            if not Subscription.objects.filter(email=data['email']).exists():
                Subscription.objects.create(email=data['email'])
                return JsonResponse({'message': 'Subscribed'})
            else:
                return JsonResponse({'message': 'Duplicate found'})
    return redirect('/')
