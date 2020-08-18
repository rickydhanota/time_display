from django.urls import path
from . import views
urlpatterns = [
    path('', views.index)
    # path('displaytime', views.display_time)
]
    