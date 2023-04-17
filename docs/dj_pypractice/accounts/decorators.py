# Este es el que vamos usar para poder crear nuestro autenticador y poder otorgar permisos
from tokenize import group
from django.http import HttpResponse
from django.shortcuts import redirect

# Ahora creamos la function que se encarga de de verificar la autentificar al usuario
# Recordar que esta function la vamos a tener que utilizar en views.py
# Para llamar a nuestra nueva function tenemos que colocarla antes de cada function de view donde aplica
# utilizando @unauthenticated_user
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
        
    return wrapper_func

# Una vez que creamos los grupos y definimos a los usuarios en cada uno, podemos ahora continuar con
# los permisos
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            # los condicionales los colocamos aquí dentro
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
            # Para verificar que todo funciona.
            # print('working: ', allowed_roles)
        return wrapper_func
    return decorator

# Creamos una function para que los usuarios sean redirigidos a otra web y no queden estancados
def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
        if group == 'customer':
            return redirect('user-page')
        
        if group == 'admin':
            return view_func(request, *args, **kwargs)
        
    return wrapper_function