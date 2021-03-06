# Generated by Django 3.0.8 on 2020-08-02 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20200802_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='nome',
            field=models.CharField(default=None, max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-ruler-pencil', 'almofada'), ('lni-support', 'outros'), ('lni-customer', 'baby'), ('lni-grid-alt', 'pet')], max_length=50, verbose_name='Icone'),
        ),
    ]
