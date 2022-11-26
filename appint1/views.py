from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Bmi

class IndexView(LoginRequiredMixin, generic.ListView):

    model = Bmi
    template_name = "example.html"

    def get_queryset(self) :
        return Bmi.objects.filter(user = self.request.user)

# Create your views here.
