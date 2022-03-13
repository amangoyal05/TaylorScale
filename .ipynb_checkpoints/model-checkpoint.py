import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split,GridSearchCV, RepeatedStratifiedKFold
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from itertools import product


def sad(stressscore):
    df = pd.read_csv('data.csv',sep='\t')

    DASS_keys = {'Depression': [3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38, 42],
             'Anxiety': [2, 4, 7, 9, 15, 19, 20, 23, 25, 28, 30, 36, 40, 41],
             'Stress': [1, 6, 8, 11, 12, 14, 18, 22, 27, 29, 32, 33, 35, 39]}

    df['wrongansw'] = 0
    df['wrongansw'] = df['wrongansw'].where(df['VCL6']== 0, df['wrongansw'] + 1)
    df['wrongansw'] = df['wrongansw'].where(df['VCL9']== 0, df['wrongansw'] + 1)
    df['wrongansw'] = df['wrongansw'].where(df['VCL12']== 0, df['wrongansw'] + 1)

    df = df[df['wrongansw'].isin([2, 3])]
    df = df.drop(columns='wrongansw')
    vcls = []
    for i in range(1, 17):
        vcls.append('VCL' + str(i))
    
    df = df.drop(columns=vcls)
    depr = []
    anx = []
    stre = []
    for i in DASS_keys["Depression"]:
        depr.append('Q' + str(i) + 'A')
    
    for i in DASS_keys["Anxiety"]:
        anx.append('Q' + str(i) + 'A')

    for i in DASS_keys["Stress"]:
        stre.append('Q' + str(i) + 'A')

    df_depr = df.filter(depr)
    df_anx = df.filter(anx)
    df_stre = df.filter(stre)
    categorical = df.select_dtypes('object').columns
    print('Categorical Columns: ', df[categorical].columns)
    print(df[categorical].nunique())
    df[depr] -= 1 
    def scores(df):
        df["ScoresD"] = df[depr].sum(axis=1)
        return df
    df = scores(df)
    df[anx] -= 1 
    def scores(df):
        df["ScoresA"] = df[anx].sum(axis=1)
        return df
    df = scores(df)
    df[stre] -= 1
    def scores(df):
        df["ScoresS"] = df[stre].sum(axis=1)
        return df
    df = scores(df)
    Category=[]
    for i in df['ScoresA']:
        if i<=7:
            Category.append('0')
        elif i<=9:
            Category.append('1')
        elif i<=14 :
            Category.append('2')
        elif i<=19:
            Category.append('3')
        else:
            Category.append('4')
    df['CATEGORY']= Category
    y = df['CATEGORY']
    X = df.drop(columns=['CATEGORY','country', 'ScoresD' ,'ScoresS','Q1A' ,'Q1I', 'Q1E', 'Q2I', 'Q2E', 'Q3A', 'Q3I', 'Q3E','Q4I','Q4E', 'Q5E', 'Q5A' ,'Q5I', 'Q6E', 'Q6A' ,'Q6I', 'Q7E' ,'Q7I', 'Q8E','Q8A' ,'Q8I', 'Q9E', 'Q9I', 'Q10E', 'Q10A', 'Q10I', 'Q11E', 'Q11A' ,'Q11I', 'Q12E', 'Q12A' ,'Q12I', 'Q13E', 'Q13A' ,'Q13I', 'Q14E', 'Q14A' ,'Q14I', 'Q15E', 'Q15I', 'Q16E', 'Q16A' ,'Q16I', 'Q17E', 'Q17A' ,'Q17I', 'Q18E', 'Q18A' ,'Q18I', 'Q19I', 'Q19E',  'Q20I', 'Q20E', 'Q21A', 'Q21I', 'Q21E', 'Q22A', 'Q22I','Q22E', 'Q23I','Q23E','Q24A','Q24I','Q24E', 'Q25I', 'Q25E', 'Q26A', 'Q26I', 'Q26E', 'Q27A', 'Q27I', 'Q27E', 'Q28I', 'Q28E', 'Q29A', 'Q29I', 'Q29E',  'Q30I', 'Q30E', 'Q31A', 'Q31I', 'Q31E', 'Q32A', 'Q32I', 'Q32E', 'Q33A', 'Q33I', 'Q33E', 'Q34A', 'Q34I', 'Q34E', 'Q35A', 'Q35I', 'Q35E', 'Q36I', 'Q36E', 'Q37A', 'Q37I', 'Q37E', 'Q38A', 'Q38I', 'Q38E', 'Q39A', 'Q39I', 'Q39E', 'Q40I', 'Q40E', 'Q41I', 'Q41E', 'Q42A', 'Q42I', 'Q42E'])
    X.head()
    scaler = StandardScaler()
    scaler.fit(X)
    X = scaler.transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, stratify=y,random_state=100)
    model = RandomForestClassifier(criterion='entropy', max_depth=9, n_estimators=100, random_state=0)
    model.fit(X_train, y_train)