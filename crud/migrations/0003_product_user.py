# Generated by Django 3.2.8 on 2021-10-28 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='crud.user'),
        ),
    ]
