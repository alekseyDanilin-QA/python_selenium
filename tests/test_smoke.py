# импортируем модули и отдельные классы
from cgitb import text
from errno import ENETRESET
from pyclbr import Class
from tkinter import N
import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

# каждый тест должен начинаться с test_
def test_product_view_sku():
    """
    Test case WERT-1
    """
		# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"
	
		# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service(ChromeDriverManager().install())
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
		# определяем адрес страницы для теста и переходим на неё
    url = "https://test.qa.studio"
    driver.get(url=url)
		# ищем по селектору элемент меню "Горячие товары" и кликаем по нему
    element = driver.find_element(by=By.CSS_SELECTOR, value="[class='tab-featured ']")
    element.click()
    time.sleep(5)
		# ищем по XPATH "Журнальный столик" и кликаем по нему, чтобы просмотреть детали
    x_path_table = '//*[@id="rz-shop-content"]/ul/li[1]/div/div[2]/h2/a'
    element = driver.find_element(By.XPATH, value=x_path_table)
    element.click()
		# ищем по имени класса артикул для "Журнального столика"
    sku = driver.find_element(By.CLASS_NAME, value="sku")
		# проверяем соответствие
    assert sku.text == 'C0MSSDSUM7', "Unexpected sku"

    # каждый тест должен начинаться с test_
def test_product_buy():
    """
    Test case WERT-2
    """
		# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"
	
		# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service(ChromeDriverManager().install())
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
		# определяем адрес страницы для теста и переходим на неё
    url = "https://test.qa.studio"
    driver.get(url=url)
		# ищем по селектору элемент меню "Бестселлеры" и кликаем по нему
    element = driver.find_element(by=By.CSS_SELECTOR, value="[class='tab-best_sellers ']")
    element.click()
    time.sleep(3)
		# ищем по XPATH "Журнальный столик" и кликаем по нему, чтобы просмотреть детали
    x_path_product = '//*[@id="rz-shop-content"]//li[8]//div/h2/a'
    element = driver.find_element(By.XPATH, value=x_path_product)
    element.click()
    time.sleep(3)
    # ищем по селектору кнопку "В корзину" и кликаем по ней
    driver.find_element(By.XPATH, value='//*[@id="product-11343"]//form//button').click()
    time.sleep(3)
    # Переходим в корзину по URL
    driver.get("https://test.qa.studio/cart/")
    time.sleep(3)
    # ищем по селектору кнопку "Оформить заказ" и кликаем по ней
    driver.find_element(by=By.CSS_SELECTOR, value="[class='checkout-button button alt wc-forward']").click()
    time.sleep(3)
    # заполняем обязательные поля
    driver.find_element(By.ID, value="billing_first_name").send_keys("Алексей")
    driver.find_element(By.ID, value="billing_last_name").send_keys("Данилин")
    driver.find_element(By.ID, value="billing_address_1").send_keys("Ямашева 51Б")
    driver.find_element(By.ID, value="billing_city").send_keys("Казань")
    driver.find_element(By.ID, value="billing_state").send_keys("Татарстан")
    driver.find_element(By.ID, value="billing_postcode").send_keys("420124")
    driver.find_element(By.ID, value="billing_phone").send_keys("5540198")
    driver.find_element(By.ID, value="billing_email").send_keys("danilin9191@list.ru")
    time.sleep(3)
    # ищем по ID кнопку "Подтвердить заказ" и кликаем по ней
    driver.find_element(By.ID, value="place_order").click()
    time.sleep(3)
		# ищем по CSS Селектору надпись об успешном принятии заказа
    a = driver.find_element(By.CSS_SELECTOR, value="p.woocommerce-notice.woocommerce-notice--success.woocommerce-thankyou-order-received")
    		# проверяем соответствие
    assert a.text == 'Ваш заказ принят. Благодарим вас.'

    # каждый тест должен начинаться с test_
def test_favorites():
    """
    Test case WERT-3
    """
		# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"
	
		# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service(ChromeDriverManager().install())
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
		# определяем адрес страницы для теста и переходим на неё
    url = "https://test.qa.studio"
    driver.get(url=url)
		# ищем по селектору Иконки "Добавить в список желаний" и кликаем по ним
    driver.find_element(By.CSS_SELECTOR, value=".product_tag-149.has-post-thumbnail.shipping-taxable.purchasable.product-type-simple div.product-thumbnail > div div span.razzi-svg-icon").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, value =".product_tag-143.product_tag-124.has-post-thumbnail.shipping-taxable.purchasable.product-type-simple div.product-thumbnail div div span.razzi-svg-icon svg").click()
    time.sleep(3)
    # ищем по селектору кнопку "Список желаний" и кликаем по ней
    driver.find_element(By.CSS_SELECTOR, value =".has-logo > div.header-wishlist > a").click()
    time.sleep(3)
    # ищем первый добавленный продукт и сверяем название
    product1 = driver.find_element(By.CSS_SELECTOR, value = "#yith-wcwl-row-11342 > td.product-name > a")
    assert product1.text == 'БРОММС Двухместная кровать'
    # ищем второй добавленный продукт и сверяем название
    product2 = driver.find_element(By.XPATH, value = "//*[@id='yith-wcwl-row-11345']/td[3]/a")
    assert product2.text == 'БРЕДБЕРРИ Комод с ящиками'

    # каждый тест должен начинаться с test_
