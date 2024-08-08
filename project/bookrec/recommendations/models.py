from django.db import models
from django.contrib.auth.models import User

class BookRecommendation(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.URLField()
    genre = models.CharField(max_length=100)
    rating = models.FloatField()
    publication_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recommendations')

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommendation = models.ForeignKey(BookRecommendation, on_delete=models.CASCADE, related_name='likes')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommendation = models.ForeignKey(BookRecommendation, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.recommendation.title}'
