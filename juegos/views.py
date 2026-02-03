from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Juego, Resena
from .forms import JuegoForm, ResenaForm

class JuegoListView(ListView):
    model = Juego


class JuegoCreateView(CreateView):
    model = Juego
    form_class = JuegoForm
    success_url = reverse_lazy('juego_list')


class JuegoUpdateView(UpdateView):
    model = Juego
    form_class = JuegoForm
    success_url = reverse_lazy('juego_list')


class JuegoDeleteView(DeleteView):
    model = Juego
    success_url = reverse_lazy('juego_list')


class ResenaListView(ListView):
    model = Resena


class ResenaCreateView(LoginRequiredMixin, CreateView):
    model = Resena
    form_class = ResenaForm
    success_url = reverse_lazy('resena_list')

    def form_valid(self, form):
        form.instance.usuario_username = self.request.user.username
        return super().form_valid(form)


class ResenaUpdateView(LoginRequiredMixin, UpdateView):
    model = Resena
    form_class = ResenaForm
    success_url = reverse_lazy('resena_list')


class ResenaDeleteView(LoginRequiredMixin, DeleteView):
    model = Resena
    success_url = reverse_lazy('resena_list')
