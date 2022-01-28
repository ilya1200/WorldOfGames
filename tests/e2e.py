from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

TIME_TO_WAIT: int = 20

locators = {
    "score": (By.ID, "score"),
}


def chrome_driver() -> WebDriver:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("no-sandbox")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--headless")
    chrome_driver: WebDriver = webdriver.Chrome(chrome_options=chrome_options)
    chrome_driver.implicitly_wait(TIME_TO_WAIT)
    return chrome_driver


def test_scores_service(app_url: str) -> bool:
    driver: WebDriver = chrome_driver()
    driver.get(app_url)
    try:
        score_element: WebElement = driver.find_element(*locators["score"])
        score: int = int(score_element.text)
        assert 1 <= score <= 1000
    except (AssertionError, NoSuchElementException):
        return False
    else:
        return True
    finally:
        driver.quit()


def main_function():
    APP_URL: str = "http://127.0.0.1:5001/"
    is_pass = test_scores_service(APP_URL)
    if is_pass:
        exit(0)
    exit(-1)


if __name__ == '__main__':
    main_function()