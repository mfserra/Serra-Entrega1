# Generated by Django 3.2.9 on 2021-12-28 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('cantJugadores', models.IntegerField()),
                ('competitivo', models.BooleanField()),
            ],
        ),
    ]