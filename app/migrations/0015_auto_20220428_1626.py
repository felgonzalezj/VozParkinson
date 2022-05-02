# Generated by Django 3.1.2 on 2022-04-28 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0014_auto_20220427_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaPublicacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombrecategoria', models.CharField(max_length=30, verbose_name='Nombre Categoria')),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Categoria Publicacion',
                'verbose_name_plural': 'Categoria Publicaciones',
            },
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.categoriapublicacion'),
        ),
    ]
