from django import template

register = template.Library()

from records.models import Category


@register.inclusion_tag('includes/nav.html')  # takes_context=True
def categories():  # context, *args, **kwargs
    category_list = Category.objects.all()
    return {'categories': category_list}
