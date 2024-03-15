from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 创建ChromeOptions对象并启用无头模式
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

# 打开网站
driver.get('https://music.163.com/#/song?id=1392155391')
# 设定起始页号
page_number = 1

# 定位元素框架
comment_frame = driver.switch_to.frame('g_iframe')

while page_number<260:

    # 滚动到页面底部，确保所有的评论都被加载
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # 等待一段时间，让评论加载
    sleep(2)
    
    # 定位评论和时间
    comments = driver.find_elements(By.CSS_SELECTOR, ".cnt.f-brk")
    times = driver.find_elements(By.CSS_SELECTOR, ".time.s-fc4")

    # 写入到文件
    with open(f'comments_page_{page_number}.txt', 'w', encoding='utf-8') as f:
        for comment in comments:
            # 提取评论用户名、文本、时间
            text = comment.text
            time = times[comments.index(comment)].text
            # 在控制台打印评论
            print(f'page_{page_number}:'+time+' '+text)
            # 写入文件
            f.write(time+' '+text + '\n')

    # 翻到下一页
    try:
        next_page_button = driver.find_element(By.CSS_SELECTOR, '.zbtn.znxt')
        next_page_button.click()
        page_number += 1
    except Exception as e:
        # 如果找不到 "下一页" 按钮，说明已经到达最后一页，跳出循环
        break
        
        # 事实上，他会一直在最后一个页面循环输出相同的结果
        # 解决方法1：手动终止程序，删除多余的txt
        # 解决方法2：写成for循环，硬编码最大页数
        # !!这里采用了硬编码最大页数的方法
    
# 关闭浏览器和结束 WebDriver 会话
driver.quit()