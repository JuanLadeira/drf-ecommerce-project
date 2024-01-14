from django.db import models


class IsActiveQueryset(models.QuerySet):
    def is_active(self):
        return self.filter(is_active=True)
