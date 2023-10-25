from django.db import models
from django.urls import reverse
from location_field.models.plain import PlainLocationField

from helpers.utils import path_and_rename


class Guide(models.Model):
    first_name = models.CharField('Имя', max_length=100, null=False, blank=False)
    last_name = models.CharField('Фамилия', max_length=100, null=False, blank=False)
    middle_name = models.CharField('Отчество', max_length=100, null=True, blank=True)

    SEX_CHOICES = (('Male', 'Мужчина'), ('Female', 'Женщина'))
    sex = models.CharField('Пол', max_length=20, choices=SEX_CHOICES, blank=True, null=True, default='Male')
    age = models.PositiveIntegerField('Возраст', null=True, blank=True)
    image = models.ImageField('Фотография', upload_to=path_and_rename('uploads/guides'), blank=True, null=True)

    daily_fee = models.PositiveIntegerField('Стоимость услуг за день (в сумах)', null=True, blank=True)
    email = models.CharField('Электронная почта', max_length=100, null=True, blank=True)
    phone = models.CharField('Телефон', max_length=100, null=True, blank=True)
    telegram = models.CharField('Telegram', max_length=100, null=True, blank=True)
    facebook = models.CharField('Фейбук', max_length=100, null=True, blank=True)
    instagram = models.CharField('Инстаграм', max_length=100, null=True, blank=True)

    notes = models.TextField('Дополнительная информация', null=True, blank=True)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('records:guide-detail', kwargs={'pk': self.pk})

    def get_fullname(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['-created']
        verbose_name = 'Гид'
        verbose_name_plural = 'Гиды'


class Restaurant(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    main_image = models.ImageField(upload_to=path_and_rename('uploads/restaurants'), null=True, blank=True)
    description = models.TextField('Краткое описание', max_length=1000, null=True, blank=True)

    address = models.CharField('Адрес', max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    telegram = models.CharField(max_length=100, null=True, blank=True)

    average_bill = models.CharField(max_length=100, null=True, blank=True)

    city = models.CharField(max_length=255, null=True, blank=True, default='Shahrisabz')
    location = PlainLocationField(based_fields=['city'], default='39.060366, 66.845915', zoom=7)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'

    def get_absolute_url(self, **kwargs):
        return reverse('records:restaurant-detail', kwargs={'pk': self.id})


class Meal(models.Model):
    title = models.CharField('Название пункта меню', max_length=200, null=False, blank=False)
    price = models.PositiveIntegerField('Цена одной единицы')
    restaurant_attached = models.ForeignKey('Restaurant', null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=path_and_rename('uploads/meals'), null=True, blank=True)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'


class RestaurantImage(models.Model):
    image = models.ImageField(upload_to=path_and_rename('uploads/restaurants'), null=True, blank=True)
    # TODO: main image is duplicated in model and here - fix it later
    restaurant_attached = models.ForeignKey('Restaurant', null=True, blank=True, on_delete=models.CASCADE)
    caption = models.CharField('Описание к изображнию', max_length=200, null=True, blank=True)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['caption']
        verbose_name = 'Изображение ресторана'
        verbose_name_plural = 'Изображения ресторана'

    def __str__(self) -> str:
        return f'{self.caption}'


class Hotel(models.Model):
    title = models.CharField('Название', max_length=100, null=False, blank=False)
    description = models.TextField('Описание', max_length=1000, null=True, blank=True)
    address = models.TextField('Адрес', max_length=1000, null=True, blank=True)
    main_image = models.ImageField(upload_to=path_and_rename('uploads/hotels'), null=True, blank=True)

    notes = models.TextField('Дополнительная информация', null=True, blank=True)

    city = models.CharField('Город', max_length=255, null=True, blank=True, default='Shahrisabz')
    location = PlainLocationField(based_fields=['city'], default='39.060366, 66.845915', zoom=7)

    phone = models.CharField('Телефон', max_length=100, null=True, blank=True)
    email = models.CharField('Электронная почта', max_length=100, null=True, blank=True)
    telegram = models.CharField('Телеграм', max_length=100, null=True, blank=True)
    facebook = models.CharField('Фейсбук', max_length=100, null=True, blank=True)
    instagram = models.CharField('Инстаграм', max_length=100, null=True, blank=True)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'

    def get_absolute_url(self, **kwargs):
        return reverse('records:hotel-detail', kwargs={'pk': self.id})


class HotelRoom(models.Model):
    title = models.CharField('Название комнаты', max_length=200, null=False, blank=False)
    price = models.PositiveIntegerField('Цена комнаты')
    hotel_attached = models.ForeignKey('Hotel', null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=path_and_rename('uploads/rooms'), null=True, blank=True)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = 'Комната отеля'
        verbose_name_plural = 'Комнаты отеля'


class HotelImage(models.Model):
    image = models.ImageField(upload_to=path_and_rename('uploads/hotels'), null=True, blank=True)
    # TODO: main image is duplicated in model and here - fix it later
    main = models.BooleanField('Главное изображение', default=False)
    hotel_attached = models.ForeignKey('Hotel', null=True, blank=True, on_delete=models.CASCADE)
    caption = models.CharField('Описание к изображнию', max_length=200, null=True, blank=True)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['caption']
        verbose_name = 'Изображение отеля'
        verbose_name_plural = 'Изображения отеля'

    def __str__(self) -> str:
        return f'{self.caption}'


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=100, null=False, blank=False)
    description = models.TextField('Текст поста', null=True, blank=True)
    image = models.ImageField('Изображение', upload_to=path_and_rename('uploads/posts'), null=True, blank=True)
    author = models.CharField('Автор', max_length=100, null=True, blank=True)

    date = models.DateField('Дата публикации')

    draft = models.BooleanField('Черновик', blank=False, null=False, default=False)

    TYPE_CHOICES = (('News', 'Новость'), ('Blog', 'Запись в блоге'), ('Other', 'Другое'))
    post_type = models.CharField('Тип публикации', max_length=20, choices=TYPE_CHOICES, blank=True, null=True,
                                 default='News')

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def get_absolute_url(self, **kwargs):
        return reverse('records:post-detail', kwargs={'pk': self.id})

    def posttype_verbose(self):
        return dict(Post.TYPE_CHOICES)[self.post_type]


class POI(models.Model):  # points of interest
    title = models.CharField('Название', max_length=100, null=False, blank=False)
    description = models.TextField('Описание', blank=True, null=True)

    TYPE_CHOICES = (
        ('geology', 'Геологические объекты'),
        ('ecotourism', 'Объекты экотуризма'),
        ('info', 'Информационные центры'),
        ('craft', 'Туристические деревни и ремесла'),
        ('shrine', 'Cвятыни'),
        ('historical_places', 'Исторические места'),
        ('gastronomy', 'Гастрономические центры'),
        ('others', 'Другие'),
    )
    poi_type = models.CharField('Тип интереса', max_length=20, choices=TYPE_CHOICES, blank=True, null=True,
                                default='Event')

    city = models.CharField('Город', max_length=255, null=True, blank=True, default='Shahrisabz')
    location = PlainLocationField(based_fields=['city'], default='39.060366, 66.845915', zoom=7)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self, **kwargs):
        return reverse('records:poi-detail', kwargs={'pk': self.id})

    def poitype_verbose(self):
        return dict(POI.TYPE_CHOICES)[self.poi_type]

    class Meta:
        ordering = ['-created']
        verbose_name = 'Точка интереса'
        verbose_name_plural = 'Точки интереса'


class POIImage(models.Model):
    image = models.ImageField(upload_to=path_and_rename('uploads/pois'), null=True, blank=True)
    main = models.BooleanField('Главное изображение', default=False)
    case_attached = models.ForeignKey('POI', null=True, blank=True, on_delete=models.CASCADE)
    caption = models.CharField(max_length=200, null=True, blank=True)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['caption']
        verbose_name = 'Изображение точки интереса'
        verbose_name_plural = 'Изображения точки интереса'

    def __str__(self) -> str:
        return f'{self.caption}'


class Transport(models.Model):
    model = models.CharField('Модель транспорта', max_length=100, null=True, blank=True)
    type = models.CharField('Тип транспорта', max_length=100, null=True, blank=True)
    transport_image = models.ImageField(upload_to=path_and_rename('uploads/transports'), null=True, blank=True)

    driver = models.CharField('Имя водителя', max_length=200, null=True, blank=True)
    phone = models.CharField('Номер телефона', max_length=50, null=True, blank=True)
    driver_image = models.ImageField(upload_to=path_and_rename('uploads/drivers'), null=True, blank=True)

    notes = models.TextField('Дополнительная информация', max_length=500, null=True, blank=True)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.model} - {self.driver}'

    class Meta:
        ordering = ['-created']
        verbose_name = 'Транспортное средство'
        verbose_name_plural = 'Транспортные средства'


