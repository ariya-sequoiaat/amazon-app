import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Input from user
item = input("Enter the item you want to buy: ")

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()

# Define Explicit Wait
wait = WebDriverWait(driver, 10)

# Locate the search box, enter the item, and press Enter
search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
search_box.send_keys(item)
search_box.send_keys(Keys.RETURN)

# Wait for results to load
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-component-type="s-search-result"]')))

# Locate and click the sorting button
sort_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Sort by:"]')))
sort_button.click()

# Click "Avg. Customer Review"
rating_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Avg. Customer Review")]')))
rating_option.click()

# Wait for sorted results to load
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-component-type="s-search-result"]')))

# Find top-rated product (ignoring sponsored items)
products = driver.find_elements(By.CSS_SELECTOR, '[data-component-type="s-search-result"]')

best_product_url = None

for product in products:
    is_sponsored = product.find_elements(By.XPATH, ".//span[contains(text(), 'Sponsored')]")
    if not is_sponsored:
        best_product_url = product.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        break  # Stop after finding the first non-sponsored product

# Open the product page
if best_product_url:
    driver.get(best_product_url)
    print(f"Opening Product Page: {best_product_url}")

    # Wait for the "Add to Cart" button to appear and ensure it's clickable
    try:
        # Wait for the button to be clickable
        #add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="a-section a-spacing-none a-padding-none"]//input[@id="add-to-cart-button"]//input[@id='add-to-cart-button-ubb']')))
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, '''//div[@class='a-section a-spacing-none a-padding-none']//input[@id='add-to-cart-button']''')))
        add_to_cart_button.click()
        print("✅ Product added to cart!")
    except Exception as e:
        print("⚠ Unable to add product to cart:", str(e))

else:
    print("❌ No product found.")

# Keep the browser open for user to review
input("Press Enter to exit...")
driver.quit()





# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# # Input from user
# item = input("Enter the item you want to buy: ")
#
# # Initialize WebDriver
# driver = webdriver.Chrome()
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
#
# # Define Explicit Wait
# wait = WebDriverWait(driver, 10)
#
# # Locate the search box, enter the item, and press Enter
# search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
# search_box.send_keys(item)
# search_box.send_keys(Keys.RETURN)
#
# # Wait for results to load
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-component-type="s-search-result"]')))
#
# # Locate and click the sorting button
# sort_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Sort by:"]')))
# sort_button.click()
#
# # Click "Avg. Customer Review"
# rating_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Avg. Customer Review")]')))
# rating_option.click()
#
# # Wait for sorted results to load
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-component-type="s-search-result"]')))
#
# # Find top-rated product (ignoring sponsored items)
# products = driver.find_elements(By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
#
# best_product_url = None
#
# for product in products:
#     is_sponsored = product.find_elements(By.XPATH, ".//span[contains(text(), 'Sponsored')]")
#     if not is_sponsored:
#         best_product_url = product.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
#         break  # Stop after finding the first non-sponsored product
#
# # Open the product page
# if best_product_url:
#     driver.get(best_product_url)
#     print(f"Opening Product Page: {best_product_url}")
#
#     # Wait for the "Add to Cart" button to appear
#     try:
#         # Wait until the "Add to Cart" button is visible and clickable
#         add_to_cart_button = wait.until(EC.visibility_of_element_located((By.ID, 'add-to-cart-button')))
#
#         # Scroll into view if necessary (if the button is outside the viewport)
#         driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
#
#         # Wait a bit for the scroll to complete
#         time.sleep(1)
#
#         # Click the "Add to Cart" button
#         add_to_cart_button.click()
#         print("✅ Product added to cart!")
#     except Exception as e:
#         print("⚠ Unable to add product to cart:", str(e))
#
# else:
#     print("❌ No product found.")
#
# # Keep the browser open for user to review
# input("Press Enter to exit...")
# driver.quit()


# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# # Input from user
# item = input("Enter the item you want to buy: ")
#
# # Initialize WebDriver
# driver = webdriver.Chrome()
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
#
# # Define Explicit Wait
# wait = WebDriverWait(driver, 10)
#
# # Locate the search box, enter the item, and press Enter
# search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
# search_box.send_keys(item)
# search_box.send_keys(Keys.RETURN)
#
# # Wait for results to load
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-component-type="s-search-result"]')))
#
# # Locate and click the sorting button
# sort_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Sort by:"]')))
# sort_button.click()
#
# # Click "Avg. Customer Review"
# rating_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Avg. Customer Review")]')))
# rating_option.click()
#
# # Wait for sorted results to load
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-component-type="s-search-result"]')))
#
# # Find top-rated product (ignoring sponsored items)
# products = driver.find_elements(By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
#
# best_product_url = None
#
# for product in products:
#     is_sponsored = product.find_elements(By.XPATH, ".//span[contains(text(), 'Sponsored')]")
#     if not is_sponsored:
#         best_product_url = product.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
#         break  # Stop after finding the first non-sponsored product
#
# # Open the product page
# if best_product_url:
#     driver.get(best_product_url)
#     print(f"Opening Product Page: {best_product_url}")
#
#     # Wait for the product page to fully load and the "Add to Cart" button to be clickable
#     try:
#         # Wait until the "Add to Cart" button becomes visible and clickable (in the viewport)
#         add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#add-to-cart-button')))
#         add_to_cart_button.click()
#         print("✅ Product added to cart!")
#     except Exception as e:
#         print("⚠ Unable to add product to cart:", str(e))
#
# else:
#     print("❌ No product found.")
#
# # Keep the browser open for user to review
# input("Press Enter to exit...")
# driver.quit()






















# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# # Input from user
# item = input("Enter the item you want to buy: ")
#
# # Initialize WebDriver
# driver = webdriver.Chrome()
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
#
# # Define Explicit Wait
# wait = WebDriverWait(driver, 10)
#
# # Locate the search box, enter the item, and press Enter
# search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
# search_box.send_keys(item)
# search_box.send_keys(Keys.RETURN)
#
# # Wait for results to load
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-component-type="s-search-result"]')))
#
# # Locate and click the sorting button
# sort_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Sort by:"]')))
# sort_button.click()
#
# # Click "Avg. Customer Review"
# rating_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Avg. Customer Review")]')))
# rating_option.click()
#
# # Wait for sorted results to load
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-component-type="s-search-result"]')))
#
# # Find top-rated product (ignoring sponsored items)
# products = driver.find_elements(By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
#
# best_product_url = None
#
# for product in products:
#     is_sponsored = product.find_elements(By.XPATH, ".//span[contains(text(), 'Sponsored')]")
#     if not is_sponsored:
#         best_product_url = product.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
#         break  # Stop after finding the first non-sponsored product
#
# # Open the product page
# if best_product_url:
#     driver.get(best_product_url)
#     print(f"Opening Product Page: {best_product_url}")
#
#     # Wait for the "Add to Cart" button to appear and ensure it's clickable
#     try:
#         # Wait for the button to be clickable
#         add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, '''//div[@class='a-section a-spacing-none a-padding-none']//input[@id='add-to-cart-button']"''')))
#         add_to_cart_button.click()
#         print("✅ Product added to cart!")
#     except Exception as e:
#         print("⚠ Unable to add product to cart:", str(e))
#
# else:
#     print("❌ No product found.")
#
# # Keep the browser open for user to review
# input("Press Enter to exit...")
# driver.quit()





















# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
# import time
#
# def wait_and_find_element(driver, by, value, timeout=10, click=False):
#     """Utility function to wait for and find an element with better error handling"""
#     try:
#         element = WebDriverWait(driver, timeout).until(
#             EC.presence_of_element_located((by, value))
#         )
#         if click and element.is_displayed() and element.is_enabled():
#             time.sleep(1)
#             element.click()
#         return element
#     except TimeoutException:
#         print(f"⚠ Timeout waiting for element: {value}")
#         return None
#
# # Input from user
# item = input("Enter the item you want to buy: ")
#
# # Initialize WebDriver with options
# options = webdriver.ChromeOptions()
# options.add_argument('--start-maximized')
# options.add_argument('--disable-blink-features=AutomationControlled')
# driver = webdriver.Chrome(options=options)
# driver.get("https://www.amazon.in/")
#
# # Define Explicit Wait
# wait = WebDriverWait(driver, 10)
#
# # Search for item
# search_box = wait_and_find_element(driver, By.ID, "twotabsearchtextbox")
# if search_box:
#     search_box.send_keys(item)
#     search_box.send_keys(Keys.RETURN)
# else:
#     print("❌ Could not find search box")
#     driver.quit()
#     exit(1)
#
# # Wait for results to load
# results = wait_and_find_element(driver, By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
# if not results:
#     print("❌ No search results found")
#     driver.quit()
#     exit(1)
#
# # Find top-rated product (ignoring sponsored items)
# products = driver.find_elements(By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
# best_product_url = None
#
# for product in products:
#     try:
#         is_sponsored = product.find_elements(By.XPATH, ".//span[contains(text(), 'Sponsored')]")
#         if not is_sponsored:
#             best_product_url = product.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
#             break
#     except NoSuchElementException:
#         continue
#
# # Open the product page
# if best_product_url:
#     driver.get(best_product_url)
#     print(f"Opening Product Page: {best_product_url}")
#
#     #Try multiple possible selectors for Add to Cart button
#     cart_button_selectors = [(By. XPATH, '''//div[@class='a-section a-spacing-none a-padding-none']//input[@id='add-to-cart-button']")''')]
#     added_to_cart = False
#     for selector_type, selector_value in cart_button_selectors:
#         try:
#             print(f"Trying to find Add to Cart button with selector: {selector_value}")
#             add_to_cart_button = wait_and_find_element(driver, selector_type, selector_value, timeout=5, click=True)
#             if add_to_cart_button:
#                 print("✅ Product added to cart!")
#                 added_to_cart = True
#                 break
#         except Exception as e:
#             continue
#
#     if not added_to_cart:
#         print("⚠ Unable to add product to cart. The item might be unavailable or require variant selection.")
#         print("Attempting to find and print available buying options...")
#         try:
#             buying_options = driver.find_elements(By.CSS_SELECTOR, '#buybox-see-all-buying-choices, #buyNow, #buy-now-button')
#             if buying_options:
#                 print("Available buying options found but require manual interaction:")
#                 for option in buying_options:
#                     print(f"- {option.get_attribute('aria-label') or option.get_attribute('value') or option.text}")
#         except Exception as e:
#             print("No additional buying options found")
#
# else:
#     print("❌ No product found.")
#
# # Keep the browser open for user to review
# input("Press Enter to exit...")
# driver.quit()















# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
# import time
#
# def wait_and_find_element(driver, by, value, timeout=10, click=False):
#     """Utility function to wait for and find an element with better error handling"""
#     try:
#         element = WebDriverWait(driver, timeout).until(
#             EC.presence_of_element_located((by, value))
#         )
#         if click and element.is_displayed() and element.is_enabled():
#             # Wait a bit for any animations/overlays to clear
#             time.sleep(1)
#             element.click()
#         return element
#     except TimeoutException:
#         print(f"⚠ Timeout waiting for element: {value}")
#         return None
#
# def handle_variant_selection(driver):
#     """Handle product variants if they exist"""
#     try:
#         # Check for color options
#         color_options = driver.find_elements(By.CSS_SELECTOR, "#variation_color_name ul li")
#         if color_options:
#             print("Found color variants, selecting first available option...")
#             for option in color_options:
#                 if 'unavailable' not in option.get_attribute('class'):
#                     option.click()
#                     time.sleep(1)
#                     break
#
#         # Check for size options
#         size_options = driver.find_elements(By.CSS_SELECTOR, "#variation_size_name ul li")
#         if size_options:
#             print("Found size variants, selecting first available option...")
#             for option in size_options:
#                 if 'unavailable' not in option.get_attribute('class'):
#                     option.click()
#                     time.sleep(1)
#                     break
#
#         # Check for style options
#         style_options = driver.find_elements(By.CSS_SELECTOR, "#variation_style_name ul li")
#         if style_options:
#             print("Found style variants, selecting first available option...")
#             for option in style_options:
#                 if 'unavailable' not in option.get_attribute('class'):
#                     option.click()
#                     time.sleep(1)
#                     break
#
#     except Exception as e:
#         print(f"⚠ Error handling variants: {str(e)}")
#
# # Input from user
# item = input("Enter the item you want to buy: ")
#
# # Initialize WebDriver with options
# options = webdriver.ChromeOptions()
# options.add_argument('--start-maximized')
# options.add_argument('--disable-blink-features=AutomationControlled')
# driver = webdriver.Chrome(options=options)
# driver.get("https://www.amazon.in/")
#
# # Define Explicit Wait
# wait = WebDriverWait(driver, 10)
#
# # Search for item
# search_box = wait_and_find_element(driver, By.ID, "twotabsearchtextbox")
# if search_box:
#     search_box.send_keys(item)
#     search_box.send_keys(Keys.RETURN)
# else:
#     print("❌ Could not find search box")
#     driver.quit()
#     exit(1)
#
# # Wait for results to load
# results = wait_and_find_element(driver, By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
# if not results:
#     print("❌ No search results found")
#     driver.quit()
#     exit(1)
#
# # Try to sort by customer review
# try:
#     sort_button = wait_and_find_element(driver, By.XPATH, '//span[text()="Sort by:"]', click=True)
#     rating_option = wait_and_find_element(driver, By.XPATH, '//a[contains(text(), "Avg. Customer Review")]', click=True)
#     # Wait for sorted results
#     time.sleep(2)
# except Exception as e:
#     print("⚠ Could not sort by rating, continuing with default sort")
#
# # Find top-rated product (ignoring sponsored items)
# products = driver.find_elements(By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
# best_product_url = None
#
# for product in products:
#     try:
#         is_sponsored = product.find_elements(By.XPATH, ".//span[contains(text(), 'Sponsored')]")
#         if not is_sponsored:
#             best_product_url = product.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
#             break
#     except NoSuchElementException:
#         continue
#
# # Open the product page
# if best_product_url:
#     driver.get(best_product_url)
#     print(f"Opening Product Page: {best_product_url}")
#
#     # Handle any variant selections first
#     handle_variant_selection(driver)
#
#     # Try multiple possible selectors for Add to Cart button
#         cart_button_selectors = [
#         (By.ID, "add-to-cart-button"),
#         (By.NAME, "submit.add-to-cart"),
#         (By.TITLE, "Add to Shopping Cart"),
#         (By.CSS_SELECTOR, '[aria-label="Add to Cart"]'),
#         (By.XPATH, '//input[@class="a-button-input"]'),
#         (By.XPATH, '//span[contains(@class, "a-button-inner")]//input[@type="submit" and @title="Add to Cart"]'),
#         (By.CSS_SELECTOR, '#buybox-see-all-buying-choices .a-button-input'),  # For "See All Buying Options"
#         (By.CSS_SELECTOR, '#buyNow input[type="submit"]'),  # Buy Now button as fallback
#         (By.XPATH, '//span[contains(text(), "Add to Cart")]'),  # Text-based button
#         (By.CSS_SELECTOR, '#buy-now-button')  # Buy Now button
#     ]
#
#     added_to_cart = False
#     for selector_type, selector_value in cart_button_selectors:
#         try:
#             print(f"Trying to find Add to Cart button with selector: {selector_value}")
#             add_to_cart_button = wait_and_find_element(driver, selector_type, selector_value, timeout=5, click=True)
#             if add_to_cart_button:
#                 print("✅ Product added to cart!")
#                 added_to_cart = True
#                 break
#         except Exception as e:
#             continue
#
#     if not added_to_cart:
#         print("⚠ Unable to add product to cart. The item might be unavailable or require variant selection.")
#         print("Attempting to find and print available buying options...")
#         try:
#             buying_options = driver.find_elements(By.CSS_SELECTOR, '#buybox-see-all-buying-choices, #buyNow, #buy-now-button')
#             if buying_options:
#                 print("Available buying options found but require manual interaction:")
#                 for option in buying_options:
#                     print(f"- {option.get_attribute('aria-label') or option.get_attribute('value') or option.text}")
#         except Exception as e:
#             print("No additional buying options found")
#
# else:
#     print("❌ No product found.")
#
# # Keep the browser open for user to review
# input("Press Enter to exit...")
# driver.quit()
#
#
#
#
#
#
# # import selenium
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.common.exceptions import TimeoutException, NoSuchElementException
# # import time
# #
# # def wait_and_find_element(driver, by, value, timeout=10, click=False):
# #     """Utility function to wait for and find an element with better error handling"""
# #     try:
# #         element = WebDriverWait(driver, timeout).until(
# #             EC.presence_of_element_located((by, value))
# #         )
# #         if click:
# #             # Wait a bit for any animations/overlays to clear
# #             time.sleep(1)
# #             element.click()
# #         return element
# #     except TimeoutException:
# #         print(f"⚠ Timeout waiting for element: {value}")
# #         return None
# #
# # # Input from user
# # item = input("Enter the item you want to buy: ")
# #
# # # Initialize WebDriver with options
# # options = webdriver.ChromeOptions()
# # options.add_argument('--start-maximized')
# # options.add_argument('--disable-blink-features=AutomationControlled')
# # driver = webdriver.Chrome(options=options)
# # driver.get("https://www.amazon.in/")
# #
# # # Define Explicit Wait
# # wait = WebDriverWait(driver, 10)
# #
# # # Search for item
# # search_box = wait_and_find_element(driver, By.ID, "twotabsearchtextbox")
# # if search_box:
# #     search_box.send_keys(item)
# #     search_box.send_keys(Keys.RETURN)
# # else:
# #     print("❌ Could not find search box")
# #     driver.quit()
# #     exit(1)
# #
# # # Wait for results to load
# # results = wait_and_find_element(driver, By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
# # if not results:
# #     print("❌ No search results found")
# #     driver.quit()
# #     exit(1)
# #
# # # Try to sort by customer review
# # try:
# #     sort_button = wait_and_find_element(driver, By.XPATH, '//span[text()="Sort by:"]', click=True)
# #     rating_option = wait_and_find_element(driver, By.XPATH, '//a[contains(text(), "Avg. Customer Review")]', click=True)
# #     # Wait for sorted results
# #     time.sleep(2)
# # except Exception as e:
# #     print("⚠ Could not sort by rating, continuing with default sort")
# #
# # # Find top-rated product (ignoring sponsored items)
# # products = driver.find_elements(By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
# # best_product_url = None
# #
# # for product in products:
# #     try:
# #         is_sponsored = product.find_elements(By.XPATH, ".//span[contains(text(), 'Sponsored')]")
# #         if not is_sponsored:
# #             best_product_url = product.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
# #             break
# #     except NoSuchElementException:
# #         continue
# #
# # # Open the product page
# # if best_product_url:
# #     driver.get(best_product_url)
# #     print(f"Opening Product Page: {best_product_url}")
# #
# #     # Try multiple possible selectors for Add to Cart button
# #     cart_button_selectors = [
# #         (By.ID, "add-to-cart-button"),
# #         (By.NAME, "submit.add-to-cart"),
# #         (By.CSS_SELECTOR, '[aria-label="Add to Cart"]'),
# #         (By.XPATH, '//input[@value="Add to Cart"]'),
# #         (By.XPATH, '//span[contains(@class, "a-button-inner")]//input[@type="submit" and @title="Add to Cart"]')
# #     ]
# #
# #     added_to_cart = False
# #     for selector_type, selector_value in cart_button_selectors:
# #         try:
# #             add_to_cart_button = wait_and_find_element(driver, selector_type, selector_value, timeout=5, click=True)
# #             if add_to_cart_button:
# #                 print("✅ Product added to cart!")
# #                 added_to_cart = True
# #                 break
# #         except Exception as e:
# #             continue
# #
# #     if not added_to_cart:
# #         print("⚠ Unable to add product to cart. The item might be unavailable or the page structure might have changed.")
# #
# # else:
# #     print("❌ No product found.")
# #
# # # Keep the browser open for user to review
# # input("Press Enter to exit...")
# # driver.quit()
#
#
#
#
#
# # import selenium
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # import time
# #
# # # Input from user
# # item = input("Enter the item you want to buy: ")
# #
# # # Initialize WebDriver
# # driver = webdriver.Chrome()
# # driver.get("https://www.amazon.in/")
# # driver.maximize_window()
# #
# # # Define Explicit Wait
# # wait = WebDriverWait(driver, 10)
# #
# # # Locate the search box, enter the item, and press Enter
# # search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
# # search_box.send_keys(item)
# # search_box.send_keys(Keys.RETURN)
# #
# # # Wait for results to load
# # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-component-type="s-search-result"]')))
# #
# # # Locate and click the sorting button
# # sort_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Sort by:"]')))
# # sort_button.click()
# #
# # # Click "Avg. Customer Review"
# # rating_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Avg. Customer Review")]')))
# # rating_option.click()
# #
# # # Wait for sorted results to load
# # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-component-type="s-search-result"]')))
# #
# # # Find top-rated product (ignoring sponsored items)
# # products = driver.find_elements(By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
# #
# # best_product_url = None
# #
# # for product in products:
# #     is_sponsored = product.find_elements(By.XPATH, ".//span[contains(text(), 'Sponsored')]")
# #     if not is_sponsored:
# #         best_product_url = product.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
# #         break  # Stop after finding the first non-sponsored product
# #
# # # Open the product page
# # if best_product_url:
# #     driver.get(best_product_url)
# #     print(f"Opening Product Page: {best_product_url}")
# #
# #     # Wait for the "Add to Cart" button to appear and ensure it's clickable
# #     try:
# #         # Wait for the button to be clickable
# #         # Example using CSS Selector (aria-label)
# #         # add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Add to Cart"]')))
# #         add_to_cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[aria-label="Add to Cart"]')))
# #         add_to_cart_button.click()
# #         print("✅ Product added to cart!")
# #     except Exception as e:
# #         print("⚠ Unable to add product to cart:", str(e))
# #
# # else:
# #     print("❌ No product found.")
# #
# # # Keep the browser open for user to review
# # input("Press Enter to exit...")
# # driver.quit()
#
#
#
#
# # import selenium
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # import time
# #
# # # Input from user
# # item = input("Enter the item you want to buy: ")
# #
# # # Initialize WebDriver
# # driver = webdriver.Chrome()
# # driver.get("https://www.amazon.in/")
# # driver.maximize_window()
# #
# # # Define Explicit Wait
# # wait = WebDriverWait(driver, 10)
# #
# # # Locate the search box, enter the item, and press Enter
# # search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
# #
# # search_box.send_keys(item)
# # search_box.send_keys(Keys.RETURN)
# #
# # # Wait for results to load
# # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-component-type="s-search-result"]')))
# #
# # # Locate and click the sorting button
# # sort_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Sort by:"]')))
# # sort_button.click()
# #
# # # Click "Avg. Customer Review"
# # rating_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Avg. Customer Review")]')))
# # rating_option.click()
# #
# # # Wait for sorted results to load
# # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-component-type="s-search-result"]')))
# #
# # # Find top-rated product (ignoring sponsored items)
# # products = driver.find_elements(By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
# #
# # best_product_url = None
# #
# # for product in products:
# #     is_sponsored = product.find_elements(By.XPATH, ".//span[contains(text(), 'Sponsored')]")
# #     if not is_sponsored:
# #         best_product_url = product.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
# #         break  # Stop after finding the first non-sponsored product
# #
# # # Open the product page
# # if best_product_url:
# #     driver.get(best_product_url)
# #     print(f"Opening Product Page: {best_product_url}")
# #
# # # Wait for the "Add to Cart" button to appear
# # try:
# #     # Handle potential iframe issues (Switch to iframe if necessary)
# #     iframe_elements = driver.find_elements(By.TAG_NAME, "iframe")
# #     if iframe_elements:
# #         driver.switch_to.frame(iframe_elements[0])  # Switch to the first iframe
# #
# #     # Locate the "Add to Cart" button and wait for it to be clickable
# #     add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-button"]')))
# #
# #     # Click the "Add to Cart" button
# #     add_to_cart_button.click()
# #     print("✅ Product added to cart!")
# #
# # except Exception as e:
# #     print(f"⚠ Unable to add product to cart: {e}")
# #     print("🔴 There might be an issue with the Add to Cart button or iframe.")
# #
# # # Wait for user input to review the cart
# # input("Press Enter to exit...")
# #
# # # Close the browser
# # driver.quit()
#
#
#
# # import selenium
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # import time
# #
# # # Input from user
# # item = input("Enter the item you want to buy: ")
# #
# # # Initialize WebDriver
# # driver = webdriver.Chrome()
# # driver.get("https://www.amazon.in/")
# # driver.maximize_window()
# #
# # # Define Explicit Wait
# # wait = WebDriverWait(driver, 10)
# #
# # # Locate the search box, enter the item, and press Enter
# # search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
# # search_box.send_keys(item)
# # search_box.send_keys(Keys.RETURN)
# #
# # # Wait for results to load
# # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-component-type="s-search-result"]')))
# #
# # # Locate and click the sorting button
# # sort_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Sort by:"]')))
# # sort_button.click()
# #
# # # Click "Avg. Customer Review"
# # rating_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Avg. Customer Review")]')))
# # rating_option.click()
# #
# # # Wait for sorted results to load
# # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-component-type="s-search-result"]')))
# #
# # # Find top-rated product (ignoring sponsored items)
# # products = driver.find_elements(By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
# #
# # best_product_url = None
# #
# # for product in products:
# #     is_sponsored = product.find_elements(By.XPATH, ".//span[contains(text(), 'Sponsored')]")
# #     if not is_sponsored:
# #         best_product_url = product.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
# #         break  # Stop after finding the first non-sponsored product
# #
# # # Open the product page
# # if best_product_url:
# #     driver.get(best_product_url)
# #     print(f"Opening Product Page: {best_product_url}")
# #
# #     # Wait for the "Add to Cart" button to appear and ensure it's clickable
# #     try:
# #         # Wait for the button to be clickable
# #         add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-button"]')))
# #         add_to_cart_button.click()
# #         print("✅ Product added to cart!")
# #     except Exception as e:
# #         print("⚠ Unable to add product to cart:", str(e))
# #
# # else:
# #     print("❌ No product found.")
# #
# # # Keep the browser open for user to review
# # input("Press Enter to exit...")
# # driver.quit()
#
