from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "price",
            "description",
            "stock",
            "category",
        ]

        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Введіть опис книги",
                }
            ),
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Назва книги",
                }
            ),
        }

    def clean_price(self):
        price = self.cleaned_data.get("price")

        if price is not None and price <= 0:
            raise forms.ValidationError(
                "Ціна повинна бути більшою за 0."
            )

        return price

