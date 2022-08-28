#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 16:47:16 2022

@author: tpombo
"""
#libraries used
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

#readline in text file for queries

query_list = []    
queries = open('100QueriesSet2.txt')
for line in queries.readlines():
   print(line)
    
