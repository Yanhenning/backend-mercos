# Generated by Django 2.1.5 on 2019-01-23 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend_mercos', '0003_auto_20190122_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='pedidos',
        ),
        migrations.AddField(
            model_name='cliente',
            name='pedidos',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='backend_mercos.Pedido'),
            preserve_default=False,
        ),
    ]