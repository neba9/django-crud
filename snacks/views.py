from django.shortcuts import render


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import snack
from django.urls import reverse_lazy

# Create your views here.

class SnackListView(ListView):
  template_name = 'snack_list.html'
  model = snack


class SnackDetailView(DetailView):
  template_name = 'snack_detail.html'
  model = snack


class SnackCreateView(CreateView):
  template_name = 'snack_create.html'
  model = snack
  fields = ['title', 'purchaser', 'description']
  success_url = reverse_lazy('snack_list')


class SnackUpdateView(UpdateView):
  template_name = 'snack_update.html'
  model = snack
  fields = ['title', 'purchaser', 'description']
  success_url = reverse_lazy('snack_list')


class SnackDeleteView(DeleteView):
  template_name = 'snack_delete.html'
  model = snack
  success_url = reverse_lazy('snack_list')
