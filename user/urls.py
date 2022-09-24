from django.urls import path
from user import views


urlpatterns = [
    path('create/',views.Userview.as_view()),  
    path('read/',views.Userview.as_view()),
    path('update/',views.Userview.as_view()),
    path('delete/',views.Userview.as_view()),
] 