def test_Questions():
    """
    Test case WERT-4
    """
		# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"
	
		# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service(ChromeDriverManager().install())
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
		# определяем адрес страницы для теста и переходим на неё
    url = "https://test.qa.studio"
    driver.get(url=url)
		# ищем по XPATH кнопку в оглавлении сайта "Часто задаваемые вопросы", сверяем её название и кликаем по ней
    element = driver.find_element(By.XPATH, value="//*[@id='menu-top']/li[2]/a")
    assert element.text == "Часто задавамые вопросы"
    element.click()
    time.sleep(3)
    # ищем по селекторам категории часто задаваемых вопросов и сверяем их названия
    element = driver.find_element(By.CSS_SELECTOR, ".elementor-element-01593e1 h4")
    assert element.text == "Заказы:"
    element = driver.find_element(By.CSS_SELECTOR, ".elementor-element-f9145f0 h4")
    assert element.text == "Доставка и возврат:"
    element = driver.find_element(By.CSS_SELECTOR, ".elementor-element-b754740 h4")
    assert element.text == "Оплата:"

def test_blog():
    """
    Test case WERT-5
    """
		# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"
	
		# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service(ChromeDriverManager().install())
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
		# определяем адрес страницы для теста и переходим на неё
    url = "https://test.qa.studio"
    driver.get(url=url)
		# ищем по XPATH в оглавлении сайта кнопку "Блог", сверяем название и кликаем по ней
    element = driver.find_element(By.XPATH, value="//*[@id='menu-top']/li[3]/a")
    assert element.text == "Блог"
    element.click()
    time.sleep(3)
    # ищем по селекторам категории блога и сверяем названия
    element = driver.find_element(By.CSS_SELECTOR, "#razzi-posts__taxs-list > ul > li:nth-child(1)> a")
    assert element.text == "Показать все"
    element = driver.find_element(By.CSS_SELECTOR, "#razzi-posts__taxs-list > ul > li:nth-child(2) > a")
    assert element.text == "Дом"
    element = driver.find_element(By.CSS_SELECTOR, "#razzi-posts__taxs-list > ul > li:nth-child(3) > a")
    assert element.text == "Интерьер"
    element = driver.find_element(By.CSS_SELECTOR, "#razzi-posts__taxs-list > ul > li:nth-child(4) > a")
    assert element.text == "Без рубрики"
    element = driver.find_element(By.CSS_SELECTOR, "#razzi-posts__taxs-list > ul > li:nth-child(5) > a")
    assert element.text == "Минимализм"
    element = driver.find_element(By.CSS_SELECTOR, "#razzi-posts__taxs-list > ul > li:nth-child(6) > a")
    assert element.text == "Эстетика"

    # каждый тест должен начинаться с test_
def test_contacts():
    """
    Test case WERT-6
    """
		# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"
	
		# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service(ChromeDriverManager().install())
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
		# определяем адрес страницы для теста и переходим на неё
    url = "https://test.qa.studio"
    driver.get(url=url)
		# ищем по XPATH кнопку в оглавлении сайта "Контакты", сверяем её название и кликаем по ней
    element = driver.find_element(By.XPATH, value="//*[@id='menu-top']/li[5]/a")
    assert element.text == "Контакты"
    element.click()
    time.sleep(3)
    # ищем по селекторам категории контактов и сверяем их названия
    element = driver.find_element(By.CSS_SELECTOR, ".elementor-element-5e4ec47c .razzi-icon-box__content span")
    assert element.text == "Позвоните нам:"
    element = driver.find_element(By.CSS_SELECTOR, ".elementor-element-10f50d22 .razzi-icon-box__content span")
    assert element.text == "Напишите нам:"
    element = driver.find_element(By.CSS_SELECTOR, ".elementor-element-36c946e8 h6")
    assert element.text == "Поддержка:"
    element = driver.find_element(By.CSS_SELECTOR, ".elementor-element-2f6c2e1 h6")
    assert element.text == "Вакансии:"

        # каждый тест должен начинаться с test_
