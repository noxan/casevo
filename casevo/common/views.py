from django.views.generic import TemplateView


class CasevoHomeView(TemplateView):
    template_name = "base.html"
