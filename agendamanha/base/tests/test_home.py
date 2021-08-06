import pytest
from django.test import Client
from django.urls import reverse

from agendamanha.django_assertions import assert_contains


@pytest.fixture
def resp_home(client: Client):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp_home):
    assert resp_home.status_code == 200


def test_home_titulo(resp_home):
    assert_contains(resp_home, '<title>Agenda manhã!</title>')


def test_home_link(resp_home):
    assert_contains(resp_home, f'href="{reverse("base:home")}">Home</a>')
