# Generated by Django 5.1.7 on 2025-04-18 18:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reportes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='reportegenerado',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reportes_generados', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='reportegenerado',
            name='tipo_reporte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reportes_generados', to='reportes.tiporeporte', verbose_name='Tipo de reporte'),
        ),
    ]
