# lyricapp/urls.py
from django.urls import path
from . import views

'app/model_viewtype'
'lyricapp/lyric_detail.html'

urlpatterns = [
    path('', views.LyricListView.as_view(), name="lyricapp-home"),
    path('lyric/<int:pk>/', views.LyricDetailView.as_view(), name="lyricapp-detail"),
    path('lyric/create/', views.LyricCreateView.as_view(), name="lyricapp-create"),
    path('lyric/<int:pk>/update/', views.LyricUpdateView.as_view(), name="lyricapp-update"),
    path('lyric/<int:pk>/delete/', views.LyricDeleteView.as_view(), name="lyricapp-delete"),
    path('about/', views.about, name="lyricapp-about"),
]