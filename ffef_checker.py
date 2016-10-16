import urllib.request
import urllib.error

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

FTP_Server = Request("http://0.0.0.0")
Flugradar_1 = Request("http://0.0.0.0")
Blog = Request("http://0.0.0.0")
Webcam = Request("http://0.0.0.0")
Mumble = Request("http://0.0.0.0")

#  Test

try:
	response = urlopen("http://www.google.de")
	print("Online")
except HTTPError as e:
	print('The server couldn\'t fulfill the request.')
	print('Error code: ', e.code)
	f = open("error.txt", "w")
	f.write("server error\n")
	f.close()
except URLError as e:
	print('We failed to reach a server.')
	print('Reason: ', e.reason)
	f = open("error.txt", "w")
	f.write("FTP_Server = offline\n")
	f.close()



# FTP_Server Test

try:
	response = urlopen(FTP_Server)
	print("Online")
except HTTPError as e:
	print('The server couldn\'t fulfill the request.')
	print('Error code: ', e.code)
	f = open("error.txt", "w")
	f.write("server error\n")
	f.close()
except URLError as e:
	print('We failed to reach a server.')
	print('Reason: ', e.reason)
	f = open("error.txt", "w")
	f.write("FTP_Server = offline\n")
	f.close()
	
# Flugradar_1 Test

try:
	response = urlopen(Flugradar_1)
	print("Online")
except HTTPError as e:
	print('The server couldn\'t fulfill the request.')
	print('Error code: ', e.code)
	f = open("error.txt", "a")
	f.write("server error\n")
	f.close()
except URLError as e:
	print('We failed to reach a server.')
	print('Reason: ', e.reason)
	f = open("error.txt", "a")
	f.write("Flugradar_1 = offline\n")
	f.close()
	
# Blog Test

try:
	response = urlopen(Blog)
	print("Online")
except HTTPError as e:
	print('The server couldn\'t fulfill the request.')
	print('Error code: ', e.code)
	f = open("error.txt", "a")
	f.write("server error\n")
	f.close()
except URLError as e:
	print('We failed to reach a server.')
	print('Reason: ', e.reason)
	f = open("error.txt", "a")
	f.write("Blog = offline\n")
	f.close()

# Webcam Test

try:
	response = urlopen(Webcam)
	print("Online")
except HTTPError as e:
	print('The server couldn\'t fulfill the request.')
	print('Error code: ', e.code)
	f = open("error.txt", "a")
	f.write("1")
	f.close()
except URLError as e:
	print('We failed to reach a server.')
	print('Reason: ', e.reason)
	f = open("error.txt", "a")
	f.write("Webcam = offline\n")
	f.write("")
	f.close()
	
# Mumble Test

try:
	response = urlopen(Mumble)
	print("Online")
except HTTPError as e:
	print('The server couldn\'t fulfill the request.')
	print('Error code: ', e.code)
	f = open("error.txt", "a")
	f.write("1")
	f.close()
except URLError as e:
	print('We failed to reach a server.')
	print('Reason: ', e.reason)
	f = open("error.txt", "a")
	f.write("Mumble = offline\n")
	f.close()
	