from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('analyze', views.analyze, name='analyze')
    # path('removepunc', views.removepunc, name='removepunc'),
    # path('fullcaps', views.fullcaps, name='fullcaps'),
    # path('extraspaceremover', views.extraspaceremover, name='extraspaceremover')



]
