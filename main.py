import time
import os
import unittest
from selenium import webdriver
from platform import system
import pickle
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SeleniumDriver(object):
    def __init__(
        self,
        # chromedriver path
        driver_path='./chrome_driver/chromedriver_win32/chromedriver.exe',
        # pickle file path to store cookies
        cookies_file_path='./Cookies',
        # list of websites to reuse cookies with
        cookies_websites=["https://tinhte.vn"]

    ):
        self.driver_path = driver_path
        self.cookies_file_path = cookies_file_path
        self.cookies_websites = cookies_websites
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(
            executable_path=self.driver_path,
            options=chrome_options
        )
        try:
            # load cookies for given websites
            cookies = pickle.load(open(self.cookies_file_path, "rb"))
            for website in self.cookies_websites:
                self.driver.get(website)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
                self.driver.refresh()
        except Exception as e:
            # it'll fail
            # for the first time, when cookie file is not present
            print(str(e))
            print("Error loading cookies")

    def save_cookies(self):
        # save cookies
        cookies = self.driver.get_cookies()
        pickle.dump(cookies, open(self.cookies_file_path, "wb"))

    def close_all(self):
        # close all open tabs
        if len(self.driver.window_handles) < 1:
            return
        for window_handle in self.driver.window_handles[:]:
            self.driver.switch_to.window(window_handle)
            self.driver.close()

    def quit(self):
        self.save_cookies()
        self.close_all()


def tinhte_login(driver):
    # driver.get("https://tinhte.vn")
    # if len(driver.find_elements_by_class_name("jsx-1783754700.blue-switch.header-mode")) == 1:
    #     return True
    # try:
    #     search = WebDriverWait(self.driver, 5).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, "jsx-3593820457.thread-login")))
    # except:
    #     self.driver.quit()
    # search.click()
    driver.find_elements_by_class_name("jsx-3867722346")[0].click()
    driver.find_elements_by_class_name("jsx-3867722346")[7].click()
    driver.find_elements_by_name("login")[1].send_keys("ndphuoc3701")
    driver.find_elements_by_name("password")[1].send_keys("abcd12345")
    driver.find_elements_by_class_name("primary")[2].click()


