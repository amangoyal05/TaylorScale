import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def anxiety_pred(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14):

    df = pd.read_csv('data.csv',sep='\t')
    df.drop(columns=['TIPI1','TIPI2','TIPI3','TIPI4','TIPI5','TIPI6','TIPI7','TIPI8','TIPI9','TIPI10','introelapse','testelapse','screensize','uniquenetworklocation','surveyelapse','country','Q1I', 'Q1E', 'Q2I', 'Q2E', 'Q3I', 'Q3E','Q4I','Q4E', 'Q5E', 'Q5I', 'Q6E', 'Q6I', 'Q7E' ,'Q7I', 'Q8E','Q8I', 'Q9E', 'Q9I', 'Q10E','Q10I', 'Q11E', 'Q11I', 'Q12E', 'Q12I', 'Q13E','Q13I', 'Q14E','Q14I', 'Q15E', 'Q15I', 'Q16E','Q16I', 'Q17E','Q17I', 'Q18E','Q18I', 'Q19I', 'Q19E',  'Q20I', 'Q20E', 'Q21I', 'Q21E', 'Q22I','Q22E', 'Q23I','Q23E','Q24I','Q24E', 'Q25I', 'Q25E', 'Q26I', 'Q26E', 'Q27I', 'Q27E', 'Q28I', 'Q28E', 'Q29I', 'Q29E',  'Q30I', 'Q30E', 'Q31I', 'Q31E', 'Q32I', 'Q32E', 'Q33I', 'Q33E', 'Q34I', 'Q34E', 'Q35I', 'Q35E', 'Q36I', 'Q36E', 'Q37I', 'Q37E', 'Q38I', 'Q38E', 'Q39I', 'Q39E', 'Q40I', 'Q40E', 'Q41I', 'Q41E', 'Q42I', 'Q42E','Q1A','Q5A','Q7A','Q9A','Q11A','Q13A','Q14A','Q15A','Q16A','Q19A','Q21A','Q23A','Q24A','Q27A','Q29A','Q30A','Q32A','Q33A','Q34A','Q36A','Q37A','major'],inplace=True)
    DASS_keys = {'Anxiety': [2,4,41,40,28,25,20],
             'Depression': [3,42,10,26,31,17,38],
             'Stress': [22,6,12,39,8,35,18]}

    depr = []
    for i in DASS_keys["Depression"]:
        depr.append('Q' + str(i) + 'A')
    
    anx = []
    for i in DASS_keys["Anxiety"]:
        anx.append('Q' + str(i) + 'A')

    stre = []
    for i in DASS_keys["Stress"]:
        stre.append('Q' + str(i) + 'A')


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
    
    feature=['source', 'education', 'urban', 'gender', 'engnat', 'age', 'hand', 'religion', 'orientation', 'race', 'voted', 'married', 'familysize','ScoresA']
    X = df[feature]
    y = df['CATEGORY']
    scaler = StandardScaler()
    scaler.fit(X)
    X = scaler.transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, stratify=y,random_state=100)
    model = RandomForestClassifier(criterion='entropy', max_depth=9, n_estimators=100, random_state=0)
    model.fit(X_train, y_train)
    [source, education, urban, gender, engnat, age, hand, religion, orientation, race, voted, married, familysize, ScoresA] = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14]
    check = [source, education, urban, gender, engnat, age, hand, religion, orientation, race, voted, married, familysize, ScoresA]
    X_test = np.array([check])
    X_test.reshape((1,-1))

    y_pred = model.predict(X_test)

    return y_pred

def stress_pred(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14):

    df = pd.read_csv('data.csv',sep='\t')
    df.drop(columns=['TIPI1','TIPI2','TIPI3','TIPI4','TIPI5','TIPI6','TIPI7','TIPI8','TIPI9','TIPI10','introelapse','testelapse','screensize','uniquenetworklocation','surveyelapse','country','Q1I', 'Q1E', 'Q2I', 'Q2E', 'Q3I', 'Q3E','Q4I','Q4E', 'Q5E', 'Q5I', 'Q6E', 'Q6I', 'Q7E' ,'Q7I', 'Q8E','Q8I', 'Q9E', 'Q9I', 'Q10E','Q10I', 'Q11E', 'Q11I', 'Q12E', 'Q12I', 'Q13E','Q13I', 'Q14E','Q14I', 'Q15E', 'Q15I', 'Q16E','Q16I', 'Q17E','Q17I', 'Q18E','Q18I', 'Q19I', 'Q19E',  'Q20I', 'Q20E', 'Q21I', 'Q21E', 'Q22I','Q22E', 'Q23I','Q23E','Q24I','Q24E', 'Q25I', 'Q25E', 'Q26I', 'Q26E', 'Q27I', 'Q27E', 'Q28I', 'Q28E', 'Q29I', 'Q29E',  'Q30I', 'Q30E', 'Q31I', 'Q31E', 'Q32I', 'Q32E', 'Q33I', 'Q33E', 'Q34I', 'Q34E', 'Q35I', 'Q35E', 'Q36I', 'Q36E', 'Q37I', 'Q37E', 'Q38I', 'Q38E', 'Q39I', 'Q39E', 'Q40I', 'Q40E', 'Q41I', 'Q41E', 'Q42I', 'Q42E','Q1A','Q5A','Q7A','Q9A','Q11A','Q13A','Q14A','Q15A','Q16A','Q19A','Q21A','Q23A','Q24A','Q27A','Q29A','Q30A','Q32A','Q33A','Q34A','Q36A','Q37A','major'],inplace=True)
    DASS_keys = {'Anxiety': [2,4,41,40,28,25,20],
             'Depression': [3,42,10,26,31,17,38],
             'Stress': [22,6,12,39,8,35,18]}

    depr = []
    for i in DASS_keys["Depression"]:
        depr.append('Q' + str(i) + 'A')
    
    anx = []
    for i in DASS_keys["Anxiety"]:
        anx.append('Q' + str(i) + 'A')

    stre = []
    for i in DASS_keys["Stress"]:
        stre.append('Q' + str(i) + 'A')


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
    for i in df['ScoresS']:
        if i<=14:
            Category.append('0')
        elif i<=18:
            Category.append('1')
        elif i<=25 :
            Category.append('2')
        elif i<=33:
            Category.append('3')
        else:
            Category.append('4')
    df['CATEGORY']= Category
    
    feature=['source', 'education', 'urban', 'gender', 'engnat', 'age', 'hand', 'religion', 'orientation', 'race', 'voted', 'married', 'familysize','ScoresS']
    X = df[feature]
    y = df['CATEGORY']
    scaler = StandardScaler()
    scaler.fit(X)
    X = scaler.transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, stratify=y,random_state=100)
    model = RandomForestClassifier(criterion='entropy', max_depth=9, n_estimators=100, random_state=0)
    model.fit(X_train, y_train)
    [source, education, urban, gender, engnat, age, hand, religion, orientation, race, voted, married, familysize, ScoresS] = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14]
    check = [source, education, urban, gender, engnat, age, hand, religion, orientation, race, voted, married, familysize, ScoresS]
    X_test = np.array([check])
    X_test.reshape((1,-1))

    y_pred = model.predict(X_test)

    return y_pred

