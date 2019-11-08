import argparse
import datetime
current = datetime.datetime.now() 
print ("Current date:", current)
parser = argparse.ArgumentParser()
parser.add_argument("--num_y", type=int)
parser.add_argument("--num_d", type=int)
args = parser.parse_args()
tdelta = datetime.timedelta(days = 5)
print('Date and Time: ', dt)
print('- 5 days: ', current - "--num_y")
print('+ 5 days: ', current + "--num_d" tdelta)



dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print('Date: ', dt, type(dt))
print('Time: ', dt.time(), type(dt.time()))
print('Year: ', dt.year)
print(dt.date(), type(dt.date()))