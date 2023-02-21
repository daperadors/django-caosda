# Generated by Django 3.2.18 on 2023-02-21 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name', 'date'],
            },
        ),
        migrations.CreateModel(
            name='Videogame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('subscription_price', models.IntegerField(default=0)),
                ('isNew', models.BooleanField(default=False)),
                ('plataform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videojocs.platform')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name', 'subscription_price', 'isNew'],
            },
        ),
    ]
