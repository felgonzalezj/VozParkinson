# Generated by Django 3.1.2 on 2022-04-19 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo_usuario', models.CharField(max_length=50)),
                ('codigo_tipo_usuario', models.IntegerField()),
                ('descripcion_tipo_usuario', models.TextField()),
            ],
        ),
    ]
