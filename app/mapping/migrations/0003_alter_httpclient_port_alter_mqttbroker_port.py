# Generated by Django 5.0.4 on 2024-04-23 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0002_endpoint_alter_mapping_endpoint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='httpclient',
            name='port',
            field=models.PositiveIntegerField(blank=True, default=80, null=True, verbose_name='Port'),
        ),
        migrations.AlterField(
            model_name='mqttbroker',
            name='port',
            field=models.PositiveIntegerField(blank=True, default=80, null=True, verbose_name='Port'),
        ),
    ]
