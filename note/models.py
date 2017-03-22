from django.db import models


class Note(models.Model):
    title = models.TextField(max_length=255)
    text = models.TextField()

    user_created = models.IntegerField()
    time_created = models.DateTimeField()
    user_modified = models.IntegerField()
    time_modified = models.DateTimeField()

    class Meta:
        db_table = 'tbl_note'
