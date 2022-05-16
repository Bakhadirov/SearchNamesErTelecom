from django.urls import path, include


from .views import *

urlpatterns = [
    path('', SearcherView.as_view(), name='searcher'),
    path('api/', SearcherViewSerializers.as_view(), name='testjson'),
    ]