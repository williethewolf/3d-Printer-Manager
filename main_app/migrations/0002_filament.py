# Generated by Django 4.1.1 on 2022-09-21 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maker', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('diameter', models.CharField(max_length=50)),
                ('weight', models.IntegerField(max_length=50)),
                ('temps', models.TextField(max_length=150)),
            ],
        ),
    ]
