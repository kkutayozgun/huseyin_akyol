from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from parler.admin import TranslatableAdmin

from page.models import (Keywords, seo_translations, HomePageSeo, About, AboutList, Image,
                         HomePageSeoSlides, AboutSlides, AboutBottomSlides)

admin.site.register(Keywords, TranslatableAdmin)
admin.site.register(Image)
admin.site.register(AboutList)

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
