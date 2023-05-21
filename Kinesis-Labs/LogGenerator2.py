# Generating log for Kinesis Test
import logging
import json
from datetime import datetime
import calendar
import random
import time

print("Started")
logging.basicConfig(filename='logfile.log', level=logging.DEBUG, format='%(asctime)s %(message)s')

# print("Define Method")
def put_to_stream(id, value, timestamp):
    payload = {
                'random': str(value),
                'timestamp': str(timestamp),
                'id': id
              }

    response ='Putting to stream: ' + str(payload)
    logging.debug(response)
    #print("inside put stream")

i=0
# print("Before While")
while True:
    value = random.randint(1, 100)
    timestamp = calendar.timegm(datetime.utcnow().timetuple())
    id = 'stream-1'
    # print("While has been called for --->", i, "Calling the Method")
    put_to_stream(id, value, timestamp)

    # wait for 5 second
    time.sleep(5)
    
    # print("after put stream", str(i))
    i +=1
    if(i>50):
        break
print("completed")
