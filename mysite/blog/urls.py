from django.urls import path
from . import views
 
 
app_name = 'blog'
 
urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),  # name to be referred for including in templates "app_name:name(of the view like name='post_list)"
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail, name='post_detail'),
]