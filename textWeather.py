#! /usr/bin/python

import smtplib  
import urllib
from xml.dom import minidom as ET

def sendMail(msg):
  fromaddr = 'your email address' #gmail is easiest  
  toaddrs  = 'your-to-address' #eg your-number@txt.att.net  
    
  # Credentials
  username = 'username' #if gmail, then this is same as fromaddr  
  password = 'password'  

  # The actual mail send  
  server = smtplib.SMTP('smtp.gmail.com:587') #change this if not using gmail 
  server.starttls()  
  server.login(username,password)  
  server.sendmail(fromaddr, toaddrs, msg)  
  server.quit()  

def getWeather(zipCode):
  weatherFile = urllib.urlopen('http://www.google.com/ig/api?weather='+str(zipCode))
  tree = ET.parse(weatherFile)
  for node in tree.documentElement.childNodes:
    if node.nodeName == 'weather':
      for current_conditions_node in node.childNodes:
        if current_conditions_node.nodeName == 'current_conditions':
          for what_i_want in current_conditions_node.childNodes:
            if what_i_want.nodeName == 'condition':
              condition = what_i_want.getAttribute('data')
            if what_i_want.nodeName == 'temp_f':
              temp_f = what_i_want.getAttribute('data')
            if what_i_want.nodeName == 'humidity':
              humidity = what_i_want.getAttribute('data')
            if what_i_want.nodeName == 'wind_condition':
              wind_condition = what_i_want.getAttribute('data')
  return (condition, temp_f, humidity, wind_condition)

def main():
  zipCode = 00000 #enter zip code here
  (condition, temp_f, humidity, wind_condition) = getWeather(zipCode)
  msg = ('Current weather:'+ '\n'+
          condition +'\n'+
          temp_f + ' degrees' +'\n'+
          humidity +'\n'+
          wind_condition)
  sendMail(msg)

if __name__ == '__main__':
  main()
