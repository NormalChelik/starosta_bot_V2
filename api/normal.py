from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from data import Lesson
from webdriver_manager.firefox import GeckoDriverManager
import time
from exceptions import *
BASE_URL = "https://attendance-app.mirea.ru/login"
DEBUG = False


def str2lesson(lesson_text: str) -> Lesson:
    lesson_text = lesson_text.split('\n')
    return Lesson(lesson_text[0], lesson_text[1], lesson_text[2], lesson_text[3] == 'Заверено')


def enter_interface(login: str, password: str) -> webdriver.Firefox:
    options = Options()
    if not DEBUG:
        options.add_argument("--headless")
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

    driver.get(BASE_URL)
    time.sleep(2)
    try:
        login_button = driver.find_element(By.XPATH, "//button[contains(@class, 'ant-btn')]")
        login_button.click()
    except NoSuchElementException as e:
        raise LoginButtonFailedException from e
    time.sleep(1)
    try:
        username_field = driver.find_element(By.XPATH, "//input[@id='id_login']")
        password_field = driver.find_element(By.XPATH, "//input[@id='id_password']")
        username_field.send_keys(login)
        password_field.send_keys(password)
        login_button = driver.find_element(By.XPATH, "//button[contains(@class, 'group')]")
        login_button.click()
    except NoSuchElementException as e:
        raise LoginCredentialsEnterException from e
    time.sleep(1)
    # LOGGED IN

    driver.find_element(By.XPATH, "//button[contains(@class, 'ant-btn-primary')]").click()
    time.sleep(2)
    return driver


def get_schedule(login: str, password: str) -> list[Lesson]:
    driver = enter_interface(login, password)
    ret = [str2lesson(i.text) for i in driver.find_elements(By.XPATH, "//div[@class='ant-card-body']")]
    driver.quit()
    return ret


def update_attendance(login: str, password: str, lesson_number: int, student_dict: dict[str, int]) -> None:
    """Student_dict - {'Агапов Арсений Александрович': 1}, где 1 - присутствует, 2 - н, 3 - У"""
    # Lesson number - Это номер, а не индекс!!!
    driver = enter_interface(login, password)
    lesson = [i for i in driver.find_elements(By.XPATH, "//div[@class='ant-card-body']")][lesson_number - 1]
    lesson.click()
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "//div[@class='ant-spin-container']")
    except NoSuchElementException as e:
        raise PageLoadFailedException from e
    for student in student_dict:
        try:
            student_click = driver.find_element(By.XPATH, f"//div[contains(text(), {student.split()[0]})]")
            student_click.find_element(By.XPATH, "//div[contains(@class, 'ant-radio-group')]"
                                       ).find_elements(By.XPATH, "//label[contains(@class, 'ant-radio-button-wrapper')]"
                                                       )[student_dict[student] - 1].click()
        except NoSuchElementException as e:
            raise StudentNotFoundException from e
    driver.find_element(By.XPATH, "//button[contains(@class, 'ant-btn-primary')]").click()
