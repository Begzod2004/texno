from unicodedata import *
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.db.models import *
from django.contrib.auth.models import Group
from django.contrib.auth import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required
def profile(request):
    return render(request, 'profile.html')

    
def order(request):
    return render(request, 'order.html')



class indexListView(ListView):
    template_name = 'main.html'
    context_object_name = 'technique'
    def get_queryset(self):
        url_data = self.request.GET
        q = technique.objects.all()

        if 'name' in url_data and url_data['name']:
            q = q.filter(name__icontains=url_data['name'])

        if 'Company' in url_data and url_data['Company']:
            q = q.filter(
                company__title__icontains=url_data['Company'])

        if 'Brand' in url_data and url_data['Brand']:
            q = q.filter(
                brand__name__icontains=url_data['Brand'])

        if 'price' in url_data and url_data['price']:
            q = q.filter(
                price=url_data['price'])

        if 'condition' in url_data and url_data['condition']:
            q = q.filter(
                condition=url_data['condition'])

        if 'color' in url_data and url_data['color']:
            q = q.filter(color__icontains=url_data['color'])
        
        return q

def add_technique(request):
    print(request.POST)
    return render(request, "add-technique.html")


class BrandListView(ListView):
    template_name = 'Brand.html'
    context_object_name = 'Brand'
   
    def get_queryset(self):
        url_data = self.request.GET
        q = Brand.objects.all()

        if 'name' in url_data and url_data['name']:
            q = q.filter(name__icontains=url_data['name'])

        return q


class BrandCreateView(CreateView):
    queryset = Brand.objects.all()
    template_name = 'Brand-add.html'
    fields = "__all__"

    success_url = '/Brand'


class BrandUpdateView(UpdateView):
    queryset = Brand.objects.all()
    template_name = 'Brand-add.html'
    fields = "__all__"
    context_object_name = 'brand'
    success_url = '/Brand'


class BrandDeleteView(DeleteView):
    queryset = Brand.objects.all()
    template_name = 'Brand-delete.html'
    fields = "__all__"

    success_url = '/Brand'


class conditionListView(ListView):
    template_name = 'condition.html'
    context_object_name = 'condition'
   
    def get_queryset(self):
        url_data = self.request.GET
        q = condition.objects.all()

        if 'name' in url_data and url_data['name']:
            q = q.filter(name__icontains=url_data['name'])

        return q


class conditionCreateView(CreateView):
    queryset = condition.objects.all()
    template_name = 'condition-add.html'
    fields = "__all__"

    success_url = '/condition'


class conditionUpdateView(UpdateView):
    queryset = condition.objects.all()
    template_name = 'condition-add.html'
    fields = "__all__"
    context_object_name = 'condition'
    success_url = '/condition'


class conditionDeleteView(DeleteView):
    queryset = condition.objects.all()
    template_name = 'condition-delete.html'
    fields = "__all__"

    success_url = '/condition'

    
class sizeListView(ListView):
    template_name = 'size.html'
    context_object_name = 'size'
   
    def get_queryset(self):
        url_data = self.request.GET
        q = size.objects.all()

        if 'name' in url_data and url_data['name']:
            q = q.filter(name__icontains=url_data['name'])

        return q


class sizeCreateView(CreateView):
    queryset = size.objects.all()
    template_name = 'size-add.html'
    fields = "__all__"

    success_url = '/size'


class sizeUpdateView(UpdateView):
    queryset = size.objects.all()
    template_name = 'size-add.html'
    fields = "__all__"
    context_object_name = 'size'
    success_url = '/size'


class sizeDeleteView(DeleteView):
    queryset = size.objects.all()
    template_name = 'size-delete.html'
    fields = "__all__"

    success_url = '/size'



class CompanyListView(ListView):
    queryset = Company.objects.all()
    template_name = 'Company.html'
    context_object_name = 'Company'
    
    def get_queryset(self):
        url_data = self.request.GET
        q = Company.objects.all()

        if 'title' in url_data and url_data['title']:
            q = q.filter(title__icontains=url_data['title'])
        return q


