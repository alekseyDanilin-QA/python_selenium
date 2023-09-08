import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

url = "https://yandex.ru/games/"

def test_category_popular():
    """
    Проверяем описание к категории игр
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)
    popular=driver.find_elements(By.CSS_SELECTOR, value='[class="category category_type_list "]')
    popular[1].click()
    WebDriverWait(driver, timeout=10, poll_frequency=2).until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "page-description__title"), "Популярные игры"))
    description=driver.find_element(By.CLASS_NAME, value="page-description__subtitle-1")

    assert description.text == "Что такое популярные игры?", 'Unexpected result'

def test_category_casino():
    """"
    Проверяем, что в категории "Казино" присутствует предупреждение для пользователей
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-infobars") 
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)
    driver.find_element(By.XPATH, value="//div//span[contains(text(),'Казино')]").click()
    WebDriverWait(driver, timeout=10, poll_frequency=2).until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "section-header__text"), "Казино"))
    warning=driver.find_element(By.CLASS_NAME, value="feed-with-header__disclaimer-text")
    assert warning.text == "Игры из раздела «Казино» предназначены для игроков, достигших 18 лет, и носят исключительно развлекательный характер. Помните, что тут нет возможности выиграть деньги или другие ценные призы. Успех в играх из данной категории также не означает будущего успеха в азартных играх и играх на реальные деньги.", 'Unexpected result'

def test_profile():
    """"
    Проверяем отображение профиля у неавторизованного пользователя
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-infobars") 
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)
    driver.find_element(By.XPATH, value="//div//a[contains(text(),'Профиль')]").click()
    WebDriverWait(driver, timeout=10, poll_frequency=2).until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "profile-header__login"), "Войдите с логином Яндекса, чтобы получать ачивки, менять имя пользователя и аватар"))
    disabling_ads=driver.find_element(By.CLASS_NAME, value="ads-disabler__title")
    assert disabling_ads.text == "Отключение рекламы", 'Unexpected result'
    description_ads=driver.find_element(By.CLASS_NAME, value="ads-disabler__description")
    assert description_ads.text == "Войти в аккаунт и отключить рекламу во всех играх и каталоге на 24 часа", 'Unexpected result'

def test_missing_tag():
    """"
    Проверяем отображение блока "Популярные" на странице с несуществующим тегом.
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-infobars") 
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://yandex.ru/games/tag/fjdkjdkf")
    WebDriverWait(driver, timeout=10, poll_frequency=2).until(EC.text_to_be_present_in_element(
        (By.XPATH, "//div/h1"), "Ошибка 404"))
    block_popular=driver.find_element(By.CLASS_NAME, value="section-header__text")
    assert block_popular.text == "Популярные", 'Unexpected result'

def test_missing_developer():
    """"
    Проверяем отображение блока "Популярные" на странице с несуществующим разработчиком.
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-infobars") 
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://yandex.ru/games/developer?name=fdfjkldfjdkfj")
    WebDriverWait(driver, timeout=10, poll_frequency=2).until(EC.text_to_be_present_in_element(
        (By.XPATH, "//div/h1"), "Ошибка 404"))
    block_popular=driver.find_element(By.CLASS_NAME, value="section-header__text")
    assert block_popular.text == "Популярные", 'Unexpected result'

def test_missing_category():
    """"
    Проверяем отображение блока "Популярные" на странице с несуществующей категорией.
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-infobars") 
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://yandex.ru/games/category/kjfksdjfkdsjfksdf")
    WebDriverWait(driver, timeout=10, poll_frequency=2).until(EC.text_to_be_present_in_element(
        (By.XPATH, "//div/h1"), "Ошибка 404"))
    block_popular=driver.find_element(By.CLASS_NAME, value="section-header__text")
    assert block_popular.text == "Популярные", 'Unexpected result'

