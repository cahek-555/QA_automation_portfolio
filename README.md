> Alex from Dare IT Challenge - QA Automated Testing 🙂
# Task 1: Software configuration ✓
## Subtask 1: Why did I choose to participate in the Dare IT Challenge?

Hello to everyone who looked at me. 
The answer to the question is simple. I really like to automate everything, especially routine work. And the process of writing code causes only positive emotions.
I invite you to familiarize yourself with my work. 😎

# Task 2: Selectors ✓
| xpath for Login page             | I selector (selected) ✓                                  | II selector (excess) ✗                                                                                          | III selector (full XPath) ✗                             |
|----------------------------------|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| title_page_xpath                 | `//title`                                                | `//*[text()='Scouts panel - sign in']`                                                                          | `/html/head/title`                                      |
| title_form_xpath                 | `//div[@class='MuiCardContent-root']//h5`                | `//form//h5[1]`                                                                                                 | `/html/body/div/form/div/div[1]/h5`                     |
| login_field_xpath                | `//*[@id='login']`                                       | `//input[@name='login']`                                                                                        | `/html/body/div/form/div/div[1]/div[1]/div/input`       |
| password_field_xpath             | `//*[@id='password']`                                    | `//form//h5[1]//following-sibling::div//input[@type='password']`                                                | `/html/body/div/form/div/div[1]/div[2]/div/input`       |
| err_msg_invalid_xpath *          | `//div[@class='MuiCardContent-root']//span`              | `//span[@class='MuiTypography-root MuiTypography-caption MuiTypography-colorError MuiTypography-gutterBottom']` | `/html/body/div/form/div/div[1]/div[3]/span`            |
| remaind_password_hyperlink_xpath | `//div[@class='MuiCardContent-root']//a`                 | `//form/div/div[1]/a[contains(@class,'MuiLink-underlineHover')]`                                                | `/html/body/div/form/div/div[1]/a`                      |
| select_languages_xpath           | `//div[@class='MuiCardActions-root']//*[@role='button']` | `//div[@class='MuiCardActions-root']//*[text()='English' or text()='Polski']`                                   | `/html/body/div/form/div/div[2]/div`                    |
| select_lang_pl_xpath             | `//*[@value='pl']`                                       | `//button[@type='submit']//preceding-sibling::div/input[@value='pl']`                                           | `/html/body/div/form/div/div[2]/div/input[@value='pl']` |
| select_lang_en_xpath             | `//*[@value='en']`                                       | `//*[@class='MuiSelect-nativeInput' and @value='en']`                                                           | `/html/body/div/form/div/div[2]/div/input[@value='en']` |
| sign_in_button_xpath             | `//*[@type='submit']`                                    | `//span[@class='MuiButton-label']//ancestor::*[@type='submit']`                                                 | `/html/body/div/form/div/div[2]/button`                 |

> _*_ Can only be found if the account information is entered incorrectly

[//]: # (```javascript)
[//]: # (var s = "Syntax highlighting JavaScript";)
[//]: # (alert&#40;s&#41;;)
[//]: # (```)

[//]: # (click [ctrl] + [/])
