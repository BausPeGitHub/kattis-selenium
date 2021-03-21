from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

#going to kattis
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://open.kattis.com/")

#clicking register link
register = driver.find_element_by_link_text("register")
ActionChains(driver).move_to_element(register).click(register).perform()

#clicking the e-mail sign up button
email_sign_up = driver.find_element_by_css_selector("button.email")
ActionChains(driver).move_to_element(email_sign_up).click(email_sign_up).perform()

#clicking the sign up button
sign_up = driver.find_element_by_link_text("Sign up for a Kattis account")
ActionChains(driver).move_to_element(sign_up).click(sign_up).perform()

#entering name
element = driver.find_element_by_css_selector("input#name_input.form-control")
element.click()
element.send_keys("Just trolling Lucian Ilea")

#getting a temporary e-mail adress
driver2 = webdriver.Chrome(ChromeDriverManager().install())
driver2.get("https://temp-mail.org/en/")

email = driver2.find_element_by_css_selector("input#mail.emailbox-input.opentip")
sleep(10)
email.click()
email.send_keys(Keys.CONTROL + "c")
driver2.close()

#entering the email adress on kattis
element = driver.find_element_by_css_selector("input#email_input.form-control")
element.click()
element.send_keys(Keys.CONTROL + "v");

#entering password
password = "Bausanis69"
element = driver.find_element_by_css_selector("input#password_input")
element.click()
element.send_keys(password)

#entering password again
element = driver.find_element_by_css_selector("input#password_input2")
element.click()
element.send_keys(password)

#capcha
element = driver.find_element_by_css_selector("input#tos-accept")
element.click()

#clicking the submit button
submit = driver.find_element_by_css_selector("input#submit-button.btn.btn-default")
ActionChains(driver).move_to_element(submit).click(submit).perform()


#country selection
country_input = driver.find_element_by_css_selector("span#select2-chosen-2.select2-chosen")
country_input.click()
inp = driver.find_element_by_css_selector("input#s2id_autogen2_search.select2-input")
inp.send_keys("Romania")
inp.send_keys(Keys.ENTER)

#university selection
university_input = driver.find_element_by_css_selector("span#select2-chosen-6.select2-chosen")
university_input.click()
inp = driver.find_element_by_css_selector("input#s2id_autogen6_search.select2-input")
inp.send_keys("Technical University of Cluj-Napoca")
inp.send_keys(Keys.ENTER)

#clicking update button
update = driver.find_element_by_css_selector("input.kat-button.kat-primary.small")
update.click()