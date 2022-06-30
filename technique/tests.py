from django.test import TestCase

# Create your tests here.



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

def about(request):
    return render(request, "about.html")
def brand(request):
    return render(request, "brand.html")
def contact(request):
    return render(request, "contact.html")
def products(request):
    return render(request, "products.html")
