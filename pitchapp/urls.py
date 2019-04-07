from django.urls import path

from pitchapp.web.views import result, home

urlpatterns = [
    path('', home, name='home'),
    path('result/', result, name='result', ),
]
