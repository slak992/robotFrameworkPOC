from robot.api.deco import library, keyword
from robot.libraries.BuiltIn import BuiltIn


@library
class Cart():
    def __init__(self):
        self.seleLib = BuiltIn().get_library_instance("SeleniumLibrary")
    @keyword
    def verify_elements_in_the_cart(self,expected_list,continue_order=False):
        self.seleLib.click_element("//a[contains(text(),'Checkout')]")
        self.seleLib.wait_until_element_is_visible("//button[contains(text(), 'Checkout')]")
        cart_items=[]
        cart_added_items_webele = self.seleLib.get_webelements("//h4[@class='media-heading']/a")
        for item in cart_added_items_webele:
            cart_items.append(self.seleLib.get_text(item))
        print(expected_list)
        print(cart_items)
        print(expected_list==cart_items)
        if  continue_order:
            self.seleLib.click_button("//button[contains(text(),'Checkout')]")

