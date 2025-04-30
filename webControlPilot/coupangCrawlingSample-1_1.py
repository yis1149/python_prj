# url 제공후 chatgpt로 크롤링 소스 생성요청
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs 
import time
import pandas as pd



def is_multiple_of_10(num):
    return num % 10 == 0

# 크롬 드라이버 옵션 설정
options = Options()
#options.add_argument('--headless')  # 브라우저 안 띄우기
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# 크롬 드라이버 경로
#driver_path = '/path/to/chromedriver'  # 크롬 드라이버 경로로 변경

# 스크래핑할 상품 URL
url = 'https://www.coupang.com/vp/products/7666070794?itemId=23361506529&vendorItemId=86478559145'

# 웹드라이버 실행
#driver = webdriver.Chrome(executable_path=driver_path, options=options)
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(3)

# 리뷰 탭으로 이동
#try:
    #review_tab = driver.find_element(By.XPATH, "//a[@data-tab-section='productReview']") # 해당 내용으로 못찾음
review_tab = driver.find_element(By.ID, 'btfTab')

print("1")
review_tab.click()
time.sleep(3)
#except:
#    print("리뷰 탭을 찾을 수 없습니다.")
#    driver.quit()
#    exit()

# 스크롤 또는 다음 페이지 탐색을 통한 리뷰 수집
review_cnt = driver.find_element(By.CLASS_NAME, 'product-tab-review-count').text.replace("(","").replace(")","").replace(",","")
review_page = int(review_cnt) / 5 
review_page_2 = int(review_cnt)%5 

reviews = []
page = 1

if review_page_2 > 0:
    review_page = int(review_page) + 1


review_page = 1  # 테스트용으로 페이지 수 조정

while page <= review_page:  # 원하는 만큼 페이지 수 조절 가능
    print(f"{page}페이지 수집 중...")
    time.sleep(2)

    #리뷰 페이지에서 리뷰 내용 추출

    review_elements = driver.find_elements(By.CLASS_NAME, 'sdp-review__article__list.js_reviewArticleReviewList')
    

    #review_elements = driver.find_elements(By.CLASS_NAME, 'sdp-review__article__list__headline')
    #review_elements = driver.find_elements(By.CLASS_NAME, 'sdp-review__article__list__info ')
    print("for문 before")
    print("reviewElementLen : " + str(len(review_elements)))
    
    element_idx = 0
    for element in review_elements:
        # print("for문 inner")
        #print("element_idx : " + str(element_idx))
        # try:
        print("try 1_0")
        #html = bs(element.text, 'html.parser')            
        print("element.text : " + element.text)
        # print(html)

        #구매자명
        #userNm = html.find('span', class_='sdp-review__article__list__info__user__name.js_reviewUserProfileImage')
        #print("userNm : " + str(userNm))
            #구매자ID
            #userId = html.find('span', class_='sdp-review__article__list__info__user__name.js_reviewUserProfileImage').get_attribute('data-member-id').text.strip()
            

            #멤버ID
            #리뷰점수
            #리뷰등록일
            #판매자
            #제품명
            #제품이미지
            #리뷰명
            #리뷰내용
            #리뷰Survey
            #리뷰Help


            # element_idx += 1

        # except:
        #     continue





''' #기존 리뷰 제목 가져오기 Start
    for element in review_elements:
        try:
            content = element.text.strip()
            if content:
                reviews.append(content)
        except:
            continue

    try:
        if is_multiple_of_10(page) and page>1:
            next_button = driver.find_element(By.CLASS_NAME, 'sdp-review__article__page__next')
            if 'disabled' in next_button.get_attribute('class'):
                break
            next_button.click()     
            page += 1       
        else:
            pageIdx = page%10
            next_button = driver.find_elements(By.CLASS_NAME, 'sdp-review__article__page__num')[pageIdx]
            if 'disabled' in next_button.get_attribute('class'):
                break
            next_button.click()
            page += 1
            
    except:
        print("다음 페이지 버튼 없음")
        break
        
    #기존 리뷰 제목 가져오기 End
''' 

driver.quit()

# 데이터 저장
df = pd.DataFrame({'Review': reviews})
df.to_csv('coupang_reviews.csv', index=False, encoding='utf-8-sig')

print("완료! coupang_reviews.csv 파일로 저장되었습니다.")
