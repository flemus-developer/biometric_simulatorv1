"""
from django.shortcuts import render
from employee.models import *
from registration.models import *

# Create your views here.

class ProductosMas(TemplateView):
    template_name="biometric_scanner.html"

    def get_Register(self):
        id_fingerprint = self.request.GET.get("id")
        f = Fingerprint.objects.get(id=id_fingerprint)
        register = Register.objects.create(fingerprint = fingerprint)
        return register

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['register'] = self.get_Register()
        return context
"""
