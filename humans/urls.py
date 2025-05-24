from django.urls import path

from humans.apps import HumansConfig
from humans.views import HomeView, HumansListView, HumanDetailView, RandomHumanDetailView

app_name = HumansConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home-humans'),
    path('list/', HumansListView.as_view(), name='list-humans'),
    path('<int:pk>', HumanDetailView.as_view(), name='detail-humans'),
    path('random/', RandomHumanDetailView.as_view(), name='random-humans'),
]
