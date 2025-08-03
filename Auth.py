from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
from dotenv import load_dotenv

# --[[ Load Environment Variables ]]--
load_dotenv()

def getCookie(username, password):
    options = webdriver.ChromeOptions()    
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 8)  # Wait up to 15 seconds

    try:
        driver.get(f"{os.getenv('SIMON_LINK', 'https://simon.sfx.vic.edu.au')}/Login/Default.aspx?ReturnUrl=%2F")

        # Wait for username input to be present
        wait.until(EC.presence_of_element_located((By.ID, "inputUsername")))

        user_input = driver.find_element(By.ID, "inputUsername")
        pass_input = driver.find_element(By.ID, "inputPassword")

        user_input.send_keys(username)
        pass_input.send_keys(password)

        # Enable the login button (if needed)
        driver.execute_script("document.getElementById('buttonLogin').removeAttribute('disabled');")

        # Wait until the login button is clickable, then click it
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "buttonLogin")))
        login_button.click()

        # Now wait for a post-login element to appear
        # (replace this with an element that only shows after login)
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "welcome-card-greetings")))
        except TimeoutException:
            return None

        # Once logged in, get cookies
        cookies = driver.get_cookies()
        for cookie in cookies:
            if cookie['name'] == 'adAuthCookie':
                return cookie['value']

        return None

    except TimeoutException:
        # Handle any other timeout exceptions
        return None
    finally:
        driver.quit()


