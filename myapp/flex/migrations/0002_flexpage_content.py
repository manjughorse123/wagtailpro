# Generated by Django 4.0.3 on 2022-03-31 13:43

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('title_and_text_block', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add Your Title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Add Additional text', required=True))]))], blank=True, null=True),
        ),
    ]
