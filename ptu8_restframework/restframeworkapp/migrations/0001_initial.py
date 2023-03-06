# Generated by Django 4.1.7 on 2023-03-06 08:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='AlbumReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1500)),
                ('score', models.IntegerField()),
                ('album_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums_reviews', to='restframeworkapp.album')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums_reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('duration', models.IntegerField()),
                ('album_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='restframeworkapp.band')),
            ],
        ),
        migrations.CreateModel(
            name='AlbumReviewLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_review_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alum_review_likes', to='restframeworkapp.albumreview')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_reivew_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AlbumReviewComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1500)),
                ('album_review_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_review_comments', to='restframeworkapp.albumreview')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_review_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='band_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='restframeworkapp.band'),
        ),
    ]