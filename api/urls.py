from django.urls import path

from api.views import ConvertApiView

urlpatterns = [
    path('convert/', ConvertApiView.as_view(), name='convert'),

]