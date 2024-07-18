import csv
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
web = Chrome()

url = f"https://iftp.chinamoney.com.cn/english/bdInfo/"
web.get(url)

# Bond Type=Treasury Bond
select_element1 = web.find_element(By.ID, "Bond_Type_select")
select = Select(select_element1)
select.select_by_index(1)

# Issue Year=2023
select_element2 = web.find_element(By.ID, "Issue_Year_select")
select = Select(select_element2)
select.select_by_index(2)

web.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/div/div[8]/a[1]')\
    .click()

tbody = web.find_element(By.TAG_NAME, "tbody")
time.sleep(1)
for i in range(8):
    with open('chinamoney.csv', 'a', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ISIN', 'Bond Code', 'Issuer', 'Bond Type', 'Issue Date', 'Latest Rating'])
        for row in tbody.find_elements(By.XPATH,'./tr'):
            row_data = []
            ISIN = row.find_element(By.XPATH, "./td[1]/span/a").text
            Bond_Code = row.find_element(By.XPATH, "./td[2]/span/a").text
            Issuer = row.find_element(By.XPATH, "./td[3]/span").text
            Bond_Type = row.find_element(By.XPATH, "./td[4]/span").text
            Issue_Date = row.find_element(By.XPATH, "./td[5]/span").text
            Latest_Rating = row.find_element(By.XPATH, "./td[6]/span").text

            row_data= [ISIN,Bond_Code,Issuer,Bond_Type,Issue_Date,Latest_Rating]
            writer.writerow(row_data)

    web.find_element(By.CSS_SELECTOR, '#pagi-bond-market > li.page-btn.page-next > a').click()

web.quit()