class Organization(models.Model):
    title = models.CharField('Название', max_length=100, null=False, blank=False)
    description = models.TextField('Описание', max_length=1000, null=True, blank=True)
    address = models.TextField('Адрес', max_length=1000, null=True, blank=True)

    TYPE_CHOICES = (
        ('government', 'Госучреждение'),
        ('business', 'Частный бизнес'),
        ('production', 'Производство'),
        ('service', 'Оказание услуг'),
        ('education', 'Образовательное учреждение'),
        ('others', 'Другие'),
    )
    org_type = models.CharField('Тип организации', max_length=20, choices=TYPE_CHOICES, blank=True, null=True,
                                default='government')

    notes = models.TextField('Дополнительная информация', null=True, blank=True)

    city = models.CharField('Город', max_length=255, null=True, blank=True, default='Shahrisabz')
    location = PlainLocationField(based_fields=['city'], default='39.060366, 66.845915', zoom=7)

    phone = models.CharField('Телефон', max_length=100, null=True, blank=True)
    email = models.CharField('Электронная почта', max_length=100, null=True, blank=True)
    telegram = models.CharField('Телеграм', max_length=100, null=True, blank=True)
    facebook = models.CharField('Фейсбук', max_length=100, null=True, blank=True)
    instagram = models.CharField('Инстаграм', max_length=100, null=True, blank=True)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def orgtype_verbose(self):
        return dict(Organization.TYPE_CHOICES)[self.org_type]

    def get_absolute_url(self, **kwargs):
        return reverse('records:organization-detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['-created']
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class OrganizationImage(models.Model):
    image = models.ImageField(upload_to=path_and_rename('uploads/organizations'), null=True, blank=True)
    main = models.BooleanField('Главное изображение', default=False)
    case_attached = models.ForeignKey('Organization', null=True, blank=True, on_delete=models.DO_NOTHING)
    caption = models.CharField(max_length=200, null=True, blank=True)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['caption']
        verbose_name = 'Изображение организации'
        verbose_name_plural = 'Изображения организации'

    def __str__(self) -> str:
        return f'{self.caption}'


class Alert(models.Model):  # TODO: require design (HTML/CSS)
    title = models.CharField(max_length=100, null=False, blank=False)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = 'Техническое объявление'
        verbose_name_plural = 'Техническое объявления'


class Category(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    slug = models.CharField(max_length=100, null=True, blank=True)
    parent_category = models.ForeignKey('self', on_delete=models.DO_NOTHING, blank=True, null=True)
    visible_on_main = models.BooleanField('Показывать в главной навигации', default=False)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Event(models.Model):
    title = models.CharField('Название', max_length=100, null=False, blank=False)
    description = models.TextField('Описание', null=True, blank=True)

    TYPE_CHOICES = (
        ('Ad', 'Анонс'),
        ('Happening', 'Событие'),
        ('Event', 'Мероприятие'),
        ('Meeting', 'Встреча'),
        ('Visit', 'Визит'))

    event_type = models.CharField('Тип', max_length=20, choices=TYPE_CHOICES, blank=True, null=True,
                                  default='Event')

    city = models.CharField('Город', max_length=255, null=True, blank=True, default='Shahrisabz')
    location = PlainLocationField(based_fields=['city'], default='39.060366, 66.845915', zoom=7)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = 'Анонс / Событие / Мероприятие'
        verbose_name_plural = 'Анонсы / События / Мероприятия'


class EventImage(models.Model):
    image = models.ImageField(upload_to=path_and_rename('uploads/events'), null=True, blank=True)
    main = models.BooleanField('Главное изображение', default=False)
    case_attached = models.ForeignKey('Event', null=True, blank=True, on_delete=models.CASCADE)
    caption = models.CharField(max_length=200, null=True, blank=True, default='Изображение')

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['caption']
        verbose_name = 'Изображение мероприятия'
        verbose_name_plural = 'Изображения мероприятия'

    def __str__(self) -> str:
        return f'{self.caption}'


class Feedback(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = 'Обратная связь - сообщение'
        verbose_name_plural = 'Обратная связь - сообщения'


class Subscription(models.Model):
    email = models.EmailField('Электронная почта пользователя', null=False, blank=False)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-created']
        verbose_name = 'Подписка на рассылку'
        verbose_name_plural = 'Подписки на рассылку'


class ImageGallery(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=1000, null=True, blank=True)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'


class ImageGalleryImage(models.Model):
    image = models.ImageField(upload_to=path_and_rename('uploads/gallery'), null=True, blank=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    caption = models.CharField(max_length=200, null=True, blank=True, default='Изображение')

    main = models.BooleanField('Главное изображение', default=False)
    case_attached = models.ForeignKey('ImageGallery', null=True, blank=True, on_delete=models.CASCADE)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['caption']
        verbose_name = 'Изображение галерии'
        verbose_name_plural = 'Изображения галерии'

    def __str__(self) -> str:
        return f'{self.title}'


class Tour(models.Model):
    title = models.CharField('Название', max_length=600, null=False, blank=False)
    description = models.TextField('Описание', max_length=1000, null=False, blank=False)
    image = models.ImageField(upload_to=path_and_rename('uploads/tours'), null=False, blank=False)
    price = models.CharField('Цена', max_length=50, null=False, blank=False)
    address = models.CharField('Адрес', max_length=200, null=False, blank=False)

    company = models.ForeignKey('Organization', on_delete=models.DO_NOTHING, null=True, blank=True,
                                verbose_name='Организатор')
    guide = models.ForeignKey('Guide', on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Гид')

    notes = models.TextField('Дополнительная информация', null=True, blank=True)
    active = models.BooleanField('Активно', default=False)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'

    def __str__(self) -> str:
        return f'{self.title}'
