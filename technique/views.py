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
    context_object_name = 'Technique'
    def get_queryset(self):
        url_data = self.request.GET
        q = Technique.objects.all()

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

        if 'Condition' in url_data and url_data['Condition']:
            q = q.filter(
                Condition=url_data['Condition'])

        if 'color' in url_data and url_data['color']:
            q = q.filter(color__icontains=url_data['color'])
        
        return q

def add_Technique(request):
    print(request.POST)
    return render(request, "add-Technique.html")


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


class ConditionListView(ListView):
    template_name = 'Condition.html'
    context_object_name = 'Condition'
   
    def get_queryset(self):
        url_data = self.request.GET
        q = Condition.objects.all()

        if 'name' in url_data and url_data['name']:
            q = q.filter(name__icontains=url_data['name'])

        return q


class ConditionCreateView(CreateView):
    queryset = Condition.objects.all()
    template_name = 'Condition-add.html'
    fields = "__all__"

    success_url = '/Condition'


class ConditionUpdateView(UpdateView):
    queryset = Condition.objects.all()
    template_name = 'Condition-add.html'
    fields = "__all__"
    context_object_name = 'Condition'
    success_url = '/Condition'


class ConditionDeleteView(DeleteView):
    queryset = Condition.objects.all()
    template_name = 'Condition-delete.html'
    fields = "__all__"

    success_url = '/Condition'



class FeaturesListView(ListView):
    template_name = 'Features.html'
    context_object_name = 'Features'
   
    def get_queryset(self):
        url_data = self.request.GET
        q = Features.objects.all()

        if 'Features' in url_data and url_data['Features']:
            q = q.filter(name__icontains=url_data['Features'])

        return q



class FeaturesCreateView(CreateView):
    queryset = Features.objects.all()
    template_name = 'Features-add.html'
    fields = "__all__"

    success_url = '/Features'


class FeaturesUpdateView(UpdateView):
    queryset = Features.objects.all()
    template_name = 'Features-add.html'
    fields = "__all__"
    context_object_name = 'Features'
    success_url = '/Features'


class FeaturesDeleteView(DeleteView):
    queryset = Features.objects.all()
    template_name = 'Features-delete.html'
    fields = "__all__"

    success_url = '/Features'

class CountryListView(ListView):
    template_name = 'Country.html'
    context_object_name = 'Color'
   
    def get_queryset(self):
        url_data = self.request.GET
        q = Country.objects.all()

        if 'Color' in url_data and url_data['Country']:
            q = q.filter(name__icontains=url_data['Color'])

        return q

class CountryCreateView(CreateView):
    queryset = Country.objects.all()
    template_name = 'Country-add.html'
    fields = "__all__"

    success_url = '/Country'


class CountryUpdateView(UpdateView):
    queryset = Country.objects.all()
    template_name = 'Country-add.html'
    fields = "__all__"
    context_object_name = 'Country'
    success_url = '/Country'


class CountryDeleteView(DeleteView):
    queryset = Country.objects.all()
    template_name = 'Country-delete.html'
    fields = "__all__"

    success_url = '/Country'


class ColorListView(ListView):
    template_name = 'Color.html'
    context_object_name = 'Color'
   
    def get_queryset(self):
        url_data = self.request.GET
        q = Condition.objects.all()

        if 'Color' in url_data and url_data['Color']:
            q = q.filter(name__icontains=url_data['Color'])

        return q


class ColorCreateView(CreateView):
    queryset = Color.objects.all()
    template_name = 'Color-add.html'
    fields = "__all__"

    success_url = '/Color'


class ColorUpdateView(UpdateView):
    queryset = Color.objects.all()
    template_name = 'Color-add.html'
    fields = "__all__"
    context_object_name = 'Color'
    success_url = '/Color'


class ColorDeleteView(DeleteView):
    queryset = Color.objects.all()
    template_name = 'Color-delete.html'
    fields = "__all__"

    success_url = '/Color'



    
class SizeListView(ListView):
    template_name = 'Size.html'
    context_object_name = 'Size'
   
    def get_queryset(self):
        url_data = self.request.GET
        q = Size.objects.all()

        if 'name' in url_data and url_data['name']:
            q = q.filter(name__icontains=url_data['name'])

        return q


class SizeCreateView(CreateView):
    queryset = Size.objects.all()
    template_name = 'Size-add.html'
    fields = "__all__"

    success_url = '/Size'


