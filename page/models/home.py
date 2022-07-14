from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext as _tr
from parler.models import TranslatableModel, TranslatedFields

from page.models import seo_translations, SEOStarterModel


class Image(models.Model):
    image = models.ImageField(_("Resim"), upload_to="images", blank=False)

    def __str__(self):
        return _tr("Resim")

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

    @property
    def slide_items(self):
        return self.homepageseoslides_set.all()

    def __str__(self):
        return _tr("Anasayfa Giriş Bloku ve SEO")

    class Meta:
        verbose_name = _("Anasayfa Giriş Bloku")
        verbose_name_plural = _("Anasayfa Giriş Bloku")


class About(TranslatableModel):
    slides = models.ManyToManyField(Image, related_name="about_slides", through="AboutSlides")
    slides_bottom = models.ManyToManyField(Image, related_name="about_slides_bottom", through="AboutBottomSlides")
    translations = TranslatedFields(
        title=models.CharField(_("Başlık"), default="", blank=True, max_length=100),
        intro=models.TextField(_("Giriş"), default="", blank=True),
        description_title=models.CharField(_("Açıklama Girişi"), default="", blank=True, max_length=200),
        description=models.TextField(_("Açıklama"), default="", blank=True),
    )

    def __str__(self):
        return _tr("Hakkımızda")

    class Meta:
        verbose_name = _("Hakkımızda")
        verbose_name_plural = _("Hakkımızda")


class AboutList(TranslatableModel):
    about = models.ForeignKey(About, verbose_name=_("Hakkımızda"), on_delete=models.CASCADE)
    translations = TranslatedFields(
        info=models.CharField(_("Madde"), default="", blank=False, max_length=100),
    )

    class Meta:
        verbose_name = _("Hakkımızda Maddeler")
        verbose_name_plural = _("Hakkımızda Maddeler")


# slide relations
class HomePageSeoSlides(TranslatableModel, models.Model):
    home = models.ForeignKey(HomePageSeo, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    translations = TranslatedFields(
        title_intro=models.CharField(_("Başlık Girişi"), default="", blank=True, max_length=60),
        title=models.CharField(_("Başlık"), default="", blank=True, max_length=80),
        description=models.TextField(_("Açıklama"), default="", blank=True)
    )

    def __str__(self):
        return _tr("Anasayfa Giriş Blok Slaytları")


class AboutSlides(models.Model):
    about = models.ForeignKey(About, related_name="about_slides", on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return _tr("Hakkımızda Üst Kısım Slaytlar")


class AboutBottomSlides(models.Model):
    about = models.ForeignKey(About, related_name="about_slides_bottom", on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return _tr("Hakkımızda Alt Kısım Slaytları")


class Surgery(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_("Başlık"), default="", blank=True, max_length=80),
        description=models.TextField(_("Açıklama"), default="", blank=True),
        image=models.ImageField(_("Resim"), upload_to="surgery", blank=False)
    )

    class Meta:
        verbose_name = _("Obezite ve Metabolik Cerrahi Bloku")
        verbose_name_plural = _("Obezite ve Metabolik Cerrahi Blokları")


class ChangeJourney(TranslatableModel):
    translations = TranslatedFields(
        image=models.ImageField(_("Resim"), upload_to="change-journey", blank=False)
    )

    def __str__(self):
        return _tr("Değişim Yolculuğu")

    class Meta:
        verbose_name = _("Değişim Yolculuğu")
        verbose_name_plural = _("Değişim Yolculukları")


class TreatmentPlan(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("Plan Adı"), blank=False, max_length=25),
    )

    class Meta:
        verbose_name = _("Tedavi Planı")
        verbose_name_plural = _("Tedavi Planları")


class TreatmentPlanItem(TranslatableModel):
    treatment_plan = models.ForeignKey(TreatmentPlan, verbose_name=_("Tedavi Planı"), on_delete=models.CASCADE)
    translations = TranslatedFields(
        info=models.CharField(_("Plan Maddesi"), blank=False, max_length=100),
    )

    def __str__(self):
        return _tr("Tedavi Planı Maddesi")

    class Meta:
        verbose_name = _("Tedavi Planı Maddeler")
        verbose_name_plural = _("Tedavi Planı Maddeler")


class Faq(TranslatableModel):
    translations = TranslatedFields(
        question=models.CharField(_("Soru"), blank=False, max_length=150),
        answer=models.TextField(_("Cevap"), blank=False),
    )

    class Meta:
        verbose_name = _("Sık Sorulan Soru")
        verbose_name_plural = _("Sık Sorulan Sorular")


class CustomerReview(TranslatableModel):
    translations = TranslatedFields(
        full_name=models.CharField(_("Müşteri İsmi"), blank=False, max_length=80),
        job_title=models.CharField(_("Meslek"), blank=False, max_length=80),
        comment=models.CharField(_("Yorum"), blank=False, max_length=250),
    )

    class Meta:
        verbose_name = _("Müşteri İncelemesi")
        verbose_name_plural = _("Müşteri İncelemeleri")
