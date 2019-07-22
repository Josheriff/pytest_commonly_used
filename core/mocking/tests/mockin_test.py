import pytest
from unittest.mock import MagicMock
import requests
import json

from core.mocking.mockin import get_pokemons_number

POKEMONS_NUMBER = 964 # In the moment of this test are 964 pokemons in the api

class MockResponse(object):
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

def test_get_pokemons_number():
    pokemons_number = get_pokemons_number(requests)

    assert pokemons_number == POKEMONS_NUMBER

def test_collaboration():
    request_mock = MagicMock()

    get_pokemons_number(request_mock)

    assert request_mock.get.called


def test_collaboration_with_argument():
    request_mock = MagicMock()

    get_pokemons_number(request_mock)

    assert request_mock.get.called_with('https://pokeapi.co/api/v2/pokemon')


def test_collaboration_called_once():
    request_mock = MagicMock()

    get_pokemons_number(request_mock)

    assert request_mock.get.called_once()

#
#   IMPORTANT NOTE:
#
#   Here we are asserting that our mock method is what we expect
#   OF COURSE IT IS, thats why we are mocking it.
#   THIS TEST it's only to whow how to "fake" a request answer
#   Usually you will have to do something with that answer, and that is:
#   WHAT YOU HAVE TO TEST == SUT (subject under test)
#
#   SUT never can be a MOCK.
#

def test_collaboration_with_return():
    request_mock = MagicMock()
    pokemon_json = MockResponse({'count':1}, 200)
    request_mock.get.return_value = pokemon_json

    mocked_result = get_pokemons_number(request_mock)

    assert mocked_result == 1