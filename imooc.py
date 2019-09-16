# @用户：李媛浩
# @名称 : imooc.py
# @编辑器: PyCharm
# @创建时间 : 2019/09/10/16:43



from selenium import webdriver
from PIL import Image
import unittest
from 识别验证码.chaojiying import Chaojiying_Client



class Login_test(unittest.TestCase):
    def setUp(self):
        print('测试开始')
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.url='https://www.imooc.com/'
        self.driver.get(self.url)

    def tearDown(self):
        print('测试结束')
        # self.driver.quit()

    def test_login(self):
        dian=self.driver.find_element_by_xpath('/html/body/div[8]/div/i').click()
        zhuce=self.driver.find_element_by_xpath('//*[@id="js-signup-btn"]')
        zhuce.click()
        user_input=self.driver.find_element_by_xpath('/html/body/div[11]/div[2]/form/div[1]/input')
        user_input.send_keys('18235233557')
        # pwd_input=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input')
        # pwd_input.send_keys('liyuanhao')
        self.driver.save_screenshot('page.png')
        image=self.driver.find_element_by_xpath('//*[@id="signup-form pr"]/div[2]/a[1]/img')
        loc=image.location
        
        size=image.size
        print(loc)
        print(size)

        left=loc['x']*1.25
        top=loc['y']*1.25
        right=(loc['x']+size['width'])*1.25
        button=(loc['y']+size['height'])*1.25

        page_pic=Image.open('page.png')
        loct=(left,top,right,button)
        yzm_pic=page_pic.crop(loct)
        yzm_pic.save('yzm.png')

        chaojiying = Chaojiying_Client('liyuanhao', 'liyuanhao', '901464')  # 用户中心>>软件ID 生成一个替换 96001
        im = open('yzm.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
        result=chaojiying.PostPic(im, 1902)
        print(result)
        code_pic=result['pic_str']
        yzm_input=self.driver.find_element_by_xpath('//*[@id="signup-form pr"]/div[2]/input')
        yzm_input.send_keys(code_pic)

        fang=self.driver.find_element_by_xpath('//*[@id="signup-protocol"]')
        fang.click()
        login_btn=self.driver.find_element_by_xpath('//*[@id="signup-btn"]')
        login_btn.click()



if __name__ == '__main__':
    unittest.main()
