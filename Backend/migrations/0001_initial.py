# Generated by Django 4.1.4 on 2022-12-08 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admindb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Email', models.EmailField(blank=True, max_length=30, null=True)),
                ('Username', models.CharField(blank=True, max_length=30, null=True)),
                ('Password', models.CharField(blank=True, max_length=30, null=True)),
                ('Confirmpassword', models.CharField(blank=True, max_length=30, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='productdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Category', models.CharField(blank=True, max_length=30, null=True)),
                ('Description', models.CharField(blank=True, max_length=30, null=True)),
                ('Price', models.CharField(blank=True, max_length=30, null=True)),
                ('Quantity', models.CharField(blank=True, max_length=30, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='product')),
            ],
        ),
    ]