import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                 help="Choose language liyaboy")





@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print(f"\nstart browser for test with language: {language}")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    
    yield browser
    
    print("\nquit browser..")
    browser.quit()