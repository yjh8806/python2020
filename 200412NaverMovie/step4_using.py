# step4_usgin.py
# from sklearn.linear_model import LogisticRegression
# from sklearn.feature_extraction.text import  TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import pickle
from time import time
import pandas as pd
# from konlpy.tag import *

def step4_using() :
    # 데이터를 읽어온다.
    with open('./data/pipe.dat', 'rb') as fp :
        pipe=pickle.load(fp)    # step3에서 저장한 pipe를 읽어와서 load한다.

    # 학습 정확도 측정
    y_pred = pipe.predict(["노잼"]) # 0이 나오면 재미없는, 1이 나오면 재밌는 감상평
    print("학습된 결과는",y_pred,"이므로 '재미없음'을 느낌")
    y_pred = pipe.predict(["정말 흥미진진함"])
    print(y_pred)
    y_pred = pipe.predict(["우와 정말 재미있어요. 한번더 보고 싶어요"])
    print(y_pred)
    y_pred = pipe.predict(["어이없다"])
    print(y_pred)
    y_pred = pipe.predict(["그닥"])
    print(y_pred)
    
    keyword = input("결과를 확인하고 싶은 단어나 문장을 입력 (결과는 0, 1) : ")
    y_pred = pipe.predict([keyword])
    print(y_pred)
    # 복사+붙여넣기로 문장을 넣어서 학습이 잘 되었는지 확인해보기
    # print('정확도 : %.3f' % accuracy_score(y_test, y_pred))
