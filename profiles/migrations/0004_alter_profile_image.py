# Generated by Django 4.2.20 on 2025-04-02 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_qdjgyp', upload_to='media/images/'),
        ),
    ]
