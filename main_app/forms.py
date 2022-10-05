from pyexpat import model
from statistics import mode
from django.forms import ModelForm
from .models import Print

class PrintForm(ModelForm):
    class Meta:
        model = Print
        fields = ('print', 'print_time', 'filament', 'nozzle_temp', 'nozzle_size', 'layer_height', 'other_settings', 'completed' )