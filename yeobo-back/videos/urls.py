from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.video_list),
    path('<int:video_pk>/', views.video_detail),
    path('<int:video_pk>/comment/', views.comment_create),
    path('<int:video_pk>/comment/<int:comment_pk>/', views.comment_update_or_delete),
]