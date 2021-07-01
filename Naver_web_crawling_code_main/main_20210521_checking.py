# 2021-05-21
# 해당 코드의 목적은 작업의 효율성과 가독성을 높이기 위함입니다.
# Chapter 2: checking
# 목적 : 오류가 발생한 파일들을 수작업하여 크롤링 가능하도록 만들고, 이를 크롤링 하여 chapter1 에서의 파일과 합치시키기

# Import packages
from selenium import webdriver
import time
import openpyxl
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.keys import Keys
import numpy as np
from urllib.parse import urlparse  # 출처: https://datamasters.co.kr/67 [데이터마스터]
from datetime import datetime


