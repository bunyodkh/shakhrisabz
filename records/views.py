from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
import json
import requests

from .forms import FeedbackForm

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
    MainBanner,
)

from helpers.utils import email_valid


def index(request):
    context = {
        'categories': Category.objects.all(),
        'poi': POI.objects.first(),
        'hotels': Hotel.objects.all(),
        'guides': Guide.objects.all(),
        'restaurants': Restaurant.objects.all(),
        'banner': MainBanner.objects.filter(active=True).first()
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


def get_tour(request, *args, **kwargs):
    tour_id = kwargs['pk']
    context = {'tour': Tour.objects.get(id=tour_id)}
    return render(request, 'tour.html', context)


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


def get_transports(request):
    context = {'transports': Transport.objects.all()}
    return render(request, 'transports.html', context)


def get_transport(request, *args, **kwargs):
    transport_id = kwargs['pk']
    context = {'transport': Transport.objects.get(pk=transport_id)}
    return render(request, 'transport.html', context)


def get_events(request):
    context = {'events': Event.objects.all()}
    return render(request, 'events.html', context)


def get_event(request, *args, **kwargs):
    event_id = kwargs['pk']
    context = {'event': Event.objects.get(pk=event_id)}
    return render(request, 'event.html', context)


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
            hotels = Hotel.objects.filter(Q(title__contains=query) | Q(description__contains=query))  # included
            restaurants = Restaurant.objects.filter(
                Q(title__contains=query) | Q(description__contains=query))  # included
            organizations = Organization.objects.filter(Q(title__contains=query) | Q(description__contains=query))
            guides = Guide.objects.filter(Q(first_name__contains=query) | Q(last_name__contains=query))  # included
            posts = Post.objects.filter(Q(title__contains=query) | Q(description__contains=query))  # included
            pois = POI.objects.filter(Q(title__contains=query) | Q(description__contains=query))  # included
            transports = Transport.objects.filter(Q(model__contains=query) | Q(driver__contains=query))  # included
            events = Event.objects.filter(Q(title__contains=query) | Q(description__contains=query))  # included
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


def get_feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': '6LdDmNMoAAAAABu5rfHHqvZPiRC6OT3ZKvLEmSAa',
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)

            result = r.json()

            if result['success']:
                form.save()
                return render(request, 'feedback.html', {'message': 'Мы получили ваше сообщение. Спасибо!', 'ok': True})
            else:
                return render(request, 'feedback.html', {
                    'message': 'Проверка обязательно. Пожалуйста, отметье галочку перед тем как отправить сообщение.',
                    'error': True})
        else:
            return render(request, 'feedback.html',
                          {'message': 'Что-то пошло не так. Попробуйте снова.', 'error': True})
    return render(request, 'feedback.html', {})


# serves 404.html page
def e_handler404(request, exception=None):
    return render(request, '404.html', {}, status=404)


# serves 500.html page
def e_handler500(request, exception=None):
    return render(request, '500.html', {}, status=500)


def show404(request):
    return render(request, '404.html', {})