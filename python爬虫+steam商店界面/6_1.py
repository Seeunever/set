import requests
from bs4 import BeautifulSoup
import pymysql
import time
import datetime
from itertools import zip_longest
from typing import List

user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"

print('连接到mysql服务器...')
db = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", charset='utf8',database = 'steam')
print('连接上了!')
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS STEAM")

# 检查mysql语句是否运行
# cursor.execute("drop table if exists yoyo")

sql = """CREATE TABLE STEAM (
    game_id varchar(100),
    game_name varCHAR(100),
    picture varchar(200),
    released_time varchar(100),
    price varchar(100),
    platform varchar(100),
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
pics = soup.find_all('div',attrs={'class':'col search_capsule'})
# tablet_win_s = soup.find_all('span',attrs={'class':'platform_img win'})
els = soup.find_all('div',attrs={'class':'col search_name ellipsis'})
# # #图片保存地址
# # # path = os.getcwd()+'\img'
# # # if not os.path.isdir(path):
# # #     os.makedirs(path)  # 判断没有此路径则创建
# # # print(path)

    # # # game_price_2s = game_price_1s.find_all('span',attrs={'style':'#888888'})
    # # # game_prices = game_price_2s.find_all('strike')

    #名称
    # print('name')
for (game_name,released_time,game_price_1,pic,el) in list(zip_longest(game_names,released_times,game_price_1s,pics,els)):
    # time.sleep(60)
    cursor = db.cursor()
    # cursor.execute('insert into steam (name) values (11);')
    print(pic.img.get('src'))

    # pic_save = requests.get(pic.img.get('src'))
    # with open(path+'.jpeg','wb') as f:
    #     f.write(r.content)
    # src=img[2].get('src')

    # # # r = requests.get(IMAGE_URL)
    # # # with open('./image/img2.png', 'wb') as f:
    # # #     f.write(r.content)     
    
    print(game_name.string)
    # sql = 'insert into steam (game_name) values %s;'
    name_now = game_name.text.strip()
    # add = cursor.execute(sql,name_now)
    released_time_now = released_time.text.strip()

    if "Free" in game_price_1.text:
            print(game_price_1.text.strip())
            price_now = game_price_1.text.strip()
    elif "-" in game_price_1:
         continue
    else:
        price = game_price_1.text.split('¥',1)
        price_now = game_price_1.text.strip()
            # print(price[1].strip())
        # if "¥" in price[1]:
        #     price_1 = price[1].split('¥',1)
        #         # print('原价')
        #         # print(price_1[0].strip()) #原价
        #         # print('现价')
        #     print(price_1[1].strip()) #现价
        #     price_now = price_1[1].strip()
        # else:
        #         # print('原价')
        #     print(price[1].strip()) #原价
        #     price_now = price[1].strip()


    platform_win = el.find('span',attrs={'class':'platform_img win'})
    platform_mac = el.find('span',attrs={'class':'platform_img mac'})
    platform_linux = el.find('span',attrs={'class':'platform_img linux'})
    print(platform_win,platform_mac,platform_linux)
    if ((platform_win != [] or platform_win is not None) and (platform_mac == [] or platform_mac is None) and (platform_linux == [] or platform_linux is None)):
        plat_now = 'win'
    elif ((platform_win != [] or platform_win is not None) and (platform_mac != [] or platform_mac is not None) and (platform_linux == [] or platform_linux is None)):
        plat_now = 'win,mac'
    elif ((platform_win != [] or platform_win is not None) and (platform_mac == [] or platform_mac is None) and (platform_linux != [] or platform_linux is not None)):
        plat_now = 'win,linux'
    elif ((platform_win != [] or platform_win is not None) and (platform_mac != [] or platform_mac is not None) and (platform_linux != [] or platform_linux is not None)):
        plat_now = 'win,linux,mac'
    else:
        plat_now = '？？？'

    

    time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在
    cursor.execute('insert into steam (game_id,game_name,released_time,price,find_time,picture,platform) values (%s,%s,%s,%s,%s,%s,%s)',
    (count,str(name_now),str(released_time_now),str(price_now),str(time_now),str(pic.img.get('src')),str(plat_now)))
    print(released_time.string)
    db.commit()
    print('******完成此条插入!')
    count+=1
    

# #     # cursor.execute('insert into wallpaper (category,view_img,img,created_time,img_tag) values (%s,%s,%s,%s,%s)', 
# #     # (str(wallPaperBeanList[ll].category), str(wallPaperBeanList[ll].view_img),
# #     # str(wallPaperBeanList[ll].img),str(wallPaperBeanList[ll].created_time),str(wallPaperBeanList[ll].img_tag)))


# #     # print(name) name输出检查正确

# #     # name = '11'
# #     # cursor.execute(sql,name)
    

# #         # name = td[1].text.strip()       # 直接从列表里取值
# #         # hex = td[2].text.strip()
# #         # # print u'颜色: ' + name + u'颜色值: '+ hex + u'背景色样式: ' + style
# #         # # print 'color: ' + name + '\tvalue: '+ hex + '\tstyle: ' + style
# #         # insert_color = ("INSERT INTO COLOR(Color,Value,Style)" "VALUES(%s,%s,%s)")
# #         # data_color = (name, hex, style)
# #         # cursor.execute(insert_color, data_color)
# #         # db.commit()

# #         # sql1 = 'select * from steam;'
# #         # print(cursor.execute(sql1))

# #         # cursor.execute("insert into steam(name)values" "('{}')".format(game_name.text))
# #         # print(cursor.execute("insert into steam(name)values" "('{}')".format(game_name.text)))
# #         # cursor.execute("insert into novel(sortname, novelname, imgurl, description, status, author)values"
# #         # "('{}', '{}', '{}', '{}', '{}', '{}')".format(sort, novel_name, img_url, u'这里是描述', status, author))
    
# #         # insert_color = ("INSERT INTO COLOR(Color,Value,Style)" "VALUES(%s,%s,%s)")
# #         # data_color = (name, hex, style)
# #         # cursor.execute(insert_color, data_color)
# #         # db.commit()
# #         # print '******完成此条插入!'

# #     # print(count)
# #     # cursor.execute('insert into steam (id) values (%s)',count)
    
# #     # db.commit()
# #     # print(released_time.string)
# #     # released_time_now = released_time.text.strip()
# #     # cursor.execute('insert into steam (released_time) values (%s)',(str(released_time_now)))
# #     # db.commit()


# # #     #发行时间
# # # print('released_time')
# # # for released_time in released_times:
# # #     print(released_time.string)
# # #     released_time_now = released_time.text.strip()
# # #     cursor.execute('insert into steam (released_time) values (%s)',(str(released_time_now)))
# # #     db.commit()

# #     #原价+现价 还要考虑free to play的情况，
# #     # for game_price_1 in game_price_1s:
# #     #     if "¥" in game_price_1 :
# #     #         price = game_price_1.text.split('¥',2)
# #     #         print('原价')
# #     #         print(price[1]) #原价
# #     #         print('现价')
# #     #         print(price[2]) #现价
# #     #     else: 
# #     #         print(game_price_1.text)

# # # for game_price_1 in game_price_1s:
# # #     if "Free" in game_price_1.text:
# # #         print(game_price_1.text.strip())
# # #     elif "-" in game_price_1:
# # #          continue
# # #     else:
# # #         price = game_price_1.text.split('¥',1)
# # #             # print(price[1].strip())
# # #         if "¥" in price[1]:
# # #             price_1 = price[1].split('¥',1)
# # #                 # print('原价')
# # #                 # print(price_1[0].strip()) #原价
# # #                 # print('现价')
# # #             print(price_1[1].strip()) #现价
# # #         else:
# # #                 # print('原价')
# # #             print(price[1].strip()) #原价