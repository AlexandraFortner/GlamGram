from django.db import models


class Photo(models.Model):
    photo = models.ImageField(upload_to="app/static/app/images")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def image_url(self):
        return self.photo.url[len('app/static/'):]