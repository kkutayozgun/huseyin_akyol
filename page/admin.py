from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from parler.admin import TranslatableAdmin, TranslatableTabularInline

from page.models import (Keywords, seo_translations, HomePageSeo, About, AboutList, Image,
                         HomePageSeoSlides, AboutSlides, AboutBottomSlides,
                         Surgery, ChangeJourney, TreatmentPlan, TreatmentPlanItem, Faq, KVKKPageSeo
                         )

admin.site.register(Keywords, TranslatableAdmin)

class HiddenModel(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}

@admin.register(Image)
class ImageAdmin(HiddenModel):
    pass
@admin.register(AboutList)
class AboutListAdmin(HiddenModel):
    pass
@admin.register(TreatmentPlanItem)
class TreatmentPlanItemAdmin(HiddenModel):
    pass

seo_fields = tuple(seo_translations.keys()) + ("meta_keywords",)

class OneEntityModel(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        return super().has_add_permission(request)

class HomeSlidesInline(admin.TabularInline):
    model = HomePageSeoSlides

@admin.register(HomePageSeo)
class HomePageSeoAdmin(TranslatableAdmin, OneEntityModel):
    fieldsets = (
        (_("Seo Information"), {'fields': seo_fields}),
    )
    inlines = [HomeSlidesInline]
    exclude = ('slides',)


class AboutListInline(TranslatableTabularInline):
    model = AboutList

class AboutSlidesBottomInline(admin.TabularInline):
    model = AboutSlides

class AboutSlidesInline(admin.TabularInline):
    model = AboutBottomSlides

@admin.register(About)
class AboutAdmin(TranslatableAdmin, OneEntityModel):
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


class TreatmentPlanItemsInline(TranslatableTabularInline):
    model = TreatmentPlanItem

@admin.register(TreatmentPlan)
class TreatmentPlanAdmin(TranslatableAdmin):
    inlines = [TreatmentPlanItemsInline]


@admin.register(KVKKPageSeo)
class KVKKPageSeoAdmin(TranslatableAdmin):
    fieldsets = (
        (_("İçerik Bilgisi"), {'fields': ('content',)}),
        (_("SEO Bilgisi"), {'fields': seo_fields}),
    )
    filter_vertical = ('meta_keywords',)