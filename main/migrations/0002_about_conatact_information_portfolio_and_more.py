# Generated by Django 4.2.5 on 2023-10-11 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('l_text', models.TextField()),
                ('r_text', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Conatact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('massage', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='')),
                ('address', models.CharField(max_length=255)),
                ('tw', models.URLField()),
                ('fb', models.URLField()),
                ('insta', models.URLField()),
                ('dribble', models.URLField()),
                ('ln', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RenameModel(
            old_name='Image',
            new_name='Client',
        ),
        migrations.RenameModel(
            old_name='Testimonial',
            new_name='Testimonials',
        ),
        migrations.DeleteModel(
            name='Info',
        ),
        migrations.AlterField(
            model_name='services',
            name='icon_code',
            field=models.CharField(help_text='icon-icons', max_length=66),
        ),
    ]