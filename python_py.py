# -*- coding: utf-8 -*-
"""python.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DZ61AliSG36ROte_bFt3_VEfp1Zh7Wa2
"""

import pandas as pd ## import pandas for general file types

import json ## import json for json files

import bs4 ## import bs4 for html files

import requests ## import requests for web requests

import sqlalchemy ## import sqlalchemy for sql queries

from PIL import Image ## import pillow for image files

from google.cloud import bigquery ## import bigquery for bigquery files

import matplotlib

import xlrd ## import xlrd for excel files, tab names

data = requests.get(https://data.cms.gov/provider-summary-by-type-of-service/medicare-post-acute-care-hospice/medicare-post-acute-care-hospice-by-provider-and-service/data)

## Error in using data requests