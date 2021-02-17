from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index_page"),
    path('about',views.about, name='about_page'),
    path('newPost',views.new_post, name='new_post_page'),
    path('profile',views.profile , name='profile_page'),
    path('logout',views.logoout, name='logout_page'),
    
]