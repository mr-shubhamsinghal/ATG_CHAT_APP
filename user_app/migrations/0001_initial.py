# Generated by Django 3.2.7 on 2021-10-02 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='captchaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('captcha_string', models.TextField()),
                ('captcha_res', models.CharField(max_length=10)),
            ],
        ),
    ]