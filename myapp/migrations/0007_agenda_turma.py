# Generated by Django 5.0.4 on 2024-05-26 19:41

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_avisos_ano_avisos_atualizado_em_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='turma',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='myapp.turma'),
            preserve_default=False,
        ),
    ]
