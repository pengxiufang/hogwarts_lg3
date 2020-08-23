import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestFrom():
    def setup(self):
        #复用浏览器
        # option = Options()
        # option.debugger_address = "127.0.0.1:9222"
        # self.driver=webdriver.Chrome(executable_path="/Users/xiaopengpeng/software/chromedriver",options=option)
        self.driver=webdriver.Chrome(executable_path="/Users/xiaopengpeng/software/chromedriver")
        self.driver.implicitly_wait(30)
    def teardown(self):
        self.driver.quit()
    def test_contact(self):
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
        sleep(2)
    def test_cookie(self):
        # cookies = self.driver.get_cookies()
        # print(cookies)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies=[{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851244509316'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'OzQOsFL2dTdtuN-Tb-4aXWsjCOSvKRrfSCJhIq8Rw6XoyvKGj57-BerAVGMuuGYTOh050ZJqcpsK8SanDaeH_WaZzrMOFoG6LTZTtcI1ZHJ0FRiij8R7dKCQmDYnbeEjwHOZdOgdOQMsrA9m2l-av-5Loyz0UiBDpqUYqBLQg_lO8SW72OIsrrsyzbkLcGmHHkEMOAs4QsfCfBMpvWVPsisdbFZI8kmjR_SaCA2caMurCLjNmkd-6YrHoZjXaC5qQKyUNfbKar1ZryExXHFrTA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851244509316'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325092151683'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'D9neASXoWwABRK5c6_67Ha0YWbGYICcNJVZddfHlf8BMwQz-gp8DLDV5hgYQq4LG'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a4528135'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629655337.2, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1598112641,1598112809,1598118157,1598119338'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1598119338'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '3005970045131443'}, {'domain': '.qq.com', 'expiry': 1598205767, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1928089191.1598081582'}, {'domain': 'work.weixin.qq.com', 'expiry': 1598130351, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '73m254c'}, {'domain': '.qq.com', 'expiry': 1598119397, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1661191367, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.590742182.1598081582'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629599419, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1600711370, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}]
        for cookie in cookies:#cookie中不能识别小数，将其删掉
                if 'expiry' in cookie.keys():
                    cookie.pop('expiry')
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
    def test_cookie1(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        #shelve 小型数据库 对象持久化
        # cookies=[{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851244509316'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'OzQOsFL2dTdtuN-Tb-4aXWsjCOSvKRrfSCJhIq8Rw6XoyvKGj57-BerAVGMuuGYTOh050ZJqcpsK8SanDaeH_WaZzrMOFoG6LTZTtcI1ZHJ0FRiij8R7dKCQmDYnbeEjwHOZdOgdOQMsrA9m2l-av-5Loyz0UiBDpqUYqBLQg_lO8SW72OIsrrsyzbkLcGmHHkEMOAs4QsfCfBMpvWVPsisdbFZI8kmjR_SaCA2caMurCLjNmkd-6YrHoZjXaC5qQKyUNfbKar1ZryExXHFrTA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851244509316'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325092151683'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'D9neASXoWwABRK5c6_67Ha0YWbGYICcNJVZddfHlf8BMwQz-gp8DLDV5hgYQq4LG'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a4528135'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629655337.2, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1598112641,1598112809,1598118157,1598119338'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1598119338'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '3005970045131443'}, {'domain': '.qq.com', 'expiry': 1598205767, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1928089191.1598081582'}, {'domain': 'work.weixin.qq.com', 'expiry': 1598130351, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '73m254c'}, {'domain': '.qq.com', 'expiry': 1598119397, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1661191367, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.590742182.1598081582'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629599419, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1600711370, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}]
        db =shelve.open("mydb/logincookies") #将cookies保存在文件中
        # db['cookie'] = cookies
        cookies = db['cookie']
        for cookie in cookies:
                if 'expiry' in cookie.keys():
                    cookie.pop('expiry')
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
        db.close()
    def test_lead(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        db = shelve.open("mydb/logincookies")
        cookies = db['cookie']
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        db.close()
        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[2]').click()
        self.driver.find_element_by_xpath('//*[@id="js_upload_file_input"]').send_keys("/Users/xiaopengpeng/Desktop/雪球-自选设置/工作簿1.xlsx")
        assert "工作簿1.xlsx" == self.driver.find_element_by_xpath('//*[@id="upload_file_name"]').text
        sleep(3)
