import random
import requests
import os
import time

id_person = -1
while(1):
  #Generate id for the person and increment the counter

  #ID method with a text file. IT IS INCOMPLETE
  # file = open('id_index.txt','r')
  # id_person = int(file.readline())
  # file.close()
  # file = open('id_index.txt','w')
  # id_person += 1
  # file.write(str(id_person))
  # file.close()

  #Easy method for id
  id_person += 1

  #Generate a random number and obtain the corresponding name in the names file
  random_index_name = random.randint(1,100)
  file = open('names.txt','r')
  names = file.readlines()
  name = names[random_index_name - 1].rstrip()
  file.close()

  #Generate a random age
  random_age = random.randint(0,100)

  #Sent Post request
  #Payload is the json to be sent to the url
  payload = {'id': id_person, 'name':name, 'age':random_age}
  #url is the url used for the requests
  url = '172.17.0.1:80'
  r = requests.post(url,json=payload)

  #Debugging
  print (id_person)
  print (name)
  print (random_age)
  print(r.text)
  time.sleep(2)
