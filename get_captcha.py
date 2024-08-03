import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time,requests
import os
import requests

class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.get("link test")
        time.sleep(3)
        self.get_captcha_image()
    
    def get_captcha_image(self):
        print("HIHIHI")
        cookies = self.driver.get_cookies()
        image_path = os.path.join("static/images", "captcha.jpg")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',  # Thay th? b?ng User Agent ph¨´ h?p
        }
        cookie_str = ""
        for cookie in cookies:
            cookie_str += f"{cookie['name']}={cookie['value']}; "
        headers['Cookie'] = cookie_str
        response = requests.get("link get captcha", headers=headers)
        if response.status_code == 200:
            with open(image_path, 'wb') as f:
                f.write(response.content)
        
    def test_login_valid_credentials(self):
        username = "username"
        password = "password"
        captcha = send_image_to_api('static/images/captcha.jpg')
        print("captcha:::", captcha.get('text'))
        username_input = self.driver.find_element(By.CLASS_NAME, 'form-control')
        password_input = self.driver.find_element(By.ID, 'password-field')
        input_captcha = self.driver.find_element(By.XPATH, '//*[@id="page-top"]/header/div/div[2]/div/div/form/div[3]/div/input')
        login_button = self.driver.find_element(By.CLASS_NAME, 'btn-primary')
        username_input.send_keys(username)
        password_input.send_keys(password)
        input_captcha.send_keys(captcha.get('text'))
        login_button.click()
        time.sleep(2)
    #     # login(self.driver, username, password, captcha.get('text'))

    def tearDown(self):
        self.driver.quit()

def send_image_to_api(image_path):
    url = 'url send api handle captcha'
    files = {'image': open(image_path, 'rb')}
    try:
        response = requests.post(url, files=files)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {"error": "Lỗi trong quá trình gửi tập tin ảnh."}
    except requests.exceptions.RequestException as e:
        return {"error": f"Lỗi: {e}"}
    
if __name__ == "__main__":
    for i in range(1,2):
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        
        suite.addTest(loader.loadTestsFromTestCase(TestLoginPage))

        unittest.TextTestRunner(verbosity=1).run(suite)
