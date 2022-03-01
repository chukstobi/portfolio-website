from django.urls import path, include
from portfolio import views

urlpatterns = [
    path('', views.index, name='home'),
    path('project/<int:id>', views.project, name='project_detail'),
]
