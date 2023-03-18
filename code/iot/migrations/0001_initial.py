# Generated by Django 4.1.7 on 2023-03-15 05:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machines',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('machine_id', models.CharField(max_length=100, null=True)),
                ('display_name', models.CharField(max_length=100, null=True)),
                ('store_id', models.UUIDField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Machine',
            },
        ),
        migrations.CreateModel(
            name='StoreSessions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WeightChanges',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('scale_id', models.CharField(max_length=10)),
                ('machine_id', models.CharField(max_length=20)),
                ('weight_change', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('session_id', models.UUIDField()),
                ('status', models.CharField(max_length=255)),
            ],
        ),
    ]
