# Generated by Django 4.0 on 2022-01-23 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0003_remove_baseeleve_type_resp1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseeleve',
            name='nationalite',
            field=models.ForeignKey(default='100', on_delete=django.db.models.deletion.CASCADE, related_name='nationalite', to='inscription.pays', verbose_name='Nationalité'),
            preserve_default=False,
        ),
    ]
