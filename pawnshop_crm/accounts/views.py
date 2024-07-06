from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView
from .forms import UserForm
from .models import Users
from django.contrib.auth.models import User


def user_login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        next_url = request.POST.get('next')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_url:
                return redirect(next_url)
            return redirect('pawnshop:index')
        else:
            context['has_error'] = True
            context['next'] = next_url
            context['username'] = username
    else:
        context = {'next': request.GET.get('next')}
    return render(request, 'registration/login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('pawnshop:index')


class UserDetailView(ListView):
    model = Users
    template_name = 'user/detail.html'
    context_object_name = 'users'

    def test_func(self):
        return self.request.user.has_perm('add_user')


class UserCreateView(UserPassesTestMixin, CreateView):
    template_name = 'user/create.html'
    model = Users
    form_class = UserForm

    def form_valid(self, form):
        data = form.cleaned_data
        user_inner = User.objects.create_superuser(username=data['username'],
                                 email=data['email'],
                                 password=data['password'],
                                 is_staff=True)
        
        # user = Users.objects.create(
        #     # username=data['username'],
        #     # first_name=data['first_name'],
        #     # middle_name=data['middle_name'],
        #     # last_name=data['last_name'],
        #     email=data['email'],
        #     user=user_inner,
        #     # password=data['password'],
        # )
        # self.object = user
        # user.save()
        
        user_inner.save()

        return redirect(self.get_success_url())

    def test_func(self):
        return self.request.user.has_perm('add_user')

    def get_success_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.request.user.pk})
