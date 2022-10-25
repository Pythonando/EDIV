from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .decorators import not_authenticated
from .forms import RegisterForm
from django.shortcuts import redirect
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from .models import Users
from django.contrib.auth import get_user_model
from django.contrib.auth import login as login_auth
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.contrib.messages import constants
from django.urls import reverse


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})
    elif request.method == "POST":
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            form_new = register_form.save(commit=False)
            form_new.is_active = False
            form_new.save()
            # TODO: REDIRECIONAR PARA LOGIN
            return redirect(reverse('login'))
        else:
            return render(request, 'register.html', {'register_form': register_form})


def active_account(request, uidb4, token):
    User = get_user_model()
    uid = force_str(urlsafe_base64_decode(uidb4))
    user = User.objects.filter(pk=uid)

    if (user := user.first()) and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login_auth(request, user)
        messages.add_message(request, constants.SUCCESS, "Seu usuário foi ativo com sucesso.")
        return redirect(reverse('login'))
    else:
        messages.add_message(request, constants.ERROR, "A url acessada não é válida.")
        return redirect(reverse('login'))

@not_authenticated
def login(request):
    return render(request, 'login.html')