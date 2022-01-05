from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    TITLE_IN_PP = (By.CSS_SELECTOR, "div.product_main h1")
    MES_ABOUT_ADD = (By.CSS_SELECTOR, "div.alertinner strong")
    PRICE_IN_PP = (By.CSS_SELECTOR, ".product_main .price_color")  # Цена в карточке товара
    MES_TOTAL = (By.CSS_SELECTOR, "div.alertinner p strong")  # Цена в сообщении
