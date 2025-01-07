from robot.api.deco import library, keyword
from robot.libraries.BuiltIn import BuiltIn


@library
class Shop():
    def __init__(self):
        self.seleLib = BuiltIn().get_library_instance("SeleniumLibrary")
    @keyword
    def add_items_to_the_cart(self,product_list):
        products_webelement = self.seleLib.get_webelements("//h4[@class='card-title']")
        i = 1
        for each_product in products_webelement:
            title = self.seleLib.get_text(each_product)
            if title in product_list:
                self.seleLib.click_element("(//div[@class='card-footer'])["+str(i)+"]/button")
            i+=1

