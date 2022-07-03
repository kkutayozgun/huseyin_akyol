from django import template
from page.models import (HomePageSeo, About, Surgery, ChangeJourney, TreatmentPlan, Faq, Image)

register = template.Library()


@register.simple_tag
def get_home_obj():
    return HomePageSeo.objects.first()

@register.simple_tag
def get_about_obj():
    return About.objects.select_related(['slides', 'slides_bottom', 'aboutlist']).first()

@register.simple_tag
def get_surgery_obj():
    return Surgery.objects.first()

@register.simple_tag
def get_change_journey_obj():
    return ChangeJourney.objects.first()

@register.simple_tag
def get_treatment_plan_obj():
    return TreatmentPlan.objects.select_related('treatmentplanitem').first()

@register.simple_tag
def get_faq_obj():
    return Faq.objects.first()
