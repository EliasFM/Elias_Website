# Generated by Django 5.1.2 on 2024-11-20 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(null='/static/assets/HDR_Elephant.jpg', upload_to='projects/'),
            preserve_default='/static/assets/HDR_Elephant.jpg',
        ),
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]