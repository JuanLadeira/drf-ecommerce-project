from django.db import models


class ActiveQueryset(models.QuerySet):
    def isactive(self):
        return self.filter(is_active=True)
