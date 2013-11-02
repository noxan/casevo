from django.views.generic import TemplateView

from casevo.accounts.models import Account


class StatisticHomeView(TemplateView):
    template_name = 'statistics/statistic_home.html'


class StatisticAccountsPieView(TemplateView):
    template_name = 'statistics/statistic_accounts_pie.html'

    def get_context_data(self, **kwargs):
        context = super(StatisticAccountsPieView, self).get_context_data(**kwargs)
        context['accounts_in'] = []
        context['accounts_out'] = []
        context['accounts'] = Account.objects.all()
        for account in context['accounts']:
            if account.balance() > 0:
                context['accounts_in'].append(account)
            else:
                context['accounts_out'].append(account)

        return context
