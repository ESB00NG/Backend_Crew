# users/views.py
from django.http import JsonResponse
from django.contrib.auth.models import User  # O usa tu modelo personalizado si no usas el modelo User de Django
from django.views.decorators.csrf import csrf_exempt
import json


def user_list(request):
    users = list(User.objects.values('id', 'username', 'email'))  # Obtiene los campos id, username y email
    return JsonResponse(users, safe=False)

@csrf_exempt  # Deshabilitar CSRF temporalmente para pruebas; eliminar en producción
def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        if not (username and email and password):
            return JsonResponse({'error': 'Missing fields'}, status=400)
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)
        
        user = User.objects.create_user(username=username, email=email, password=password)
        return JsonResponse({'message': 'User created successfully'}, status=201)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)