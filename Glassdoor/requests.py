# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 23:18:23 2021

@author: hp
"""
import requests

url = 'http://localhost:5000/predict_api'

r = requests.post(url,json={"Size":5, "Founded":21, "Type":1, "Revenue":7, "Basic_Pay":1596545.0, "Rating":4, "Positive":72, "Online":48, 
"Industry_Banking/Finance":0, "Industry_Cable, Internet & Telephone Providers":0, "Industry_Consulting":0, 
"Industry_Education":0, "Industry_Film Production & Distribution":0, "Industry_General Merchandise & Superstores":0,
"Industry_Government Agencies":0, "Industry_Healthcare Medicine":0, "Industry_Information Technology":1, 
"Industry_Manufacturing":0, "Industry_Outsource":0, "Industry_Real Estate":0, "Industry_Telecommunication/Television":0,
"Industry_Transportation":0, "City_Banglore":1, "City_Mumbai":0, "City_Pune":0})

print(r.json())

