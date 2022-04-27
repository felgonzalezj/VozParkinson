# Generated by Django 3.1.2 on 2022-04-26 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0011_auto_20220426_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicamentoCompra',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_compra', models.DateField()),
                ('id_app_usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Id Usuario')),
                ('idapp_medicamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.medicamento', verbose_name='Nombre Laboratorio')),
                ('idapp_paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.paciente', verbose_name='Rut Paciente')),
            ],
        ),
    ]
