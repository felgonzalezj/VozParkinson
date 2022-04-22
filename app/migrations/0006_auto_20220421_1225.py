# Generated by Django 3.1.2 on 2022-04-21 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_paciente'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesional',
            name='id_app_usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='auth.user'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Fonoaudiologo_paciente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombrepaciente', models.CharField(max_length=30)),
                ('apellidopatpaciente', models.CharField(max_length=30)),
                ('apellidomatpaciente', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('audio', models.FileField(upload_to='')),
                ('video', models.FileField(upload_to='')),
                ('feedback', models.TextField()),
                ('id_app_usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
