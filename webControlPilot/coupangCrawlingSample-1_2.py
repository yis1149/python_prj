from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# === 설정 ===
URL = 'https://www.coupang.com/vp/products/7666070794?itemId=23361506529&vendorItemId=86478559145'
#CHROME_DRIVER_PATH = '/path/to/chromedriver'  # <-- 본인의 크롬드라이버 경로로 수정하세요
MAX_PAGE = 5  # 가져올 최대 페이지 수

# === 크롬 옵션 설정 ===
options = Options()
options.add_argument("--headless")  # 브라우저 띄우지 않음
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# === 드라이버 실행 ===
#service = Service(CHROME_DRIVER_PATH)
#driver = webdriver.Chrome(service=service, options=options)
driver = webdriver.Chrome(options=options)
driver.get(URL)

# === 리뷰 탭으로 스크롤 ===
try:
    # 리뷰 섹션이 로드될 때까지 기다리기
    print("1")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'sdp-review__article__list js_reviewArticleReviewList'))
    )
    (print("2"))
    # 리뷰 섹션으로 스크롤
    review_section = driver.find_element(By.CLASS_NAME, 'sdp-review__article__list js_reviewArticleReviewList')
    # driver.execute_script("arguments[0].scrollIntoView(true);", review_section)
    print(review_section.text)  # 리뷰 섹션의 텍스트 출력 (디버깅용)
    time.sleep(2)
except:
    print("❌ 리뷰 섹션을 찾을 수 없습니다.")
    driver.quit()
    exit()

'''
# === 리뷰 추출 ===
reviews = []
for page in range(1, MAX_PAGE + 1):
    print(f"📄 {page}페이지 수집 중...")
    time.sleep(2)

    # 리뷰 내용 가져오기
    review_elements = driver.find_elements(By.CSS_SELECTOR, 'div.sdp-review__article__list__headline')
    for element in review_elements:
        text = element.text.strip()
        if text:
            reviews.append(text)

    # 다음 페이지 클릭
    try:
        next_btn = driver.find_element(By.CSS_SELECTOR, 'button.sdp-pagination__btn--next')
        if 'disabled' in next_btn.get_attribute('class'):
            print("⛔ 다음 페이지 없음.")
            break
        next_btn.click()
    except:
        print("⛔ 다음 버튼을 찾을 수 없습니다.")
        break

driver.quit()

# === 결과 저장 ===
df = pd.DataFrame({'Review': reviews})
df.to_csv('coupang_reviews.csv', index=False, encoding='utf-8-sig')
print("✅ 리뷰 수집 완료! 'coupang_reviews.csv'로 저장됨.")
'''