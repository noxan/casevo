from django.views.generic import TemplateView


class StatisticHomeView(TemplateView):
    template_name = 'statistics/statistic_home.html'
