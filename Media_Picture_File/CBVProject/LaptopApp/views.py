from django.shortcuts import render,redirect
from .forms import LaptopModelForm
from .models import Laptop
from django.views import View


class AddLaptopView(View):
    def get(self,request):
        form = LaptopModelForm()
        template_name = 'LaptopApp/addlaptopform.html'
        context = {'form':form}
        return render(request, template_name, context)
    def post(self,request):
        form = LaptopModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("show_laptop")
        template_name = 'LaptopApp/addlaptopform.html'
        context = {'form': form}
        return render(request, template_name, context)

class ShowLaptopView(View):
    def get(self,request):
        laptop_obj = Laptop.objects.all()
        template_name = 'LaptopApp/showlaptopinfo.html'
        context = {'laptop_obj': laptop_obj}
        return render(request, template_name, context)

class LaptopUpdateView(View):
    def get(self,request,i):
        laptop = Laptop.objects.get(id=i)
        form = LaptopModelForm(instance=laptop)
        template_name = 'LaptopApp/addlaptopform.html'
        context = {'form':form}
        return render(request, template_name, context)
    def post(self,request,i):
        laptop = Laptop.objects.get(id=i)
        form = LaptopModelForm(request.POST,instance=laptop)
        if form.is_valid():
            form.save()
            return redirect("show_laptop")
        template_name = 'LaptopApp/addlaptopform.html'
        context = {'form': form}
        return render(request, template_name, context)

class LaptopDeleteView(View):
    def get(self,request,i):
        laptop = Laptop.objects.get(id=i)
        template_name = 'LaptopApp/confirmdelete.html'
        context = {'laptop': laptop }
        return render(request, template_name, context)
    def post(self,request,i):
        laptop = Laptop.objects.get(id=i)
        laptop.delete()
        return redirect("show_laptop")

class LaptopDetails(View):
    def get(self,request,i):
        laptop = Laptop.objects.get(id=i)
        template_name = 'LaptopApp/laptop_details.html'
        context = {'laptop': laptop}
        return render(request, template_name, context)

