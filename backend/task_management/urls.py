from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


# Пример простого представления для корневой страницы
def home_view(request):
    return HttpResponse("Welcome to the Task Management System")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),  # Подключаем urls приложения tasks к api/
    path('', home_view, name='home'),  # Добавляем маршрут для корневого URL
]
