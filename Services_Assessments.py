from lib2to3.pgen2 import driver
import unittest
import time
from urllib import response
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

class TestGoodsAssessments(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_services_assessments_add(self):
        driver=self.driver
        driver.maximize_window()
        driver.get("http://10.9.98.65/gais65/")
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div[2]/div[6]/div/div/form/input[4]").send_keys("it.appsupport")
        time.sleep(1)
        driver.find_element(By.ID,"regularInput").send_keys("Gais432")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[2]/div[6]/div/div/form/div/button").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//input[@id='14']").click()
        time.sleep(3)
        driver.find_element(By.ID,"save").click()
        time.sleep(5)

        driver.find_element(By.XPATH,"//a[@data-id='427']").click()
        time.sleep(2)

        driver.find_element(By.XPATH,"//img[@src='assets/images/btn/button-master-data.gif']").click()
        time.sleep(1)

        driver.find_element(By.XPATH,"//img[@src='assets/images/btn/target-list.png']").click()
        time.sleep(1)

        driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div/ul/li/a[5]/img").click()
        time.sleep(2)

        driver.find_element(By.XPATH,"//a[@title='Add ']").click()
        time.sleep(1)

        driver.find_element(By.XPATH,"/html/body/div[13]/div[2]/form/table/tbody/tr[1]/td/input").send_keys("Item1")
        driver.find_element(By.XPATH,"/html/body/div[13]/div[2]/form/table/tbody/tr[2]/td/input").send_keys("testing desc")
        driver.find_element(By.XPATH,"//*[@id='form_input']/table/tbody/tr[3]/td/input").send_keys("10")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[13]/div[2]/form/table/tbody/tr[5]/td/table/tbody/tr[1]/td[2]/input[2]").send_keys("Description A")
        driver.find_element(By.XPATH,"/html/body/div[13]/div[2]/form/table/tbody/tr[5]/td/table/tbody/tr[2]/td[2]/input[2]").send_keys("Description B")
        driver.find_element(By.XPATH,"/html/body/div[13]/div[2]/form/table/tbody/tr[5]/td/table/tbody/tr[3]/td[2]/input[2]").send_keys("Description C")
        time.sleep(1)
        select = Select(driver.find_element(By.XPATH,"/html/body/div[13]/div[2]/form/table/tbody/tr[5]/td/table/tbody/tr[1]/td[3]/select"))
        select.select_by_visible_text('<=')
        select = Select(driver.find_element(By.XPATH,"/html/body/div[13]/div[2]/form/table/tbody/tr[5]/td/table/tbody/tr[2]/td[3]/select"))
        select.select_by_visible_text('>=')
        select = Select(driver.find_element(By.XPATH,"/html/body/div[13]/div[2]/form/table/tbody/tr[5]/td/table/tbody/tr[3]/td[3]/select"))
        select.select_by_visible_text('>=')
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[13]/div[2]/form/table/tbody/tr[5]/td/table/tbody/tr[3]/td[3]/input").clear()
        driver.find_element(By.XPATH,"/html/body/div[13]/div[2]/form/table/tbody/tr[5]/td/table/tbody/tr[3]/td[3]/input").send_keys("2")
        driver.find_element(By.XPATH,"/html/body/div[13]/div[2]/form/table/tbody/tr[6]/td/button").click()
        time.sleep(3)

        driver.find_element(By.XPATH,"/html/body/div[4]/div/form/table/tbody/tr[1]/td/input").send_keys("Item1")
        driver.find_element(By.XPATH,"/html/body/div[4]/div/form/table/tbody/tr[4]/td/button").click()
        time.sleep(1)

        response_data_item = driver.find_element(By.XPATH,"/html/body/div[4]/div/div/table/tbody/tr[1]/td[3]").text
        response_data_description = driver.find_element(By.XPATH,"/html/body/div[4]/div/div/table/tbody/tr[1]/td[4]").text
        response_data_weight = driver.find_element(By.XPATH,"/html/body/div[4]/div/div/table/tbody/tr[1]/td[5]").text
        self.assertEqual(response_data_item,"Item1")
        self.assertEqual(response_data_description,"testing desc")
        self.assertEqual(response_data_weight,"10")

        # response_data = driver.find_element(By.CSS_SELECTOR,"#change_unit > span").text
        # self.assertEqual(response_data,"Business Unit : PUTERA SAMPOERNA FOUNDATION (PSF)")

    def test_b_services_assessments_edit(self):
        driver=self.driver
        driver.maximize_window()
        driver.get("http://10.9.98.65/gais65/")
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div[2]/div[6]/div/div/form/input[4]").send_keys("it.appsupport")
        time.sleep(1)
        driver.find_element(By.ID,"regularInput").send_keys("Gais432")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[2]/div[6]/div/div/form/div/button").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//input[@id='14']").click()
        time.sleep(3)
        driver.find_element(By.ID,"save").click()
        time.sleep(5)

        driver.find_element(By.XPATH,"//a[@data-id='427']").click()
        time.sleep(2)

        driver.find_element(By.XPATH,"//img[@src='assets/images/btn/button-master-data.gif']").click()
        time.sleep(1)

        driver.find_element(By.XPATH,"//img[@src='assets/images/btn/target-list.png']").click()
        time.sleep(1)

        driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div/ul/li/a[5]/img").click()
        time.sleep(2)

        driver.find_element(By.XPATH,"/html/body/div[4]/div/form/table/tbody/tr[1]/td/input").send_keys("Item1")
        driver.find_element(By.XPATH,"/html/body/div[4]/div/form/table/tbody/tr[4]/td/button").click()
        time.sleep(2)

        driver.find_element(By.XPATH,"//a[@title='Edit ']").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='form_input']/table/tbody/tr[1]/td/input").clear()
        driver.find_element(By.XPATH,"//*[@id='form_input']/table/tbody/tr[1]/td/input").send_keys("Item1Rev1")
        driver.find_element(By.XPATH,"/html/body/div[13]/div[2]/form/table/tbody/tr[3]/td/input").clear()
        driver.find_element(By.XPATH,"/html/body/div[13]/div[2]/form/table/tbody/tr[3]/td/input").send_keys("15")
        driver.find_element(By.XPATH,"/html/body/div[13]/div[2]/form/table/tbody/tr[6]/td/button").click()
        time.sleep(2)

        driver.find_element(By.XPATH,"/html/body/div[4]/div/form/table/tbody/tr[1]/td/input").clear()
        driver.find_element(By.XPATH,"/html/body/div[4]/div/form/table/tbody/tr[1]/td/input").send_keys("Item1Rev1")
        driver.find_element(By.XPATH,"/html/body/div[4]/div/form/table/tbody/tr[4]/td/button").click()
        time.sleep(1)

        response_item = driver.find_element(By.XPATH,"/html/body/div[4]/div/div/table/tbody/tr/td[3]").text
        response_description = driver.find_element(By.XPATH,"/html/body/div[4]/div/div/table/tbody/tr/td[4]").text
        response_weight = driver.find_element(By.XPATH,"/html/body/div[4]/div/div/table/tbody/tr/td[5]").text
        self.assertEqual(response_item,"Item1Rev1")
        self.assertEqual(response_description,"testing desc")
        self.assertEqual(response_weight,"15")

    # def test_c_goods_assessments_delete(self):
    #     driver=self.driver
    #     driver.maximize_window()
    #     driver.get("http://10.9.98.65/gais65/")
    #     time.sleep(3)
    #     driver.find_element(By.XPATH,"/html/body/div[2]/div[6]/div/div/form/input[4]").send_keys("it.appsupport")
    #     time.sleep(1)
    #     driver.find_element(By.ID,"regularInput").send_keys("Gais432")
    #     time.sleep(1)
    #     driver.find_element(By.XPATH,"/html/body/div[2]/div[6]/div/div/form/div/button").click()
    #     time.sleep(3)
    #     driver.find_element(By.XPATH,"//input[@id='14']").click()
    #     time.sleep(3)
    #     driver.find_element(By.ID,"save").click()
    #     time.sleep(5)

    #     driver.find_element(By.XPATH,"//a[@data-id='427']").click()
    #     time.sleep(2)

    #     driver.find_element(By.XPATH,"//img[@src='assets/images/btn/button-master-data.gif']").click()
    #     time.sleep(1)

    #     driver.find_element(By.XPATH,"//img[@src='assets/images/btn/target-list.png']").click()
    #     time.sleep(1)

    #     driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div/ul/li/a[4]/img").click()
    #     time.sleep(2)

    #     driver.find_element(By.XPATH,"/html/body/div[4]/div/form/table/tbody/tr[1]/td/input").clear()
    #     driver.find_element(By.XPATH,"/html/body/div[4]/div/form/table/tbody/tr[1]/td/input").send_keys("Item1Rev1")
    #     driver.find_element(By.XPATH,"/html/body/div[4]/div/form/table/tbody/tr[4]/td/button").click()
    #     time.sleep(1)

    #     driver.find_element(By.XPATH,"//a[@title='Delete']").click()
    #     time.sleep(1)
    #     driver.find_element(By.XPATH,"//*[@id='popup_ok']").click()
    #     time.sleep(2)

    #     response_data = driver.find_element(By.XPATH,"/html/body/div[4]/div/div/table/tbody/tr/td").text
    #     self.assertEqual(response_data,"-- Data not found --")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()