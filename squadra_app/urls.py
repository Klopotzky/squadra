from django.urls import path
from squadra_app import views

urlpatterns = [
    path('', views.app_page, name='app_page'),
    path('ajax_html_text/', views.ajax_html_text, name='ajax_html_text'),
    path('ajax_storage_content/', views.ajax_storage_content, name='ajax_storage_content'),
    path('ajax_open_file/', views.ajax_open_file, name='ajax_open_file'),
    path('add_file/', views.upload_file, name='upload_file'),
    path('new_file/', views.new_file, name='new_file'),
]




