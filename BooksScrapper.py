from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
import time

author = "Arik Eindrok"
secction = "Novedades"
driver = Firefox()
driver.get('https://freeditorial.com/')
driver.implicitly_wait(1)
booklists = driver.find_elements(By.CLASS_NAME, "booklist")
links = []
for book_list in booklists:
    if secction in book_list.text[:20]:
        books = book_list.find_elements(By.CLASS_NAME, "book")
        for book in books:
            try:
                if author in book.find_element(By.CLASS_NAME,"book__author").text:
                    links.append(book.find_element(By.TAG_NAME, "li").
                                 find_element(By.TAG_NAME, "a").get_attribute("href"))
            except:
                pass
    break
for link in links:
    driver.get(link)
    for ele in driver.find_elements(By.TAG_NAME, "li"):
        if "PDF" in ele.text[:10]:
            ele.click()
            time.sleep(2)
            break

driver.quit()
