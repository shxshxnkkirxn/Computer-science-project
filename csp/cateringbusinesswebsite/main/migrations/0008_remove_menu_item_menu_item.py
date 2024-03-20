# Generated by Django 4.2.7 on 2024-03-06 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_order_menu_order_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='item',
        ),
        migrations.AddField(
            model_name='menu',
            name='item',
            field=models.ManyToManyField(related_name='item', to='main.item'),
        ),
    ]