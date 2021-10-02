
import random
import base64
from PIL import Image
from io import BytesIO
from captcha.image import ImageCaptcha

from user_app.models import captchaModel


def str_to_image(data):
	str_obj = data.split(',')
	to_byte = base64.b64decode(str_obj[1])
	#PIL object
	img_obj = Image.open(BytesIO(to_byte))
	return img_obj


def image_to_str(data):
	# data obj must be BytesIO obj
	to_byte = base64.b64encode(data.getvalue())
	str_value = to_byte.decode('utf-8')
	return str_value


def get_captcha():
	ops = ['+', '*']
	num1 = random.randint(1, 12)
	num2 = random.randint(1, 10)
	operation = random.choice(ops)
	image = ImageCaptcha()
	content = str(num1) + operation + str(num2)
	res = eval(content)
	data = image.generate(content)
	decoded_img = image_to_str(data)
	data = f"data:image/jpeg;base64,{decoded_img}"
	instance = captchaModel.objects.create(captcha_string=data, captcha_res=res)
	instance.save()
	return data
