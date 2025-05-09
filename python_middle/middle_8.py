import numpy as np
import pandas as pd

emp_df=pd.read_csv("c:\pydata\EMP.csv")
print(emp_df)
#create table empcp as select * from emp where deptno=30
#empcp=emp_df[emp_df['DEPTNO']==30]
#print(empcp)
# emp_df => select ename from emp
print(emp_df['ENAME'])
# empno,ename,job, sal => deptno=20
data=emp_df[emp_df['DEPTNO']==20][['EMPNO','ENAME','JOB','SAL']].copy()
print(data)
# select empno,ename,job from emp where job='MANAGER';
print(emp_df[['EMPNO','ENAME','JOB']][emp_df['JOB']=='MANAGER'])

