# Generated by Django 2.0 on 2019-06-30 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkformhc',
            name='data_remark',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='备注'),
        ),
    ]
