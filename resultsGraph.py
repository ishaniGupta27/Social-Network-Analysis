import pandas as pd
import matplotlib.pyplot as plt


file_to_use='Results.xlsx'

x1=pd.ExcelFile(file_to_use)

print(x1.sheet_names)

'''
df1=x1.parse('Execution Time') ##directly populating df1

df1_bruteforce=df1.iloc[:7,:2]
#df1_bruteforce_x = df1_bruteforce['Number of node']
#df1_bruteforce_y= df1_bruteforce['Execution Time(s)']
df1_ourAlgo=df1.iloc[10:17,:2]

plt.plot(df1_bruteforce['Number of node'], df1_bruteforce['Execution Time(s)'],'--bo',label='Brute_force_Algo.')
#plt.plot(df1_ourAlgo['Number of node'], df1_ourAlgo['Execution Time(s)'],'--ro',label='Max Coverage with k diversification  Algorithm')
plt.xlabel('Number of Nodes')
plt.ylabel('Execution Time(s)')
plt.show()
#ax=df1_bruteforce.plot(x='Number of node',y='Execution Time(s)')
#df1_ourAlgo.plot(x='Number of node',y='Execution Time(s)',ax=ax)
#plt.show()


#print df1_bruteforce

#print '------------------------'

#print df1_ourAlgo
'''
'''
print '-------------Section 2-------------------'


df2=x1.parse('Coverage')

#print df2
df2_bruteforce=df2.iloc[:20,:2]
df2_ourAlgo=df2.iloc[24:45,:2]
print df2_bruteforce
print '-------------'
print df2_ourAlgo


algo_1=plt.plot(df2_bruteforce['Iteration Count'], df2_bruteforce['Coverage'],'--bo',label='Brute Force Algorithm')
algo_2=plt.plot(df2_ourAlgo['Iteration Count'], df2_ourAlgo['Coverage'],'--go',label='Max Coverage with k diversification  Algorithm')
plt.xlabel('Iteration Count')
plt.ylabel('Coverage')
plt.legend()
plt.show()


'''

print '-------------Sheet 3------------------'


df3=x1.parse('Complex')


df3_ourAlgo_4feature=df3.iloc[:20,5:7]
df3_bruteForce_4feature=df3.iloc[:20,7:9]
print '------Committee Size = 4-------'
print df3_ourAlgo_4feature
print '-----------brute force--------'
print df3_bruteForce_4feature


algo_1=plt.plot(df3_ourAlgo_4feature['Iteration.1'], df3_ourAlgo_4feature['CoverageCount.1'],'--bo',label='Max Coverage with k diversification Algorithm')
algo_2=plt.plot(df3_bruteForce_4feature['itCou'], df3_bruteForce_4feature['CovCou'],'--go',label='Brute Force Algorithm')
plt.xlabel('Iteration Count')
plt.ylabel('Coverage')
plt.title('Size of Committee =4,Number of attributes =3')
plt.legend(loc='best')

plt.show()



'''
df3=x1.parse('Complex')
df3_ourAlgo_2size=df3.iloc[:20,11:13]
df3_brute_2size=df3.iloc[:20,13:15]
#print df2_bruteforce

print '------Committtee size=2 -------'
print df3_ourAlgo_2size
print '-----------brute force--------'
print df3_brute_2size


algo_1=plt.plot(df3_ourAlgo_2size['Iteration.2'], df3_ourAlgo_2size['CoverageCount.2'],'--bo',label='Max Coverage with k diversification  Algorithm')
algo_2=plt.plot(df3_brute_2size['itCount'], df3_brute_2size['CoverageCountBrute'],'--go',label='Brute Force Algorithm')
plt.xlabel('Iteration Count')
plt.ylabel('Coverage')
plt.title('Size of Committee =2,Number of attributes =3')
plt.legend(loc='left center')
plt.show()


'''
'''





print '---------Comparing coverage for all three cases----------'


df4=x1.parse('Complex')

###Splittig data for size =3 committee
df4_size3=df4.iloc[:20,1:3]
print '--------Committee Size =3 --------'
print df4_size3


###Splittig data for size =4 committee
df4_size4=df4.iloc[:20,5:7]
print '------Committee Size = 4-------'
print df4_size4



###Splittig data for size =2 committee
df4_size2=df4.iloc[:20,9:11]
print '------Committee Size = 2-------'
print df4_size2

pltSize4=plt.plot(df4_size4['Iteration.1'], df4_size4['CoverageCount.1'],'--go',label='Committee Size=4')
pltSize3=plt.plot(df4_size3['Iteration'], df4_size3['CoverageCount'],'--bo',label='Committee Size=3')
pltSize2=plt.plot(df4_size2['Iteration.2'], df4_size2['CoverageCount.2'],'--ro',label='Committee Size=2')



plt.xlabel('Iteration Count')
plt.ylabel('Coverage')
plt.legend()
plt.show()
'''