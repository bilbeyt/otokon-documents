from django import forms
from django.template.defaultfilters import slugify
from uploader.models import Document


class DocumentCreateForm(forms.ModelForm):
    class Meta:
        model = Document
        exclude = ["author", "slug"]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        slug = slugify(title)
        if Document.objects.filter(slug=slug).exists():
            raise forms.ValidationError("This title exists. Change the title.")
        return title


class DocumentUpdateForm(forms.ModelForm):
    class Meta:
        model = Document
        exclude = ["author", "slug"]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        slug = slugify(title)
        if Document.objects.filter(slug=slug).exists():
            raise forms.ValidationError("This title exists. Change the title.")
        return title
