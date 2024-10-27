# users/views.py
from django.http import JsonResponse
from django.contrib.auth.models import User  # O usa tu modelo personalizado si no usas el modelo User de Django

def user_list(request):
    users = list(User.objects.values('id', 'username', 'email'))  # Obtiene los campos id, username y email
    return JsonResponse(users, safe=False)
