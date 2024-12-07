import requests
from rest_framework.exceptions import ValidationError


def positive_validator(number: float):
    if number < 0:
        raise ValidationError('Salary must be more than 0!')


def breed_validator(breed: str):
    all_breads = list(map(lambda dog: dog['name'], requests.get('https://api.thecatapi.com/v1/breeds').json()))
    if breed not in all_breads:
        raise ValidationError('Unknown type of breed.')

