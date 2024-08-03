import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time,requests
import os
import requests
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, username, password, captcha):
    username_input = driver.find_element(By.CLASS_NAME, 'form-control')
    password_input = driver.find_element(By.ID, 'password-field')
    input_captcha = driver.find_element(By.XPATH, '//*[@id="page-top"]/header/div/div[2]/div/div/form/div[3]/div/input')
    login_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
    username_input.send_keys(username)
    password_input.send_keys(password)
    input_captcha.send_keys(captcha)
    login_button.click()
    time.sleep(2)


class Test_all_SO(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.get("http://")#link test
        time.sleep(3)

    def test_all(self):
        self.get_captcha_image()
        self.login_valid_credentials()
        self.create_order_so()
        # self.get_order_so()

    def get_captcha_image(self):
        cookies = self.driver.get_cookies()
        image_path = os.path.join("static/images", "captcha.jpg")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',  # Thay th? b?ng User Agent ph¨´ h?p
        }
        cookie_str = ""
        for cookie in cookies:
            cookie_str += f"{cookie['name']}={cookie['value']};"
        headers['Cookie'] = cookie_str
        response = requests.get("https://link captcha", headers=headers)
        if response.status_code == 200:
            with open(image_path, 'wb') as f:
                f.write(response.content)
        
    def login_valid_credentials(self):
        #send giá trị đăng nhập
        username = "user_name"
        password = "password"
        captcha = send_image_to_api('static/images/captcha.jpg')
        print("Captcha::: ", captcha.get('text'))
        username_input = self.driver.find_element(By.CLASS_NAME, 'form-control')
        password_input = self.driver.find_element(By.ID, 'password-field')
        input_captcha = self.driver.find_element(By.XPATH, '//*[@id="page-top"]/header/div/div[2]/div/div/form/div[3]/div/input')
        login_button = self.driver.find_element(By.CLASS_NAME, 'btn-primary')
        username_input.send_keys(username)
        time.sleep(1)
        password_input.send_keys(password)
        time.sleep(1)
        input_captcha.send_keys(captcha.get('text'))
        login_button.click()
        time.sleep(1)
        Next_conti = self.driver.find_element(By.XPATH , '//*[@id="continue-form"]/div[4]/button')
        Next_conti.click()
        time.sleep(3)

    def create_order_so(self, sleep = 0.5):
        path_pdf = 'path_pdf_send'
        #khai báo ngẫu nhiên các biến trong bảng nhập
        bu = 'bu_test'
        sales_office = 'sales_office_test'
        sales_area = random.choice(['Area1', 'Area2', 'Area3'])
        order_type = random.choice(['Type1', 'Type2', 'Type3'])
        sold_to_party = random.randint(1000, 9999)
        ship_to_party = random.randint(1000, 9999)
        po_no = 'PO' + str(random.randint(10000, 99999))
        material_name = 'Material' + str(random.randint(1, 100))
        customer_material_no = 'CustMaterial' + str(random.randint(1, 100))
        shipping_type = random.choice(['TypeA', 'TypeB', 'TypeC'])
        stor_location = random.choice(['Location1', 'Location2', 'Location3'])
        po_item = random.randint(1, 10)
        pq_no = 'PQ' + str(random.randint(100, 999))
        reference_no = 'Ref' + str(random.randint(1000, 9999))
        packingslip = 'Packing' + str(random.randint(1, 100))
        incoterm = random.choice(['Incoterm1', 'Incoterm2', 'Incoterm3'])
        po_rev = 'Rev' + str(random.randint(1, 5))
        location = random.choice(['LocationX', 'LocationY', 'LocationZ'])

        create_order = self.driver.find_element(By.ID, 'btn_create')
        create_order.click()
        time.sleep(4)

        input_bu = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[4]/input')
        input_bu.send_keys(bu)
        time.sleep(sleep)

        input_sales_office = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[5]/input')
        input_sales_office.send_keys(sales_office)
        time.sleep(sleep)

        input_sales_area = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[6]/input')
        input_sales_area.send_keys(sales_area)
        time.sleep(sleep)

        input_order_type = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[7]/input')
        input_order_type.send_keys(order_type)
        time.sleep(sleep)

        input_sold_to_party = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[8]/input')
        input_sold_to_party.send_keys(sold_to_party)
        time.sleep(sleep)

        input_ship_to_party = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[9]/input')
        input_ship_to_party.send_keys(ship_to_party)
        time.sleep(sleep)

        input_po_no = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[10]/input')
        input_po_no.send_keys(po_no)
        time.sleep(sleep)

        po_date_value = '04-11-2023'
        po_date = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[11]/input')
        po_date.send_keys(po_date_value)
        time.sleep(1)

        input_material_name = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[12]/input')
        input_material_name.send_keys(material_name)
        time.sleep(sleep)

        input_customer_material_no = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[13]/input')
        input_customer_material_no.send_keys(customer_material_no)
        time.sleep(sleep)

        order_quantity_value = '25'
        order_quantity = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[14]/input')
        order_quantity.send_keys(order_quantity_value)
        time.sleep(1)

        unit_price_value = '4'
        unit_price = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[15]/input')
        unit_price.send_keys(unit_price_value)
        time.sleep(1)

        input_shipping_type = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[18]/input')
        input_shipping_type.send_keys(shipping_type)
        time.sleep(sleep)

        input_stor_location = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[19]/input')
        input_stor_location.send_keys(stor_location)
        time.sleep(sleep)

        input_po_item = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[20]/input')
        input_po_item.send_keys(po_item)
        time.sleep(sleep)

        input_pq_no = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[21]/input')
        input_pq_no.send_keys(pq_no)
        time.sleep(sleep)

        input_reference_no = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[22]/input')
        input_reference_no.send_keys(reference_no)
        time.sleep(sleep)

        input_packingslip = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[23]/input')
        input_packingslip.send_keys(packingslip)
        time.sleep(sleep)

        input_incoterm = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[24]/input')
        input_incoterm.send_keys(incoterm)
        time.sleep(sleep)

        input_po_rev = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[25]/input')
        input_po_rev.send_keys(po_rev)
        time.sleep(sleep)

        input_location = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[27]/input')
        input_location.send_keys(location)
        time.sleep(sleep)
        
        source = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[1]/input')
        source.click()
        # time.sleep(sleep)

        target = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[2]/input')
        target.click()
        # time.sleep(3)

        back_home = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[3]/div/form/div/div/input[1]')
        back_home.send_keys(path_pdf)
        time.sleep(5)

      
        upload_pdf = self.driver.find_element(By.ID, 'inputGroupFileAddon01')
        upload_pdf.click()
        wait = WebDriverWait(self.driver, 5)
        alert = wait.until(EC.alert_is_present())
        alert.accept()
        time.sleep(sleep)

        ma_chuquancapphong = 'V1055463'
        input_capphong = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[4]/table/tbody/tr[2]/td[2]/input')
        input_capphong.send_keys(ma_chuquancapphong)
        time.sleep(2)

        button_kydongcap1 = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[4]/table/tbody/tr[2]/td[5]/button[2]')
        button_kydongcap1.click()
        time.sleep(2)

        ma_chuquancapphong1 = 'V1032437'
        input_capphong1 = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[4]/table/tbody/tr[3]/td[2]/input')
        input_capphong1.send_keys(ma_chuquancapphong1)
        time.sleep(2)

        ma_chuquancapbophan = 'V1008647'
        input_capbophan = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[4]/table/tbody/tr[5]/td[2]/input')
        input_capbophan.send_keys(ma_chuquancapbophan)
        time.sleep(2)

        select_sign = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[4]/div/div/div[2]/select')
        select_sign.click()
        time.sleep(2)

        select_sign_selenium_test = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[4]/div/div/div[2]/select/option[8]')
        select_sign_selenium_test.click()
        time.sleep(2)

        button_load_sign = self.driver.find_element(By.ID, 'add_group')
        button_load_sign.click()
        time.sleep(3)
        wait = WebDriverWait(self.driver, 5)
        alert = wait.until(EC.alert_is_present())
        alert.accept()

        submit_click = self.driver.find_element(By.ID, 'send_api')
        submit_click.click()
        time.sleep(2)
        wait = WebDriverWait(self.driver, 2)
        alert = wait.until(EC.alert_is_present())
        alert.accept()
        time.sleep(3)
        alert.accept()
        time.sleep(10)

    def upload_file_so(self):
        create_order = self.driver.find_element(By.ID, 'btn_create1')
        create_order.click()
        time.sleep(8)

    def get_order_so(self):
        input_order_name = 'SO_11032023110903742'
        create_order = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[2]/div[3]/button')
        create_order.click()
        time.sleep(5)
        create_order = self.driver.find_element(By.XPATH, '//*[@id="input_search_order"]')
        create_order.send_keys(input_order_name)
        time.sleep(5)
        create_order = self.driver.find_element(By.XPATH, '//*[@id="order-search"]/tr[1]/td[1]')
        create_order.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

