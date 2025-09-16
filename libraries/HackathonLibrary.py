from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class HackathonLibrary:
    def __init__(self):
        self.driver = None

    def open_browser(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def go_to_url(self, url):
        self.driver.get(url)
    
    def click_element(self, locator_value, locator_type="id", double=False):
        if locator_type == "id":
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_type == 'class':
            element = self.driver.find_element(By.CLASS_NAME, locator_value)

        if double:
            actions = ActionChains(self.driver)
            actions.double_click(element).perform()
        else: 
            element.click()

    def click_element_with_text(self, text): 
        xpath = xpath = f'//button[normalize-space(text())="{text}"]'
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()
    
    def type_element_by_placeholder(self, placeholder, text):
        xpath = xpath = f"//input[@placeholder='{placeholder}']"
        element = self.driver.find_element(By.XPATH, xpath)
        element.send_keys(text)
    
    def select_country(self, country):
        element = self.driver.find_element(By.TAG_NAME, 'select')
        dropdown = Select(element)
        dropdown.select_by_value(country)

    def wait_for_element_with_class_visible(self, locator_class, timeout=0):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, locator_class)))
        return element

    def wait_for_element_with_id_visible(self, locator_id, timeout=0):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.visibility_of_element_located((By.ID, locator_id)))
        return element
    
    def wait_for_url_contains(self, partial_url, timeout=0): 
        WebDriverWait(self.driver, timeout).until(EC.url_contains(partial_url))

    def get_switch_values(self, class_name):
        elements = self.driver.find_elements(By.CLASS_NAME, class_name)

        values = [el.text.strip() for el in elements]
        return values
    
    def solve_switches(self, values):
        actions = ActionChains(self.driver)

        for i, value in enumerate(values):
            switch_element = self.driver.find_element(By.ID, f"switch-{i}")

            if value == "1":
                switch_element.click()
            elif value == "0":
                actions.double_click(switch_element).perform()
            
    def solve_arrows(self):
        for _ in range(10):
            arrow_element = self.driver.find_element(By.CLASS_NAME, "arrow")
            element_src = arrow_element.get_attribute('src')

            direction = element_src.split("/")[-1].strip().lower()

            key = None
            if direction == "right.png":
                key = Keys.ARROW_RIGHT
            elif direction == "left.png":
                key = Keys.ARROW_LEFT
            elif direction == "up.png":
                key = Keys.UP
            elif direction == "down.png":
                key = Keys.DOWN
            
            self.driver.switch_to.active_element.send_keys(key)
            time.sleep(0.3)

    def solve_doors(self):
        actions = ActionChains(self.driver)

        for i in range(4):
            door = self.driver.find_element(By.ID, f"square-{i}")

            actions.move_to_element(door).perform()
            time.sleep(0.3)

            class_attr = door.get_attribute("class")
            if class_attr and "active" in class_attr:
                actions.double_click(door).perform()
                break

    def solve_cave_puzzle(self):
        letters = ["A", "T", "L", "N", "I", "S"]
        actions = ActionChains(self.driver)

        for letter in letters:
            source_selector = f"[data-letter='{letter}'][draggable='true']"
            target_selector = f"[data-letter='{letter}']:not([draggable])"

            sources = self.driver.find_elements(By.CSS_SELECTOR, source_selector)
            targets = self.driver.find_elements(By.CSS_SELECTOR, target_selector)

            count = min(len(sources), len(targets))

            for i in range(count):
                source = sources[i]
                target = targets[i]

                actions.click_and_hold(source).move_to_element(target).release().perform()
                time.sleep(0.3)


    def close_browser(self):
        if self.driver:
            self.driver.quit()