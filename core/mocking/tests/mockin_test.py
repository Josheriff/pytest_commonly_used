import pytest
from unittest.mock import MagicMock
import requests

from core.mocking.mockin import get_pokemons_number

POKEMONS_NUMBER = 964 # In the moment of this test are 964 pokemons in the api

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