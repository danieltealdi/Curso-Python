from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from products.models import Product


class ProductListView(ListView):
    template_name='index.html'
    queryset=Product.objects.all()

    model = Product
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['mensaje']='Productos'
        return context
    
class ProductDetailView(DetailView) :
    model = Product
    template_name = 'products/product.html'
    def get_queryset(self):
    #   queryset=Product.objects.filter(id=self.kwargs['pk'])
        queryset=Product.objects.filter(slug=self.kwargs['slug'])
        
        return queryset
    
class ProductSearchListView(ListView):
    template_name = 'products/search.html'
    def get_queryset(self):
        filters=Q(title__icontains=self.query())|Q(category__title__icontains=self.query())
        return Product.objects.filter(filters)
    def query(self):
        return self.request.GET.get('i')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        return context

    
    
    
    
        