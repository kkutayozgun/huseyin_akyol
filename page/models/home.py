from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

from page.models import seo_translations, SEOStarterModel


class HomePageSeo(TranslatableModel, SEOStarterModel):
    translations = TranslatedFields(
        **seo_translations
    )

    class Meta:
        verbose_name = _("Anasayfa SEO")
        verbose_name_plural = _("Anasayfa SEO")
