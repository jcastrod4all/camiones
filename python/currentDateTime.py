from time import gmtime, strftime
dateTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print(dateTime)