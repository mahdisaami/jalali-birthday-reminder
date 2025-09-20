from django.contrib import messages
from django.urls import reverse_lazy

from .forms import CustomUserForm
from .models import CustomUser

from django.views.generic import ListView, CreateView
from django.views import View
from django.shortcuts import render, redirect


class BirthdayListView(ListView):
    model = CustomUser
    template_name = 'home.html'
    ordering = ['ceremony_datetime']


class BirthdayCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = "add_birthday.html"
    success_url = reverse_lazy("home")  # redirect after success
    # not_success_url = reverse_lazy("home")
    
    def post(self, request):
        form = CustomUserForm(request.POST)
        if form.is_valid():
            CustomUser.objects.create(**form.cleaned_data)
            messages.success(request, "🎉 اطلاعات با موفقیت ذخیره شد.")
            return redirect('home')
        else:
            messages.error(request, "❌ فرم معتبر نیست، لطفاً خطاها را بررسی کنید." )

            return redirect('add_birthday',)


