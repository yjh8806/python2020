# step3_learning.py
from sklearn.linear_model import LogisticRegression             # 회귀분석 베이스이지만 결과값을 두 가지 경우로 구분한다 (맞다 / 아니다)
from sklearn.feature_extraction.text import  TfidfVectorizer    # 자연어처리, 빈도 수가 낮을수록 가중치 높게, 빈도 수 높을수록 가중치는 낮게
from sklearn.pipeline import Pipeline                           # 관리하기 편함
from sklearn.metrics import accuracy_score                      # 정확도 체크용
import pickle                                                   # 쓰는 개체 그대로 저장할 수 있음 pipeline도 가능 / 이후, 똑같이 불러와서 비슷한 학습에 도움 가능
from time import time
import pandas as pd
from konlpy.tag import *                            

okt = Okt()

def tokenizer(text) :
    return okt.morphs(text) # 형태소 return

def step3_learning() :      # 실제 학습
    # 데이터를 읽어온다.
    train_df = pd.read_csv('./data/movie_train_data.csv') # 학습할 때 쓰는 파일
    test_df = pd.read_csv('./data/movie_test_data.csv')   # 테스트할 때 쓰는 파일

    X_train = train_df['text'].tolist() # dataframe은 그냥 넣어서 쓸 수 없으므로 .tolist()로 리스트 안에 넣는다
    y_train = train_df['star'].tolist()

    X_test = test_df['text'].tolist()
    y_test = test_df['star'].tolist()
    # 학습을 위한 객체를 생성한다.
    tfidf = TfidfVectorizer(lowercase=False, tokenizer=tokenizer) # tokenizer=tokenizer : 위의 def tokenizer(text)를 불러와서 사용함 
    # tfidf : 수치화 하는 작업
    logistic = LogisticRegression(C=10.0, penalty='l2', random_state=0,solver='lbfgs')
                # 회귀분석 베이스이지만 결과값을 두 가지 경우로 구분한다 (맞다 / 아니다 둘 중 하나로)
    pipe = Pipeline([('vect', tfidf), ('clf', logistic)])
                        # 처음 처리         그 다음 처리
    # 학습한다.
    stime = time()              # 학습에 걸리는 시간 check하기 위해서
    print("학습 시작")          
    pipe.fit(X_train, y_train)  # .fit() -> 학습 종료
    print("학습 종료")              
    etime = time()              
    print("총 학습 시간 : %d" % (etime - stime)) # 끝난 시간 - 시작 시간 = 총 학습 시간

    # 학습 정확도 측정
    y_pred = pipe.predict(X_test)                           # 학습한 내용을 Test함 / 가설에 의해서 나온 값 = y_pred (실제 값과 가설의 값을 비교해보자)
    print('정확도 : %.3f' % accuracy_score(y_test, y_pred))  # y_test : 정답, y_pred : 가설에 의해 나온 값 (비교한 값의 정확도를 보기 위함)

    # 객체 저장
    with open('./data/pipe.dat', 'wb') as fp : # 객체 저장을 위해 pipe.dat를 저장
        pickle.dump(pipe, fp)

    print('저장완료')
