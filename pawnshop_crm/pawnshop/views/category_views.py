from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, RedirectView, View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect, render
from django.urls import reverse

from ..models import Category
from ..forms import CategoryCreateForm


class CategoryCreateView(UserPassesTestMixin, CreateView):
    template_name = 'category/create.html'
    model = Category
    form_class = CategoryCreateForm

    def form_valid(self, form):
        data = form.cleaned_data
        # user_inner = Category.objects.create_superuser(category_name=data['category_name'],
        #                          subcategory_namemail=data['subcategory_name'])
        
        print(data)

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
        return self.request.user.has_perm('accounts.add_loan')

    def get_success_url(self):
        return reverse('pawnshop:confirm_document_create', kwargs={'client_pk': self.object.pk})
