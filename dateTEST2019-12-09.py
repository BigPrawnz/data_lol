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

# if __name__ == '__main__':
#     for date in dateRange('2018-02-01', '2018-02-10'):
#     	date_new = date.split("-")
#     	print('%d-%d-%d' % (int(date_new[0]), int(date_new[1]), int(date_new[2])))
print(dateRange('2018-02-01', '2018-02-10'))