# Generated by Django 4.1.1 on 2022-09-21 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maker', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('build_volume_X', models.IntegerField()),
                ('build_volume_Y', models.IntegerField()),
                ('build_volume_Z', models.IntegerField()),
                ('print_materials', models.CharField(max_length=50)),
                ('usage', models.TextField(max_length=150)),
            ],
        ),
    ]