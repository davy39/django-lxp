# Generated by Django 4.0 on 2022-01-23 16:31

import address.models
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('inscription', '0002_alter_baseeleve_civility_alter_baseeleve_genre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseeleve',
            name='type_resp1',
        ),
        migrations.RemoveField(
            model_name='baseeleve',
            name='type_resp2',
        ),
        migrations.AddField(
            model_name='baseeleve',
            name='resp1',
            field=models.CharField(choices=[('pere', 'Père'), ('mere', 'Mère'), ('autre', 'Autre responsable légal ou référent')], default='mere', max_length=5, verbose_name='Responsable 1'),
        ),
        migrations.AlterField(
            model_name='baseeleve',
            name='adresse_resp1',
            field=address.models.AddressField(on_delete=django.db.models.deletion.CASCADE, related_name='resp1', to='address.address', verbose_name='Adresse'),
        ),
        migrations.AlterField(
            model_name='baseeleve',
            name='adresse_resp2',
            field=address.models.AddressField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resp2', to='address.address', verbose_name='Adresse'),
        ),
        migrations.AlterField(
            model_name='baseeleve',
            name='email_resp2',
            field=models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='baseeleve',
            name='nom_resp2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nom de famille'),
        ),
        migrations.AlterField(
            model_name='baseeleve',
            name='prenom_resp2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Prénom'),
        ),
        migrations.AlterField(
            model_name='baseeleve',
            name='resp2',
            field=models.CharField(choices=[('pere', 'Père'), ('mere', 'Mère'), ('autre', 'Autre responsable légal ou référent'), ('aucun', 'Aucun')], default='pere', max_length=5, verbose_name='Responsable 2'),
        ),
        migrations.AlterField(
            model_name='baseeleve',
            name='sociopro_resp1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resp1', to='inscription.sociopro', verbose_name='Profession'),
        ),
        migrations.AlterField(
            model_name='baseeleve',
            name='sociopro_resp2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resp2', to='inscription.sociopro', verbose_name='Profession'),
        ),
        migrations.AlterField(
            model_name='baseeleve',
            name='tel_resp2',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Numéro de téléphone'),
        ),
    ]
