import pandas as pd
df=pd.read_excel("E:\Book1.xlsx")
print(df.sort_values('experience',ascending=False))


## out put ##
name  experience       job      title        dob
2  Mukesh           5  software  recruiter 1992-09-08
0  Ramesh           4  software  developer 1996-04-14
1  Suresh           3  software     tester 1994-09-07