class CompanyCreateView(CreateView):
    queryset = Company.objects.all()
    template_name = 'Company-add.html'
    fields = "__all__"

    success_url = '/Company'


class CompanyUpdateView(UpdateView):
    queryset = Company.objects.all()
    template_name = 'Company-add.html'
    fields = "__all__"

    success_url = '/Company'


class CompanyDeleteView(DeleteView):
    queryset = Company.objects.all()
    template_name = 'Company-delete.html'
    fields = "__all__"

    success_url = '/Company'


class techniqueListView(ListView):
    queryset = technique.objects.all()
    template_name = 'technique.html'


    context_object_name = 'technique'

    def render_to_response(self, context, **response_kwargs) -> HttpResponse:
        response = super().render_to_response(context, **response_kwargs)

        for key, val in self.last_user_query.items():
            response.set_cookie(key,val)
        return response

 
    


    def get_queryset(self):
        url_data = self.request.GET
        q = technique.objects.all()
        
        self.last_user_query = {}
        
        xaridor = Group.objects.get(name='Xaridor')
        if self.request.user.has_perm('can_view_technique') or xaridor in self.request.user.groups.all():


            if 'name' in url_data and url_data['name']:
                q = q.filter(name__icontains=url_data['name'])
                self.last_user_query['name'] = url_data['name']

            if 'Company' in url_data and url_data['Company']:
                q = q.filter(
                    company__title__icontains=url_data['Company'])

            if 'Brand' in url_data and url_data['Brand']:
                q = q.filter(
                    brand__name__icontains=url_data['Brand'])

            if 'price' in url_data and url_data['price']:
                q = q.filter(
                    price=url_data['price'])

            if 'condition' in url_data and url_data['condition']:
                q = q.filter(
                    condition=url_data['condition'])

            if 'country' in url_data and url_data['country']:
                q = q.filter(color__icontains=url_data['country'])
            
            if 'size' in url_data and url_data['size']:
                q = q.filter(color__icontains=url_data['size'])

            if 'color' in url_data and url_data['color']:
                q = q.filter(color__icontains=url_data['color'])
                
            if 'img' in url_data and url_data['img']:
                q = q.filter(color__icontains=url_data['img'])
            return q



class techniqueCreateView(CreateView):
    queryset = technique.objects.all()
    template_name = 'technique-add.html'
    fields = "__all__"

    success_url = '/technique'


class techniqueUpdateView(UpdateView):
    queryset = technique.objects.all()
    template_name = 'technique-add.html'
    fields = "__all__"

    success_url = '/technique'


def main(request):
    bks = technique.objects.all()

    context = {'technique': bks}
    return render(request, "main.html", context=context)




class techniqueDeleteView(DeleteView):
    queryset = technique.objects.all()
    template_name = 'technique-delete.html'
    fields = "__all__"

    success_url = '/technique'

def about(request):
    return render(request, "about.html")
def brand(request):
    return render(request, "brand.html")
def contact(request):
    return render(request, "contact.html")
def products(request):
    return render(request, "products.html")



def user_login_view(request):
    if request.method == 'GET':
        form = UserLoginForm()
        return render(request, template_name='user-login.html', context={'form': form})
    else:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user:
                login(request=request, user=user)
                return redirect('techniques')
            else:
                return render(request, template_name='user-login.html', context={'form': form})


def user_register_view(request):
    if request.method == 'GET':
        form = UserRegisterModelForm()
        return render(request, template_name='user-register.html', context={'form': form})
    else:
        form = UserRegisterModelForm(data=request.POST)
        password = request.POST['password']
        confirm = request.POST['confirm']
        if form.is_valid() and password == confirm:
            form.save()
            user = form.instance
            user.groups.add(Group.objects.get(name='Xaridor'))
            user.save()

            login(request, user)

            return redirect('index')
        else:
            return render(request, template_name='user-register.html', context={'form': form})
