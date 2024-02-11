# Generated by Django 4.2.10 on 2024-02-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0011_alter_auction_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='auction-images/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null='avatar.jpg', upload_to='media/avatars'),
        ),
    ]