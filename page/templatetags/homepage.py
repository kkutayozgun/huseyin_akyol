from math import ceil
from django import template
from page.models import (HomePageSeo, About, Surgery, ChangeJourney, TreatmentPlan, Faq, CustomerReview)
from numpy import array_split

register = template.Library()

@register.filter(name='chunk')
def chunk(collection, num):
    return array_split(collection, num)

@register.filter(name='pieces')
def pieces(collection, num):
    total = len(collection)
    chunk_size = ceil(total/num)
    if chunk_size <= 0:
        chunk_size = 1
    return array_split(collection, chunk_size)

@register.simple_tag
def get_home_obj():
    return HomePageSeo.objects.first()

@register.simple_tag
def get_about_obj():
    return About.objects.prefetch_related('slides', 'slides_bottom', 'aboutlist_set').first()

@register.simple_tag
def get_surgery_obj():
    return Surgery.objects.all()

@register.simple_tag
def get_change_journey_obj():
    return ChangeJourney.objects.all()

@register.simple_tag
def get_treatment_plan_obj():
    return TreatmentPlan.objects.prefetch_related('treatmentplanitem_set').all()

@register.simple_tag
def get_faq_obj():
    return Faq.objects.all()

@register.simple_tag
def get_customer_review_obj():
    return CustomerReview.objects.all()
