from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

from page.models import seo_translations, SEOStarterModel


class Image(models.Model):
    image = models.ImageField(_("Resim"), upload_to="images", blank=False)

    class Meta:
        verbose_name = _("Resim")
        verbose_name_plural = _("Resimler")

class HomePageSeo(TranslatableModel, SEOStarterModel):
    slides = models.ManyToManyField(Image, related_name="intro_slides", through="HomePageSeoSlides")
    translations = TranslatedFields(
        **seo_translations,
        title_intro=models.CharField(_("Başlık Girişi"), default="", blank=True, max_length=60),
        title=models.CharField(_("Başlık"), default="", blank=True, max_length=80),
        description=models.TextField(_("Açıklama"), default="", blank=True),
        bottom_content=models.TextField(_("Alt Bant İçeriği"), default="", blank=True),
    )

    class Meta:
        verbose_name = _("Anasayfa Giriş Bloku")
        verbose_name_plural = _("Anasayfa Giriş Bloku")

class About(TranslatableModel):
    slides = models.ManyToManyField(Image, related_name="about_slides", through="AboutSlides")
    slides_bottom = models.ManyToManyField(Image, related_name="about_slides_bottom", through="AboutBottomSlides")
    translations = TranslatedFields(
        title=models.CharField(_("Başlık"), default="", blank=True, max_length=80),
        intro=models.TextField(_("Giriş"), default="", blank=True),
        description_title=models.CharField(_("Açıklama Girişi"), default="", blank=True, max_length=80),
        description=models.TextField(_("Açıklama"), default="", blank=True),
    )

    class Meta:
        verbose_name = _("Hakkımızda")
        verbose_name_plural = _("Hakkımızda")

class AboutList(models.Model):
    about = models.ForeignKey(About, verbose_name=_("Hakkımızda"), on_delete=models.CASCADE)
    item=models.CharField(_("Madde"), default="", blank=False, max_length=25)

    class Meta:
        verbose_name = _("Hakkımızda Maddeler")
        verbose_name_plural = _("Hakkımızda Maddeler")

# slide relations
class HomePageSeoSlides(models.Model):
    home=models.ForeignKey(HomePageSeo, on_delete=models.CASCADE)
    image=models.ForeignKey(Image, on_delete=models.CASCADE)

class AboutSlides(models.Model):
    about=models.ForeignKey(About, related_name="about_slides", on_delete=models.CASCADE)
    image=models.ForeignKey(Image, on_delete=models.CASCADE)

class AboutBottomSlides(models.Model):
    about=models.ForeignKey(About, related_name="about_slides_bottom", on_delete=models.CASCADE)
    image=models.ForeignKey(Image, on_delete=models.CASCADE)


class Surgery(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("Başlık"), default="", blank=True, max_length=80),
        description=models.TextField(_("Açıklama"), default="", blank=True),
        image = models.ImageField(_("Resim"), upload_to="surgery", blank=False)
    )

    class Meta:
        verbose_name = _("Obezite ve Metabolik Cerrahi")
        verbose_name_plural = _("Obezite ve Metabolik Cerrahi")


class ChangeJourney(models.Model):
    image = models.ImageField(_("Resim"), upload_to="change-journey", blank=False)

    class Meta:
        verbose_name = _("Değişim Yolculuğu")
        verbose_name_plural = _("Değişim Yolculukları")


class TreatmentPlan(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("Adı"), blank=False, max_length=25),
    )

    class Meta:
        verbose_name = _("Tedavi Planı")
        verbose_name_plural = _("Tedavi Planları")

class TreatmentPlanItems(models.Model):
    treatment_plan = models.ForeignKey(TreatmentPlan, verbose_name=_("Tedavi Planı"), on_delete=models.CASCADE)
    item=models.CharField(_("Madde"), blank=False, max_length=25)

    class Meta:
        verbose_name = _("Tedavi Planı Maddeler")
        verbose_name_plural = _("Tedavi Planı Maddeler")


class Faq(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("Soru"), blank=False, max_length=85),
        description=models.TextField(_("Cevap"), blank=False),
    )
    class Meta:
        verbose_name = _("Sık Sorulan Soru")
        verbose_name_plural = _("Sık Sorulan Sorular")