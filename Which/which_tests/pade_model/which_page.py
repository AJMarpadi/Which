

from Which.which_tests.Locators.Locators_which import WhichLocators


class WebPage:
    def __init__(self):
        self.driver = driver

    def URL(self):
        return 'https://www.which.co.uk/reviews/televisions'

    def BestBuys(self):
        return self.driver.find_element(*WhichLocators.BestBuy)

    def DontBuy(self):
        return self.driver.find_element(*WhichLocators.DontBuy)

    def ScreenSize(self):
        return self.driver.find_element(*WhichLocators.ScreenSize)

    def Brand(self):
        return self.driver.find_element(*WhichLocators.Brand)