def test_about_company():
    """
    Test case WERT-7
    """
		# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"
	
		# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service(ChromeDriverManager().install())
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
		# определяем адрес страницы для теста и переходим на неё
    url = "https://test.qa.studio"
    driver.get(url=url)
		# ищем по XPATH кнопку в оглавлении сайта "О компании", сверяем её название и кликаем по ней
    element = driver.find_element(By.XPATH, value="//*[@id='menu-top']/li[4]/a")
    assert element.text == "О компании"
    element.click()
    time.sleep(3)
    # ищем по селектору заголовок "О компании" и сверяем его название
    element = driver.find_element(By.CSS_SELECTOR, "#page-header h1")
    assert element.text == "О компании"

    # каждый тест должен начинаться с test_
def test_product_filter1():
    """
    Test case WERT-8
    """
		# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"
	
		# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service(ChromeDriverManager().install())
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
		# определяем адрес страницы для теста и переходим на неё
    url = "https://test.qa.studio"
    driver.get(url=url)
		# ищем по селектору кнопку "Фильтр" и кликаем по ней
    driver.find_element(By.CSS_SELECTOR, value=".catalog-toolbar-right > a").click()
    time.sleep(3)
    # ищем по селектору кнопку "Категории" и кликаем по ней
    driver.find_element(By.CSS_SELECTOR, value = ".checkboxes.products-filter--collapsible > span").click()
    time.sleep(3)
    # ищем по селектору чекбокс "Подвесные светильники" и ставим галочку
    driver.find_element(By.CSS_SELECTOR, ".rz-active li:nth-child(6) span").click()
    time.sleep(3)
    # ищем по селектору кнопку "Фильтр" и кликаем по ней
    driver.find_element(By.CSS_SELECTOR, ".products-filter__filters-buttons .filter-button").click()
    # ищем по селектору применённый фильтр "Подвесные светильники" и сверяем надпись
    element = driver.find_element(By.CSS_SELECTOR, "#rz-products-filter__activated a")
    assert element.text == "Подвесные светильники"

    # каждый тест должен начинаться с test_
def test_product_filter2():
    """
    Test case WERT-9
    """
		# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"
	
		# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service(ChromeDriverManager().install())
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
		# определяем адрес страницы для теста и переходим на неё
    url = "https://test.qa.studio"
    driver.get(url=url)
		# ищем по селктору кнопку "Фильтр" и кликаем по ней
    driver.find_element(By.CSS_SELECTOR, value=".catalog-toolbar-right > a").click()
    time.sleep(3)
    # ищем по селектору кнопку "Бренды" и кликаем по ней
    driver.find_element(By.CSS_SELECTOR, value = ".checkboxes.products-filter--scrollable > span").click()
    time.sleep(3)
    # ищем по селектору чекбокс "rannar" и ставим галочку
    driver.find_element(By.CSS_SELECTOR, ".rz-active li:nth-child(2) > span").click()
    time.sleep(3)
    # ищем по селектору кнопку "Фильтр" и кликаем по ней
    driver.find_element(By.CSS_SELECTOR, ".products-filter__filters-buttons .filter-button").click()
    # ищем по селектору применённый фильтр "rannar"
    element = driver.find_element(By.CSS_SELECTOR, "#rz-products-filter__activated a")
    # назначаем переменную "y" значение которой, равно значению атрибута "data-value"
    y = element.get_attribute("data-value")
    # сверяем значение с ожидаемым текстом
    assert y == "rannar"

  # каждый тест должен начинаться с test_
def test_product_search():
    """
    Test case WERT-10
    """
		# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"
	
		# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service(ChromeDriverManager().install())
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
		# определяем адрес страницы для теста и переходим на неё
    url = "https://test.qa.studio"
    driver.get(url=url)
		# ищем по селктору кнопку "Поиск" и кликаем по ней
    driver.find_element(By.CSS_SELECTOR, ".search-type-icon > span").click()
    time.sleep(3)
    # ищем по селектору поле ввода "Поиск предметов" и кликаем по ней
    element = driver.find_element(By.CSS_SELECTOR, ".search-wrapper .search-field").send_keys('диван\n')
    time.sleep(3)
    # ищем по селектору чекбокс "rannar" и ставим галочку
    element = driver.find_element(By.CSS_SELECTOR, "nav > a:nth-child(1)")
    assert element.text == 'Главная'
    element = driver.find_element(By.CSS_SELECTOR, "nav > a:nth-child(3)")
    assert element.text == 'Диваны'

