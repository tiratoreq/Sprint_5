from selenium.webdriver.common.by import By


class Locators:
    #ссылки на переходы в:
    # Личный кабинет
    LK = (By.XPATH, "//a[@href= '/account']")
    # регистрацию
    REG_BUTTON = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
    # страницу входа
    ENTER_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")
    # страницу восстановления пароля
    PASSWORD_RESET = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")
    # конструктор заказа
    CONSTRUCTOR = (By.XPATH, "//p[contains(text(), 'Конструктор')]")

    # Поля:
    # Имя
    NAME = (By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input")
    # Эмейл
    EMAIL = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")
    # Пароль
    PASSWORD = (By.XPATH, "//label[contains(text(), 'Пароль')]/following-sibling::input")

    # Собщения:
    # Некорректный пароль
    PASSWORD_MESS = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")
    # В этом разделе вы можете изменить свои персональные данные
    LK_TEXT = (By.XPATH, "//p[contains(text(), 'В этом разделе вы можете изменить свои персональные данные')]")

    # Кнопки:
    # Авторизация
    AUTH_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    # Оформить заказ
    ORDER = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    # Войти в аккаунт
    ENTER_ACCOUNT = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    # Выход
    LOGOUT = (By.XPATH, "//button[contains(text(), 'Выход')]")


    # Картинка с бургером в шапке сайта
    PICTURE = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")

    #Меню:
    # Соусы
    SOUSES = (By.XPATH, "//span[contains(text(), 'Соусы')]")
    # Булки
    BOOLOCHKI = (By.XPATH, "//span[contains(text(), 'Булки')]")
    # Начинки
    NACHINKI = (By.XPATH, "//span[contains(text(), 'Начинки')]")

    # Выделенные пункты в меню
    # Для булок
    BOOLKA_IN_MENU = (By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[contains(text(), 'Булки')]")
    # Для соусов
    SOUS_IN_MENU = (By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[contains(text(), 'Соусы')]")
    # Для начинок
    NACHINKA_IN_MENU = (By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span[contains(text(), 'Начинки')]")