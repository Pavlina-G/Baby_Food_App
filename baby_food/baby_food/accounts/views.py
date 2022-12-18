import six
from django.contrib import messages
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic as views, View
from multi_form_view import MultiModelFormView

from baby_food.accounts.forms import SignInForm, SignUpForm, ProfileForm, UserEditForm, UserForm, ChildForm, \
    UserUpdateForm, ProfileEditForm, ChildEditForm
from baby_food.accounts.models import Profile, AppUser, Child


UserModel = get_user_model()


class SignUpView(views.CreateView):
    template_name = 'accounts/register.html'

    form_class = SignUpForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    authentication_form = SignInForm


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class ProfileHomeView(views.DetailView):
    template_name = 'profile_home.html'
    model = UserModel

    def get_object(self, queryset=None):
        return self.request.user


class ProfileDetailsFormView(MultiModelFormView, views.DetailView):
    form_classes = {

        'profile_form': ProfileForm,
        'user_form': UserForm,
        'child_form': ChildForm,
    }

    record_id = None
    template_name = 'accounts/profile-details.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_form_kwargs(self):
        kwargs = super(ProfileDetailsFormView, self).get_form_kwargs()
        kwargs['user_form']['prefix'] = 'user'
        # kwargs['profile_form']['prefix'] = 'profile'
        kwargs['child_form']['prefix'] = 'child'
        return kwargs

    def get_objects(self):

        user_id = self.request.user.pk
        try:
            profile = Profile.objects.get(user_id=self.kwargs.get('user_id', None))
            # user = model.objects.get(pk=self.kwargs.get('pk', None))
        except Profile.DoesNotExist:
            profile = None
        return {
            'profile_form': profile,
            'user_form': profile.user if profile else None,
            'child_form': profile.user.child_set if profile else None,
        }

    def get_success_url(self):
        return reverse('profile home')

    def forms_valid(self, forms):
        profile = forms['profile_form'].save(commit=False)
        profile.user = forms['user_form'].save()
        profile.child = forms['child_form'].save()
        profile.save()
        return super(ProfileDetailsFormView, self).forms_valid(forms)

    def get_context_data(self, **kwargs):
        user = AppUser.objects.get(pk=self.request.user.pk)

        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user

        # total_children = 0
        # for child in user.child_set.all:
        #     total_children += 1
        # return total_children
        #
        context['total_children'] = user.child_set.count() if user.child_set else user.profile.number_of_children

        return context


@login_required
def profile_update(request, pk):
    user = request.user
    profile = Profile.objects.get(user_id=user.pk)
    children = Child.objects.filter(parent_id=user.pk).all()
    children_forms = []

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        for child in children:
            child_form = ChildEditForm(request.POST, instance=child)
            children_forms.append(child_form)
            if child_form.is_valid():
                # child_form.save_m2m()
                child_form.save()

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile details', pk=user.pk)
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileEditForm(instance=profile)

        for child in children:
            child_form = ChildEditForm(instance=child)
            children_forms.append(child_form)

    return render(request, 'accounts/profile-edit.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'children_forms': children_forms})


class ProfileDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete.html'
    model = UserModel
    success_url = reverse_lazy('index')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('profile home')