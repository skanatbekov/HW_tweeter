# Generated by Django 4.2 on 2023-05-02 05:52

from django.db import migrations, models
import django.db.models.deletion
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='TweetImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=posts.models.tweet_image_store)),
                ('tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.tweet')),
            ],
        ),
    ]
