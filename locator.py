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
    LOCATOR_BUTTON_ADD_NEW_DASHBOARD = '(//button[@class="ghostButton__ghost-button--1PhF7 ghostButton__color-topaz--2GTla with-icon ghostButton__filled-icon--bHBq5 ghostButton__mobile-minified--1m7Pj"])[1]'
    LOCATOR_INPUT_NAME_NEW_DASHBOARD = '//input[@placeholder="Enter dashboard name"]'
    LOCATOR_BUTTON_CONFIRM_ADD_NEW_DASHBOARD = '//button[@class="bigButton__big-button--ivY7j bigButton__color-booger--2IfQT"]'
    LOCATOR_DELETE_DASHBOARD = '//i[@class="icon__icon--2m6Od icon__icon-delete--1jIHF"]'
    LOCATOR_CONFIRM_DELETE_DASHBOARD = '//button[@class="bigButton__big-button--ivY7j bigButton__color-tomato--Wvy5L"]'
    LOCATOR_DASHBOARD_NAME = '//a[@class="gridCell__grid-cell--3e2mS gridCell__align-left--2beIG dashboardTable__name--1sWJs"]'
    LOCATOR_LIST_DASHBOARD_NAME = '//*[@class="gridRow__grid-row-wrapper--1dI9K"]'


class LocatorsNewWidget:
    LOCATOR_ADD_NEW_WIDGET = '(//button[@class="ghostButton__ghost-button--1PhF7 ghostButton__color-topaz--2GTla with-icon ghostButton__filled-icon--bHBq5 ghostButton__mobile-minified--1m7Pj"])[2]'
    LOCATOR_WIDGET_TYPE_NEXT_STEP = '//div[@class="widgetWizardModal__widget-wizard--fG8kx"]//button[@class="ghostButton__ghost-button--1PhF7 ghostButton__color-topaz--2GTla with-icon ghostButton__filled-icon--bHBq5 ghostButton__mobile-minified--1m7Pj"]'
    LOCATOR_CONFIGURE_WIDGET_FILTER_SDDF = '//div[@class="filtersItem__filter-item--1OosV"]'
    LOCATOR_CONFIGURE_WIDGET_TYPE_NEXT_STEP = '(//div[@class="widgetWizardModal__widget-wizard--fG8kx"]//button[@class="ghostButton__ghost-button--1PhF7 ghostButton__color-topaz--2GTla with-icon ghostButton__filled-icon--bHBq5 ghostButton__mobile-minified--1m7Pj"])[3]'
    LOCATOR_SAVE_ADD = '//button[@class="bigButton__big-button--ivY7j bigButton__color-booger--2IfQT"]'
    LOCATOR_WIDGET_NAME = '//div[@class="widget__widget--mVI7B"]'
    LOCATOR_INPUT_WIDGET_NAME = '//*[@placeholder="Enter widget name"]'