class SizeUpdateView(UpdateView):
    queryset = Size.objects.all()
    template_name = 'Size-add.html'
    fields = "__all__"
    context_object_name = 'Size'
    success_url = '/Size'


class SizeDeleteView(DeleteView):
    queryset = Size.objects.all()
    template_name = 'Size-delete.html'
    fields = "__all__"

    success_url = '/Size'



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


class TechniqueListView(ListView):
    queryset = Technique.objects.all()
    template_name = 'Technique.html'


    context_object_name = 'Technique'

    def render_to_response(self, context, **response_kwargs) -> HttpResponse:
        response = super().render_to_response(context, **response_kwargs)

        for key, val in self.last_user_query.items():
            response.set_cookie(key,val)
        return response

 
    


    def get_queryset(self):
        url_data = self.request.GET
        q = Technique.objects.all()
        
        self.last_user_query = {}
        
        xaridor = Group.objects.get(name='Xaridor')
        if self.request.user.has_perm('can_view_Technique') or xaridor in self.request.user.groups.all():


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

            if 'Condition' in url_data and url_data['Condition']:
                q = q.filter(
                    Condition=url_data['Condition'])

            if 'Country' in url_data and url_data['Country']:
                q = q.filter(color__icontains=url_data['Country'])
            
            if 'Size' in url_data and url_data['Size']:
                q = q.filter(color__icontains=url_data['Size'])

            if 'color' in url_data and url_data['color']:
                q = q.filter(color__icontains=url_data['color'])
                
            if 'img' in url_data and url_data['img']:
                q = q.filter(color__icontains=url_data['img'])
            return q



class TechniqueCreateView(CreateView):
    queryset = Technique.objects.all()
    template_name = 'Technique-add.html'
    fields = "__all__"

    success_url = '/Technique'


class TechniqueUpdateView(UpdateView):
    queryset = Technique.objects.all()
    template_name = 'Technique-add.html'
    fields = "__all__"

    success_url = '/Technique'


def main(request):
    bks = Technique.objects.all()

    context = {'Technique': bks}
    return render(request, "main.html", context=context)




class TechniqueDeleteView(DeleteView):
    queryset = Technique.objects.all()
    template_name = 'Technique-delete.html'
    fields = "__all__"

    success_url = '/Technique'

def about(request):
    return render(request, "about.html")
def brand(request):
    return render(request, "brand.html")
def contact(request):
    return render(request, "contact.html")
def products(request):
    return render(request, "products.html")





class AksiyaListView(ListView):
    queryset = Aksiya.objects.all()
    template_name = 'Aksiya.html'


    context_object_name = 'Aksiya'

    def render_to_response(self, context, **response_kwargs) -> HttpResponse:
        response = super().render_to_response(context, **response_kwargs)

        for key, val in self.last_user_query.items():
            response.set_cookie(key,val)
        return response

 
    


    def get_queryset(self):
        url_data = self.request.GET
        q = Aksiya.objects.all()
        
        self.last_user_query = {}
        
        xaridor = Group.objects.get(name='Xaridor')
        if self.request.user.has_perm('can_view_Aksiya') or xaridor in self.request.user.groups.all():


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

            if 'Condition' in url_data and url_data['Condition']:
                q = q.filter(
                    Condition=url_data['Condition'])

            if 'Country' in url_data and url_data['Country']:
                q = q.filter(color__icontains=url_data['Country'])
            
            if 'Size' in url_data and url_data['Size']:
                q = q.filter(color__icontains=url_data['Size'])

            if 'color' in url_data and url_data['color']:
                q = q.filter(color__icontains=url_data['color'])
                
            if 'img' in url_data and url_data['img']:
                q = q.filter(color__icontains=url_data['img'])
            return q



class AksiyaCreateView(CreateView):
    queryset = Aksiya.objects.all()
    template_name = 'Aksiya-add.html'
    fields = "__all__"

    success_url = '/Aksiya'


class AksiyaUpdateView(UpdateView):
    queryset = Aksiya.objects.all()
    template_name = 'Aksiya-add.html'
    fields = "__all__"

    success_url = '/Aksiya'


def main(request):
    bks = Aksiya.objects.all()

    context = {'Aksiya': bks}
    return render(request, "main.html", context=context)




class AksiyaDeleteView(DeleteView):
    queryset = Aksiya.objects.all()
    template_name = 'Aksiya-delete.html'
    fields = "__all__"

    success_url = '/Aksiya'



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
                return redirect('Techniques')
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
