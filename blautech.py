# -*- coding: utf-8 -*-
"""
Created on Mon May 25 08:08:38 2020

@author: mau_b
"""
import requests
import csv


paises = []
region = []
americas = []

max_population = 10000000

request_url = 'https://restcountries.eu/rest/v2/regionalbloc/cais'
res = requests.request('GET', request_url)
if res.status_code != 200:
   if res.status_code == 404:
      print('There is a problem with the request URL. Make sure that it is correct')
   else:
      print('There was a problem retrieving data: ', res.text)
else:
    jsonData = res.json()
    for data in jsonData:
        info = []
        info.append(data['name'])
        info.append(data['capital'])
        info.append(data['region'])
        info.append(data['alpha3Code'])
        info.append(data['subregion'])
        info.append(data['population'])
        paises.append(info)
     
     
     
header = ["Nombre","Capital","Region","Codigo de Pais Alpha 3","Subregion","Poblacion"]
with open('paises.csv','w',newline='') as csvfile:
         csvWriter = csv.writer(csvfile)
         csvWriter.writerow(header)
         
         for info in paises:
             csvWriter.writerow(info)
         csvfile.close
         print(":::Se creo el archivo csv:::")
         

with open('paises-1_fra_csv.csv') as csvfile:
         csvReader = csv.reader(csvfile)
         print(":::Países cuya población sea menor a 10,000,000")
         rows = 0
         for row in csvReader:
             if rows != 0:
                 if int(row[5]) < max_population:
                     print(row[0] + " - " +row[5])
                     
                 if any(row[2] in sublist for sublist in region) is False:
                     region.append(row[2])
             rows+=1
         print(":::Regiones existentes: "+str(region))
         
    

with open('paises-1_fra_csv.csv') as csvfile:
         csvReader = csv.reader(csvfile)
         print(":::Ordenados por region (Agregue Europa para lograrlo)")
         filterRegion = 'Europa'
         
         rows = 0
         for row in csvReader:
             if rows != 0:
                 if row[2] == 'Europa':
                     print(row[0] + " - " +row[1]+ " - " +row[4])
                 else:
                     americas.append(row[0] + " - " +row[1]+ " - " +row[4])
             rows+=1
         for paises in americas:
             print(paises)
         
         
             
             