class LocatorsNameWidget:
    LOCATOR_WIDGET_LAUNCH_STATISTICS_CHART = '//div[@class="widget-type-selector"]//div[text() ="Launch statistics chart"]'
    LOCATOR_WIDGET_OVERALL_STSTISTICS = '//div[@class="widget-type-selector"]//div[text() ="Overall statistics"]'
    LOCATOR_WIDGET_LAUNCHES_DURATION_CHART = '//div[@class="widget-type-selector"]//div[text() ="Launches duration chart"]'
    LOCATOR_WIDGET_LAUNCH_EXECUTION_AND_ISSUE_STATISTIC = '//div[@class="widget-type-selector"]//div[text() ="Launch execution and issue statistic"]'
    LOCATOR_WIDGET_PROJECT_ACTIVITY_PANEL = '//div[@class="widget-type-selector"]//div[text() ="Project activity panel"]'
    LOCATOR_WIDGET_TEST_CASES_GROWTH_TREND_CHART = '//div[@class="widget-type-selector"]//div[text() ="Test-cases growth trend chart"]'
    LOCATOR_WIDGET_INVESTIGATED_PERCENTAGE_OF_LAUNCHES = '//div[@class="widget-type-selector"]//div[text() ="Investigated percentage of launches"]'
    LOCATOR_WIDGET_LAUNCHES_TABLE = '//div[@class="widget-type-selector"]//div[text() ="Launches table"]'
    LOCATOR_WIDGET_UNIQUE_BUGS_TABLE = '//div[@class="widget-type-selector"]//div[text() ="Unique bugs table"]'
    LOCATOR_WIDGET_MOST_FAILED_TEST_CASES_TABLE = '//div[@class="widget-type-selector"]//div[text() ="Most failed test-cases table (TOP-20)"]'
    LOCATOR_WIDGET_FAILED_CASES_TREND_CHART = '//div[@class="widget-type-selector"]//div[text() ="Failed cases trend chart"]'
    LOCATOR_WIDGET_NON_PASSED_TEST_CASES_TREND_CHART = '//div[@class="widget-type-selector"]//div[text() ="Non-passed test-cases trend chart"]'
    LOCATOR_WIDGET_DIFFEREN_LAUNCHES_COMPARISON_CHART = '//div[@class="widget-type-selector"]//div[text() ="Different launches comparison chart"]'
    LOCATOR_WIDGET_PASSING_RATE_PER_LAUNCH = '//div[@class="widget-type-selector"]//div[text() ="Passing rate per launch"]'
    LOCATOR_WIDGET_PASSING_RATE_SUMMARY = '//div[@class="widget-type-selector"]//div[text() ="Passing rate summary"]'
    LOCATOR_WIDGET_FLAKY_TEST_CASES_TABLE = '//div[@class="widget-type-selector"]//div[text() ="Flaky test cases table (TOP-20)"]'
    LOCATOR_WIDGET_CUMULATIVE_TREND_CHART = '//div[@class="widget-type-selector"]//div[text() ="Cumulative trend chart"]'
    LOCATOR_WIDGET_MOST_POPULAR_PATTERN_TABLE = '//div[@class="widget-type-selector"]//div[text() ="Most popular pattern table (TOP-20)"]'
    LOCATOR_WIDGET_COMPONENT_HEALTH_CHECK = '//div[@class="widget-type-selector"]//div[text() ="Component health check"]'
    LOCATOR_WIDGET_COMPONENT_HEALTH_CHECK_TABLE_VIEW = '//div[@class="widget-type-selector"]//div[text() ="Component health check (table view)"]'
    LOCATOR_WIDGET_MOST_TIME_CONSUMING_TEST_CASES_WIDGET = '//div[@class="widget-type-selector"]//div[text() ="Most time-consuming test cases widget (TOP-20)"]'


class LocatorsNameFilter:
    LOCATOR_FILTER_1 = "// *[text() = 'filter_1']"
    LOCATOR_FILTER_2 = "// *[text() = 'filter_2']"
    LOCATOR_FILTER_3 = "// *[text() = 'filter_3']"


class LocatorsProfile:
    LOCATOR_EDITING_NICKNAM = '//span[@class="userInfo__pencil-icon--2WZhA"]'
    LOCATOR_USER_NAME = '//input[ @ placeholder = "Enter user name"]'
    LOCATOR_SUBMIT = '//button[@class="bigButton__big-button--ivY7j bigButton__color-booger--2IfQT"]'
    LOCATOR_USER_NAME_ON_THE_PAGE = '//span[@class="userInfo__name--1aIPl"]'


class LocatorsLaunches:
    LOCATOR_TEST_EXAMPLE = '(//*[@class="tooltip__tooltip-trigger--3Z4Hc itemInfo__name--27fwI"])[1]'
    LOCATOR_DASHBOARD_STATUS_PASSED = '//*[@class="gridRow__grid-row-wrapper--1dI9K"]//*[text()="test_launches.py::test_dashboard_passed"]/../../../../../../..//*[@class="inputDropdown__value--2gB2s statusDropdown__value--2-1wZ"]'
    LOCATOR_DASHBOARD_STATUS_FAILED = '//*[@class="gridRow__grid-row-wrapper--1dI9K stepGrid__failed--2d38k"]//*[text()="test_launches.py::test_dashboard_failed"]/../../../../../../..//*[@class="inputDropdown__value--2gB2s statusDropdown__value--2-1wZ"]'
    LOCATOR_DASHBOARD_STATUS_SKIPPED = '//*[@class="gridRow__grid-row-wrapper--1dI9K"]//*[text()="test_launches.py::test_dashboard_skipped"]/../../../../../../..//*[@class="inputDropdown__value--2gB2s statusDropdown__value--2-1wZ"]'
