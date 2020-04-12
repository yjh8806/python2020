import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

def Getdata(code_list,page=None):
    # 영화 코드
    # code_list = code_list    
    # 현재 크롤링 중인 영화가 첫 번째 영화인지 여부
    # chk = False
    # 영화의 개수만큼 반복한다.
    df = pd.DataFrame()
    
    for code in code_list:
        # 1단계 : 해당 영화의 평점 페이지 수 계산
        # 접속한다.
        # code= 뒤의 %d를 지우고 원하는 영화코드를 입력해서 웹에서 검색해서 접속한다.
        site1 = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code={}&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false'.format(code)
        res1 = requests.get(site1)
        if res1.status_code == requests.codes.ok:
            # 코드를 잘 읽어 왔는지 확인하는 코드
            # html코드를 분석한다.
            bs1 = BeautifulSoup(res1.text, 'html.parser')
            score_total = bs1.find(class_='score_total')
            ems = score_total.find_all('em')
            # print(ems[0].text)
            score_total = int(ems[0].text.replace(',', ''))
            # replace하고 int로 자료형 변경해주어야 함
            print(score_total)
            # 페이지 수를 계산한다.
            pageCnt = score_total // 10
            print(pageCnt)
            # 한 페이지에 10개씩 들어가므로 나머지가 남으면 페이지 수 + 1해준다
            if score_total % 10 > 0:
                pageCnt += 1
            # 현재 페이지 번호(기본 page는 None으로 지정되어 있음)
            if page!=None and pageCnt>=page:
                pageCnt=page
                
            print(pageCnt)
            # 현재 페이지는 첫 번째 페이지로
            now_page = 1

            # 2단계 : 평점 글 정보와 평점을 가져온다.
            while now_page <= pageCnt:
                sleep(0.5) # 잠깐 쉬었다 실행
                
                print('%d / %d' % (now_page, pageCnt))
                # 요청 할 페이지의 주소
                site2 = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code={}&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'.format(code, now_page)
                res2 = requests.get(site2)
                if res2.status_code == requests.codes.ok:
                    # 코드 잘 읽었는지 확인
                    bs2 = BeautifulSoup(res2.text, 'html.parser')
                    score_result = bs2.find(class_='score_result')
                    lis = score_result.find_all('li')
                    
                    for obj in lis:
                        # 평점
                        star_score = obj.find(class_='star_score')
                        star_em = star_score.find('em')
                        star_score = int(star_em.text)
                        # 평가글
                        score_reple = obj.find(class_='score_reple')
                        reple_p = score_reple.find('span')
                        score_reple = reple_p.text.strip()
                        print(star_score, score_reple)
                        # 데이터를 누적한다
                        if score_reple=='' or score_reple=='관람객':
                            continue
                        else:
                            df = df.append([[score_reple, star_score]], ignore_index=True)
                    now_page += 1
    df.columns = ['text', 'star']
    return df