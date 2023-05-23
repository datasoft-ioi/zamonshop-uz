from mptt.forms import TreeNodeMultipleChoiceField
from django import forms

from .models import ProductCategory


class ProductCategoryForm(forms.Form):
    category = TreeNodeMultipleChoiceField(
        queryset = ProductCategory.objects.all()
)
