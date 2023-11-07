import csv
import datetime
import time
from _csv import writer

with open('rows_300.csv', 'w', encoding='UTF-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда ', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second,
                        datetime.datetime.now().microsecond])
        time.sleep(0.01)