#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
step02_reshape.py

DataFrame 모양 변경
"""

import pandas as pd

buy = pd.read_csv("buy_data.csv")
type(buy) # pandas.core.frame.DataFrame

buy.shape # (22, 3) : 2차원
buy

# 1. row -> column(wide -> long)
buy_long = buy.stack() # stack : 2차원 0> 1차원
buy_long.shape # (66,)
buy_long

# 2. column -> row(long -> wide)
buy_wide = buy_long.unstack()
buy_wide.shape # (22, 3)
buy_wide

# 3. 전치행렬 : t() -> .T
wide_t = buy_wide.T
wide_t.shape # (3, 22)

# 4. 중복 행 제거
buy_df = buy.drop_duplicates()
buy_df.shape # (20,3)
