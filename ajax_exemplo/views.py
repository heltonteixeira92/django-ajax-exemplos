from django.shortcuts import render, redirect
from django.views.generic import View
from ajax_exemplo.models import Product


# Create your views here.


class ProductView(View):
    def get(self, request):
        allproducts = Product.objects.all()
        context = {
            'products': allproducts
        }
        return render(request, "product/index.html", context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            product_ids = request.POST.getlist('id[]')
            for id in product_ids:
                product = Product.objects.get(pk=id)
                product.delete()
            return redirect('delete-product')
