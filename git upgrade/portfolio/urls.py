from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='portfolio-home'),
    path('about/', views.about, name='portfolio-about'),
    path('contact/', views.contact, name='portfolio-contact'),
    path('project/', views.project, name='portfolio-project'),
    path('projectsingle1/', views.projectsingle1, name='portfolio-projectsingle1'),
    path('projectsingle2/', views.projectsingle2, name='portfolio-projectsingle2'),
    path('projectsingle3/', views.projectsingle3, name='portfolio-projectsingle3'),
    path('projectsingle4/', views.projectsingle4, name='portfolio-projectsingle4'),
    path('projectsingle5/', views.projectsingle5, name='portfolio-projectsingle5'),
    path('projectsingle6/', views.projectsingle6, name='portfolio-projectsingle6'),
    path('projectsingle7/', views.projectsingle7, name='portfolio-projectsingle7'),
    path('projectsingle8/', views.projectsingle8, name='portfolio-projectsingle8'),
    path('projectsingle9/', views.projectsingle9, name='portfolio-projectsingle9'),
    path('projectsingle10/', views.projectsingle10, name='portfolio-projectsingle10'),
]