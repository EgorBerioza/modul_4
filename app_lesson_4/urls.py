from django.urls import path
from .views import index_Lesson_4

urlpatterns = [
    path('', index_Lesson_4),
    path('lesson_4', index_Lesson_4)
]