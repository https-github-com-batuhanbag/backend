from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserAccount
from userprofile.forms import RegistrationForm, AccountAuthenticationForm, AccountUptadeForm
from django.contrib.auth import login, authenticate, logout
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.http import HttpResponse
from .tokens import account_activation_token
from django.contrib.auth.hashers import check_password
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

# Create your views here.


def registration_view(request):
    if request.method == 'GET':
        return render(request, "register.html")
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print("code is here 1")
        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)

            mail_subject = 'Activate your account.'
            message = render_to_string('registration/user_activate_mail.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.id)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            print("code is here 2")
            return render(request, "registerINFO.html")

        else:
            messages.info(
                request, 'Kayıt işlemi başarısız oldu, lütfen bilgilerinizi kontrol ediniz.')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserAccount.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, UserAccount.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, "registerOK.html")
    else:
        return render(request, "registerFAIL.html")


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("index")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)

                return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, "Giriş başarısız lütfen tekrar deneyiniz")
            return redirect(request.META['HTTP_REFERER'])

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    return render(request, "login.html", context)


def logout_view(request):
    logout(request)
    return redirect('index')


def user_view(request):

    if not request.user.is_authenticated:
        return redirect("userprofile:login")

    context = {}

    print(request)

    if request.POST or request.FILES:

        form = AccountUptadeForm(
            request.POST, request.FILES,
            instance=request.user)

        if form.is_valid():

            form.initial = {
                "email": request.POST['email'],
                "fullName": request.POST['fullName'],
                "account_avatar": request.FILES.get('account_avatar'),
                "website": request.POST['website'],
                "country": request.POST['country'],
                "city": request.POST['city'],
                "birthdate": request.POST['birthdate'],
                "biography": request.POST['biography'],
                "job": request.POST['job'],

            }
            print(form.initial)

            context['succes_message'] = "Başarıyla Güncellendi."

            form.save()

    else:
        form = AccountUptadeForm(
            initial={
                "email": request.user.email,
                "fullName": request.user.fullName,
                "account_avatar": request.user.account_avatar,
                "website": request.user.website,
                "country": request.user.country,
                "city": request.user.city,
                "birthdate": request.user.birthdate,
                "biography": request.user.biography,
                "job": request.user.job
            }
        )

    context['account_form'] = form
    return render(request, "user_update.html", context)