def test_missing_game():
    """"
    Проверяем отображение блока "Популярные" на странице с несуществующей игрой.
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-infobars") 
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://yandex.ru/games/app/iewqjekjsdfkvmcvnkjdfskjsdf")
    WebDriverWait(driver, timeout=10, poll_frequency=2).until(EC.text_to_be_present_in_element(
        (By.XPATH, "//div/h1"), "Ошибка 404"))
    block_popular=driver.find_element(By.CLASS_NAME, value="section-header__text")
    assert block_popular.text == "Популярные", 'Unexpected result'

def test_footer():
    """"
    Проверяем отображение футера страницы
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-infobars") 
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://yandex.ru/games/category/economic?win=574")
    time.sleep(2)
    html = driver.find_element(By.TAG_NAME, 'html')
    html.send_keys(Keys.END)
    time.sleep(1)
    html.send_keys(Keys.END)
    time.sleep(1)
    html.send_keys(Keys.END)
    time.sleep(1)
    html.send_keys(Keys.END)
    time.sleep(1)
    html.send_keys(Keys.END)
    time.sleep(1)
    button=driver.find_element(By.CSS_SELECTOR, value='[class="Button2 Button2_type_link Button2_size_l Button2_view_action"]')
    assert button.text == "Подробнее", 'Unexpected result'
    button_footer=driver.find_elements(By.CLASS_NAME,value="footer-links__link")
    assert button_footer[0].text == "Пользовательское соглашение", 'Unexpected result'
    assert button_footer[1].text == "Политика конфиденциальности", 'Unexpected result'
    assert button_footer[2].text == "Техническая поддержка", 'Unexpected result'

def test_authorization():
    """"
    Проверяем отображение профиля авторизованного пользователя
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-infobars") 
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)
    time.sleep(2)
    authorization_button=driver.find_elements(By.CSS_SELECTOR, value='[class="Button2 Button2_type_link Button2_size_m Button2_view_action login-button"]')
    authorization_button[0].click()
    time.sleep(2)
    driver.find_element(By.ID, value = "passp-field-login").send_keys("Games-auto-Test1")
    driver.find_element(By.ID, value = "passp:sign-in").click()
    time.sleep(2)
    driver.find_element(By.ID, value = "passp-field-passwd").send_keys("Asd9205416647)")
    driver.find_element(By.ID, value = "passp:sign-in").click()
    time.sleep(2)
    driver.find_element(By.XPATH, value="//div//a[contains(text(),'Профиль')]").click()
    time.sleep(2)
    login=driver.find_element(By.CLASS_NAME, value="profile-header-title__handle")

    assert login.text == "games-auto-test1", 'Unexpected result'

def test_authorization_kid():
    """"
    Проверяем отображение доступности игр 16+ для пользователя с детсим аккаунтом
    """
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-infobars") 
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)
    time.sleep(2)
    authorization_button=driver.find_elements(By.CSS_SELECTOR, value='[class="Button2 Button2_type_link Button2_size_m Button2_view_action login-button"]')
    authorization_button[0].click()
    time.sleep(2)
    driver.find_element(By.ID, value = "passp-field-login").send_keys("Games-auto-Test-kid2")
    driver.find_element(By.ID, value = "passp:sign-in").click()
    time.sleep(2)
    driver.find_element(By.ID, value = "passp-field-passwd").send_keys("Asd9205416647)")
    driver.find_element(By.ID, value = "passp:sign-in").click()
    time.sleep(2)
    driver.get("https://yandex.ru/games/app/102019#app-id=102019&catalog-session-uid=catalog-00e54210-1ac1-5cd2-b4e7-778f5a0e6b0d-1694086848341-d6ec&rtx-reqid=9008577927166428183&pos=%7B%22listType%22%3A%22suggested%22%2C%22tabCategory%22%3A%22action%22%7D&redir-data=%7B%22block%22%3A%22suggested%22%2C%22block_index%22%3A1%2C%22card%22%3A%22adaptive_recommended_new%22%2C%22col%22%3A2%2C%22first_screen%22%3A1%2C%22page%22%3A%22cat_action%22%2C%22rn%22%3A563175251%2C%22row%22%3A0%2C%22rtx_reqid%22%3A%229008577927166428183%22%2C%22wrapper%22%3A%22grid-list%22%2C%22http_ref%22%3A%22https%253A%252F%252Fyandex.ru%252Fgames%252Fcategory%252Faction%22%7D")
    WebDriverWait(driver, timeout=10, poll_frequency=2).until(EC.text_to_be_present_in_element(
        (By.XPATH, "//div[2]/section/h1/span"), "Похожие"))
    error=driver.find_element(By.CSS_SELECTOR, value='[class="error-page__title centered-content"]')

    assert error.text == "Ошибка 404", 'Unexpected result'

    