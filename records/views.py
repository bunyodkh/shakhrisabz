from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
import json

from .models import (
    Category,
    Hotel,
    POI,
    Guide,
    Restaurant,
    Tour,
    Organization,
    Post,
    Event,
    Transport,
    Subscription,
)

from helpers.utils import email_valid


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
    return render(request, 'pois.html', context)


def get_poi(request, *args, **kwargs):
    poi_id = kwargs['pk']
    context = {'poi': POI.objects.get(id=poi_id)}
    return render(request, 'poi.html', context)


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


def search(request):
    query = None
    hotels = restaurants = organizations = guides = posts = pois = transports = events = tours = None
    if request.method == 'GET':
        query = request.GET.get('query')
        print(query)
        try:
            hotels = Hotel.objects.filter(Q(title__contains=query) | Q(description__contains=query))
            restaurants = Restaurant.objects.filter(Q(title__contains=query) | Q(description__contains=query))
            organizations = Organization.objects.filter(Q(title__contains=query) | Q(description__contains=query))
            guides = Guide.objects.filter(Q(first_name__contains=query) | Q(last_name__contains=query))
            posts = Post.objects.filter(Q(title__contains=query) | Q(description__contains=query))
            pois = POI.objects.filter(Q(title__contains=query) | Q(description__contains=query))
            transports = Transport.objects.filter(Q(model__contains=query) | Q(driver__contains=query))
            events = Event.objects.filter(Q(title__contains=query) | Q(description__contains=query))
            tours = Tour.objects.filter(Q(title__contains=query) | Q(description__contains=query))
        except:
            hotels = None
            restaurants = None
            organizations = None
            guides = None
            posts = None
            pois = None
            transports = None
            events = None
            tours = None

    return render(request, 'search.html', {
        'hotels': hotels,
        'query': query,
        'restaurants': restaurants,
        'organizations': organizations,
        'pois': pois,
        'posts': posts,
        'transports': transports,
        'events': events,
        'tours': tours,
        'guides': guides,
    })
