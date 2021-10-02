from django.db import models

# Create your models here.


class captchaModel(models.Model):
	captcha_string = models.TextField()
	captcha_res = models.CharField(max_length=10)
