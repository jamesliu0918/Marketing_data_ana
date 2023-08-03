import twstock
import time
import csv
import pandas as pd

def catch( stock_code , syear , smonth , fyear , fmonth ) :
    file_name = stock_code + "_" + str(syear) + "_" + str(smonth) + "_" + str(fyear) + "_" + str(fmonth)

    stock = twstock.Stock(stock_code)
    data_list = []
    for year in range(syear, fyear + 1):
        for month in range(1, 13):
            if year == syear and month < smonth:
                continue

            print('抓資料中 每一筆都有12秒預設間隔現在在抓',year, "年", month, "月 ")
            data_list.append(stock.fetch(year, month))
            if year == fyear and month == fmonth:
                break
            time.sleep(5)
    with open(file_name + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(['date', 'close', ])

        for data_list_month in data_list:
            for data in data_list_month:
                writer.writerow([data[0].strftime('%Y-%m-%d'), data[6]])
    csvfile_name = str(file_name) + ".csv"

    data = pd.read_csv(r'%s' % (csvfile_name))

    data['date'] = pd.to_datetime(data['date'])
    data.set_index("date", inplace=True)

    return data
