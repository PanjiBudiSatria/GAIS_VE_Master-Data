from lib2to3.pgen2 import driver
import unittest
import time
from urllib import response
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestGroupGradePoints(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_group_grade_points_add(self):
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

        driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div/ul/li/a[3]/img").click()
        time.sleep(2)

        driver.find_element(By.XPATH,"//a[@title='Add Group Point']").click()
        time.sleep(1)

        driver.find_element(By.XPATH,"//input[@name='score_start']").send_keys("10")
        driver.find_element(By.XPATH,"//input[@name='score_end']").send_keys("20")
        driver.find_element(By.XPATH,"/html/body/div[13]/div[2]/form/table/tbody/tr[2]/td/input").send_keys("F")
        driver.find_element(By.XPATH,"/html/body/div[13]/div[2]/form/table/tbody/tr[3]/td/input").send_keys("Blacklist")
        driver.find_element(By.XPATH,"/html/body/div[13]/div[2]/form/table/tbody/tr[4]/td/button[1]").click()
        time.sleep(3)

        driver.find_element(By.XPATH,"/html/body/div[4]/div/form/table/tbody/tr[1]/td/input").send_keys("F")
        driver.find_element(By.XPATH,"/html/body/div[4]/div/form/table/tbody/tr[4]/td/button").click()
        time.sleep(1)

        response_data_rating = driver.find_element(By.XPATH,"/html/body/div[4]/div/div/table/tbody/tr/td[3]").text
        response_data_score = driver.find_element(By.XPATH,"/html/body/div[4]/div/div/table/tbody/tr/td[4]").text
        response_data_action = driver.find_element(By.XPATH,"/html/body/div[4]/div/div/table/tbody/tr/td[5]").text
        self.assertEqual(response_data_rating,"F")
        self.assertEqual(response_data_score,"10-20")
        self.assertEqual(response_data_action,"Blacklist")

        # response_data = driver.find_element(By.CSS_SELECTOR,"#change_unit > span").text
        # self.assertEqual(response_data,"Business Unit : PUTERA SAMPOERNA FOUNDATION (PSF)")

    def test_b_group_grade_points_edit(self):
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

        driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div/ul/li/a[3]/img").click()
        time.sleep(2)

        driver.find_element(By.XPATH,"/html/body/div[4]/div/form/table/tbody/tr[1]/td/input").send_keys("F")
        driver.find_element(By.XPATH,"/html/body/div[4]/div/form/table/tbody/tr[4]/td/button").click()
        time.sleep(1)

        driver.find_element(By.XPATH,"//a[@title='Edit Group Point']").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//input[@name='score_start']").clear()
        driver.find_element(By.XPATH,"//input[@name='score_end']").clear()
        driver.find_element(By.XPATH,"/html/body/div[13]/div[2]/form/table/tbody/tr[2]/td/input").clear()
        driver.find_element(By.XPATH,"/html/body/div[13]/div[2]/form/table/tbody/tr[3]/td/input").clear()
        time.sleep(1)
        driver.find_element(By.XPATH,"//input[@name='score_start']").send_keys("11")
        driver.find_element(By.XPATH,"//input[@name='score_end']").send_keys("21")
        driver.find_element(By.XPATH,"/html/body/div[13]/div[2]/form/table/tbody/tr[2]/td/input").send_keys("F")
        driver.find_element(By.XPATH,"/html/body/div[13]/div[2]/form/table/tbody/tr[3]/td/input").send_keys("Blacklist1")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[13]/div[2]/form/table/tbody/tr[4]/td/button[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH,"/html/body/div[4]/div/form/table/tbody/tr[1]/td/input").clear()
        driver.find_element(By.XPATH,"/html/body/div[4]/div/form/table/tbody/tr[1]/td/input").send_keys("F")
        driver.find_element(By.XPATH,"/html/body/div[4]/div/form/table/tbody/tr[4]/td/button").click()
        time.sleep(1)

        response_data_rating = driver.find_element(By.XPATH,"/html/body/div[4]/div/div/table/tbody/tr/td[3]").text
        response_data_score = driver.find_element(By.XPATH,"/html/body/div[4]/div/div/table/tbody/tr/td[4]").text
        response_data_action = driver.find_element(By.XPATH,"/html/body/div[4]/div/div/table/tbody/tr/td[5]").text
        self.assertEqual(response_data_rating,"F")
        self.assertEqual(response_data_score,"11-21")
        self.assertEqual(response_data_action,"Blacklist1")

    def test_c_group_grade_points_delete(self):
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
        time.sleep(2)

        driver.find_element(By.XPATH,"//img[@src='assets/images/btn/target-list.png']").click()
        time.sleep(1)

        driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div/ul/li/a[3]/img").click()
        time.sleep(2)

        driver.find_element(By.XPATH,"/html/body/div[4]/div/form/table/tbody/tr[1]/td/input").send_keys("F")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[4]/div/form/table/tbody/tr[4]/td/button").click()
        time.sleep(1)

        driver.find_element(By.XPATH,"//a[@title='Delete']").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//input[@value='OK']").click()
        time.sleep(2)

        driver.find_element(By.XPATH,"/html/body/div[4]/div/form/table/tbody/tr[1]/td/input").send_keys("F")
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[4]/div/form/table/tbody/tr[4]/td/button").click()
        time.sleep(1)

        response_data = driver.find_element(By.XPATH,"/html/body/div[4]/div/div/table/tbody/tr/td").text
        self.assertEqual(response_data,"-- Data not found --")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()