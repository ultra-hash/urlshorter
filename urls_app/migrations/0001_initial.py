# Generated by Django 4.1.5 on 2023-01-17 08:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=40, unique=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shorturls',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('target_url', models.URLField()),
                ('short_url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='urls_app.users')),
            ],
        ),
    ]
