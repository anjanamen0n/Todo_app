# Generated by Django 3.2.23 on 2023-11-10 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField(blank=True)),
                ('Date', models.DateField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
