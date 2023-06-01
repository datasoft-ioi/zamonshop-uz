from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


from rest_framework import generics
from rest_framework import viewsets


from .models import Basket, Category, Subcategory, Product
from .serializers import CategorySerializer, SubcategorySerializer, ProductSerializer

from django.views.generic import TemplateView, ListView
from django.db.models import Q 

class SearchResultsView(ListView):
    model = Product
    template_name = "home/base.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Product.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list

def products(request):
    return render(request, "products/products.html")

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product":product,
    }
    return render(request, 'products/product_detail.html', context)

def productCategory(request):
    return render(request, "products/productsCategory.html")


@login_required
def basket(request):

    baskets = Basket.objects.filter(user=request.user)
    context = {
        "baskets": baskets,
        "total_sum": sum(basket.sum() for basket in baskets),
        "total_quantity": sum(basket.quantity for basket in baskets),
    }

    return render(request, 'orders/savat.html', context)



@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):

    basket = Basket.objects.get(id=basket_id)
    basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])




class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        category_slug = self.request.query_params.get('category_slug', None)
        if category_slug is not None:
            queryset = queryset.filter(slug=category_slug)
        return queryset


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

class SubcategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    