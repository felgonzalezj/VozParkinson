# Generated by Django 3.1.2 on 2022-04-21 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20220421_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente_Profesional',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idapp_paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.paciente')),
                ('idapp_profesional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.profesional')),
            ],
        ),
    ]
