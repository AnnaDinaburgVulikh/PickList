# Generated by Django 3.2.3 on 2021-05-19 11:25

import datetime
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
            name='Eventlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('location', models.CharField(max_length=300)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Items_to_bring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventlist.eventlist')),
            ],
        ),
        migrations.CreateModel(
            name='Items_for_invitees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchased', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventlist.items_to_bring')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Invitees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventlist.eventlist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
