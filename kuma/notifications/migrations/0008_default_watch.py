# Generated by Django 3.2.7 on 2022-01-06 03:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0007_watch_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwatch',
            name='custom_default',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='DefaultWatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_updates', models.BooleanField(default=True)),
                ('browser_compatibility', models.JSONField(default=list)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
