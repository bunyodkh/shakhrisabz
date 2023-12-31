from django.urls import path

app_name = 'records'

from .views import (
    index,
    get_hotels, get_hotel,
    get_restaurants, get_restaurant,
    get_pois, get_poi,
    get_guide,
    get_tours, get_tour,
    get_organizations, get_organization,
    get_posts, get_post,
    get_transports, get_transport,
    get_events, get_event,
    subscribe,
    search,
    get_feedback_form,
    show404
)

urlpatterns = [
    path('', index, name='index'),

    path('hotels/', get_hotels, name='hotel-list'),
    path('hotels/<int:pk>', get_hotel, name='hotel-detail'),

    path('restaurants/', get_restaurants, name='restaurant-list'),
    path('restaurants/<int:pk>', get_restaurant, name='restaurant-detail'),

    path('guides/<int:pk>', get_guide, name='guide-detail'),

    path('tours/', get_tours, name='tour-list'),
    path('tours/<int:pk>', get_tour, name='tour-detail'),

    path('organizations/', get_organizations, name='organization-list'),
    path('organization/<int:pk>', get_organization, name='organization-detail'),

    path('posts/', get_posts, name='post-list'),
    path('posts/<int:pk>', get_post, name='post-detail'),

    path('point-of-interests/', get_pois, name='poi-list'),
    path('point-of-interests/<int:pk>', get_poi, name='poi-detail'),

    path('transports/', get_transports, name='transport-list'),
    path('transports/<int:pk>', get_transport, name='transport-detail'),

    path('events/', get_events, name='event-list'),
    path('events/<int:pk>', get_event, name='event-detail'),

    path('posts/', get_posts, name='post-list'),
    path('post/<int:pk>', get_post, name='post-detail'),

    path('subscribe/', subscribe, name='subscribe'),
    path('search/', search, name='search'),

    path('feedback/', get_feedback_form, name='feedback'),

    path('404/', show404, name='404'),

]
