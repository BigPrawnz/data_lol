import datetime

def dateRange(beginDate, endDate):
    dates = []
    dates_return = []
    dt = datetime.datetime.strptime(beginDate, "%Y-%m-%d")
    date = beginDate[:]
    while date <= endDate:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y-%m-%d")
    # return dates
    for i in range(len(dates)):
        date_new = dates[i].split("-")
        dates_return.append('%d-%d-%d' % (int(date_new[0]), int(date_new[1]), int(date_new[2])))
    return dates_return
print(dateRange("2019-05-27","2019-08-18"))
dates_list = dateRange("2019-05-27","2019-08-18")
all_dates_list = []
for k in range(0,len(dates_list),7):
    seven_dates_list = []
    for j in range(k,k+7):
        seven_dates_list.append(dates_list[j])
    all_dates_list.append(seven_dates_list)
print(all_dates_list)