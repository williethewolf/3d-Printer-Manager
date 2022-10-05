from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Printer, Filament
from .forms import PrintForm

# Create your views here.
def home (request):
    return render( request, 'home.html', {'page_name' : 'Home'})

def about (request):
    return render( request, 'about.html', {'page_name' : 'About'})

# class Printer:
#     def __init__ (self, maker, model, build_volume_X, build_volume_Y, build_volume_Z, print_materials, usage):
#         self.maker = maker
#         self.model = model
#         self.build_volume_X = build_volume_X
#         self.build_volume_Y = build_volume_Y
#         self.build_volume_Z = build_volume_Z
#         self.print_materials = print_materials
#         self.usage = usage


# printers =[
#     Printer('Voxelab', 'Aquila', 220,220,250, ['PLA','ABS','PETG', 'Nylon'],"Models" ),
#     Printer('Creality', 'Ender 3 v2', 220,220,250, ['PLA','ABS','PETG', 'Nylon'], 'parts' ),
#     Printer('ANYCUBIC', 'Mega S', 210, 210, 205, ['PLA','ABS','PETG', 'Nylon'], 'parts' ),
# ]


def printers_index (request):
    printers = Printer.objects.all()
    return render( request, 'printers/index.html', {'page_name' : 'Printers Collection', 'printers':printers})

def printer_details(request, printer_id):
    printer = Printer.objects.get(id=printer_id)
    print_form = PrintForm
    return render (request, 'printers/details.html', {'page_name' : printer.model+"'s details", 'printer': printer, 'print_form':print_form})

def add_print(request, printer_id):
    form = PrintForm(request.POST)
    if form.is_valid():
        new_print = form.save(commit=False)
        new_print.printer_id = printer_id
        new_print.save()
    return redirect ('printer_details', printer_id=printer_id)

#classes instead of functions

class PrinterCreate(CreateView):
    model = Printer
    fields = '__all__'
class PrinterUpdate(UpdateView):
    model = Printer
    fields = ('build_volume_X', 'build_volume_Y', 'build_volume_Z', 'print_materials', 'usage')
class PrinterDelete(DeleteView):
    model = Printer
    success_url = '/printers/'


# FILAMENTS
def filaments_index (request):
    filaments = Filament.objects.all()
    return render( request, 'filaments/index.html', {'page_name' : 'Filaments Collection', 'filaments':filaments})

def filament_details(request, filament_id):
    filament = Filament.objects.get(id=filament_id)
    return render (request, 'filaments/details.html', {'page_name' : filament.maker+"'s filament details", 'filament': filament})


#classes instead of functions

class FilamentCreate(CreateView):
    model = Filament
    fields = '__all__'

class FilamentUpdate(UpdateView):
    model = Filament
    fields = ('material', 'color', 'diameter', 'weight', 'temps')

class FilamentDelete(DeleteView):
    model = Filament
    success_url = '/filaments/'