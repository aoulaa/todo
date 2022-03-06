# Generated by Django 3.0.5 on 2020-09-09 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200908_1013'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CardItem',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderProduct',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
