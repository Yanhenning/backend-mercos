# Generated by Django 2.1.5 on 2019-02-02 19:00

import backend_mercos.enums_merc
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeProduto', models.CharField(max_length=100)),
                ('preco', models.BigIntegerField(default=0)),
                ('precoCliente', models.BigIntegerField()),
                ('quantidadeProduto', models.BigIntegerField(default=1)),
                ('receita', models.BigIntegerField()),
                ('multiplo', models.BigIntegerField()),
                ('lucro', models.BigIntegerField()),
                ('rentabilidade', models.CharField(choices=[(backend_mercos.enums_merc.TipoRentabilidade('Sem Rentabilidade'), 'Sem Rentabilidade'), (backend_mercos.enums_merc.TipoRentabilidade('Rentabilidade Ótima'), 'Rentabilidade Ótima'), (backend_mercos.enums_merc.TipoRentabilidade('Rentabilidade Boa'), 'Rentabilidade Boa'), (backend_mercos.enums_merc.TipoRentabilidade('Rentabilidade Ruim'), 'Rentabilidade Ruim')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidadeItem', models.BigIntegerField(default=0)),
                ('valor', models.BigIntegerField(default=0)),
                ('rentabilidade', models.CharField(choices=[(backend_mercos.enums_merc.TipoRentabilidade('Sem Rentabilidade'), 'Sem Rentabilidade'), (backend_mercos.enums_merc.TipoRentabilidade('Rentabilidade Ótima'), 'Rentabilidade Ótima'), (backend_mercos.enums_merc.TipoRentabilidade('Rentabilidade Boa'), 'Rentabilidade Boa'), (backend_mercos.enums_merc.TipoRentabilidade('Rentabilidade Ruim'), 'Rentabilidade Ruim')], max_length=60)),
                ('cliente', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend_mercos.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('compra_minima', models.IntegerField(default=0)),
                ('preco', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=20)),
                ('quantidade_pedidos', models.BigIntegerField(default=0)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.AddField(
            model_name='pedido',
            name='usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend_mercos.Usuario'),
        ),
        migrations.AddField(
            model_name='itempedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_mercos.Pedido'),
        ),
    ]
