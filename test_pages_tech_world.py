import pages_tech_world
import pytest
from selenium import webdriver


@pytest.fixture
def driver():

    driver = webdriver.Chrome()

    driver.get("C:/Users/User/Downloads/project_for_test/index.html")

    yield driver
    driver.quit()

#testing the login
def test_login(driver):
    login_page = pages_tech_world.LoginPage(driver)
    login_page.login("admin","@Dm1n")

    assert "Photo Tech World" in driver.page_source


#testing navigation bar
def test_navbar(driver):
    test_login(driver)
    navBar = pages_tech_world.Navbar(driver)



    navBar.go_to_cameras()
    navBar.go_to_lenses()
    navBar.go_to_contact()



def  test_contact_form(driver):
    test_login(driver)
    navBar = pages_tech_world.Navbar(driver)
    navBar.go_to_contact()

    contact_page = pages_tech_world.ContactPage(driver)


    contact_page.fill_form("Philos","philos@gmail.com","0777785897",
                           "Hello l would like some digital cameras")
    contact_page.submit()

    assert "Contact Photo Tech World" in driver.page_source

def test_logout(driver):
    test_login(driver)
    log_out = pages_tech_world.LogOut(driver)
    log_out.logout()

    assert "Login" in driver.page_source