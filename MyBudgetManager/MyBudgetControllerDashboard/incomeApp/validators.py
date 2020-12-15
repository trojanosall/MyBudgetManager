from django.core.validators import RegexValidator


result_validator = RegexValidator(
    r'^[0-9a-zA-Z!@#$%^&*(),.?":{}|<>|\s]*$', R'Only alphanumeric characters are allowed and (!#&@$%^*(),.?:{}|<>).')
