from django.urls import path

from school.views import students_list_fast

urlpatterns = [
    path('', students_list_fast, name='students'),
]
