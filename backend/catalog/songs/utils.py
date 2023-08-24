from django.utils.translation import gettext_lazy as _


def get_help_text_required_max_chars(max_chars):
    return _(
        'Required. %(max_chars)s characters or fewer.'
    ) % {'max_chars': max_chars}

def get_error_message_min_validator(min_value):
    return _(
        'Value can not be less than %(min_value)s.'
    ) % {'min_value': min_value}

def get_error_message_max_validator(max_value):
    return _(
        'Value can not be more than %(max_value)s.'
    ) % {'max_value': max_value}
