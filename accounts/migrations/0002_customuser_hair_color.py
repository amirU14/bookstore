# Generated by Django 5.0.2 on 2024-03-06 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='hair_color',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]