from django.db import models


class Publicaton(models.Model):
    city = models.CharField(max_length=200, verbose_name="Город")
    time = models.TimeField(auto_now=False, verbose_name="Время")

    def __str__(self):
        return str(self.city) + ' ' + str(self.time)

    class Meta:
        verbose_name = "Время публикаций"
        verbose_name_plural = "Время публикаций"
        ordering = ["city", "time"]


class Groups(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    chat_id = models.CharField(max_length=200, verbose_name="ID")
    city = models.CharField(max_length=200, default="t",  verbose_name="Город")
    approved = models.BooleanField(default=False,  verbose_name="Доступ")

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
        ordering = ["name"]
