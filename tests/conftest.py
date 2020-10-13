# coding: utf-8
"""Configurations for py.tests runner"""
import pytest
from ctrlibrary.core import settings
from ctrlibrary.threatresponse import token
from tests.dataset import observables


def pytest_collection_modifyitems():
    if not settings.configured:
        settings.configure()
    return settings


@pytest.fixture(scope='module')
def module_token():
    return token.request_token(
        settings.server.ctr_client_id, settings.server.ctr_client_password)


@pytest.fixture(scope='module')
def module_headers(module_token):
    return {'Authorization': 'Bearer {}'.format(module_token)}


@pytest.fixture(scope='module', params=observables)
def observables(request):
    return request.param
