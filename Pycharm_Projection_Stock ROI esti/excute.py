#import twstock
#import time
#import csv
#import pandas as

#跑之前再環境設定上樓上這些要先裝在環境裡  麻煩惹

import mathproj
import mathproj.data_find
import mathproj.trade


data = mathproj.data_find.catch("2409",2019,2,2019,3)
#資料抓取為  股號str  日期範圍 起始年>月  結束年 月
cd = data['close']
#因為我只看收盤資料  所以用data也只抓了close 當然twstock也有其他的資料 ex日最高之類的
mathproj.trade.buy_sell(20, 5, 20, 5, cd)
# 買入點為 5 日線突破 20日線 (前兩個參數)   賣出點為  5日線 跌破 20日線
# 例如賣出點想要改短一點 3日跌破6日MA 就可以變成  mathproj.trade.buy_sell(20, 5, 6, 3, cd)