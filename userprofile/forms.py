from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.db.models import fields
from userprofile.models import UserAccount


class RegistrationForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = UserAccount
        fields = ("email", "fullName", "password1", "password2",
                  "gender")


class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserAccount
        fields = ('email', 'password')

    def clean(self):

        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Giriş Başarısız.")


# class EditorAuthenticationForm(forms.ModelForm):

#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = EditorAccount
#         fields = ('email', 'password')

#     def clean(self):

#         if self.is_valid():
#             email = self.cleaned_data['email']
#             password = self.cleaned_data['password']

#             if not authenticate(email=email, password=password):
#                 raise forms.ValidationError("Editor Girişi Başarısız")


class AccountUptadeForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ('email', 'fullName', 'website',
                  'country', 'city', 'account_avatar', 'birthdate', 'biography', 'job')

        def clean_email(self):
            email = self.cleaned_data['email']

            try:
                account = UserAccount.objects.exclude(
                    pk=self.instance.pk).get(email=email)
            except UserAccount.DoesNotExist:
                return email
            raise forms.ValidationError('Bu Email "%s" kullanılıyor' % account)


class UserDeleteForm(forms.ModelForm):

    class Meta:
        model = UserAccount

        fields = []
