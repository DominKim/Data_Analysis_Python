'''
step03_t_test.py

집단 간 평균차이 검정(t-test)
 1. 한 집단 평균차이 검정
 2. 두 집단 평균차이 검정
 3. 대응 두 집단 평균차이 검정
'''

from scipy import stats # t 검정
import numpy as np      # 숫자 연산
import pandas as pd     # file read

# 1. 한 집단 평균차이 검정

# 대한민국 남자 평균 키(모평균) : 175.5cm
# 모집단 -> 표준 추출(300명)

sample_data = np.random.uniform(172, 180,size = 300)
sample_data

# 기술통계
sample_data.mean() # 175.97428577726424

one_group_test = stats.ttest_1samp(sample_data, 175.5)
one_group_test
# tatistic=3.561553564664822, pvalue=0.000428807703967506
print("statistic = %.5f, pvalue = %.5f" % (one_group_test))
# statistic = 3.56155, pvalue = 0.00043

# 2. 두 집단 평균차이 검정
female_score = np.random.uniform(50, 100, size = 30)
male_score = np.random.uniform(45, 95, size = 30)
two_sample = stats.ttest_ind(female_score, male_score)

print("statistic = %.5f, pvalue = %.5f" % (two_sample))
# statistic = 2.05667, pvalue = 0.04423

# 기술통계
female_score.mean() # 77.70465463880878
male_score.mean()   # 70.3663550435343

# csv file load
two_sample = pd.read_csv("/Users/mac/Desktop/bigdata/Python/4_Python-II/data/two_sample.csv")
two_sample.info()

sample_data = two_sample[["method", "score"]]
sample_data.head() # method score
sample_data["method"].value_counts()
'''
2    120
1    120
'''

method1 = sample_data[sample_data["method"] == 1]
method2 = sample_data[sample_data["method"] == 2]

score1 = method1.score
score2 = method2.score

# NA 제거 후
score1 = score1.fillna(score1.mean())
score2 = score2.fillna(score2.mean())

# na -> error
two_sample = stats.ttest_ind(score1, score2)
two_sample
print("statistic = %.5f, pvalue = %.5f" % (two_sample))

score1.mean() # 5.496590909090908
score2.mean() # 5.591304347826086


# 3. 대응 두 집단 평균차이 검정 : 복용전 = 65 -> 복용후 : 60 변환
before = np.random.randint(65, size= 30) * 0.5
after  = np.random.randint(60, size = 30) * 0.5

before.mean() # 15.916666666666666
after.mean()  # 15.116666666666667

paired_test = stats.ttest_rel(before, after)
print("statistic = %.5f, pvalue = %.5f" % (paired_test))
#  statistic = 0.44136, pvalue = 0.66222
