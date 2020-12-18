import requests
from bs4 import BeautifulSoup
import pymysql
import time
import datetime



def doSth():
    #反爬虫策略 模仿浏览器 控制访问频率和速度 

    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"
    print('连接到mysql服务器...')
    db = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", charset='utf8',database = 'steam')
    print('连接上了!')
    cursor = db.cursor()

    cursor.execute("DROP TABLE IF EXISTS STEAM")

    sql = """CREATE TABLE STEAM (
            ID int ,
            name varCHAR(100),
            picture MEDIUMBLOB,
            released_time varchar(100),
            price varchar(100),
            tablet BLOB,
            find_time varchar(100)
            )character set = utf8"""

    cursor.execute(sql)

    ###三级注释为测试后舍弃内容

    r = requests.get("https://store.steampowered.com/search/?os=win&filter=popularnew")
    soup = BeautifulSoup(r.text,"html.parser")

    count = 1

    game_names = soup.find_all('span',attrs={'class':'title'}) 
    released_times = soup.find_all('div',attrs={'class':'col search_released responsive_secondrow'})
    game_price_1s = soup.find_all('div',attrs={'class': 'col search_price_discount_combined responsive_secondrow'})
    game_dicounts = soup.find_all('div',attrs={'class':'col search_discount responsive_secondrow'}) 

    # # # game_price_2s = game_price_1s.find_all('span',attrs={'style':'#888888'})
    # # # game_prices = game_price_2s.find_all('strike')

    #名称
    # print('name')
    for game_name in game_names:
        time.sleep(60)
        cursor = db.cursor()
        cursor.execute('insert into steam (name) values (11);')
        print(game_name.string)
        sql = ('insert into steam (name) values (%s);')
        # name = game_name.string.strip()
        name = '11'
        cursor.execute(sql,name)
        print('******完成此条插入!')

        # name = td[1].text.strip()       # 直接从列表里取值
        # hex = td[2].text.strip()
        # # print u'颜色: ' + name + u'颜色值: '+ hex + u'背景色样式: ' + style
        # # print 'color: ' + name + '\tvalue: '+ hex + '\tstyle: ' + style
        # insert_color = ("INSERT INTO COLOR(Color,Value,Style)" "VALUES(%s,%s,%s)")
        # data_color = (name, hex, style)
        # cursor.execute(insert_color, data_color)
        # db.commit()

        # sql1 = 'select * from steam;'
        # print(cursor.execute(sql1))

        # cursor.execute("insert into steam(name)values" "('{}')".format(game_name.text))
        # print(cursor.execute("insert into steam(name)values" "('{}')".format(game_name.text)))
        # cursor.execute("insert into novel(sortname, novelname, imgurl, description, status, author)values"
        # "('{}', '{}', '{}', '{}', '{}', '{}')".format(sort, novel_name, img_url, u'这里是描述', status, author))
        db.commit
        # insert_color = ("INSERT INTO COLOR(Color,Value,Style)" "VALUES(%s,%s,%s)")
        # data_color = (name, hex, style)
        # cursor.execute(insert_color, data_color)
        # db.commit()
        # print '******完成此条插入!'

        print(count)
        count+=1

    #发行时间
    print('released_time')
    for released_time in released_times:
        print(released_time.string)

    #原价+现价 还要考虑free to play的情况，
    # for game_price_1 in game_price_1s:
    #     if "¥" in game_price_1 :
    #         price = game_price_1.text.split('¥',2)
    #         print('原价')
    #         print(price[1]) #原价
    #         print('现价')
    #         print(price[2]) #现价
    #     else: 
    #         print(game_price_1.text)

    for game_price_1 in game_price_1s:
        if "Free" in game_price_1.text:
            print(game_price_1.text.strip())
        elif "-" in game_price_1:
            continue
        else:
            price = game_price_1.text.split('¥',1)
            # print(price[1].strip())
            if "¥" in price[1]:
                price_1 = price[1].split('¥',1)
                # print('原价')
                # print(price_1[0].strip()) #原价
                # print('现价')
                print(price_1[1].strip()) #现价
            else:
                # print('原价')
                print(price[1].strip()) #原价
                


    # # # for game_price_1 in game_price_1s:
    # # #     # print(game_price_1.span.strike.string) 
    # # #     # str.split(' ', 1 )
    # # #     # print(game_price_1.text)
    # # #     print(price[1]) #原价

    # # # print('现价')
    # # # for game_price_1 in game_price_1s:
    # # #     print(price[2]) #现价

    #折扣信息
    # print('折扣信息')
    # for game_discount in game_dicounts:

    #     print(game_discount.text)


#每天八点运行
def time_ti(h=8, m=00):
    while True:
        now = datetime.datetime.now()
        # print(now.hour, now.minute)
        if now.hour == h and now.minute == m:
            doSth()
        # 每隔60秒检测一次
        time.sleep(60)
time_ti()