class TinhTeAutomationTesting(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        if system() == 'Windows':
            self.PATH = "./chrome_driver/chromedriver_win32/chromedriver.exe"
        elif system() == 'Linux':
            self.PATH = "./chrome_driver/chromedriver_linux64/chromedriver"
        elif system() == 'Darwin':
            self.PATH = "./chrome_driver/chromedriver_mac64/chromedriver"
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.get("https://tinhte.vn")

        print("==========================START-TEST==========================")

    def login_(self):
        # self.driver.close()
        # seleniumObj = SeleniumDriver(driver_path=self.PATH)
        # self.driver = seleniumObj.driver
        # if tinhte_login(self.driver):
        #     print("Already logged in")
        # else:
        #     print("Not logged in. Login")
        #     seleniumObj.save_cookies()
        tinhte_login(self.driver)

    def search_(self, str):
        searchButton = self.driver.find_element_by_class_name("placeholder")
        searchButton.click()

        searchTextBox = self.driver.find_element_by_class_name(
            "search-textbox")
        searchTextBox.send_keys(str)
        searchTextBox.send_keys(Keys.RETURN)
        # time.sleep(10)

    # def test_search_S0C(self):
    #     """Search without a character."""
    #     self.search_("")

    # def test_search_S1C(self):
    #     """Search with text have an only character."""
    #     self.search_("k")

    # def test_search_SOneorMoreSpace(self):
    #     """Search with text have only one or more space character."""
    #     self.search_("a simple string")

    # def test_search_SNoSpace(self):
    #     """Search a string and no space character."""
    #     self.search_("aSimpleString")

    # def test_search_SSpace(self):
    #     """Search a string with space character."""
    #     self.search_("    ")

    # def test_search_SUnicode(self):
    #     """Search a string with unicode character."""
    #     self.search_("con chó mùa thu")

    # def test_search_SLink(self):
    #     """Search a link."""
    #     self.search_("https://www.google.com/")

    # def test_search_Shieroglyphics(self):
    #     """Search a link."""
    #     self.search_("ベトナム人")

    # def makeMessage(self, participants, title, paragraph):
    #     try:
    #         search = WebDriverWait(self.driver, 5).until(
    #             EC.presence_of_element_located((By.CLASS_NAME, "jsx-2504361010.main")))
    #     except:
    #         self.driver.quit()
    #     # self.driver.find_element_by_class_name("jsx-2504361010.main").click()
    #     try:
    #         search = WebDriverWait(self.driver, 5).until(
    #             EC.presence_of_element_located((By.CLASS_NAME, "jsx-3867722346.main")))
    #     except:
    #         self.driver.quit()
    #     # self.driver.find_element_by_class_name("jsx-3867722346.view-all-btn").click()
    #     self.driver.find_element_by_class_name("callToAction").click()
    #     participantBox = self.driver.find_element_by_id("ctrl_recipients")

    #     for participant in participants:
    #         participantBox.send_keys(participant)
    #         time.sleep(1)
    #         participantBox.send_keys(Keys.RETURN)

    #     titleBox = self.driver.find_element_by_id("ctrl_title")
    #     titleBox.send_keys(title)

    #     iframe = self.driver.find_element_by_tag_name("iframe")
    #     self.driver.switch_to.frame(iframe)
    #     pTag = self.driver.find_element_by_tag_name("p")
    #     self.driver.execute_script(
    #         "arguments[0].textContent = arguments[1];", pTag, paragraph)

    #     self.driver.switch_to.default_content()

    #     writeBtn = self.driver.find_elements_by_class_name("button.primary")[1]
    #     writeBtn.click()
    #     # time.sleep(10)

    # def test_CMFullComplete(self):
    #     """Create a message with at least one participants and message not empty"""
    #     self.login_()
    #     self.makeMessage(["hi", "hehe"], "hello", "Tui la An ne")

    # def test_CMWithoutPar(self):
    #     """Create a message without participants"""
    #     self.login_()
    #     self.makeMessage([], "Hello", "Lai la tui day")

    # def test_CMWithoutMess(self):
    #     """Create a message without text field"""
    #     self.login_()
    #     self.makeMessage(["ankun"], "Hello", "")

    # def test_CMWithUnvalidPar(self):
    #     """Create a message with a not valid recipient."""
    #     self.login_()
    #     self.makeMessage(["conchomuathumuadongmuaha"],"Hello", "Lai la tui day")

    # def test_CMWithUnValidTitle(self):
    #     """Create a message with a not valid recipient."""
    #     self.login_()
    #     self.makeMessage(["ankun"],"", "Lai la tui day")

    def makeReview(self, title, price, description, like, dislike, advice, isSendImg=True):
        self.driver.find_element_by_class_name("jsx-817685855.cta").click()
        txtBox = self.driver.find_elements_by_class_name(
            "review-editor-text-input")
        txtBox[0].send_keys(title)
        txtBox[1].send_keys(price)
        txtBox[2].send_keys(description)
        txtBox[3].send_keys(like)
        txtBox[4].send_keys(dislike)
        txtBox[5].send_keys(advice)
        section = self.driver.find_elements_by_class_name(
            "jsx-2282145060.section-container")
        img = section[3].find_element_by_tag_name("input")
        self.driver.execute_script(
            "arguments[0].setAttribute('style','display:')", img)
        if isSendImg:
            img.send_keys(os.getcwd() + ("\image.png" if system()
                          == 'Windows' else "/image.png"))
            time.sleep(5)

    def test_RVFullComplete(self):
        """Create a review full infomation"""
        self.login_()
        self.makeReview("iPhone 12 Pro Max", "19 triệu VND", "To, 1 pin, màn hình rộng, RAM 8GB",
                        "Mình thích thiết kế của nó, đẹp, gọn, màn hình rất sáng, camera chụp rất đẹp",
                        "Màn hình hơi nhỏ", "Nên mua")
        self.driver.find_element_by_class_name(
            "jsx-2282145060.toolbar-save-button").click()
        time.sleep(10)
        self.assertTrue(len(self.driver.find_elements_by_class_name(
            "jsx-1378818985.thread-is-draft")) == 1)

    # def test_RVWithoutName(self):
    #     """Create a review without a product name"""
    #     self.login_()
    #     self.makeReview("", "19 triệu VND", "To, 1 pin, màn hình rộng, RAM 8GB",
    #         "Mình thích thiết kế của nó, đẹp, gọn, màn hình rất sáng, camera chụp rất đẹp",
    #         "Màn hình hơi nhỏ", "Nên mua")
    #     # time.sleep(10)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("jsx-2282145060.error")) == 1)

    # def test_RVWithoutImage(self):
    #     """Create a review without a product name"""
    #     self.login_()
    #     self.makeReview("IP12", "19 triệu VND", "To, 1 pin, màn hình rộng, RAM 8GB",
    #         "Mình thích thiết kế của nó, đẹp, gọn, màn hình rất sáng, camera chụp rất đẹp",
    #         "Màn hình hơi nhỏ", "Nên mua", False)
    #     self.driver.find_element_by_class_name("jsx-2282145060.toolbar-save-button").click()
    #     # time.sleep(10)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("jsx-1378818985.thread-is-draft")) == 1)

    # def test_RVEdit(self):
    #     """Edit a review exist"""
    #     self.login_()
    #     self.makeReview("IP12", "19 triệu VND", "To, 1 pin, màn hình rộng, RAM 8GB",
    #         "Mình thích thiết kế của nó, đẹp, gọn, màn hình rất sáng, camera chụp rất đẹp",
    #         "Màn hình hơi nhỏ", "Nên mua")
    #     self.driver.find_element_by_class_name("jsx-2282145060.toolbar-save-button").click()
    #     time.sleep(5)
    #     self.driver.find_element_by_class_name("jsx-2176532799.moderator-action__button").click()
    #     self.driver.find_element_by_class_name("jsx-2282145060.toolbar-save-button").click()
    #     # time.sleep(10)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("jsx-1378818985.thread-is-draft")) == 1)

    # def test_RVDelete(self):
    #     """Delete a review exist"""
    #     self.login_()
    #     self.makeReview("IP12", "19 triệu VND", "To, 1 pin, màn hình rộng, RAM 8GB",
    #         "Mình thích thiết kế của nó, đẹp, gọn, màn hình rất sáng, camera chụp rất đẹp",
    #         "Màn hình hơi nhỏ", "Nên mua")
    #     self.driver.find_element_by_class_name("jsx-2282145060.toolbar-save-button").click()
    #     time.sleep(5)
    #     self.driver.find_elements_by_class_name("jsx-1378818985.moderator-action__button")[3].click()
    #     # time.sleep(10)
    #     self.assertTrue(len(self.driver.find_elements_by_id("ctrl_reason")) == 1)

    # def commentReview(self, content):
    #     self.driver.get("https://tinhte.vn/thread/review-iphone-12-pro-max.3327910/")
    #     txtBox = self.driver.find_elements_by_class_name("post-reply-input")[1]
    #     txtBox.click()
    #     txtBox.send_keys(content)

    # def test_CoRP1(self):
    #     """Comment on review as a guest"""
    #     self.login_()

    # def test_CoRP2(self):
    #     """Comment blank"""
    #     self.commentReview("Review của bạn thật là xịn")
    #     if len(self.driver.find_elements_by_class_name("jsx-3593820457.post-reply-submit.active")) != 0:
    #         # self.driver.find_element_by_class_name("jsx-3593820457.post-reply-submit.active").click()
    #         self.assertTrue(False)
    #     else:
    #         self.assertTrue(True)

    # def test_CoRP3(self):
    #     """Comment with whitespace only"""
    #     self.commentReview("Review của bạn thật là xịn")
    #     if len(self.driver.find_elements_by_class_name("jsx-3593820457.post-reply-submit.active")) != 0:
    #         self.driver.find_element_by_class_name("jsx-3593820457.post-reply-submit.active").click()
    #         if len(self.driver.find_elements_by_class_name("jsx-3593820457.error")) != 0:
    #             self.assertTrue(False)
    #         else:
    #             self.assertTrue(True)
    #     else:
    #         self.assertTrue(False)

    # def test_CoRP4(self):
    #     """Comment with hyperlink"""
    #     self.commentReview("https://stackoverflow.com/questions/36614118/python-selenium-sending-keys-into-textarea")
    #     if len(self.driver.find_elements_by_class_name("jsx-3593820457.post-reply-submit.active")) != 0:
    #         self.driver.find_element_by_class_name("jsx-3593820457.post-reply-submit.active").click()
    #         self.assertTrue(False)
    #     else:
    #         self.assertTrue(True)

    # def test_CoRP5(self):
    #     """Comment with hieroglyphics character"""
    #     self.commentReview("ベトナム人")
    #     if len(self.driver.find_elements_by_class_name("jsx-3593820457.post-reply-submit.active")) != 0:
    #         self.driver.find_element_by_class_name("jsx-3593820457.post-reply-submit.active").click()
    #         self.assertTrue(False)
    #     else:
    #         self.assertTrue(True)

    # def test_CoRP6(self):
    #     """Delete a comment"""
    #     self.login_()
    #     self.commentReview("hehehe")
    #     if len(self.driver.find_elements_by_class_name("jsx-3593820457.post-reply-submit.active")) != 0:
    #         self.driver.find_element_by_class_name("jsx-3593820457.post-reply-submit.active").click()
    #         buttons = self.driver.find_elements_by_class_name("jsx-2274533257.thread-action")
    #         buttons[2].click()
    #         self.driver.find_element_by_class_name("jsx-3932553558.button.active").click()
    #         self.assertTrue(True)
    #     else:
    #         self.assertTrue(False)

    # def test_CoRP7(self):
    #     """Delete a comment"""
    #     self.login_()
    #     self.commentReview("hehehe")
    #     if len(self.driver.find_elements_by_class_name("jsx-3593820457.post-reply-submit.active")) != 0:
    #         self.driver.find_element_by_class_name("jsx-3593820457.post-reply-submit.active").click()
    #         buttons = self.driver.find_elements_by_class_name("jsx-2274533257.thread-action")
    #         buttons[2].click()
    #         self.driver.find_element_by_class_name("jsx-3932553558.button.active").click()
    #         self.assertTrue(True)
    #     else:
    #         self.assertTrue(False)

    # def test_CoRP8(self):
    #     """Delete a comment"""
    #     self.login_()
    #     self.commentReview("hehehe")
    #     if len(self.driver.find_elements_by_class_name("jsx-3593820457.post-reply-submit.active")) != 0:
    #         self.driver.find_element_by_class_name("jsx-3593820457.post-reply-submit.active").click()
    #         buttons = self.driver.find_elements_by_class_name("jsx-2274533257.thread-action")
    #         buttons[2].click()
    #         self.driver.find_element_by_class_name("jsx-3932553558.button.active").click()
    #         self.assertTrue(True)
    #     else:
    #         self.assertTrue(False)

    # def test_CoRP9(self):
    #     """Delete a comment"""
    #     self.login_()
    #     self.commentReview("hehehe")
    #     if len(self.driver.find_elements_by_class_name("jsx-3593820457.post-reply-submit.active")) != 0:
    #         self.driver.find_element_by_class_name("jsx-3593820457.post-reply-submit.active").click()
    #         buttons = self.driver.find_elements_by_class_name("jsx-2274533257.thread-action")
    #         buttons[2].click()
    #         self.driver.find_element_by_class_name("jsx-3932553558.button.active").click()
    #         self.assertTrue(True)
    #     else:
    #         self.assertTrue(False)

    # def test_CoRP10(self):
    #     """Delete a comment"""
    #     self.login_()
    #     self.commentReview("hehehe")
    #     if len(self.driver.find_elements_by_class_name("jsx-3593820457.post-reply-submit.active")) != 0:
    #         self.driver.find_element_by_class_name("jsx-3593820457.post-reply-submit.active").click()
    #         buttons = self.driver.find_elements_by_class_name("jsx-2274533257.thread-action")
    #         buttons[2].click()
    #         self.driver.find_element_by_class_name("jsx-3932553558.button.active").click()
    #         self.assertTrue(True)
    #     else:
    #         self.assertTrue(False)

    # def test_CoRP11(self):
    #     """Delete a comment"""
    #     self.login_()
    #     self.commentReview("hehehe")
    #     if len(self.driver.find_elements_by_class_name("jsx-3593820457.post-reply-submit.active")) != 0:
    #         self.driver.find_element_by_class_name("jsx-3593820457.post-reply-submit.active").click()
    #         buttons = self.driver.find_elements_by_class_name("jsx-2274533257.thread-action")
    #         buttons[2].click()
    #         self.driver.find_element_by_class_name("jsx-3932553558.button.active").click()
    #         self.assertTrue(True)
    #     else:
    #         self.assertTrue(False)

    # def makePost(self,driver,paragraph):
    #     iframe = driver.find_element_by_tag_name("iframe")
    #     driver.switch_to.frame(iframe)
    #     pTag = driver.find_element_by_tag_name("p")
    #     driver.execute_script("arguments[0].textContent = arguments[1];", pTag, paragraph)
    #     driver.switch_to.default_content()
    #     textfield = driver.find_element_by_id("ctrl_location")
    #     textfield.send_keys(Keys.RETURN)

    # def fillPassText(self,driver,text,locator):
    #     textfield = driver.find_element_by_id(locator)
    #     textfield.clear()
    #     textfield.send_keys(text)

    # def fillText(self,driver,text,locator):
    #     textfield = driver.find_element_by_id(locator)
    #     textfield.clear()
    #     textfield.send_keys(text)
    #     textfield.send_keys(Keys.RETURN)
    #     time.sleep(1)

    # def test_CA(self):
    #     """ Change avatar """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.driver.find_element_by_class_name("img.m").click()
    #     time.sleep(2)
    #     s = self.driver.find_element_by_class_name("labelText")
    #     input_text= s.find_element_by_tag_name("input")
    #     input_text.send_keys(os.getcwd() + ("\image.jpg" if system() == 'Windows' else "/image.jpg"))
    #     time.sleep(5)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)

    # def test_CARIT(self):
    #     """ Change avatar with wrong image type """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.driver.find_element_by_class_name("img.m").click()
    #     time.sleep(1)
    #     s = self.driver.find_element_by_class_name("labelText")
    #     input_text= s.find_element_by_tag_name("input")
    #     input_text.send_keys(os.getcwd() + ("\image.jpg" if system() == 'Windows' else "/image.jpg"))
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 0)

    # def test_FPNT(self):
    #     """ Fill place with no text """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.fillText(self.driver,"","ctrl_location")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)

    # def test_FPWT(self):
    #     """ Fill place with text """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.fillText(self.driver,"66/7, Hùng Vương, phường 1, quận 10, TP.HCM","ctrl_location")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)

    # def test_FPWU(self):
    #     """ Fill place with unicode """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.fillText(self.driver,"ベトナムの都市","ctrl_location")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)

    # def test_FPWL(self):
    #     """ Fill place with numerous char"""
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.fillText(self.driver,"66/7, Hùng Vương, phường 1, quận 10, TP.HCM,MV không phải là một câu chuyện tình yêu mà như một khoảng hoài niệm về tuổi trẻ/ tuổi thơ ngây an nhiên (tiếng tút micro ở đầu và cuối clip như là mở đầu/kết thúc của một đoạn băng tư liệu ko liên quan gì đến accident).","ctrl_location")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 0)

    # def test_FJT(self):
    #     """ Fill job with text """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.fillText(self.driver,"Kỹ sư","ctrl_occupation")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)

    # def test_FJNT(self):
    #     """ Fill job with no text """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.fillText(self.driver,"","ctrl_occupation")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)

    # def test_FP(self):
    #     """Fill phone number"""
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.fillText(self.driver,"0919891230","ctrl_custom_field_citizenPhoneNumber")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)

    # def test_CSWT(self):
    #     # create share test 2
    #     # create share without character
    #     self.login_()
    #     self.createShare()
    #     postBtn = self.driver.find_elements_by_class_name("publish-btn")
    #     postBtn[0].click()
    #     time.sleep(3)

    # def test_FPE(self):
    #     """Fill phone number with Empty number """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.fillText(self.driver,"","ctrl_custom_field_citizenPhoneNumber")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)

    # def test_FPS(self):
    #     """ Fill string in phone number """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.fillText(self.driver,"Đây là 1 chuỗi","ctrl_custom_field_citizenPhoneNumber")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 0)

    # def test_FIU(self):
    #     """ Fill user's information """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.makePost(self.driver,"Tôi là Ankunkun")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)

    # def test_FIUC(self):
    #     """ Fill user's information with unicode """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.makePost(self.driver,"ベトナム人")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)

    # def test_FIUS(self):
    #     """ Fill user's information with special character """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.makePost(self.driver,"@#$%!")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)

    # def test_FIUI(self):
    #     """ Fill user's information with icon """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/personal-details")
    #     self.makePost(self.driver,"@@,:>,:)")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("content.baseHtml")) == 1)

    # def test_FA(self):
    #     """ Fill following account with text """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/following")
    #     self.fillText(self.driver,"Ankunkun","ctrl_users")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("username.StatusTooltip")) == 1)

    # def test_FAE(self):
    #     """ Fill following account with empty text """
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/following")
    #     time.sleep(1)
    #     self.fillText(self.driver,"","ctrl_users")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("errorOverlay")) == 1)

    # def test_FAU(self):
    #     """Fill following account with unicode"""
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/following")
    #     time.sleep(1)
    #     self.fillText(self.driver,"うずまきナルト","ctrl_users")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("errorOverlay")) == 1)

    # def test_FAL(self):
    #     """Fill following account with link"""
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/following")
    #     time.sleep(1)
    #     self.fillText(self.driver,"https://tinhte.vn/members/ankunkun.2693711/","ctrl_users")
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("errorOverlay")) == 1)

    # def test_CP(self):
    #     """Change password"""
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/security")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password_original")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password_confirm")
    #     confirm = self.driver.find_element_by_id("ctrl_password_confirm")
    #     confirm.send_keys(Keys.RETURN)
    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("errorOverlay")) == 0)

    # def test_CP8(self):
    #     """Change password with less than 8 character"""
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/security")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password_original")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password_confirm")
    #     confirm = self.driver.find_element_by_id("ctrl_password_confirm")
    #     confirm.send_keys(Keys.RETURN)

    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("errorOverlay")) == 0)

    # def test_CPES(self):
    #     """Change password with empty string"""
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/security")
    #     self.fillPassText(self.driver,"","ctrl_password_original")
    #     self.fillPassText(self.driver,"","ctrl_password")
    #     self.fillPassText(self.driver,"","ctrl_password_confirm")
    #     confirm = self.driver.find_element_by_id("ctrl_password_confirm")
    #     confirm.send_keys(Keys.RETURN)

    #     time.sleep(2)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("close.OverlayCloser"))==1)

    # def test_CPOP(self):
    #     """Change password with old password"""
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/security")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password_original")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password_confirm")
    #     confirm = self.driver.find_element_by_id("ctrl_password_confirm")
    #     confirm.send_keys(Keys.RETURN)

    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("errorOverlay")) == 0)

    # def test_CPWU(self):
    #     """Change password with unicode password"""
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/security")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password_original")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password")
    #     self.fillPassText(self.driver,"うずまきナルト","ctrl_password_confirm")
    #     confirm = self.driver.find_element_by_id("ctrl_password_confirm")
    #     confirm.send_keys(Keys.RETURN)

    #     time.sleep(1)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("errorOverlay")) == 0)

    # def test_CPW(self):
    #     """Change password with wrong confirm password"""
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/account/security")
    #     self.fillPassText(self.driver,"","ctrl_password_original")
    #     self.fillPassText(self.driver,"","ctrl_password")
    #     self.fillPassText(self.driver,"","ctrl_password_confirm")
    #     confirm = self.driver.find_element_by_id("ctrl_password_confirm")
    #     confirm.send_keys(Keys.RETURN)

    #     time.sleep(2)
    #     self.assertTrue(len(self.driver.find_elements_by_class_name("close.OverlayCloser"))==1)

    # def createFact(self):
    #     factBtn = self.driver.find_elements_by_class_name("create-fact")
    #     factBtn[0].click()
    #     time.sleep(2)

    # def createShare(self):
    #     self.createFact()
    #     shareBtn = self.driver.find_elements_by_class_name("switch-toggle")
    #     shareBtn[0].click()
    #     time.sleep(2)

    # def test_CFWC(self):
    #     # create fact test 1
    #     # create fact without character
    #     self.login_()
    #     self.createFact()
    #     postBtn = self.driver.find_elements_by_class_name("publish-btn")
    #     postBtn[0].click()
    #     time.sleep(3)

    # def test_CFLT(self):
    #     # create fact test 2
    #     #create fact with less than 10 charater
    #     self.login_()
    #     self.createFact()
    #     content = self.driver.find_elements_by_class_name("createTinhteFact")
    #     content[0].send_keys("testing")
    #     time.sleep(3)
    #     postBtn = self.driver.find_elements_by_class_name("publish-btn")
    #     postBtn[0].click()
    #     time.sleep(3)

    # def test_CFWFP(self):
    #     # create fact test 3
    #     # create fact with the wrong format picture
    #     self.login_()
    #     self.createFact()
    #     picBtn = self.driver.find_elements_by_class_name("image-picker")
    #     inputFile = picBtn[0].find_elements_by_tag_name("input")
    #     inputFile[0].send_keys(os.getcwd() + "\\image.txt")
    #     time.sleep(10)

    # def test_CFCFWT(self):
    #     # create fact test 4
    #     # create fact with the correct format but without text
    #     self.login_()
    #     self.createFact()
    #     picBtn = self.driver.find_elements_by_class_name("image-picker")
    #     inputFile = picBtn[0].find_elements_by_tag_name("input")
    #     inputFile[0].send_keys(os.getcwd() + "\\image.jpg")
    #     time.sleep(2)
    #     postBtn = self.driver.find_elements_by_class_name("publish-btn")
    #     postBtn[0].click()
    #     time.sleep(3)

    # def test_CFCFLT(self):
    #     # create fact test 5
    #     #create fact with the correct format but less than 10 character
    #     self.login_()
    #     self.createFact()
    #     picBtn = self.driver.find_elements_by_class_name("image-picker")
    #     inputFile = picBtn[0].find_elements_by_tag_name("input")
    #     inputFile[0].send_keys(os.getcwd() + "\\image.jpg")
    #     content = self.driver.find_elements_by_class_name("createTinhteFact")
    #     content[0].send_keys("testing")
    #     time.sleep(2)
    #     postBtn = self.driver.find_elements_by_class_name("publish-btn")
    #     postBtn[0].click()
    #     time.sleep(3)

    # def test_CFMT(self):
    #     # create fact test 6
    #     # create fact with more than 10 charater
    #     self.login_()
    #     self.createFact()
    #     content = self.driver.find_elements_by_class_name("createTinhteFact")
    #     content[0].send_keys("Software testing")
    #     time.sleep(2)
    #     postBtn = self.driver.find_elements_by_class_name("publish-btn")
    #     postBtn[0].click()
    #     time.sleep(3)

    # def test_CFMTP(self):
    #     # create fact test 7
    #     # create fact with more than 10 charater with picture
    #     self.login_()
    #     self.createFact()
    #     content = self.driver.find_elements_by_class_name("createTinhteFact")
    #     picBtn = self.driver.find_elements_by_class_name("image-picker")
    #     inputFile = picBtn[0].find_elements_by_tag_name("input")
    #     inputFile[0].send_keys(os.getcwd() + "\\image.jpg")
    #     content[0].send_keys("Software testing")
    #     time.sleep(2)
    #     postBtn = self.driver.find_elements_by_class_name("publish-btn")
    #     postBtn[0].click()
    #     time.sleep(5)

    # def test_CS(self):
    #     # create share test 1
    #     # switch to share mode
    #     self.login_()
    #     self.createShare()

    # def test_CSWT(self):
    #     # create share test 2
    #     # create share without character
    #     self.login_
    #     self.createShare()
    #     postBtn = self.driver.find_elements_by_class_name("publish-btn")
    #     postBtn[0].click()
    #     time.sleep(3)

    # def test_CSLT(self):
    #     # create share test 3
    #     # create share with less than 10 charater
    #     self.login_()
    #     self.createShare()
    #     content = self.driver.find_elements_by_tag_name("textarea")
    #     content[0].send_keys("testing")
    #     time.sleep(2)
    #     postBtn = self.driver.find_elements_by_class_name("publish-btn")
    #     postBtn[0].click()
    #     time.sleep(10)

    # def test_CSMT(self):
    #     # create share test 4
    #     # create share with more than 10 charater
    #     self.login_()
    #     self.createShare()
    #     content = self.driver.find_elements_by_tag_name("textarea")
    #     content[0].send_keys("Software testing")
    #     time.sleep(3)
    #     postBtn = self.driver.find_elements_by_class_name("publish-btn")
    #     postBtn[0].click()
    #     time.sleep(10)

    # def test_CSLSF(self):
    #     # create share test 5
    #     # create share click add link button then switch to Fact mode
    #     self.login_()
    #     self.createFact()
    #     shareBtn = self.driver.find_elements_by_class_name("switch-toggle")
    #     shareBtn[0].click()
    #     self.driver.find_elements_by_class_name("thread-background-switch")[0].click()
    #     time.sleep(1)
    #     shareBtn[0].click()
    #     time.sleep(3)

    # def test_CSTSF(self):
    #     # create share test 6
    #     # create share and click change theme button then switch to Fact mode
    #     self.login_()
    #     self.createFact()
    #     shareBtn = self.driver.find_elements_by_class_name("switch-toggle")
    #     shareBtn[0].click()
    #     self.driver.find_elements_by_class_name("thread-background-switch")[1].click()
    #     time.sleep(1)
    #     s = self.driver.find_elements_by_class_name("thread-background-image")
    #     s[0].click()
    #     time.sleep(1)
    #     shareBtn[0].click()
    #     time.sleep(3)

    # def test_CSWL(self):
    #     # create share test 7
    #     # Create share with link
    #     self.login_()
    #     self.createShare()
    #     content = self.driver.find_elements_by_tag_name("textarea")
    #     content[0].send_keys("Software testing")
    #     time.sleep(1)
    #     self.driver.find_elements_by_class_name("thread-background-switch")[0].click()
    #     time.sleep(1)
    #     self.driver.find_elements_by_class_name("link-input")[0].send_keys("https://www.youtube.com/channel/UCVJ6jQF0XOaBVTPCT-en2sw")
    #     time.sleep(2)
    #     postBtn = self.driver.find_elements_by_class_name("publish-btn")
    #     postBtn[0].click()
    #     time.sleep(3)

    # def test_CSWT(self):
    #     # create share test 8
    #     # create share with theme
    #     self.login_()
    #     self.createShare()
    #     self.driver.find_elements_by_class_name("thread-background-switch")[1].click()
    #     time.sleep(1)
    #     s = self.driver.find_elements_by_class_name("thread-background-image")
    #     s[0].click()
    #     time.sleep(1)
    #     content = self.driver.find_elements_by_tag_name("textarea")
    #     content[0].send_keys("Software testing")
    #     time.sleep(1)
    #     postBtn = self.driver.find_elements_by_class_name("publish-btn")
    #     postBtn[0].click()
    #     time.sleep(3)

    # def test_CSLP(self):
    #     # create share test 9
    #     # create share and test long post feature
    #     self.login_()
    #     self.createShare()
    #     self.driver.find_elements_by_class_name("category-selector-switch")[0].click()
    #     time.sleep(5)
    #     self.driver.find_elements_by_class_name("title-input")[0].send_keys("Ba rọi béo - Thầy giáo ba")
    #     time.sleep(1)
    #     self.driver.find_elements_by_class_name("ck-content")[0].send_keys("Baroibeo tên thật là Phan Tấn Trung, sinh năm 1989. Anh là rapper thế hệ F1 tự xưng. Baroibeo từng là tuyển thủ Liên Minh Huyền Thoại chuyên nghiệp và hiện tại là 1 streamer nổi tiếng Việt Nam. Hiện nay, kênh Youtube của Thầy Giáo Ba có khoảng nửa triệu người đăng ký còn trang Facebook thì cũng có tới hàng trăm ngàn lượt theo dõi. Phan BaRoiBeo Tấn Trung is a streamer and top laner for Academy SBTC. He is also known as Thầy Giáo Ba. He was previously known as 3RB, Teacher Ba and Ba Gà.")
    #     time.sleep(3)
    #     postBtn = self.driver.find_elements_by_class_name("save-button")
    #     postBtn[0].click()
    #     time.sleep(10)

    # def test_CSLPS(self):
    #     # create share test 10
    #     # create share and test save function in long post feature
    #     self.login_()
    #     self.createShare()
    #     self.driver.find_elements_by_class_name("category-selector-switch")[0].click()
    #     time.sleep(3)
    #     self.driver.find_elements_by_class_name("title-input")[0].send_keys("Ba rọi béo - Thầy giáo ba")
    #     time.sleep(1)
    #     self.driver.find_elements_by_class_name("ck-content")[0].send_keys("Baroibeo tên thật là Phan Tấn Trung, sinh năm 1989. Anh là rapper thế hệ F1 tự xưng. Baroibeo từng là tuyển thủ Liên Minh Huyền Thoại chuyên nghiệp và hiện tại là 1 streamer nổi tiếng Việt Nam. Hiện nay, kênh Youtube của Thầy Giáo Ba có khoảng nửa triệu người đăng ký còn trang Facebook thì cũng có tới hàng trăm ngàn lượt theo dõi. Phan BaRoiBeo Tấn Trung is a streamer and top laner for Academy SBTC. He is also known as Thầy Giáo Ba. He was previously known as 3RB, Teacher Ba and Ba Gà.")
    #     time.sleep(2)
    #     postBtn = self.driver.find_elements_by_class_name("toolbar-save-button")
    #     postBtn[0].click()
    #     time.sleep(3)

    # def test_CSLPAS(self):
    #     # create share test 11
    #     # create share and test and test auto save function in long post feature
    #     self.login_()
    #     self.createShare()
    #     self.driver.find_elements_by_class_name("category-selector-switch")[0].click()
    #     time.sleep(10)
    #     self.driver.find_elements_by_class_name("title-input")[0].send_keys("Ba rọi béo - Thầy giáo ba")
    #     time.sleep(1)
    #     self.driver.find_elements_by_class_name("ck-content")[0].send_keys("Baroibeo tên thật là Phan Tấn Trung, sinh năm 1989. Anh là rapper thế hệ F1 tự xưng. Baroibeo từng là tuyển thủ Liên Minh Huyền Thoại chuyên nghiệp và hiện tại là 1 streamer nổi tiếng Việt Nam. Hiện nay, kênh Youtube của Thầy Giáo Ba có khoảng nửa triệu người đăng ký còn trang Facebook thì cũng có tới hàng trăm ngàn lượt theo dõi. Phan BaRoiBeo Tấn Trung is a streamer and top laner for Academy SBTC. He is also known as Thầy Giáo Ba. He was previously known as 3RB, Teacher Ba and Ba Gà.")
    #     time.sleep(70) #After 1 minute, auto save function will enable

    # def test_CoT1(self):
    #     self.driver.get("https://tinhte.vn/thread/tai-sao-trai-tao-co-the-de-duoc-10-thang-ma-khong-hu.3328438/")
    #     try:
    #         search = WebDriverWait(self.driver, 5).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-3593820457.thread-login")))
    #     except:
    #         self.driver.quit()
    #     search.click()

    # def test_CoT2(self):
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/thread/tai-sao-trai-tao-co-the-de-duoc-10-thang-ma-khong-hu.3328438/")
    #     try:
    #         search = WebDriverWait(self.driver, 5).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-3593820457.post-reply-submit")))
    #     except:
    #         self.driver.quit()
    #     search.click()

    # def test_CoT3(self):
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/thread/tai-sao-trai-tao-co-the-de-duoc-10-thang-ma-khong-hu.3328438/")
    #     try:
    #         search = WebDriverWait(self.driver, 5).until(
    #         EC.presence_of_element_located((By.CLASS_NAME,"jsx-3593820457.post-reply-main ")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_tag_name("textarea")
    #     search.send_keys("                                                                      ")
    #     search = search.find_element_by_xpath("//button[contains( text( ), 'Đăng')]")
    #     search.click()

    # def test_CoT4(self):
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/thread/tai-sao-trai-tao-co-the-de-duoc-10-thang-ma-khong-hu.3328438/")
    #     try:
    #         search = WebDriverWait(self.driver, 5).until(
    #         EC.presence_of_element_located((By.CLASS_NAME,"jsx-3593820457.post-reply-main ")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_tag_name("textarea")
    #     search.send_keys("https://www.google.com")
    #     search = search.find_element_by_xpath("//button[contains( text( ), 'Đăng')]")
    #     search.click()

    # def test_CoT5(self):
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/thread/tai-sao-trai-tao-co-the-de-duoc-10-thang-ma-khong-hu.3328438/")
    #     try:
    #         search = WebDriverWait(self.driver, 5).until(
    #         EC.presence_of_element_located((By.CLASS_NAME,"jsx-3593820457.post-reply-main ")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_tag_name("textarea")
    #     search.send_keys("ベトナム人")
    #     search = search.find_element_by_xpath("//button[contains( text( ), 'Đăng')]")
    #     search.click()
    # def CoT5(self):
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/thread/tai-sao-trai-tao-co-the-de-duoc-10-thang-ma-khong-hu.3328438/")
    #     try:
    #         search = WebDriverWait(self.driver, 5).until(
    #         EC.presence_of_element_located((By.CLASS_NAME,"jsx-3593820457.post-reply-main ")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_tag_name("textarea")
    #     search.send_keys("ベトナム人")
    #     search = search.find_element_by_xpath("//button[contains( text( ), 'Đăng')]")
    #     search.click()

    # def test_Cot6(self):
    #     self.CoT5()
    #     time.sleep(2)
    #     self.driver.refresh()
    #     count = 2
    #     breaker = 0
    #     while(1):
    #         search = self.driver.find_element_by_class_name("jsx-1984507624.thread-comments__container")
    #         search = search.find_elements_by_class_name("jsx-1984507624")
    #         for each in search:
    #             number = each.find_elements_by_tag_name("button")
    #             if (len(number)>=5):
    #                 breaker += 1
    #                 break
    #         if breaker == 2:
    #             break
    #         time.sleep(2)
    #         self.driver.get("https://tinhte.vn/thread/tai-sao-trai-tao-co-the-de-duoc-10-thang-ma-khong-hu.3328438/page-"+str(count))
    #         count += 1
    #         if (count>10):
    #             break
    #     number[3].click()
    #     self.driver.find_element_by_class_name("jsx-3932553558.button.active").click()

    # def test_Cot7(self):
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/thread/tai-sao-trai-tao-co-the-de-duoc-10-thang-ma-khong-hu.3328438/")
    #     count = 2
    #     breaker = 0
    #     while(1):
    #         search = self.driver.find_element_by_class_name("jsx-1984507624.thread-comments__container")
    #         search = search.find_elements_by_class_name("jsx-1984507624")
    #         for each in search:
    #             number = each.find_elements_by_tag_name("button")
    #             if (len(number)>=5):
    #                 breaker += 1
    #                 break
    #         if breaker == 2:
    #             break
    #         time.sleep(2)
    #         self.driver.get("https://tinhte.vn/thread/tai-sao-trai-tao-co-the-de-duoc-10-thang-ma-khong-hu.3328438/page-"+str(count))
    #         count += 1
    #         if (count>10):
    #             break
    #     number[3].click()
    #     self.driver.find_element_by_class_name("jsx-3932553558.button.active").click()
    #     self.driver.find_element_by_xpath("//button[contains( text( ), 'Sửa')]").click()

    # def test_Cot10(self):
    #     self.login_()
    #     self.driver.get("https://tinhte.vn/thread/tai-sao-trai-tao-co-the-de-duoc-10-thang-ma-khong-hu.3328438/")
    #     self.driver.find_element_by_class_name("jsx-3529665607.sticker-button").click()
    #     time.sleep(2)
    #     search = self.driver.find_element_by_class_name("jsx-3529665607.stickers")
    #     search.find_elements_by_tag_name("button")[0].click()
    #     self.driver.find_element_by_class_name("jsx-3529665607.sticker-button").click()
    #     time.sleep(2)
    #     search = self.driver.find_element_by_class_name("jsx-3529665607.stickers")
    #     search.find_elements_by_tag_name("button")[1].click()

    # #Visit a thread by headline as a user
    # def test_VTasUH(self):
    #     self.login_()

    #     try:
    #         search = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_tag_name("article")
    #     search = search.find_element_by_tag_name("h3")
    #     search = search.find_element_by_tag_name("a")
    #     search.click()
    # # Visit a thread by image as a guest
    # def test_VTasGI(self):
    #     try:
    #         search = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_tag_name("a")
    #     search.click()

    # # Visit a thread by image as a registered user
    # def test_VTasUI(self):
    #     self.login_()
    #     try:
    #         search = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_tag_name("a")
    #     search.click()

    # # Visit author of a thread on home screen
    # def test_VTauthor(self):
    #     try:
    #         search = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_class_name("jsx-631305314.author")
    #     search.click()

    # # Visit author of  thread on thread screen
    # def test_Vauthor(self):
    #     try:
    #         search = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_tag_name("a")
    #     search.click()
    #     try:
    #         search = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-1378818985.info")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_class_name("jsx-1378818985.author-name")
    #     search = search.find_element_by_class_name("jsx-1378818985")
    #     search.click()

    # # Fast travel to a fragment of thread
    # def test_Fasttravel(self):
    #     count = 0
    #     while(1):
    #         try:
    #             listSearch= WebDriverWait(self.driver, 2).until(
    #             EC.presence_of_all_elements_located((By.CLASS_NAME, "jsx-3078623109.thumb ")))
    #         except:
    #             self.driver.quit()
    #         listSearch[count].click()
    #         try:
    #             search = WebDriverWait(self.driver, 4).until(
    #             EC.presence_of_element_located((By.CLASS_NAME, "jsx-1378818985.content-list")))
    #         except:
    #             self.driver.back()
    #             count += 1
    #             continue
    #         break
    #     search = search.find_element_by_class_name("jsx-1378818985")
    #     search.click()
    # # Visit advertisement
    # def test_Vads(self):
    #     try:
    #         search = WebDriverWait(self.driver, 3).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_tag_name("a")
    #     search.click()
    #     try:
    #         search = WebDriverWait(self.driver, 5).until(
    #         EC.presence_of_element_located((By.ID, "landing")))
    #     except:
    #         self.driver.quit()
    #     search.click()

    # # Visit most active user
    # def test_VAuser(self):
    #     try:
    #         search = WebDriverWait(self.driver, 3).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_tag_name("a")
    #     search.click()
    #     try:
    #         search = WebDriverWait(self.driver, 5).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-2501851499.active-user-list")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_class_name("jsx-984767296.active-user")
    #     search.click()

    # # Visit popular community
    # def test_VPcom(self):
    #     try:
    #         search = WebDriverWait(self.driver, 3).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_tag_name("a")
    #     search.click()
    #     try:
    #         search = WebDriverWait(self.driver, 5).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-938776874.main")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_class_name("jsx-938776874.item-container")
    #     search = search.find_element_by_class_name("jsx-938776874.item")
    #     search = search.find_element_by_tag_name("a")
    #     search.click()

    # # Bookmark thread as a guest
    # def test_BthreadG(self):
    #     try:
    #         search = WebDriverWait(self.driver, 3).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_tag_name("a")
    #     search.click()
    #     try:
    #         search = WebDriverWait(self.driver, 5).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-725335046.bookmark-button")))
    #     except:
    #         self.driver.quit()
    #     print(search.text)

    # # React love when logged in
    # def test_RLoveU(self):
    #     self.login_()
    #     try:
    #         search = WebDriverWait(self.driver, 3).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_tag_name("a")
    #     search.click()
    #     try:
    #         search = WebDriverWait(self.driver, 5).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-1378818985.thread-like")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_class_name("jsx-1378818985.thread-like__button")
    #     search = search.find_element_by_tag_name("svg")
    #     search.click()

    # # React love as a guest
    # def test_RLoveG(self):
    #     try:
    #         search = WebDriverWait(self.driver, 3).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_tag_name("a")
    #     search.click()
    #     try:
    #         search = WebDriverWait(self.driver, 5).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-1378818985.thread-like")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_class_name("jsx-1378818985.thread-like__button")
    #     search = search.find_element_by_tag_name("svg")
    #     search.click()

    # # Subcribe to author of thread as a registered user\
    # def test_SubcribeU(self):
    #     self.login_()
    #     try:
    #         search = WebDriverWait(self.driver, 3).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_tag_name("a")
    #     search.click()
    #     try:
    #         search = WebDriverWait(self.driver, 5).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-3973219579.follow-button-container")))
    #     except:
    #         self.driver.quit()
    #     time.sleep(2)
    #     search.click()

    # # Subcribe to author of thread as a guest
    # def test_SubcribeG(self):
    #     try:
    #         search = WebDriverWait(self.driver, 3).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_tag_name("a")
    #     search.click()
    #     try:
    #         search = WebDriverWait(self.driver, 5).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-3973219579.follow-button-container")))
    #     except:
    #         self.driver.quit()
    #     search.click()

    # # Share thread with no comment
    # def test_ShareU(self):
    #     self.login_()
    #     try:
    #         search = WebDriverWait(self.driver, 3).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_tag_name("a")
    #     search.click()
    #     try:
    #         search = WebDriverWait(self.driver, 5).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-3454747502.fact-share-button")))
    #     except:
    #         self.driver.quit()
    #     search.click()
    #     search = search.find_element_by_xpath("//button[contains( text( ), 'Chia sẻ')]")
    #     search.click()

    # # Share thread with extensive length
    # def test_ShareULC(self):
    #     self.login_()
    #     try:
    #         search = WebDriverWait(self.driver, 3).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_tag_name("a")
    #     search.click()
    #     try:
    #         search = WebDriverWait(self.driver, 5).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-3454747502.fact-share-button")))
    #     except:
    #         self.driver.quit()
    #     search.click()
    #     try:
    #         search = WebDriverWait(self.driver, 2).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "caption-text-input")))
    #     except:
    #         self.driver.quit()
    #     search.clear()
    #     search.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    #     # search = search.find_element_by_xpath("//button[contains( text( ), 'Chia sẻ')]")
    #     # search.click()

    # # Share thread as guest
    # def test_ShareG(self):

    #     try:
    #         search = WebDriverWait(self.driver, 3).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-631305314")))
    #     except:
    #         self.driver.quit()
    #     search = search.find_element_by_tag_name("a")
    #     search.click()
    #     try:
    #         search = WebDriverWait(self.driver, 5).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "jsx-3454747502.fact-share-button")))
    #     except:
    #         self.driver.quit()
    #     search.click()
    #     try:
    #         search = WebDriverWait(self.driver, 2).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "caption-text-input")))
    #     except:
    #         self.driver.quit()
    #     search.clear()
    #     search.send_keys("pycon")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
