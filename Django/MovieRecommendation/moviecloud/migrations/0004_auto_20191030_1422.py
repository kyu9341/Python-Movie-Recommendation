# Generated by Django 2.2.6 on 2019-10-30 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviecloud', '0003_auto_20191030_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedata',
            name='wordcloud',
            field=models.CharField(max_length=400, verbose_name='wordcloud 이미지 경로'),
        ),
    ]
