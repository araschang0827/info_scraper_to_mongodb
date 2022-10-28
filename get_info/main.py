from selenium import webdriver
from selenium.webdriver.common.by import By
import get_info.constants as const
import os


class get_information(webdriver.Chrome):
    def __init__(self, web_driver='/Users/araschang/Desktop/coding/DATA SCIENCE/selenium tutorial', teardown=False):
        self.web_driver = web_driver
        os.environ['PATH'] = self.web_driver
        self.teardown = teardown
        super(get_information, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_on_first_page(self):
        self.get(const.NTU_URL)

    def login_page(self):
        login_element = self.find_element(By.XPATH, '/html/body/table/tbody/tr['
                                                    '1]/td/table/tbody/tr/td/table/tbody/tr[2]/td['
                                                    '2]/table/tbody/tr/td/a[1]')
        login_element.click()

    def user_password(self, username, password):
        user_element = self.find_element(By.NAME, 'user')
        pass_element = self.find_element(By.NAME, 'pass')
        user_element.clear()
        user_element.send_keys(username)
        pass_element.clear()
        pass_element.send_keys(password)

    def login_button(self):
        login_element = self.find_element(By.NAME, 'Submit')
        login_element.click()

    def land_on_home_page(self):
        home_page = self.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td[1]/div[1]/a')
        home_page.click()


    def find_ID(self):
        ID = self.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td[2]/div/div/div/table/tbody/tr[1]/td[2]')
        return ID.text.strip()

    def find_name(self):
        name = self.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td[2]/div/div/div/table/tbody/tr[1]/td[4]')
        return name.text.strip()

    def find_DEPT(self):
        DEPT = self.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td[2]/div/div/div/table/tbody/tr[2]/td[2]')
        return DEPT.text.strip()


    def score_page(self):
        page_element = self.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td[1]/div[11]/a')
        page_element.click()


    def get_score(self):
        scores = self.find_elements(By.CSS_SELECTOR, 'font[color="#0000FF"]')
        full_score = []
        for score in scores:
            full_score.append(score.text)
        correct_score = []
        for i in range(len(full_score)):
            if i % 2 == 1:
                correct_score.append(float(full_score[i][8:]))
        print(correct_score)


