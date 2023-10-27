from django.contrib import admin

from .models import (
    Guide,
    Post,
    Hotel, HotelImage, HotelRoom,
    Restaurant, RestaurantImage, Meal,
    Category,
    Transport,
    POI, POIImage,
    Organization, OrganizationImage,
    Subscription,
    Event, EventImage,
    ImageGallery, ImageGalleryImage,
    Tour,
    MainBanner
)


class POIImageInline(admin.TabularInline):
    model = POIImage
    extra = 0
    fields = ['image', 'caption', 'main']


class POIAdmin(admin.ModelAdmin):
    inlines = [POIImageInline]

    list_display = ['title', 'poi_type']
    list_display_links = ['title', ]
    list_filter = ['poi_type']
    search_fields = ['title', 'description', 'poi_type']
    # readonly_fields = ['']

    fieldsets = (
        ('Общая информация', {
            'fields': (
                'title',
                'description',
                'address',
                'poi_type',
                'city',
                'location'
            )
        }),
    )


admin.site.register(POI, POIAdmin)


class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 0
    fields = ['image', 'caption', 'main']


class HotelRoomInline(admin.TabularInline):
    model = HotelRoom
    extra = 0
    fields = ['title', 'price', 'image']


class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelImageInline, HotelRoomInline]

    list_display = ['title', 'email', 'phone']
    list_display_links = ['title', 'email', 'phone']
    search_fields = ['title', 'description', 'email']

    fieldsets = (
        ('Общая информация', {
            'fields': (
                'title',
                'description',
                'address',
                'main_image',
                'city',
                'location',
                'notes'
            )
        }),
        ('Контактные данные', {
            'fields': (
                'phone',
                'email',
                'telegram',
                'facebook',
                'instagram'
            )
        }),
    )


admin.site.register(Hotel, HotelAdmin)


class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 0
    fields = ['image', 'caption', 'main']


class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline]

    list_display = ['title', ]
    list_display_links = ['title', ]
    list_filter = ['event_type']
    search_fields = ['title', 'description', 'event_type']

    fieldsets = (
        ('Общая информация', {
            'fields': (
                'title',
                'address',
                'description',
                'event_type',
                'city',
                'location',
            )
        }),
    )


admin.site.register(Event, EventAdmin)


class GuideAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone']
    list_display_links = ['first_name', 'last_name', 'phone']
    list_filter = ['age', 'sex', 'first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'phone']

    fieldsets = (
        ('Общая информация', {
            'fields': (
                'first_name',
                'last_name',
                'middle_name',
                'sex',
                'age',
                'daily_fee',
                'image',
                'notes'
            )
        }),

        ('Контактные данные', {
            'fields': (
                'email',
                'phone',
                'telegram',
                'instagram',
                'facebook',
            )
        }),
    )


admin.site.register(Guide, GuideAdmin)


class OrganizationImageInline(admin.TabularInline):
    model = OrganizationImage
    extra = 0
    fields = ['image', 'caption', 'main']


class OrganizationAdmin(admin.ModelAdmin):
    inlines = [OrganizationImageInline]

    list_display = ['title', 'email', 'phone']
    list_display_links = ['title', 'email', 'phone']
    search_fields = ['title', 'description', 'email']

    fieldsets = (
        ('Общая информация', {
            'fields': (
                'title',
                'description',
                'org_type',
                'address',
                'city',
                'location',
                'notes'
            )
        }),
        ('Контактные данные', {
            'fields': (
                'phone',
                'email',
                'telegram',
                'facebook',
                'instagram'
            )
        }),
    )


admin.site.register(Organization, OrganizationAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'post_type', 'draft']
    list_display_links = ['title']
    search_fields = ['title', 'description']

    fieldsets = (
        ('Общая информация', {
            'fields': (
                'title',
                'description',
                'post_type',
                'draft',
                'main_image',
                'author',
            )
        }),
    )


class ImageGalleryImageInline(admin.TabularInline):
    model = ImageGalleryImage
    extra = 0
    fields = ['image', 'caption', 'main']


class ImageGalleryAdmin(admin.ModelAdmin):
    inlines = [ImageGalleryImageInline]

    list_display = ['title', ]
    list_display_links = ['title']
    search_fields = ['title', ]

    fieldsets = (
        ('Общая информация', {
            'fields': (
                'title',
                'description',
            )
        }),
    )


admin.site.register(ImageGallery, ImageGalleryAdmin)


class RestaurantImageInline(admin.TabularInline):
    model = RestaurantImage
    extra = 0
    fields = ['image', 'caption']


class MealInline(admin.TabularInline):
    model = Meal
    extra = 0
    fields = ['title', 'price', 'image']


class RestaurantAdmin(admin.ModelAdmin):
    inlines = [RestaurantImageInline, MealInline]

    list_display = ['title', 'email', 'phone']
    list_display_links = ['title', 'email', 'phone']
    search_fields = ['title', 'description', 'email']

    fieldsets = (
        ('Общая информация', {
            'fields': (
                'title',
                'description',
                'address',
                'main_image',
                'city',
                'location',
                'average_bill',
            )
        }),
        ('Контактные данные', {
            'fields': (
                'phone',
                'email',
                'telegram',
                'facebook',
                'instagram'
            )
        }),
    )


admin.site.register(Restaurant, RestaurantAdmin)

admin.site.register(Transport)
admin.site.register(Category)
admin.site.register(Subscription)
admin.site.register(Tour)
admin.site.register(Post)
admin.site.register(MainBanner)