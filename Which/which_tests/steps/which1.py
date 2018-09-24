from behave import *
from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

from Which.which_tests.pade_model import which_page

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

use_step_matcher('re')  # This allows the steps to receive arguments from the scenario


@given('I have the URL')
def step_impl(context):
    context.driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    context.driver.get('https://www.which.co.uk/reviews/televisions')
    context.driver.maximize_window()


@then('The website should load successfully')
def step_impl(context):
    expected_url = 'https://www.which.co.uk/reviews/televisions'
    assert context.driver.current_url == expected_url


''''@given('I have the URL')
def step_impl(context):
    context.browser = webdriver.Chrome("/usr/local/bin/chromedriver")
    context.browser.get('https://www.which.co.uk/reviews/televisions')'''''


@when('I click on Best Buys')
def step_impl(context):
    from Which.which_tests.Locators.Locators_which import WhichLocators
    #context.driver.find_element(*WhichLocators.BestBuy).click()
    context.driver.find_element_by_link_text('Best Buys (52)').click()


@then('The page should display Best Buy items')
def step_impl(context):
    expected_url1 = 'https://www.which.co.uk/reviews/televisions/article/recommendations/which-best-buy-televisions'
    assert context.driver.current_url == expected_url1


@when('I click on Dont Buys')
def step_impl(context):
    from Which.which_tests.Locators.Locators_which import WhichLocators
    context.driver.find_element_by_link_text("Don't Buys (22)").click()



@then('The page should display the dont buy content')
def step_impl(context):
    expected_url2 = 'https://www.which.co.uk/reviews/televisions/article/recommendations/which-dont-buy-televisions'
    assert context.driver.current_url == expected_url2


@when('I click on the different Screen size')
def step_impl(context):
    from Which.which_tests.Locators.Locators_which import WhichLocators
    context.driver.find_element_by_id("screen_size_20_28").click()
    context.driver.implicit_wait(10)


@then('The page should display the Screen Size content')
def step_impl(context):
    expected_URL3 = 'https://www.which.co.uk/reviews/televisions/search?search[range][screen_size][Screen_size][]=20-28&sortby=testing_date_desc&page=1'
    assert context.driver.current_url == expected_URL3


@when('I select a brand')
def step_impl(context):
    from Which.which_tests.Locators.Locators_which import WhichLocators
    context.driver.find_element(*WhichLocators.Brand).click()
    context.driver.implicit_wait(3)


@then('he page should display the selected brands')
def step_impl(context):
    expected_URL4 = 'https://www.which.co.uk/reviews/televisions/samsung/brand'
    assert context.driver.current_url == expected_URL4
