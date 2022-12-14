# Generated by Django 4.1.1 on 2022-10-03 20:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.TextField(verbose_name='Title')),
                ('position', models.IntegerField(verbose_name='Position')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.TextField(verbose_name='Title')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.TextField(verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('position', models.IntegerField(verbose_name='Position')),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.column')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='column',
            name='frame',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='tasks.frame'),
        ),
    ]
