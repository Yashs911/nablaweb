# -*- coding: utf-8 -*-

from django.views.generic import DetailView, ListView, UpdateView, FormView
from django.contrib.auth import get_user_model

from braces.views import LoginRequiredMixin, FormMessagesMixin, MessageMixin

from .forms import UserForm, RegistrationForm
from .models import NablaUser
from .utils import activate_user_and_create_password, send_activation_email

User = get_user_model()


#  Brukerprofil
class UserDetailView(LoginRequiredMixin, DetailView):
    """Viser brukerens profil."""
    context_object_name = 'member'
    template_name = "accounts/view_member_profile.html"

    def get_object(self, queryset=None):
        return NablaUser.objects.get(username=self.kwargs['username'])


class UpdateProfile(LoginRequiredMixin, FormMessagesMixin, UpdateView):
    form_class = UserForm
    template_name = 'accounts/edit_profile.html'
    form_valid_message = 'Profil oppdatert.'
    form_invalid_message = 'Du har skrevet inn noe feil.'

    def get_object(self, queryset=None):
        return self.request.user


class UserList(LoginRequiredMixin, ListView):
    queryset = NablaUser.objects.filter(is_active=True).prefetch_related('groups').order_by('username')
    context_object_name = 'users'
    template_name = 'accounts/list.html'


class RegistrationView(MessageMixin, FormView):
    form_class = RegistrationForm
    template_name = 'accounts/user_registration.html'
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data['username'] 
        user, created_user = NablaUser.objects.get_or_create(username=username)

        password = activate_user_and_create_password(user)
        send_activation_email(user, password)

        self.messages.info('Registreringsepost sendt til %s' % user.email)
        return super(RegistrationView, self).form_valid(form)