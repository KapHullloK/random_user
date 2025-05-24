from django.views.generic import TemplateView, ListView, DetailView

from humans.models import Human
from humans.services import create_humans_by_cnt


class HomeView(TemplateView):
    template_name = "humans/home_page.html"


class HumansListView(ListView):
    model = Human
    template_name = 'humans/humans_list.html'
    context_object_name = 'humans'
    paginate_by = 10

    def get_queryset(self):
        cnt = self.request.GET.get('count')
        if cnt and cnt.isdigit():
            cnt = int(cnt)
            create_humans_by_cnt(cnt)
            return super().get_queryset().order_by('id')[:cnt]
        return super().get_queryset().order_by('id')[:25]


class HumanDetailView(DetailView):
    model = Human
    template_name = 'humans/human_detail.html'
    context_object_name = 'human'


class RandomHumanDetailView(DetailView):
    model = Human
    template_name = 'humans/human_detail.html'
    context_object_name = 'human'

    def get_queryset(self):
        return Human.objects.order_by('?').first()

    def get_object(self, queryset=None):
        if queryset is None:
            return self.get_queryset()
        return queryset
