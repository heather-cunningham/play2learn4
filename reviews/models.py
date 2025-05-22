from django.conf import settings
from django.db import models


## aka Feedback
class Review(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    email = models.EmailField(max_length=250, 
                              help_text="(Please, enter a valid email address.)")
    username = models.TextField(max_length=100, blank=True, null=True, 
                                help_text="(Optional)")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
                             blank=True, null=True)
    comments = models.TextField()
    review_date_time = models.DateTimeField(auto_now_add=True)
    # 
    # 
    def save(self, *args, **kwargs):
        # If the review is tied to a registered user but no username is entered, 
        # set it automatically.
        if (not self.username and self.user):
            self.username = self.user.username
        super().save(*args, **kwargs)
    #
    #
    def __str__(self):
        submitted_by = f"{self.first_name} {self.last_name}"
        username_info = f"Username: ({self.username})" if self.username else ""

        return f"""Review submitted by:\n
        {'-' * 20}\n
        {submitted_by}, {username_info}\n
        Email: {self.email},
        On: {self.review_date_time},
        Comments:\n
        {'-' * 10}\n
        {self.comments}"""
## END class Review aka Feedback
