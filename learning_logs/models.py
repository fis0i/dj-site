from django.db import models


class Topic(models.Model):
    # тема, которую захочет добавить пользователь.
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # возвращает строковое представление модели.
        return self.text


class Entry(models.Model):
    # информация, полученная пользователем по теме
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        # возвращает строковое представление модели
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return f"{self.text[:50]}"
