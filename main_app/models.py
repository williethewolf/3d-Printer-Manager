from datetime import datetime
from django.db import models
from django.urls import reverse
# Import the User
from django.contrib.auth.models import User

# Create your models here.
FILAMENTS = (
    ('PLA', 'PLA'),
    ('PLA+', 'PLA+'),
    ('PTEG', 'PTEG'),
    ('ABS', 'ABS'),
    ('NY', 'Nylon'),
)
    
class Filament(models.Model):
    maker= models.CharField(max_length=50)
    material= models.CharField(max_length=4, choices=FILAMENTS, default=FILAMENTS[0][0])
    color= models.CharField(max_length=50)
    diameter= models.DecimalField( max_digits=3, decimal_places=2, default=1.75)
    weight= models.IntegerField()
    temps = models.TextField(max_length=150)

    def __str__(self):
        return self.material

    def get_absolute_url(self):
        return reverse("filament_details", kwargs={"filament_id": self.id})

COMPLETED = (
    ("1", 'Success'),
    ("0", 'Failure')
)

class Print(models.Model):
    print = models.CharField(max_length=50)
    print_time = models.IntegerField()
    #filament =  models.CharField(max_length=4, choices=FILAMENTS, default=FILAMENTS[0][0])
    nozzle_temp = models.IntegerField(default=200)
    nozzle_size = models.DecimalField( max_digits=3, decimal_places=2, default=0.4)
    layer_height= models.DecimalField(max_digits=3, decimal_places=2, default=0.4)
    other_settings = models.TextField(max_length=250, default='Additional slicer settings')
    completed = models.CharField(max_length=1, choices=COMPLETED, default=COMPLETED[0][0])
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # printer = models.ForeignKey(Printer, on_delete = models.SET_DEFAULT, default= "unavailable")
    def __str__(self):
        hours = self.print_time // 60
        minutes = self.print_time % 60
        print_time_string ="{}h:{}m".format(hours, minutes)
        if self.completed == "1":
            return f'{self.print} on {self.printer} printed successfully on {self.date.strftime("%d/%m/%Y %H:%M:%S")} and took {print_time_string}'
        else:
            return f'{self.print} on {self.printer} failed on {datetime.now()} after {print_time_string}'
    class Meta:
        ordering = ['-date']
    def get_absolute_url(self):
        return reverse("print_details", kwargs={"print_id": self.id})

class Printer(models.Model):
    #     maker, model, build_volume_X,build_volume_Y,build_volume_Z , print_materials, usage
    maker = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    build_volume_X = models.IntegerField()
    build_volume_Y = models.IntegerField()
    build_volume_Z = models.IntegerField()
    print_materials = models.ManyToManyField(Filament)
    usage = models.TextField(max_length=150)
    prints = models.ManyToManyField(Print)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse("printer_details", kwargs={"printer_id": self.id})



