from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.utils.crypto import get_random_string
from django.views import View
from django.views.generic import CreateView, UpdateView, TemplateView, ListView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from users.services import send_verification_email, send_password


class LoginView(BaseLoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('app_send_mail:get_start')


class LogoutView(BaseLogoutView):

    def get_success_url(self):
        return reverse_lazy('app_send_mail:get_start')


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()

        if new_user.is_verified is False:
            user_code = get_random_string(length=12)
            form.instance.code_verification = user_code
            send_verification_email(new_user.email, user_code)
            return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('users:verified_email')


class VerifiedEmailView(View):
    template_name = 'users/verified_email.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        verification_code = request.POST.get('verification_code')
        User = get_user_model()
        try:
            user = User.objects.get(code_verification=verification_code)
            if not user.is_verified:
                user.is_verified = True
                user.save()
                return redirect('users:confirm_user')
        except User.DoesNotExist:
            pass
        return redirect('users:confirm_user_error')


class ConfirmUserView(TemplateView):
    template_name = 'users/confirm_user.html'


class ConfirmUserErrorView(TemplateView):
    template_name = 'users/confirm_user_error.html'


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('app_send_mail:get_start')

    def get_object(self, request=None):
        return self.request.user


def generate_new_password(request):
    new_password = get_random_string(length=16)
    request.user.set_password(new_password)
    request.user.save()

    send_password(request.user.email, new_password)

    return redirect(reverse('users:login'))


class UserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = 'users/user_list.html'

    def test_func(self):
        return self.request.user.is_staff

    def get_queryset(self):
        queryset = User.objects.filter(is_staff=False)
        return queryset


# class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
#     model = get_user_model()
#     template_name = 'users/user_form.html'
#     success_url = reverse_lazy('users:user_list')
#     permission_required = 'users.set_active'
#     fields = ['is_active', ]


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserProfileForm

    def get_object(self, queryset=None):
        return self.request.user
