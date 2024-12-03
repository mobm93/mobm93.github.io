from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.preloader = (By.CSS_SELECTOR, ".preloader")
        self.page_element = (By.CSS_SELECTOR, ".page")
        self.toggle_button = (By.CSS_SELECTOR, ".toggle-button")
        self.body_tag = (By.TAG_NAME, "body")
        self.mobile_header = (By.CSS_SELECTOR, ".mobile-header")
        self.arrow_svg_wrapper = (By.CSS_SELECTOR, '.arrow-svg-wrapper')

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    

    def wait_for_element_to_be_invisible(self, locator, timeout=30):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def get_page_title(self):
        return self.driver.title
    
    
    def wait_for_element_to_be_visible(self, element_locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(element_locator)
        )

    def scroll_page(self, y_offset):
        self.driver.execute_script(f"window.scrollBy(0, {y_offset});")

    

    def get_theme(self):
        return self.driver.find_element(*self.body_tag).get_attribute("class")
    
    def svg_opacity(self):
        # Wait until the opacity is 1 before checking the value
        WebDriverWait(self.driver, 10).until(
        lambda driver: driver.find_element(*self.arrow_svg_wrapper).value_of_css_property("opacity") == "1"
        )
        return True  # Return True if the opacity is 1, indicating the element is fully visible

    

    def toggle_theme(self):
        self.driver.find_element(*self.toggle_button).click()

    def is_mobile_header_displayed(self):
        return self.driver.find_element(*self.mobile_header).is_displayed()
