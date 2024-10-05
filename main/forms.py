from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class DairyEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "fat_content", "quantity", "rating"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
    
    def fat_content(self):
        fat_content = self.cleaned_data["fat_content"]
        return strip_tags(fat_content)
    
    def clean_quantity(self):
        quantity = self.cleaned_data["quantity"]
        return strip_tags(quantity)
    
    def clean_rating(self):
        rating = self.cleaned_data["rating"]
        return strip_tags(rating)
