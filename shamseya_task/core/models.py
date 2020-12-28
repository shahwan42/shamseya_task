from django.db import models


class Review(models.Model):
    submitted_at = models.DateField()

    class Meta:
        indexes = [models.Index(fields=["submitted_at"])]


class Choice(models.Model):
    text = models.CharField(max_length=20)


class Question(models.Model):
    text = models.TextField()
    choices = models.ManyToManyField(Choice, related_name="questions")


class Answer(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
