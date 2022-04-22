# Generated by Django 3.1.2 on 2022-04-20 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipo_usuario',
            options={'verbose_name': 'Tipo de usuario', 'verbose_name_plural': 'Tipo de usuarios'},
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tipo_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tipo_usuario')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
