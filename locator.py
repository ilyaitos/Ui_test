class LocatorsRegistrationPage:
    LOCATOR_LOGIN_FIELD = "//*[@class='inputOutside__input--1Sg9p'][@type='text']"
    LOCATOR_PASSWORD_FIELD = "//*[@class='inputOutside__input--1Sg9p'][@type='password']"
    LOCATOR_BUTTON_TO_COME_IN = '//*[@type="submit"]'


class LocatorsHomePage:
    LOCATOR_BUTTON_DASHBOARD = '//a[@class="sidebarButton__nav-link--2TC0L sidebarButton__active--3dvg_"]'
    LOCATOR_BUTTON_LAUNCHES = '//a[@href="#default_personal/launches"]'
    LOCATOR_BUTTON_FILTERS = '//a[@href="#default_personal/filters"]'
    LOCATOR_BUTTON_DEBUG = '//a[@href="#default_personal/userdebug/all"]'
    LOCATOR_BUTTON_PROJECT_MEMBERS = '//a[@href="#default_personal/members"]'
    LOCATOR_BUTTON_PROJECT_SETTINGS = '//a[@href="#default_personal/settings"]'
    LOCATOR_BUTTON_DEFAULT_DROP = '(//*[@class="userBlock__avatar-wrapper--_Jkks"])[1]'
    LOCATOR_BUTTON_PROFILE = '(//a[contains(@href,"#user-profile")])[2]'
    LOCATOR_BUTTON_LOGOUT = '//div[@class="userBlock__menu-item--3VBsZ"]'


class LocatorsNewDashboard:
    LOCATOR_BUTTON_ADD_NEW_DASHBOARD = '(//button[@class="ghostButton__ghost-button--1PhF7 ghostButton__color-topaz--2GTla with-icon ghostButton__filled-icon--bHBq5 ghostButton__mobile-minified--1m7Pj"])[2]'
    LOCATOR_INPUT_NAME_NEW_DASHBOARD = '//input[@placeholder="Enter dashboard name"]'
    LOCATOR_BUTTON_CONFIRM_ADD_NEW_DASHBOARD = '//button[@class="bigButton__big-button--ivY7j bigButton__color-booger--2IfQT"]'
    LOCATOR_DELETE_DASHBOARD = '//i[@class="icon__icon--2m6Od icon__icon-delete--1jIHF"]'
    LOCATOR_CONFIRM_DELETE_DASHBOARD = '//button[@class="bigButton__big-button--ivY7j bigButton__color-tomato--Wvy5L"]'
    LOCATOR_DASHBOARD_NAME = '//a[@class="gridCell__grid-cell--3e2mS gridCell__align-left--2beIG dashboardTable__name--1sWJs"]'


class LocatorsNewWidget:
    LOCATOR_ADD_NEW_WIDGET = '(//button[@class="ghostButton__ghost-button--1PhF7 ghostButton__color-topaz--2GTla with-icon ghostButton__filled-icon--bHBq5 ghostButton__mobile-minified--1m7Pj"])[2]'
    LOCATOR_WIDGET_LAUNCH_STATISTICS_CHART = '(//div[@class="widgetTypeItem__widget-type-item--17_3G"])[1]'
    LOCATOR_WIDGET_TYPE_NEXT_STEP = '//div[@class="widgetWizardModal__widget-wizard--fG8kx"]//button[@class="ghostButton__ghost-button--1PhF7 ghostButton__color-topaz--2GTla with-icon ghostButton__filled-icon--bHBq5 ghostButton__mobile-minified--1m7Pj"]'
    LOCATOR_CONFIGURE_WIDGET_FILTER_SDDF = '//div[@class="filtersItem__filter-item--1OosV"]'
    LOCATOR_CONFIGURE_WIDGET_TYPE_NEXT_STEP = '(//div[@class="widgetWizardModal__widget-wizard--fG8kx"]//button[@class="ghostButton__ghost-button--1PhF7 ghostButton__color-topaz--2GTla with-icon ghostButton__filled-icon--bHBq5 ghostButton__mobile-minified--1m7Pj"])[3]'
    LOCATOR_SAVE_ADD = '//button[@class="bigButton__big-button--ivY7j bigButton__color-booger--2IfQT"]'
    LOCATOR_WIDGET_NAME = '//div[@class="widget__widget--mVI7B"]'


class LocatorsProfile:
    LOCATOR_EDITING_NICKNAM = '//span[@class="userInfo__pencil-icon--2WZhA"]'
    LOCATOR_USER_NAME = '//input[ @ placeholder = "Enter user name"]'
    LOCATOR_SUBMIT = '//button[@class="bigButton__big-button--ivY7j bigButton__color-booger--2IfQT"]'
    LOCATOR_USER_NAME_ON_THE_PAGE = '//span[@class="userInfo__name--1aIPl"]'


class LocatorsLaunches:
    LOCATOR_TEST_EXAMPLE = '(//*[@class="tooltip__tooltip-trigger--3Z4Hc itemInfo__name--27fwI"])[1]'
    LOCATOR_DASHBOARD_STATUS_PASSED = '//*[@class="gridRow__grid-row-wrapper--1dI9K"]//*[text()="test.py::test_dashboard_passed"]/../../../../../../..//*[@class="inputDropdown__value--2gB2s statusDropdown__value--2-1wZ"]'
    LOCATOR_DASHBOARD_STATUS_FAILED = '//*[@class="gridRow__grid-row-wrapper--1dI9K stepGrid__failed--2d38k"]//*[text()="test.py::test_dashboard_failed"]/../../../../../../..//*[@class="inputDropdown__value--2gB2s statusDropdown__value--2-1wZ"]'
    LOCATOR_DASHBOARD_STATUS_SKIPPED = '//*[@class="gridRow__grid-row-wrapper--1dI9K"]//*[text()="test.py::test_dashboard_skipped"]/../../../../../../..//*[@class="inputDropdown__value--2gB2s statusDropdown__value--2-1wZ"]'
