from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from parler.admin import TranslatableAdmin

from page.models import (Keywords, seo_translations, HomePageSeo, About, AboutList, Image,
                         HomePageSeoSlides, AboutSlides, AboutBottomSlides,
                         Surgery, ChangeJourney, TreatmentPlan, TreatmentPlanItems, Faq
                         )

admin.site.register(Keywords, TranslatableAdmin)
admin.site.register(Image)
admin.site.register(AboutList)
admin.site.register(TreatmentPlanItems)

seo_fields = tuple(seo_translations.keys()) + ("meta_keywords",)

class HomeSlidesInline(admin.TabularInline):
    model = HomePageSeoSlides

@admin.register(HomePageSeo)
class HomePageSeoAdmin(TranslatableAdmin):
    fieldsets = (
        (_("Seo Information"), {'fields': seo_fields}),
    )
    inlines = [HomeSlidesInline]
    exclude = ('slides',)


class AboutListInline(admin.TabularInline):
    model = AboutList

class AboutSlidesBottomInline(admin.TabularInline):
    model = AboutSlides

class AboutSlidesInline(admin.TabularInline):
    model = AboutBottomSlides

@admin.register(About)
class AboutAdmin(TranslatableAdmin):
    exclude = ('slides', 'slides_bottom')
    inlines = [AboutListInline, AboutSlidesInline, AboutSlidesBottomInline]


@admin.register(Surgery)
class SurgeryAdmin(TranslatableAdmin):
    pass

@admin.register(Faq)
class FaqAdmin(TranslatableAdmin):
    pass

@admin.register(ChangeJourney)
class ChangeJourneyAdmin(admin.ModelAdmin):
    pass


class TreatmentPlanItemsInline(admin.TabularInline):
    model = TreatmentPlanItems

@admin.register(TreatmentPlan)
class TreatmentPlanAdmin(TranslatableAdmin):
    inlines = [TreatmentPlanItemsInline]