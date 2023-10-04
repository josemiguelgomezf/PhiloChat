from django.db import models


class User(models.Model):
    pass


class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    philosopher = models.CharField(max_length=255)
    question = models.TextField()
    response = models.TextField()

    def get_absolute_url(self):
        return reverse('philochat:conversation', args=[self.pk])


class Question(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    question = models.TextField()


class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.TextField()
