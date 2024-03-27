#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 SepineTam, Inc. All Rights Reserved 
#
# @Time    : 2024/3/26 16:41
# @Author  : 谭淞
# @Email   : xiaoyuluowork@gmail.com
# @File    : main.py
# @IDE     : PyCharm
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main(username, password):
    login_url = "https://newsso.shu.edu.cn/login/eyJ0aW1lc3RhbXAiOjE3MTE0NDY2NTMzNjg1MzYzNjMsInJlc3BvbnNlVHlwZSI6ImNvZGUiLCJjbGllbnRJZCI6IldVSFdmcm50bldZSFpmelE1UXZYVUNWeSIsInNjb3BlIjoiMSIsInJlZGlyZWN0VXJpIjoiaHR0cHM6Ly9jbXJqeXkuc2h1LmVkdS5jbi9Mb2dpblNTTy5hc3B4Iiwic3RhdGUiOiIifQ=="

    # 设置Firefox选项（如果需要）
    driver = webdriver.Chrome()
    driver.get(login_url)

    username_field = driver.find_element(By.ID, 'username')
    password_field = driver.find_element(By.ID, 'password')

    username_field.send_keys(username)
    password_field.send_keys(password)

    submit_button = driver.find_element(By.ID, "submit-button")
    submit_button.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'XingMing'))
    )

    # 如果需要，这里可以添加导航到特定页面的步骤
    try:
        late_btn = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.ID, "Msg"))
        )
        late_btn.click()

        # 执行确认操作
        driver.execute_script("confirmSubmit();")
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()

    except Exception as e:
        print(e, '???')


if __name__ == '__main__':
    account = "your_account"
    password = "<PASSWORD>"
    main(username=account, password=password)
