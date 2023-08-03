def buy_sell(day, dayMaa, sday, sMAday, data_):
    MA = data_.rolling(day).mean()
    MAa = data_.rolling(dayMaa).mean()
    sMA = data_.rolling(sday).mean()
    sMAa = data_.rolling(sMAday).mean()
    hold = 1
    cash = 0
    fcash = data_[1 + day]

    for i in range(1 + day, len(data_)):
        if MA[i - 1] > MAa[i - 1] and MA[i] < MAa[i] and hold == 0: #買入點
            hold += 1
            cash -= data_[i] * (1 - 0.0035)
        elif sMA[i - 1] < sMAa[i - 1] and sMA[i] > sMAa[i] and hold == 1:  #賣出點
            hold -= 1
            cash += data_[i] * (1 - 0.0035)
    if hold ==1 :
        cash += (data_[len(data_)-1])
    rt = ((cash / fcash) - 1) * 100
    print(rt, '%')