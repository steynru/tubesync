# Generated by nothing. Done manually by InterN0te on 2023-12-10 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sync', '0020_auto_20231024_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='copy_channel_thumbnails',
            field=models.BooleanField(default=False, help_text='Copy channel thumbnails in poster.jpg and season-poster.jpg, these may be detected and used by some media servers', verbose_name='copy channel thumbnails'),
        ),
    ]
