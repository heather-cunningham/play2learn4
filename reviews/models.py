# from django.conf import settings
from django.db import models


class Review(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    email = models.EmailField(help_text="Please, enter a valid email address.")
    comments = models.TextField()
    review_date_time = models.DateTimeField(auto_now_add=True)
    #
    #
    def __str__(self):
        return f""" Review submitted by: {self.first_name} {self.last_name}\n
        On: {self.review_date_time}
        Comments:\n{'-' * 10}\n
        {self.comments}"""
