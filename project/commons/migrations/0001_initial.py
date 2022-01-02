# Generated by Django 4.0 on 2022-01-02 15:26

from django.db import migrations, models
import project.commons.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('file', models.FileField(upload_to=project.commons.models.get_file_upload_path)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('-updated_at',),
                'abstract': False,
            },
        ),
    ]
