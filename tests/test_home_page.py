import time
import pytest
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver


from pages.home_page import HomePage
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pages')))

@pytest.fixture(scope="module")
def setup():
    geckodriver_path = r"C:\Users\Alpha1\Downloads\geckodriver.exe"
    options = Options()
    options.add_argument('--enable-logging')
    options.headless = False
    options.set_preference("devtools.console.stdout.content", True)
    service = Service(geckodriver_path)
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_home_page_loads_correctly(setup):
    driver = setup
    driver.get("https://mobm93.github.io")  # Replace with your actual 3.js website URL

    # Initialize the HomePage object
    home_page = HomePage(driver)

    # Wait for preloader to be visible
    home_page.wait_for_element_to_be_visible(home_page.preloader)
    print(".preloader is visible.")

    # Wait for preloader to disappear (page load completion)
    home_page.wait_for_element_to_be_invisible(home_page.preloader)
    print(".preloader is now invisible.")

    # Wait for the main page element to be visible
    page_element = home_page.page_element
    print(".page is visible.")
    assert page_element is not None, "Main page element not found"
  

    # Scroll down by 300px using ActionChains
    time.sleep(7)
    # 10 sec wait
    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element(By.CSS_SELECTOR,'.page')).perform()
    actions.scroll_by_amount(0, 600).perform()
    print("Scrolled down 300px.")
    time.sleep(9)
    

    # Scroll down to the bottom of the page
    home_page.svg_opacity()  # Wait for the opacity of the SVG to become 1
    print("SVG opacity is 1, ready for interaction.")
    home_page.scroll_page(3000)  # Scroll by 3000px
    assert driver.execute_script("return window.scrollY;") > 0, "Page did not scroll down"

    # Scroll back to the top
    home_page.scroll_page(-3000)
    assert driver.execute_script("return window.scrollY;") == 0, "Page did not scroll back to the top"

    # Verify the initial theme
    initial_theme = home_page.get_theme()
    print(f"Initial theme class: {initial_theme}")
    assert initial_theme in ["dark-theme", "light-theme"], f"Unexpected initial theme class: {initial_theme}"

    # Toggle theme and verify the change
    home_page.toggle_theme()
    updated_theme = home_page.get_theme()
    print(f"Updated theme class: {updated_theme}")
    assert initial_theme != updated_theme, f"Theme did not change. Initial: {initial_theme}, Updated: {updated_theme}"

    # Check if the page title is correct
    title = home_page.get_page_title()
    assert title == "Muhammad Osama - Portfolio", f"Expected 'Muhammad Osama - Portfolio', but got {title}"

    # Test for mobile responsiveness by switching to mobile viewport
    driver.set_window_size(375, 812)  # iPhone X dimensions
    try:
        assert home_page.is_mobile_header_displayed(), "Mobile header is not displayed"
    except Exception as e:
        print(f"Mobile view test failed: {e}")
