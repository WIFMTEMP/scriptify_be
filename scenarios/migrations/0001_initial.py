# Generated by Django 4.2.8 on 2024-11-25 02:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scenarios', to='movies.genre')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scenarios', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('request', 'Request'), ('response', 'Response')], max_length=10)),
                ('message_type', models.CharField(choices=[('first', 'First'), ('revise', 'Revise'), ('line', 'Line'), ('detail', 'Detail')], max_length=10)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='scenarios.scenario')),
            ],
        ),
    ]
