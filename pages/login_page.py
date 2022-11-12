from pages.base_page import BasePage


class LoginPage(BasePage):
    title_page_xpath = "//title"
    title_form_xpath = "//div[@class='MuiCardContent-root']//h5"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    err_msg_invalid_xpath = "//div[@class='MuiCardContent-root']//span"
    remaind_password_hyperlink_xpath = "//div[@class='MuiCardContent-root']//a"
    select_languages_xpath = "//div[@class='MuiCardActions-root']//*[@role='button']"
    select_lang_pl_xpath = "//*[@value='pl']"
    select_lang_en_xpath = "//*[@value='en']"
    sign_in_button_xpath = "//*[@type='submit']"
    header_of_form = "Scouts Panel"
    expected_title = "Scouts panel - sign in"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def check_login_form_title(self):
        self.assert_element_text(self.title_form_xpath, self.header_of_form)
