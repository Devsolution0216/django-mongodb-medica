# Generated by Django 2.0.1 on 2018-01-28 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.CharField(max_length=255)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('mobile_number', models.CharField(blank=True, max_length=10)),
                ('description', models.TextField(max_length=255)),
                ('date', models.DateField(verbose_name='%m/%d/%Y')),
                ('created_at', models.DateTimeField(verbose_name='%m/%d/%Y %H:%M:%S')),
                ('updated_at', models.DateTimeField(verbose_name='%m/%d/%Y %H:%M:%S')),
            ],
        ),
    ]
