import pandas as pd
import numpy as np
from statsmodels.stats import proportion


chat_id = 544835691 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    s1 = x_success 
    n1 = x_cnt
    s2 = y_success
    n2 = y_cnt
    stat, pval = proportion.proportions_ztest([s1, s2], [n1, n2], alternative='larger')
    #print('{0:0.19f}'.format(pval))
    return True if pval < 0.07 else False
   
