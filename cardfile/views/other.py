from django.views.generic import TemplateView

from cardfile.views.common_mixins import NavMixin


class BaseView(NavMixin, TemplateView):
    template_name = "cardfile/base.html"