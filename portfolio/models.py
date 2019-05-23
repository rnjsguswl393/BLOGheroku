from django.db import models

class Portfolio(models.Model):
    title=models.CharField(max_length=255)
    image=models.ImageField(upload_to='images/')
    description=models.CharField(max_length=500)
#이미지를 쓰기위해선 필로를 설치해줘야함 pip install pillow
#필로는 파이썬으로 이미지를 효율적으러 해주게하는 시스템

    def __str__(self):
        return self.title
