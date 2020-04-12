from flask import Flask,request,render_template,redirect,url_for,jsonify
import naver_movie,movie_start,movie_wordcloud
import pandas as pd
from soynlp.noun import LRNounExtractor

app=Flask(__name__)

import sqlalchemy as sa

metadata = sa.MetaData()
data_table = sa.Table('movie', metadata,
                     sa.Column('code', sa.Integer, primary_key = True),
                     sa.Column('title', sa.String),
                     sa.Column('time', sa.Integer),
                     sa.Column('sdate', sa.String),
                     sa.Column('grade', sa.String),
                     sa.Column('audience', sa.Integer),
                     sa.Column('summary', sa.String),
                     sa.Column('thumb', sa.String)
)

from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:qwer1234@maria/test", encoding='utf-8')

@app.route('/')
def index():
    return render_template('bootstraptest.html')

@app.route('/movieinfo')
def movieinfo():
    return render_template('movieinfo.html')

@app.route('/moviesearch')
def moviesearch():
    try:
        df = naver_movie.naverMovie()
        df.to_sql(name='movie', con=engine, if_exists='replace',index=False)
        message = "Data Crawling 작업 완료"
    except Exception as ex:
        print(ex)
        message = "Data Crawling 작업 실패"
    return message

@app.route('/movielist')
def movielist():
    df=pd.read_sql('movie',engine)
    movielist= df.to_dict(orient="record")
    return render_template('movielist.html', movielist=movielist )

@app.route('/content/<code>')
def content(code):
    df=pd.read_sql_query(sa.select([data_table]).where(data_table.c.code == code) , engine) # c.code : c는 column
    movielist= df.to_dict(orient="record") # orient = "record" : 행단위로
    # df1=movie_start.Getdata([code],10)
    # movie_wordcloud.displayWordCloud(str(code),' '.join(df1['text'])) 
    return render_template('content.html', movielist=movielist)

@app.route('/movieword/<code>')
def movieword(code):
    df1=movie_start.Getdata([code],15)
    # Soynlp로 명사 추출
    noun_extractor = LRNounExtractor(verbose=True)
    noun_extractor.train(df1['text'])
    nouns = noun_extractor.extract()
    movie_wordcloud.displayWordCloud(str(code),' '.join(nouns))
    return "ok"

@app.route('/moviechart/<code>')
def moviechart(code):
      
    return "ok"


if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0',port=8891)