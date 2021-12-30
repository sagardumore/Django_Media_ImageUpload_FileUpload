from django import forms
from .models import Laptop

class LaptopModelForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = "__all__"
        labels = {
            'company':'Enter Company Name',
            'model_name':'Enter Laptop Model Name',
            'ram':'RAM',
            'rom':'ROM',
            'weight':'Weight (in kg)'
        }
        widgets = {
            'ram':forms.TextInput(attrs={'placeholder':'in GB'}),
            'rom':forms.TextInput(attrs={'placeholder':'in GB'}),
        }

    def clean_ram(self):
        ram = self.cleaned_data['ram']
        if ram <= 0:
            raise forms.ValidationError("ROM must be greater than zero")
        elif ram % 2 != 0:
            raise forms.ValidationError("Invalid RAM (must be even number)")
        else:
            return ram

    def clean_rom(self):
        rom = self.cleaned_data['rom']
        if rom <= 0:
            raise forms.ValidationError("ROM must be greater than zero")
        else:
            return rom

    def clean_weight(self):
        weight = self.cleaned_data['weight']
        if weight <= 0:
            raise forms.ValidationError("Weight must be greater than zero")
        else:
            return weight


    def clean(self):
        laptop = Laptop.objects.all()
        all_cleaned_data = super().clean()
        for object in laptop:
           if all_cleaned_data["company"] == object.company and \
                   all_cleaned_data["model_name"] == object.model_name and \
                   all_cleaned_data["ram"] == object.ram and \
                   all_cleaned_data["rom"] == object.rom and \
                   all_cleaned_data["processor"] == object.processor and \
                   all_cleaned_data["price"] == object.price and \
                   all_cleaned_data["weight"] == object.weight:
               raise forms.ValidationError("Record already exists")








