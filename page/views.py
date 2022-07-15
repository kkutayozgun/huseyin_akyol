from django.views.generic import TemplateView
from utils.views import HandleEmailFormView


class HomePage(TemplateView):
    template_name = "home.html"

class KVKKPage(TemplateView):
    template_name = "kvkk.html"

class ContactFormEmailView(HandleEmailFormView):
    subject = "Dr. Hüseyin Akyol - İletişim Sayfası formu dolduruldu: {first_name} {last_name}"
    email_template_name = "emailtemps/contact_form.html"
    form_identifier = "contact-form"

    def get_email_context(self, request):
        return {
            "first_name": request.POST.get('first_name', ""),
            "last_name": request.POST.get('last_name', ""),
            "email": request.POST.get('email', ""),
            "treatment": request.POST.get('treatment', ""),
            "full_phone_number": request.POST.get('contact-full_number', ""),
            "phone": request.POST.get('phone', ""),
            "via": request.POST.get('via', ""),
            "message": request.POST.get('message', "")
        }
