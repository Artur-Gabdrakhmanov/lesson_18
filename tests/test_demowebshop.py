'''import allure
from selene import have
from selene.support.shared import browser

Login = 'ChevChelios@gu.ru'
Password = '123456'
url = 'https://demowebshop.tricentis.com/'
browser.config.base_url = url


def test_login():
    with allure.step('Открытие страницы авторизации'):
        browser.open('/login')

    with allure.step('Ввод логина и пароля'):
        browser.element('#Email').send_keys(Login)
        browser.element('#Password').send_keys(Password).press_enter()

    with allure.step('Подтверждение успешной авторизации'):
        browser.element('.account').should(have.text(Login))
'''

from selene import have
import allure


def test_auth(app):
    app.open('')
    with allure.step('Verification of successful authorization'):
        app.element(".account").should(have.text("ChevChelios@gu.ru"))


def test_filling_cart(demoshop, app):
    app.open('')
    with allure.step('Added cart'):
        demoshop.post('/addproducttocart/catalog/31/1/1')
    with allure.step('Filling the cart'):
        app.element('.ico-cart').click()
        app.element('.product-name').should(have.text('14.1-inch Laptop'))


def test_delete_product_from_cart(demoshop, app):
    with allure.step('Remove cart'):
        app.element('.ico-cart').click()
        app.element('[name="removefromcart"]').click()
        app.element('[name="updatecart"]').click()
        app.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))


def test_search_box(demoshop, app):
    app.open('')
    with allure.step('Checking the search'):
        app.element('.search-box-text').type('00000').press_enter()
    with allure.step('Filling the cart'):
        app.element('.result').should(have.text('No products were found that matched your criteria.'))


def test_logout(app):
    app.open("")
    with allure.step('Checking the logout'):
        app.element('.ico-logout').click()
        app.element('.ico-login').should(have.text('Log in'))
