from typing import Any
from django.db import models
from django.core import checks
from django.db.models import Model
from django.core.exceptions import ObjectDoesNotExist


class OrderField(models.PositiveIntegerField):
    description = "Ordering Field on a unique field"

    def __init__(self, unique_for_field=None, *args: Any, **kwargs: Any) -> None:
        self.unique_for_field = unique_for_field
        super().__init__(*args, **kwargs)


    def check(self, **kwargs: Any) -> list:
        return [
            *super().check(**kwargs), 
            *self._check_for_field_attribute(**kwargs),
        ]
    
    def _check_for_field_attribute(self, **kwargs: Any) -> list:
        if self.unique_for_field is None:
            return [
                checks.Error("OrderField must have a unique_for_field attribute", obj=self)
            ]
        elif self.unique_for_field not in [field.name for field in self.model._meta.get_fields()]:
            return [
                checks.Error(
                    f"OrderField has invalid unique_for_field attribute: {self.unique_for_field}",
                    obj=self,
                )
            ]
        return []
    

    def pre_save(self, model_instance: Model, add: bool) -> Any:
        if getattr(model_instance, self.attname) is None:
            qs = self.model.objects.all()
            try:
                query = {self.unique_for_field: getattr(model_instance, self.unique_for_field)}
                qs = qs.filter(**query)
                last_item = qs.latest(self.attname)
                value = last_item.order + 1
            except ObjectDoesNotExist:
                value = 1
            setattr(model_instance, self.attname, value)
        return super().pre_save(model_instance, add)