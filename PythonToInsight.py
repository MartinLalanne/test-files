import requests
import json
import time
import calendar
import datetime
import random

myHeaders={
        'Content-Type':'application/json',
        'Authorization' : '{data soure token}' #Add AVEVA data source token here
        }

while True: 
        myData={
        "data": [
            {
                "dateTime": datetime.datetime.utcnow(),
                "Reactor3.Level":random.randint(0, 100),
                "Reactor3.Temp":random.randint(0, 100),
                "Reactor3.InletValve": random.randint(10, 20),
                "Reactor3.Step": random.randint(100, 150),
                "Line3.Units": random.randint(70, 90),
                "Line3.Product": "AVEVA"
            }
            ]
        } 

        #Add AVEVA data source upload endpoint below
        response = requests.post('{upload endpoint}', data=json.dumps(myData, default=str), headers=myHeaders)
        print("Status code: ", response.status_code)
        time.sleep(1)
        print(json.dumps(myData, default=str))
        time.sleep(9)




