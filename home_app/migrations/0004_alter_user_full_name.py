# Generated by Django 5.0.7 on 2024-08-17 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0003_user_full_name_user_is_active_user_is_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
