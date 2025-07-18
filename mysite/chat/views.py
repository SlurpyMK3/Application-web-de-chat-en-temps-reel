from django.shortcuts import get_object_or_404, render,  redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .form import CustomUserCreationForm

def contact_view(request):
    return render(request, 'contact.html')
def home(request):
    return render(request, "home.html")

def chat(request):
    return render(request, "chat/chat.html")

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'login/inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'login/connexion.html')

def deconnexion(request):
    logout(request)
    return redirect('/')