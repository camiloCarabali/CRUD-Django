# Generated by Django 4.1.5 on 2023-01-06 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tercero', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='profesion',
            field=models.CharField(choices=[('INDETERMINADO', 'Indeterminado'), ('DESEMPLEADO', 'Desempleado'), ('EMPLEADO', 'Empleado'), ('PENSIONADO', 'Pensionado')], max_length=200),
        ),
    ]
