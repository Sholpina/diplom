from django.urls import path
from lawersagenda import views

app_name = 'lawersagenda'

urlpatterns = [
        path('signup/', views.signupuser, name='signupuser'),
        path('currentagenda/', views.currentagenda, name='currentagenda')
]
