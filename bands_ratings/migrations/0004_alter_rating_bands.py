# Generated by Django 4.1 on 2023-06-06 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bands_ratings', '0003_alter_rating_bands'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='bands',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bands_ratings.bands'),
        ),
    ]