class Test_all_debit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.get("http://link test")
        time.sleep(3)

    def test_all(self):
        self.debit_click()
        self.get_captcha_image()
        self.login_valid_credentials(5)
        # self.create_order_debit()
        # self.upload_file_debit()
        self.search_order_debit()
    
    def debit_click(self):
        debit = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div[2]/h1')
        debit.click()
        time.sleep(2)

    def get_captcha_image(self):
        cookies = self.driver.get_cookies()
        image_path = os.path.join("static/images", "captcha.jpg")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',  # Thay th? b?ng User Agent ph¨´ h?p
        }
        cookie_str = ""
        for cookie in cookies:
            cookie_str += f"{cookie['name']}={cookie['value']};"
        headers['Cookie'] = cookie_str
        response = requests.get("link get captcha", headers=headers)
        if response.status_code == 200:
            with open(image_path, 'wb') as f:
                f.write(response.content)
        
    def login_valid_credentials(self,sleep=2):
        #send giá trị đăng nhập
        username = "username"
        password = "password"
        captcha = send_image_to_api('static/images/captcha.jpg')
        print("Captcha::: ", captcha.get('text'))
        username_input = self.driver.find_element(By.CLASS_NAME, 'form-control')
        password_input = self.driver.find_element(By.ID, 'password-field')
        input_captcha = self.driver.find_element(By.XPATH, '//*[@id="page-top"]/header/div/div[2]/div/div/form/div[3]/div/input')
        login_button = self.driver.find_element(By.CLASS_NAME, 'btn-primary')
        username_input.send_keys(username)
        password_input.send_keys(password)
        input_captcha.send_keys(captcha.get('text'))
        login_button.click()
        time.sleep(sleep)
        Next_conti = self.driver.find_element(By.XPATH , '//*[@id="continue-form"]/div[4]/button')
        Next_conti.click()
        time.sleep(sleep)

    # def create_order_debit(self):
    #     Next_conti = self.driver.find_element(By.ID , 'new_order')
    #     Next_conti.click()
    #     time.sleep(5)

    # def upload_file_debit(self):
    #     create_order = self.driver.find_element(By.ID, 'upload_file')
    #     create_order.click()
    #     time.sleep(8)

    # def edit_order_debit(self):
    #     create_order = self.driver.find_element(By.ID, 'Edit_order')
    #     create_order.click()
    #     time.sleep(8)

    def search_order_debit(self):
        input_order_name = 'DebitDemand-2023-09-11-1-2664'
        create_order = self.driver.find_element(By.ID, 'search_order')
        create_order.click()
        time.sleep(2)
        create_order = self.driver.find_element(By.ID, 'input_search')
        create_order.send_keys(input_order_name)
        time.sleep(3)
        create_order = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/form/div/button')
        create_order.click()
        time.sleep(2)
        create_order = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/table/tbody/tr/td[1]/a')
        create_order.click()
        time.sleep(8)

    def tearDown(self):
        self.driver.quit()

def send_image_to_api(image_path):
    url = 'post image captcha'
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
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(Test_all_SO))
    # suite.addTest(loader.loadTestsFromTestCase(Test_all_debit))

    unittest.TextTestRunner(verbosity=1).run(suite)
