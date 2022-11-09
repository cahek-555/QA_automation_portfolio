from pages.base_page import BasePage


class AddPlayer(BasePage):
    name_input_xpath = '//*[@name="name"]'
    surname_input_xpath = '//*[@name="surname"]'
    leg_open_list_xpath = '//*[@id="mui-component-select-leg"]'
    leg_right_xpath = '//*[@id="menu-leg"]//li[1]'
    leg_left_xpath = '//*[@id="menu-leg"]//li[2]'
    age_input_xpath = '//*[@name="age"]'
    position_input_xpath = '//*[@name="mainPosition"]'
    submit_button_xpath = '//*[@type="submit"]'
