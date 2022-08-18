from django.urls import path
from .views import allPost, postDetail

app_name = 'blog'


urlpatterns = [
    path('', allPost),
    path('<int:id>', postDetail)
    
]