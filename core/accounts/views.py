from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic import UpdateView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from .forms import CustomUserCreationForm,ProfileUpdateForm
from .models import Profile

class LoginView(LoginView):
    # form_class = CustomAuthenticationForm
    def form_valid(self, form):
        # کاربر را وارد کنید
        # login(self.request, form.get_user())
        messages.success(self.request, "شما با موفقیت وارد سایت شدید.")
        return super().form_valid(form)

    def form_invalid(self, form):
        # پرینت ارورهای فرم
        print("Form validation failed. Here are the errors:")
        for field in form:
            for error in field.errors:
                print(f"Error in field '{field.label}': {error}")
        for error in form.non_field_errors():
            print(f"Non-field error: {error}")

        # ادامه‌ی عملکرد پیش‌فرض
        return super().form_invalid(form)


class LogoutView(BaseLogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "شما با موفقیت از سایت خارج شدید.")
        response = super().dispatch(request, *args, **kwargs)
        return response


class RegisterView(FormView):
    template_name = "registration/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("accounts:login")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "ثبت نام با موفقیت انجام شد")
        return super().form_valid(form)

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'registration/update_profile.html'
    success_url = reverse_lazy('userpanel:index')
    
    def get_object(self):
        return Profile.objects.get(user=self.request.user)
    
    def form_valid(self, form):
        messages.success(self.request, "پروفایل شما با موفقیت بروز رسانی شد.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "خطایی در بروز رسانی پروفایل شما رخ داد.")
        response = super().form_invalid(form)
        return response