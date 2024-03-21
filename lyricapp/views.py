# recipes/views.pycd
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView ,DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls  import reverse_lazy

from . import models
from .models import lyric



# Create your views here.
def home(request):
  lyricapp = models.lyric.objects.all()
  context = {
    'lyricapp': lyricapp
  }
  return render(request, 'lyricapp/home.html', context)
  
  
class LyricListView(ListView):
  model = models.lyric
  template_name = 'lyricapp/home.html'
  context_object_name = 'lyricapp'
  
  
class LyricDetailView(DetailView):  
  model = models.lyric
  template_name = 'lyricapp/lyric_detail.html'
  
  
class LyricCreateView(LoginRequiredMixin, CreateView):
  model = models.lyric
  fields = ['title', 'description']
  
  def form_valid (self, form):
    form.instance.writer = self.request.user
    return super().form_valid(form)


class LyricUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = models.lyric
  fields = ['title', 'description']
  
  def test_func(self):
    lyric = self.get_object()
    return self.request.user == lyric.writer 
  
  def form_valid (self, form):
    form.instance.writer = self.request.user
    return super().form_valid(form) 
    
    
class LyricDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = models.lyric
  success_url = reverse_lazy('lyricapp-home')
  
  def test_func(self):
    lyric = self.get_object()
    return self.request.user == lyric.writer 

  
def about(request):
  return render(request, 'lyricapp/about.html', {'title':'about us page'})