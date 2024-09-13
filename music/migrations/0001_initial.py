# Generated by Django 5.1.1 on 2024-09-13 05:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('release_date', models.DateField()),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('duration', models.IntegerField(help_text='Duration in seconds')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.artist')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.genre')),
            ],
        ),
    ]
