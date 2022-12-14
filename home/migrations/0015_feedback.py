# Generated by Django 4.0.3 on 2022-05-19 12:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0005_remove_profile_crs'),
        ('home', '0014_studymaterial'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('rating', models.IntegerField(max_length=5)),
                ('message', models.TextField(max_length=1000)),
                ('added_on', models.DateTimeField(auto_now=True)),
                ('brn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.service')),
                ('fname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('prf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
            ],
        ),
    ]
