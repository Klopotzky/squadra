from django.urls import path
from workflow import views

urlpatterns = [
    path('', views.board_basic, name='board_basic'),
    path('add_issue/', views.add_issue, name='add_issue'),
    path('issue_details/', views.issue_details, name='issue_details'),
    path('issue_edit/', views.issue_edit, name='issue_edit'),
]
