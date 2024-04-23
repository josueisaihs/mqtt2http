# Generated by Django 5.0.4 on 2024-04-23 19:18

import app.config.validators
import autoslug.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HTTPClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=2500, null=True, verbose_name='Description')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='name', unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('host', models.URLField(max_length=1000, verbose_name='Host')),
                ('port', models.PositiveIntegerField(blank=True, default=80, help_text='Port number. Default is 80. If you are using a secure connection, the default is 443. If you are using MQTT, the default is 1883.', null=True, verbose_name='Port')),
                ('username', models.CharField(blank=True, max_length=100, null=True, verbose_name='Username')),
                ('password', models.CharField(blank=True, max_length=100, null=True, verbose_name='Password')),
                ('method', models.CharField(blank=True, default='POST', editable=False, max_length=4, verbose_name='Method')),
            ],
            options={
                'verbose_name': 'HTTP Client',
                'verbose_name_plural': 'HTTP Clients',
            },
        ),
        migrations.CreateModel(
            name='MQTTBroker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=2500, null=True, verbose_name='Description')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='name', unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('host', models.URLField(max_length=1000, verbose_name='Host')),
                ('port', models.PositiveIntegerField(blank=True, default=80, help_text='Port number. Default is 80. If you are using a secure connection, the default is 443. If you are using MQTT, the default is 1883.', null=True, verbose_name='Port')),
                ('username', models.CharField(blank=True, max_length=100, null=True, verbose_name='Username')),
                ('password', models.CharField(blank=True, max_length=100, null=True, verbose_name='Password')),
            ],
            options={
                'verbose_name': 'MQTT Broker',
                'verbose_name_plural': 'MQTT Brokers',
            },
        ),
        migrations.CreateModel(
            name='TopicPattern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=2500, null=True, verbose_name='Description')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='name', unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('pattern', models.CharField(max_length=1000, validators=[app.config.validators.validation_pattern], verbose_name='Topic Pattern')),
            ],
            options={
                'verbose_name': 'Topic Pattern',
                'verbose_name_plural': 'Topic Patterns',
                'unique_together': {('slug', 'name', 'pattern')},
            },
        ),
        migrations.CreateModel(
            name='Mapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=2500, null=True, verbose_name='Description')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='name', unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('endpoint', models.CharField(max_length=100, verbose_name='Index Field')),
                ('http_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapping.httpclient', verbose_name='HTTP Client')),
                ('mqtt_broker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapping.mqttbroker', verbose_name='MQTT Broker')),
                ('topic_pattern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapping.topicpattern', verbose_name='Topic Pattern')),
            ],
            options={
                'verbose_name': 'Mapping',
                'verbose_name_plural': 'Mappings',
                'unique_together': {('topic_pattern', 'mqtt_broker', 'http_client')},
            },
        ),
    ]
