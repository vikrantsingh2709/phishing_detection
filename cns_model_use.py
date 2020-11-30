#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 10:00:50 2020

@author: vikrant
"""

from cns_phishing_feature_extraction import generate_data_set
import joblib

def model(url):
    arr = generate_data_set(url)
    model = joblib.load('phishing_decision.pkl')
    ans = model.predict([arr])
    print(ans)
    if ans == 1 or ans == 1.0 or ans == '1':
        print('Legitimate Website')
        
    else:
        print('Phishing URL')
    return ans

#model('http://webscraping.com/')
    