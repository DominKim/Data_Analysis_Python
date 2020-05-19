'''
step02_chisquare_test.py

카이제곱검정(chisquare test)
 - 일원 카이제곱, 이원 카이제곱
'''

from scipy import stats
import numpy as np

# 1. 일원 카이제곱 검정
# 귀무가설 : 관측치와 기대치는 차이가 없다.(게임에 적합하다.)
# 대립가설 : 관측치와 기대치는 차이가 있다.(게임에 적합하지 않다.)
real_data = [4, 6, 17, 16, 8, 9] # 관측치
exp_data = [10, 10, 10, 10, 10, 10] # 기대치
chis = stats.chisquare(real_data, exp_data)
chis
# (statistic=14.200000000000001, pvalue=0.014387678176921308)

# statistic=14.200000000000001 = 기대비율
#  기대비율 = (관측값 - 기댓값)^2 / 기댓값

print("statistic = %.3f, pvalue = %.3f" % (chis))
#  statistic = 14.200, pvalue = 0.014

# list -> numpy
real_arr = np.array(real_data)
exp_arr = np.array(exp_data)

chis2 = sum((real_arr - exp_arr)**2 / exp_arr)
chis2 # 14.200000000000001


# 2. 이원 카이제곱 검정
import pandas as pd
'''
 교육수준 vs 흡연유무 독립성 검정
 귀무가설 : 교육수준과 흡연유무간의 관련성이 없다.
'''

import os
os.getcwd()
smoke = pd.read_csv("/Users/mac/Desktop/bigdata/Python/4_Python-II/data/smoke.csv")
smoke.info()
'''
RangeIndex: 355 entries, 0 to 354
Data columns (total 2 columns):
'''

# DF -> vector
education = smoke.education
smoking = smoke.smoking

# cross table
table = pd.crosstab(education, smoking)
table
'''
smoking	1	2	3
education			
1	51	92	68
2	22	21	9
3	43	28	21
'''

chis = stats.chisquare(education, smoking)
chis

'''
성별 vs 흡연유무 독립성 검정
'''
tips = pd.read_csv("/Users/mac/Desktop/bigdata/Python/4_Python-II/data/tips.csv")

sex = tips.sex
smoker = tips.smoker

# dummy 생성
sex_dummy = [1 if i == "Male" else 2 for i in sex]
smoker_dummy = [1 if i == "No" else 2 for i in smoker]

chis = stats.chisquare(sex_dummy, smoker_dummy)
chis
# statistic=84.0, pvalue=1.0