from django.db import models
from commonmodel.models import CommonModel

#모델 이름은 단수로 통일하기
class DateMemo(CommonModel):
  """ 특정 날짜의 메모 """
  description= models.CharField(max_length=100 ,default = "")
  user = models.ForeignKey("users.User" , on_delete=models.CASCADE)
  date = models.DateTimeField()
  
  def __str__(self):
    return f"{self.user} : {self.description}"