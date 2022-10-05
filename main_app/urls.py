from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    #Printers
    path('printers/', views.printers_index, name = 'printers_index'),
    path('printers/<int:printer_id>/', views.printer_details, name = "printer_details"),
    path('printers/create', views.PrinterCreate.as_view(), name='printer_create'),
    path('printers/<int:pk>/update', views.PrinterUpdate.as_view(), name='printer_update'),
    path('printers/<int:pk>/delete', views.PrinterDelete.as_view(), name='printer_delete'),
    #Prints
    path('printers/<int:printer_id>/add_print/', views.add_print, name = 'add_print'),
    #Filament
    path('filaments/', views.filaments_index, name = 'filament_index'),
    path('filaments/<int:filament_id>/', views.filament_details, name = "filament_details"),
    path('filaments/create', views.FilamentCreate.as_view(), name='filament_create'),
    path('filaments/<int:pk>/update', views.FilamentUpdate.as_view(), name='filament_update'),
    path('filaments/<int:pk>/delete', views.FilamentDelete.as_view(), name='filament_delete'),
]