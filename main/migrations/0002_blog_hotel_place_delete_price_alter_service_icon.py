# Generated by Django 5.0.3 on 2024-03-15 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='Blogs/')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='Hotels/')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('body', models.TextField()),
                ('where', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='Places/')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('body', models.TextField()),
                ('how_long', models.TextField()),
                ('where', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Price',
        ),
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.FileField(upload_to='Services/'),
        ),
    ]
