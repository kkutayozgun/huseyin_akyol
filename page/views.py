from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "home.html"

class KVKKPage(TemplateView):
    template_name = "kvkk.html"