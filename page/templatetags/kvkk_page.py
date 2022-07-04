from django import template
from page.models import KVKKPageSeo

register = template.Library()


@register.simple_tag
def get_kvkk_obj ():
    return KVKKPageSeo.objects.first()