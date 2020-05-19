a = [[1, 4], [3, 4], [3, 10]]	
import pandas as pd
df =pd.DataFrame(a)
x = df[0].value_counts().index[1]
y = df[1].value_counts().index[1]

import re
a = ["l","r"]
"".join(a)

numbers = [1, 2, 3, 4, 5, 6, 7]
result = []
if 4 in [1,4,7]:
    result.append("L")

"".join(result)
import numpy as np
z = np.array([1, 2])
s = np.array([2, 1])

t = z - s
abs(t).sum()

import pandas as pd
    operater = pd.DataFrame([[3,2,1],[3,1,2],[2,3,1],[2,1,3],[1,3,2],[1,2,3]], 
                           columns = ["*", "+", "-"])
    result = []
    answer = 0

expression = "100-200*300-500+20"	
num = re.findall("[0-9]{1,}", expression)
for i in range(len(num)):
    num[i] = int(num[i])
opp = re.sub("[0-9]{1,}", " ", expression).split(" ")[1:-1]
cnt = 0
for i in range(len(num)): 
    for j in range(len(opp)):
        if j == "+":
            pass
        elif j == "-":
            pass
        elif j == "*":
            num

import pandas as pd
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
a = pd.Series(gems)
stone = pd.DataFrame(a.unique())

answer = []
cnt = []

for i in range(len(gems) - (len(stone)) + 1):
    stone["count"] = None
    for idx, value in enumerate(gems[i:]):
        if stone["count"].isnull().any():
            stone.loc[stone[0] == value,"count"] = 1
        else:
            answer.append([i+1 ,i + idx])
            cnt.append(abs(i+1)-(i + idx))
            break

min_num = cnt[0]
idx = 0
len(set(cnt)) > 1
for i in range(len(cnt)):
    if cnt[i] < min_num:
        idx = i
        min_num = cnt[i]
min_num
idx

answer = answer[i]
import numpy as np
answer


stone.iloc[1,1] = 1
stone

if stone["count"].all():
    print("a")
else:
    print("b")



