from behave import *
import time


@given(u'the user access worlds best app')
def go_to_url(context):
    context.browser.get('https://sprinkle-burn.glitch.me/')


@when(u'the user enters username')
def enter_username(context):
    context.browser.find_element_by_name('email').send_keys('test@drugdev.com')


@when(u'the user enters password')
def enter_password(context):
    context.browser.find_element_by_name('password').send_keys('supers3cret')


@when(u'clicks Login')
def click_login_button(context):
    context.browser.find_element_by_xpath('//button[contains(text(),"Login")]').click()


@then(u'the user is presented with a welcome message')
def welcome_message(context):
    time.sleep(2)
    elem = context.browser.find_elements_by_xpath('/html/body/article')
    for welcomeText in elem:
        text = welcomeText.text
        assert "Welcome Dr I Test" == text


@when(u'the user has the incorrect credentials')
def enter_wrong_credentials(context):
    context.browser.find_element_by_name('email').send_keys('test@drugdev.co')
    context.browser.find_element_by_name('password').send_keys('supers')
    

@when(u'the user has correct username and incorrect password')
def enter_wrong_credentials(context):
    context.browser.find_element_by_name('email').send_keys('test@drugdev.com')
    context.browser.find_element_by_name('password').send_keys('supers')

@when(u'the user has correct username and no password')
def enter_only_username(context):
    context.browser.find_element_by_name('email').send_keys('test@drugdev.com')

@when(u'the user has no username and correct password')
def enter_only_password(context):
    context.browser.find_element_by_name('password').send_keys('supers3cret')

@when(u'the user has blank credentials')
def enter_no_credentials(context):
    context.browser.find_element_by_name('email').send_keys('')
    context.browser.find_element_by_name('password').send_keys('')


@then(u'the user is presented with an error message')
def error_message(context):
    time.sleep(2)
    elem = context.browser.find_element_by_xpath('//*[@id="login-error-box"]')
    welcomeText = elem.text
    print (welcomeText)
    assert "Credentials are incorrect" == welcomeText

    
