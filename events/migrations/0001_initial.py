# Generated by Django 5.1.4 on 2025-01-02 08:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total_points', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='Posters/')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('individual_score', models.PositiveIntegerField(default=0)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.department')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')),
                ('program', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.category')),
                ('first_place', models.ManyToManyField(blank=True, related_name='first_place', to='events.student')),
                ('second_place', models.ManyToManyField(blank=True, related_name='second_place', to='events.student')),
                ('third_place', models.ManyToManyField(blank=True, related_name='third_place', to='events.student')),
            ],
        ),
    ]
