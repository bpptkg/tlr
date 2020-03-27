#!/usr/bin/env python3
"""
Capture any character shown on telnet console and save it to text file.
Telnet console is connected to MOXA device.
Instead of simulating serial connection, connecting telnet to local TCP port is enough to get the data.

NOTE FOR MOXA: set on TCP Server Mode

IMPORTANT: Execute with './tlr_data.py' so the script able to restart itself without putting additional scheduler/cron
script by: Tejo
Modified by: Indra R
"""

from datetime import datetime
import telnetlib, MySQLdb
import time
import sys, os
import pytz

LOCAL_TZ = 'Asia/Jakarta'
LOGFILE = 'tlr.log'


def tlr_wrt_sql(time1, line, idx):
    db = MySQLdb.connect(host="localhost", port=3306, user="user", passwd="secret", db="geochemistry")
    cursor = db.cursor()
    if idx == 0:
        sql = "INSERT INTO vgms_l530_0 (dtime, temp1, temp2, temp3, temp4, V_bat) \
           VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % \
           (time1, line[0], line[1], line[2], line[3], line[4])

    elif idx == 1:
        sql = "INSERT INTO vgms_l530_1 (dtime, co2_min, co2_max, co2_avg, temp_min, temp_max, temp_avg, humi_min, humi_max, humi_avg, V_in) \
           VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
           (time1, line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9])

    elif idx == 2:
        sql = "INSERT INTO vgms_l530_2 (dtime, temp) VALUES ('%s', '%s')" % (time1, line[0])

    elif idx == 3:
        sql = "INSERT INTO vgms_l530_3 (dtime, temp) VALUES ('%s', '%s')" % (time1, line[0])

    else:
        return 0

    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
    db.close()


def fix_line0(line):
    line[0] = line[0].split(" ")[1]
    line[4] = line[4][:-5]
    line = [str(float(i)) for i in line]
    return line


def fix_line1(line):
    line = line[-11:-1]
    line = [str(float(i)) for i in line]
    return line


def fix_line2(line):
    line[0] = line[0].split(" ")[1]
    line = [str(float(i)) for i in line]
    return line


def teln_tlr():
    tn = telnetlib.Telnet(host='192.168.10.102', port=2009)
    line = str(tn.read_until(b'\n\n', 300))
    print('raw:', line, file=open(LOGFILE, 'a'))
    if len(line)>10:
        l_ = ""
        time1 = datetime.now(pytz.timezone(LOCAL_TZ)).strftime("%Y-%m-%d %H:%M:%S")
        if "#03" in line:
            """TEMP data"""
            print('#03', line, file=open(LOGFILE, 'a'))

            l_ = line[line.index("T#03")+5:line.index("\\r\\n \\r\\n")].split(",")
            tlr_wrt_sql(time1, l_, 0)

        elif "LR0101256" in line:
            """GAS data"""

            print('LR0101256:', line, file=open(LOGFILE, 'a'))

            l_ = line[line.index("TLR0101256")+11:line.index("\\r\\n")].split(" ")
            tlr_wrt_sql(time1, l_, 1)

        elif "#01" in line:

            print('#01:', line, file=open(LOGFILE, 'a'))

            l_ = fix_line2(line.split(","))
            tlr_wrt_sql(time1, l_, 2)

        elif "#02" in line:

            print('#02:', line, file=open(LOGFILE, 'a'))

            l_ = fix_line2(line.split(","))
            tlr_wrt_sql(time1, l_, 3)

        else :
            return 0
    else:

        print('##:', line, file=open(LOGFILE, 'a'))


if __name__ == '__main__':
    try:
        teln_tlr()
    except Exception as e:
        #time1 = datetime.now(pytz.timezone(LOCAL_TZ)).strftime("%Y-%m-%d %H:%M:%S")
        #print(time1, e, file=open("tlr_data.err", 'a'))
        pass

    os.execv(__file__, sys.argv)
    os.system()
