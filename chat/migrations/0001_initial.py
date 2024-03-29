# Generated by Django 3.0 on 2022-06-29 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages', models.TextField(blank=True, max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('reciver', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='reciver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
