from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Note


# Create your views here.
from .models import Note
from .forms import NoteForm

@login_required
def home(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('home')  # Rediriger vers home au lieu de note_list
    else:
        form = NoteForm()

    notes = Note.objects.filter(user=request.user)  # Filtrer par utilisateur
    return render(request, 'notes/home.html', {'form': form, 'notes': notes})

@login_required
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)  # S'assurer que l'utilisateur ne peut modifier que ses propres notes

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')  # Rediriger vers home au lieu de note_list
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/note_update.html', {'form': form})

class RegisterView(FormView):
    template_name = 'notes/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')  # page après inscription - rediriger vers home

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = 'notes/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
    


def logout_get_view(request):
    logout(request)
    return redirect('login')

def landing_page(request):
    citation = "Bienvenue dans votre application de notes. Organisez vos idées facilement !"
    return render(request, 'notes/landing.html', {'citation': citation})




@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, "notes/note_list.html", {"notes": notes})


@login_required
def note_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        categorie = request.POST.get('categorie')  # si tu as un champ de catégorie
        Note.objects.create(
            user=request.user,                # 👈 TRÈS IMPORTANT
            title=title,
            content=content,
            categorie=categorie
        )
        return redirect('home')  # Rediriger vers home au lieu de note_list
    return render(request, 'notes/note_create.html')