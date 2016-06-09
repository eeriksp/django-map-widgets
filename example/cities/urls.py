from django.conf.urls import url
from cities.views import CityCreateView, CityListView

urlpatterns = [
    url(r'^$', CityListView.as_view(), name="list"),
    url(r'^create/$', CityCreateView.as_view(), name="create"),
]