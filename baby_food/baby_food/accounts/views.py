from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import modelformset_factory, inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic as views
from multi_form_view import MultiModelFormView

from baby_food.accounts.forms import SignInForm, SignUpForm, ProfileForm, UserForm, ChildForm, ProfileEditForm, \
    ChildEditForm
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
    template_name = 'common/profile_home.html'
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
            'child_form': profile.child_set if profile else None,
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
        profile = Profile.objects.get(user_id=self.request.user.pk)

        context = super().get_context_data(**kwargs)

        context['total_children'] = profile.child_set.count() if profile.child_set else user.number_of_children
        context['children'] = profile.child_set.all()
        return context


def get_child_by_user_id(pk, parent_id):
    return Child.objects \
        .filter(pk=pk, parent_id=parent_id) \
        .get()


@login_required
def profile_edit(request, pk):
    user = request.user

    # profile = get_object_or_404(Profile, user_id=user.pk)
    profile = Profile.objects.get(user_id=user.pk)

    if request.method == 'POST':
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()

        return redirect('profile details', pk=user.pk)

    else:
        profile_form = ProfileEditForm(instance=profile)

        context = {
            'profile_form': profile_form,
        }

    return render(request, 'accounts/profile-edit.html',
                  context, )


@login_required
def child_update(request, user_id, pk):
    user = request.user
    child = Child.objects.get(pk=pk, parent_id=user_id)

    if request.method == 'POST':
        child_form = ChildEditForm(request.POST, request.FILES, instance=child)
        if child_form.is_valid():
            child_form.save()

        return redirect('profile details', pk=user.pk)

    else:
        child_form = ChildEditForm(instance=child)

        context = {
            'child_form': child_form,
            'child_pk': child.id
        }

    return render(request, 'accounts/child-edit.html', context)


class ProfileDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete.html'
    model = UserModel
    success_url = reverse_lazy('index')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('profile home')
