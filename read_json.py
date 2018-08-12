# -*- coding: UTF-8 -*-
 
import json
import re

def loadflow_hour():
    f = open("data.json", encoding='utf-8')
    w_1 = open("receiveflow_hour.txt",'a')
    w_2 = open("sendflow_hour.txt",'a')
    try:
        for line in f:
            print(line)
            flow_data = json.loads(line)
            time = flow_data['originTime']
            hour = re.findall(r"\S+\s+(\d+):\S+", time)
        
            w_1.writelines(hour[0] + '\n')
            receive = flow_data['receiveFlow']
            w_1.writelines(receive + '\n')
            w_2.writelines(hour[0] + '\n')
            send = flow_data['sendFlow']
            w_2.writelines(send + '\n')
    finally:
        f.close
        w_1.close
        w_2.close
            

def loadflow_day():
    f = open("data.json", encoding='utf-8')
    w_1 = open("receiveflow_day.txt",'a')
    w_2 = open("sendflow_day.txt",'a')
    try:
        for line in f:
            print(line)
            flow_data = json.loads(line)
            time = flow_data['originTime']
            day = re.findall(r"\d+-\d+-(\d+)\s+\S+", time)
        
            w_1.writelines(day[0] + '\n')
            receive = flow_data['receiveFlow']
            w_1.writelines(receive + '\n')
            w_2.writelines(day[0] + '\n')
            send = flow_data['sendFlow']
            w_2.writelines(send + '\n')
    finally:
        f.close
        w_1.close
        w_2.close
        
        
loadflow_hour()
loadflow_day()
