import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_step():
    # 通过环境变量获取邮箱和密码
    email = '1820888196@qq.com'
    password = 'liuxu520'
    step = random.randint(16000, 16999)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://yd.shuabu.cn/")
        
        # 使用WebDriverWait动态等待元素
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="确 定"]'))).click()

        # 输入账号、密码、步数
        wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Zepp账号："]/../div/input'))).send_keys(email)
        wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Zepp密码："]/../div/span/input'))).send_keys(password)
        wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="运动步数："]/../div/input'))).send_keys(str(step))

        # 提交
        wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="提 交"]'))).click()

        # 确认操作成功
        # 这里使用动态等待，等待"确定"按钮出现，然后进行点击
        wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="同步成功"]')))

        print(f"步数已刷：{step}步")

    except (NoSuchElementException, TimeoutException) as e:
        print(f"加载元素失败：{e}")
    except Exception as e:
        print(f"发生异常：{e}")
        # 不再打印堆栈信息，可根据实际需要添加
    finally:
        if 'driver' in locals():
            driver.quit()  # 确保WebDriver关闭，避免NameError异常

if __name__ == '__main__':
    get_step()
