# Generated by Django 4.0.3 on 2022-05-17 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_rename_feedback_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='studymaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matname', models.CharField(max_length=30)),
                ('materials', models.FileField(upload_to='materials')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('bran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.service')),
            ],
        ),
    ]
