import sys,shlex
from captcha.image import ImageCaptcha
mr_dark = " ".join(map(shlex.quote, sys.argv[1:]))
image = ImageCaptcha(width = 280, height = 90)
captcha_text = mr_dark
data = image.generate(captcha_text) 
image.write(captcha_text, "CAPTCHA.png")