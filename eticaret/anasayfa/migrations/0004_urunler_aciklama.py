# Generated by Django 3.2.13 on 2022-07-07 18:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0003_urunler_urun_resim'),
    ]

    operations = [
        migrations.AddField(
            model_name='urunler',
            name='aciklama',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
