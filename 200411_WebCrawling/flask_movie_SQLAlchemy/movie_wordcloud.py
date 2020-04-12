from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

def displayWordCloud(code,data = None, backgroundcolor = 'white', width=800, height=600 ):
    # 제외할 단어 지정
    stopwords_kr = ['있었다','것이다'] 
    wordcloud = WordCloud(
                        #font_path = '/Library/Fonts/NanumBarunGothic.ttf', 
                        font_path = '/opt/conda/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/ttf/NanumBarunGothic.ttf',
                        stopwords = stopwords_kr,
                        background_color = backgroundcolor, # 기본 인자값으로 white로 받았음. 추후 변경 가능
                        width = width, height = height).generate(data)
    #print(wordcloud.words_)
    # 이미지로 결과 저장
    print(os.getcwd())
    file_dir=os.path.dirname(os.path.realpath(__file__))
    os.path.dirname(os.path.realpath(__file__))
    file_name="img" + code + ".png"
    wordcloud.to_file(file_dir+"/static/img/"+file_name)