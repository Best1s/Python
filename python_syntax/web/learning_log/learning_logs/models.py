from django.db import models

# Create your models here.
class Topic(models.Model):
  """用户学习的主题"""
  #定义 CharField 属性时，必须告诉Django该在数据库中预留多少空间
  text = models.CharField(max_length=200)
  #记录日期和时间的数据,jango将这个属性自动设置成当前日期和时间
  date_added = models.DateTimeField(auto_now_add=True)  
  def __str__(self):
    """返回模型的字符串表示"""
    return self.text
class Entry(models.Model):
  """学到的有关某个主题的具体知识"""
  topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
  text = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)
  class Meta:
    verbose_name_plural = 'entries'
  def __str__(self):
    """返回模型的字符串表示"""
    if len(self.text) >= 50:
      return self.text[:50] + "..."
    else:
      return self.text