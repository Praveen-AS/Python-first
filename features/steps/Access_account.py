from behave import given,when,then
from helper.helper import Webdriver_reusable

@given('the user is able to launch the webpage URL')
def step_impl(context):
    set = Webdriver_reusable()
    set.launchweb('https://www1.bgo.bgdigitaltest.co.uk')
    set.closebrowser()



