# Generated by Django 4.0 on 2022-01-23 13:55

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseeleve',
            name='civility',
            field=models.CharField(choices=[('M.', 'M.'), ('MME', 'Mme')], default='M.', help_text="Quel sexe t'est attribué dans les documents administratifs ?", max_length=3, verbose_name='Civilité'),
        ),
        migrations.AlterField(
            model_name='baseeleve',
            name='genre',
            field=models.CharField(choices=[('il', 'il'), ('elle', 'elle'), ('iel', 'iel')], default='Iel', help_text="Veux-tu que l'on parle de toi en disant il, elle ou iel ?", max_length=5, verbose_name='Pronom'),
        ),
        migrations.AlterField(
            model_name='baseeleve',
            name='nom_usage',
            field=models.CharField(help_text="Comment souhaites-tu qu'on t'appelle au lycée ?", max_length=255, verbose_name="Nom d'usage"),
        ),
        migrations.AlterField(
            model_name='baseeleve',
            name='telephone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='0000000000', max_length=128, region=None, verbose_name='Téléphone'),
            preserve_default=False,
        ),
    ]
