# Generated by Django 4.2.2 on 2023-06-30 15:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.IntegerField()),
                ('minutes', models.IntegerField()),
                ('seconds', models.IntegerField()),
                ('am_pm', models.CharField(max_length=5)),
                ('refid', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
        ),
    ]