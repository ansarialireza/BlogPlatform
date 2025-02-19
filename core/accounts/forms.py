from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User,Profile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label="ایمیل",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "ایمیل خود را وارد کنید"}
        ),
    )

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].help_text = "رمز عبور باید حداقل ۸ کاراکتر باشد."
        self.fields["password2"].help_text = (
            "تکرار گذرواژه باید مشابه گذرواژه اصلی باشد."
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("ایمیل وارد شده قبلاً ثبت شده است.")
        return email

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name',]
        
