# Generated by Django 4.0.2 on 2022-02-10 13:44
from django.core.management import call_command
from django.db import migrations

def forwards_func(apps, schema_editor):
    data_list = ['./data/mee.json', './data/sociopro.json', './data/spe.json', './data/departement.json', './data/pays.json', './data/communes.json']

    print('forwards')
    print(data_list)
    for data in data_list:
        print(data)
        call_command('loaddata', data, verbosity=2)


def reverse_func(apps, schema_editor):
    print('reverse')

class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func, elidable=False)
    ]