def depression_pred(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14):

    df = pd.read_csv('data.csv',sep='\t')
    df.drop(columns=['TIPI1','TIPI2','TIPI3','TIPI4','TIPI5','TIPI6','TIPI7','TIPI8','TIPI9','TIPI10','introelapse','testelapse','screensize','uniquenetworklocation','surveyelapse','country','Q1I', 'Q1E', 'Q2I', 'Q2E', 'Q3I', 'Q3E','Q4I','Q4E', 'Q5E', 'Q5I', 'Q6E', 'Q6I', 'Q7E' ,'Q7I', 'Q8E','Q8I', 'Q9E', 'Q9I', 'Q10E','Q10I', 'Q11E', 'Q11I', 'Q12E', 'Q12I', 'Q13E','Q13I', 'Q14E','Q14I', 'Q15E', 'Q15I', 'Q16E','Q16I', 'Q17E','Q17I', 'Q18E','Q18I', 'Q19I', 'Q19E',  'Q20I', 'Q20E', 'Q21I', 'Q21E', 'Q22I','Q22E', 'Q23I','Q23E','Q24I','Q24E', 'Q25I', 'Q25E', 'Q26I', 'Q26E', 'Q27I', 'Q27E', 'Q28I', 'Q28E', 'Q29I', 'Q29E',  'Q30I', 'Q30E', 'Q31I', 'Q31E', 'Q32I', 'Q32E', 'Q33I', 'Q33E', 'Q34I', 'Q34E', 'Q35I', 'Q35E', 'Q36I', 'Q36E', 'Q37I', 'Q37E', 'Q38I', 'Q38E', 'Q39I', 'Q39E', 'Q40I', 'Q40E', 'Q41I', 'Q41E', 'Q42I', 'Q42E','Q1A','Q5A','Q7A','Q9A','Q11A','Q13A','Q14A','Q15A','Q16A','Q19A','Q21A','Q23A','Q24A','Q27A','Q29A','Q30A','Q32A','Q33A','Q34A','Q36A','Q37A','major'],inplace=True)
    DASS_keys = {'Anxiety': [2,4,41,40,28,25,20],
             'Depression': [3,42,10,26,31,17,38],
             'Stress': [22,6,12,39,8,35,18]}

    depr = []
    for i in DASS_keys["Depression"]:
        depr.append('Q' + str(i) + 'A')
    
    anx = []
    for i in DASS_keys["Anxiety"]:
        anx.append('Q' + str(i) + 'A')

    stre = []
    for i in DASS_keys["Stress"]:
        stre.append('Q' + str(i) + 'A')


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
    for i in df['ScoresD']:
        if i<=9:
            Category.append('0')
        elif i<=13:
            Category.append('1')
        elif i<=20 :
            Category.append('2')
        elif i<=27:
            Category.append('3')
        else:
            Category.append('4')
    df['CATEGORY']= Category
    
    feature=['source', 'education', 'urban', 'gender', 'engnat', 'age', 'hand', 'religion', 'orientation', 'race', 'voted', 'married', 'familysize','ScoresD']
    X = df[feature]
    y = df['CATEGORY']
    scaler = StandardScaler()
    scaler.fit(X)
    X = scaler.transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, stratify=y,random_state=100)
    model = RandomForestClassifier(criterion='entropy', max_depth=9, n_estimators=100, random_state=0)
    model.fit(X_train, y_train)
    [source, education, urban, gender, engnat, age, hand, religion, orientation, race, voted, married, familysize, ScoresD] = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14]
    check = [source, education, urban, gender, engnat, age, hand, religion, orientation, race, voted, married, familysize, ScoresD]
    X_test = np.array([check])
    X_test.reshape((1,-1))

    y_pred = model.predict(X_test)

    return y_pred