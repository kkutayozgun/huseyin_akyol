from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from ckeditor_uploader.fields import RichTextUploadingField

from page.models import seo_translations, SEOStarterModel


class KVKKPageSeo(TranslatableModel, SEOStarterModel):
    translations = TranslatedFields(
        content=RichTextUploadingField(verbose_name=_("Content"), blank=True, null=True),
        **seo_translations
    )
    banner_image = models.ImageField(_("Banner Image"), upload_to="about/banner", blank=True, null=True)

    class Meta:
        verbose_name = _("KVKK Sayfası SEO")
        verbose_name_plural = _("KVKK Sayfası SEO")