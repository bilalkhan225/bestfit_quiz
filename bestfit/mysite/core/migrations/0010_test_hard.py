# Generated by Django 3.0 on 2019-12-26 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test_hard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Eng', 'English'), ('Math', 'Maths'), ('Programing', 'Programming'), ('Comp', 'Computer')], default=None, max_length=64)),
                ('question', models.CharField(max_length=255)),
                ('option_1', models.CharField(max_length=255)),
                ('option_2', models.CharField(max_length=255)),
                ('option_3', models.CharField(max_length=255)),
                ('option_4', models.CharField(max_length=255)),
                ('answer', models.CharField(default=None, max_length=255)),
            ],
        ),
    ]
