# coding: utf-8
import unittest
import os
from time import sleep
from BaseOperate.run import run_testcaseYaml
from BaseOperate.getDriver import mdriver
from BaseOperate.grabLog import kill_logcat
from BaseOperate.Excel import Report


class Settings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = mdriver("settings")
        sleep(2)
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )
        app_yamlFolder = PATH('../common/testcaseyaml/settings/')
        # app_yamlFolder = os.path.join(os.getcwd(), 'common/testcaseYaml/settings/')
        cls.app_yamlFolder = app_yamlFolder
        cls.tag = "YOcSettings"
        print("settings Start")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("settings End")

    # def test_settings(self):      # 统一集成测试会导致一个case失败，剩余的case停止无法继续运行
    #     yamlFile_list = os.listdir(self.app_yamlFolder)
    #     yamlFile_list.sort()
    #     # print(yamlFile_list)
    #     for file in yamlFile_list:
    #         yamlFile = os.path.join(self.app_yamlFolder, file)
    #         print(yamlFile)
    #         # actualResult, resultOutput, testConclusion = run_testcaseYaml(self.driver, yamlFile).run_testcase(self.tag)
    #         # Report().worksheet2_write_data(yamlFile, actualResult, resultOutput, testConclusion)
    #         result_tuple = run_testcaseYaml(self.driver, yamlFile).run_testcase(self.tag)
    #         print(result_tuple)
    #         Report().worksheet2_write_data(yamlFile, result_tuple)

    def test_01_wifi(self):
        yamlFile = os.path.join(self.app_yamlFolder, '01_wifi.yaml')
        result_tuple = run_testcaseYaml(self.driver, yamlFile).run_testcase(self.tag)
        print(result_tuple)
        Report().worksheet2_write_data(yamlFile, result_tuple)

    # def test_06_drivingCollision(self):
    #     yamlFile = os.path.join(self.app_yamlFolder, '06_driving_collision.yaml')
    #     result_tuple = run_testcaseYaml(self.driver, yamlFile).run_testcase(self.tag)
    #     Report().worksheet2_write_data(yamlFile, result_tuple)

    # def test_o7_stopCollision(self):
    #     yamlFile = os.path.join(self.app_yamlFolder, '07_stop_collision.yaml')
    #     result_tuple = run_testcaseYaml(self.driver, yamlFile).run_testcase(self.tag)
    #     Report().worksheet2_write_data(yamlFile, result_tuple)


if __name__ == "__main__":
    unittest.main()
