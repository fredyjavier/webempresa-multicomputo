# Generated by Django 4.0.6 on 2022-09-24 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lienapedido',
            old_name='pedido_id',
            new_name='pedido',
        ),
        migrations.RenameField(
            model_name='lienapedido',
            old_name='producto_id',
            new_name='producto',
        ),
    ]