#!/usr/bin/env python3
"""
Capture any character shown on telnet console and save it to text file.
Telnet console is connected to MOXA device.
Instead of simulating serial connection, connecting telnet to local TCP port is enough to get the data.

NOTE FOR MOXA: set on TCP Server Mode

for testing purpose with the same function as tlr_data.py -- Tejo
"""

from datetime import datetime
import telnetlib
#import MySQLdb
import time
import sys, os

def fix_line0(line):
	line[0] = line[0].split(" ")[1]
	line[4] = line[4][:-5]
	line = [str(float(i)) for i in line]
	return line

def fix_line1(line):
	line = line[-11:-1]
	line = [str(float(i)) for i in line]
	return line

def teln_tlr():
	"""Capturing ascii traffic from telnet connection"""
	tn = telnetlib.Telnet(host='192.168.10.102', port=2009)
	line = str(tn.read_until(b'\n\n', 300))
	time1 = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
	print(time1,line)
	if len(line)>10:
		print(time1,line, file=open("tlr_raw", 'a'))
		if "#03" in line:
			"""TEMP data"""
			l_ = line[line.index("T#03")+5:line.index("\\r\\n \\r\\n")].split(",")
			print(time1+","+",".join(l_))
			#tlr_wrt_sql(time1, l_, 0)
		elif "LR0101256" in line:
			"""GAS data"""
			l_ = line[line.index("TLR0101256")+11:line.index("\\r\\n")].split(" ")
			print(time1+","+",".join(l_))
			#tlr_wrt_sql(time1, l_, 1)
		else :
			return 0

if __name__ == '__main__':
	try:
		teln_tlr()
	except Exception as e:
		time1 = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
		print(time1, e, file=open("tlr_err", 'a'))
		pass
	# Run a new iteration of the current script, providing any command line args from the current iteration
	os.execv(__file__, sys.argv)
	os.system()
	#os.execv(sys.executable, ['python'] + sys.argv)
