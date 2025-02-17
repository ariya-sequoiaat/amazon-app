import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class TestAmazonScraper:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Setup method that runs before each test"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()

    def test_amazon_homepage_loads(self):
        """Test that Amazon homepage loads successfully"""
        self.driver.get("https://www.amazon.in/")
        assert "Amazon" in self.driver.title
        assert self.driver.current_url == "https://www.amazon.in/"

    def test_search_functionality(self):
        """Test the search functionality"""
        self.driver.get("https://www.amazon.in/")

        # Find and use search box
        search_box = self.wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        search_box.send_keys("Laptop")
        search_box.send_keys(Keys.RETURN)

        # Verify search results appear
        results = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
        ))
        assert results is not None

    def test_sort_by_rating(self):
        """Test sorting functionality by customer review"""
        self.driver.get("https://www.amazon.in/")

        # Search for an item
        search_box = self.wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        search_box.send_keys("Laptop")
        search_box.send_keys(Keys.RETURN)

        # Wait for results and sort button
        self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
        ))

        # Click sort button
        sort_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//span[text()="Sort by:"]')
        ))
        sort_button.click()

        # Click rating option
        rating_option = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//a[contains(text(), "Avg. Customer Review")]')
        ))
        rating_option.click()

        # Verify results are reloaded
        self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
        ))

        # Allow time for sorting to complete
        time.sleep(2)
        assert True  # If we got here without exceptions, test passes

    def test_find_non_sponsored_product(self):
        """Test finding first non-sponsored product"""
        self.driver.get("https://www.amazon.in/")

        # Search for an item
        search_box = self.wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        search_box.send_keys("Laptop")
        search_box.send_keys(Keys.RETURN)

        # Wait for results
        self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
        ))

        # Find products
        products = self.driver.find_elements(By.CSS_SELECTOR, '[data-component-type="s-search-result"]')

        # Find first non-sponsored product
        best_product_url = None
        for product in products:
            is_sponsored = product.find_elements(By.XPATH, ".//span[contains(text(), 'Sponsored')]")
            if not is_sponsored:
                best_product_url = product.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                break

        assert best_product_url is not None
        assert "amazon.in" in best_product_url

    def test_add_to_cart_button_presence(self):
        """Test that add to cart button is present on product page"""
        self.driver.get("https://www.amazon.in/")

        # Search and get to a product page
        search_box = self.wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        search_box.send_keys("Laptop")
        search_box.send_keys(Keys.RETURN)

        # Wait for results and get first non-sponsored product
        self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
        ))

        products = self.driver.find_elements(By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
        best_product_url = None
        for product in products:
            is_sponsored = product.find_elements(By.XPATH, ".//span[contains(text(), 'Sponsored')]")
            if not is_sponsored:
                best_product_url = product.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                break

        assert best_product_url is not None

        # Go to product page
        self.driver.get(best_product_url)

        # Check for various possible add to cart button selectors
        add_to_cart_selectors = [
            (By.XPATH, '//div[@class="a-section a-spacing-none a-padding-none"]//input[@id="add-to-cart-button"]'),
            (By.ID, 'add-to-cart-button'),
            (By.NAME, 'submit.add-to-cart')
        ]

        button_found = False
        for selector_type, selector in add_to_cart_selectors:
            try:
                self.wait.until(EC.presence_of_element_located((selector_type, selector)))
                button_found = True
                break
            except TimeoutException:
                continue

        assert button_found, "No Add to Cart button found with any of the expected selectors"

    def test_error_handling(self):
        """Test error handling for invalid search"""
        self.driver.get("https://www.amazon.in/")

        # Search with invalid characters
        search_box = self.wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        search_box.send_keys("@#$%^&*()")
        search_box.send_keys(Keys.RETURN)

        # Verify we're still on Amazon (even if no results found)
        assert "Amazon" in self.driver.title