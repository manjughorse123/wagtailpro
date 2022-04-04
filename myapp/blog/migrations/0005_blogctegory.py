# Generated by Django 4.0.3 on 2022-04-04 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blockauthorsorderable'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCtegory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(allow_unicode=True, help_text='A slug to identify posts by this category', max_length=255, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Blog Category',
                'verbose_name_plural': ' Blog Categories',
                'ordering': ['name'],
            },
        ),
    ]
