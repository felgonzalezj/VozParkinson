# Generated by Django 3.1.2 on 2022-04-20 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220420_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rutprofesional', models.CharField(max_length=30)),
                ('nombreprofesional', models.CharField(max_length=30)),
                ('apellidopaternoprofesional', models.CharField(max_length=30)),
                ('apellidomaternoprofesional', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
                ('whatsapp', models.CharField(max_length=15)),
                ('telegram', models.CharField(max_length=30)),
                ('id_tipo_usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tipo_usuario')),
            ],
        ),
    ]
