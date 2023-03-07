import allure
from schemas.user import *
from pytest_voluptuous import S


def test_create_user(reqres):
    name = 'Chev'
    job = 'leader'
    with allure.step('create_user'):
        create_user = reqres.post('api/users', {'name': name, 'job': job})

        assert create_user.status_code == 201
        assert create_user.json() == S(create_single_user)
        assert create_user.json()['name'] == name
        assert create_user.json()['job'] == job


def test_update_user(reqres):
    update_name = 'morpheus'
    update_job = 'follower'
    with allure.step('update_name'):
        update_user = reqres.put('api/users/2', {'name': update_name, 'job': update_job})

        assert update_user.status_code == 200
        assert update_user.json() == S(update_single_user)
        assert update_user.json()['name'] == update_name
        assert update_user.json()['job'] == update_job


def test_register_successful(reqres):
    email = 'eve.holt@reqres.in'
    password = 'pistol'
    with allure.step('register_successful'):
        register_successful = reqres.post('api/register', {'email': email, 'password': password})

        assert register_successful.status_code == 200
        assert register_successful.json()['id'] == 4
        assert register_successful.json()['token'] == 'QpwL5tke4Pnpja7X4'


def test_register_unsuccessful(reqres):
    email = 'sydney@fife'
    password = 'pistol'
    with allure.step('register_unsuccessful'):
        register_unsuccessful = reqres.post('api/register', {'email': email, 'password': password})

        assert register_unsuccessful.status_code == 400


def test_delete_user(reqres):
    with allure.step('delete user'):
        delete_user = reqres.delete('api/users/2')

        assert delete_user.status_code == 204
