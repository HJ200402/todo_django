from django.db import models


# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=200, null=False, help_text="할 일을 채워주세요!")
    is_done = models.BooleanField(default=False)

    def __str__(self):  #이 함수를 넣어줘야 object로 뜨지 않는다.
        return self.task