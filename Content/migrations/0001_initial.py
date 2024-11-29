# Generated by Django 5.1.2 on 2024-11-28 05:13

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Images', '0003_alter_images_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('data', models.DateField(default=django.utils.timezone.now)),
                ('reaction_positive', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('reaction_negative', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('comments_amount', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Images.images')),
            ],
        ),
    ]