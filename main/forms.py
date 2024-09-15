from django.forms import ModelForm
from main.models import Product

class DairyEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "fat_content", "quantity", "rating"]
