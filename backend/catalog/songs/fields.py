from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from catalog.songs.utils import (  # isort: skip
    get_error_message_max_validator,
    get_error_message_min_validator
)


class ValidatePositiveSmallIntegerField(models.PositiveSmallIntegerField):

    def __init__(self, *args, **kwargs) -> None:
        min = kwargs.pop('min_value', 0)
        max = kwargs.pop('max_value', 32767)
        kwargs['validators'] = (
            MinValueValidator(
                limit_value=min,
                message=get_error_message_min_validator(min)
            ),
            MaxValueValidator(
                limit_value=max,
                message=get_error_message_max_validator(max)
            ),
        )
        super().__init__(*args, **kwargs)
