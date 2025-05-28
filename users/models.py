from django.contrib.auth.models import AbstractUser
# from django.core.exceptions import ValidationError
# from django.core.files.images import get_image_dimensions
from django.db import models
from django.urls import reverse

## Commenting out Avatar code for now because it's not part of the Final Project instructions.
####  If I have time, I'll add it back in.
# def validate_avatar(img):
#     width, height = get_image_dimensions(img)
#     if(width > 200 or height > 200):
#         raise ValidationError("Avatar/profile pic must be no larger than 200 x 200 pixels.")
#     return  ## Former college prof convention to mark the end of the methods in Python 


class CustomUser(AbstractUser):
    joined = models.DateTimeField(verbose_name="Date Joined", auto_now_add=True, blank=True, null=True)
    birthdate = models.DateField(null=True, blank=True)
    # avatar = models.ImageField(upload_to="avatars/", blank=True, null=True, 
    #                            help_text="Must be a jpg, jpeg, jfif, or png no larger than 200 x 200px.", 
    #                            validators=[validate_avatar])
    #
    #
    def get_absolute_url(self):
        return reverse('my-account')
    #
    #
    def __str__(self):
        return f"{self.first_name} {self.last_name}, Username: {self.username}, Date Joined: {self.joined}"