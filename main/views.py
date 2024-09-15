from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import DairyEntryForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    products = Product.objects.all() # retrieve seluruh data

    context = {
        'name': 'Aileen Josephine Halim',
        'class': 'PBP F',
        'npm': '2306165761',
        'products': products
    }

    return render(request, "main.html", context)

# function untuk menambahkan product
def create_product(request):
    form = DairyEntryForm(request.POST or None)

    # jika methodnya POST, maka save formnya dan redirect ke show_main
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    # jika selain POST request, tampilkan main.html beserta context
    context = {'form': form}
    return render(request, "create_product.html", context)

# mengembalikan data dalam bentuk xml
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# mengembalikan data dalam bentuk json
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# mengembalikan data dalam bentuk xml, mengambilnya berdasarkan id
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# mengembalikan data dalam bentuk json, mengambilnya berdasarkan id
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")