from django.urls import path

from ems_app import views

urlpatterns = [
    path('users/', views.UserAPIView.as_view()),
    path('users/<str:id>/', views.UserAPIView.as_view()),

    path('emp/', views.EmployeeGenericAPIView.as_view()),
    path('emp/<str:id>/', views.EmployeeGenericAPIView.as_view()),
]
