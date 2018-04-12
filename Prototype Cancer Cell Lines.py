#import all the relevant packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

apopcand = pd.read_csv('Apo_Mutations.tar.gz', error_bad_lines=False)
print(apopcand(head())
apopcand.to_csv('apopcand.csv')
apopcand['mutation_ccle_cosmic'] = apopcand['mutation_ccle_cosmic'].apply(lambda x:x.split('')[0])

#reading the csv files with pandas and checking data
achilles=pd.read_csv('Achilles_v2.4_SampleInfo_small.csv')
print(achilles(head())

gene_dependency=pd.read_csv('gene_dependency.csv')
print(gene_dependency(head())

#selecting only KRas mutant cell lines from the csv
remove_WT=achilles.loc[(achilles['KRAS'] != 'WT') & (achilles['KRAS'] !='NA/WT')]
solamente=remove_WT.dropna(subset=['KRAS'])

#truncate file to only cell lines and tumor type
trunc=solamente.truncate(before='Name', after='Type', axis=1)
trunc.to_csv('truncate.csv')

#merge Dataframes based on KRas mutants
match_column=truncate.merge(trunc, gene_dependency, how='left', left_on=None, right_on=None)
match_column=truncate.merge(gene_dependency, how='inner', left_on='Name', right_on='line')

print (match_column(head())

#generate csv to examine output
merged3=match_column.to_csv('merged.csv')

#removing unessessary columns
unify=match_column.loc[:, 'line':]
unify = unify.rename(columns={'line': 'Name'})

#Renaming the cell lines in the 'Name' columns
unify['Name'] = unify['Name'].apply(lambda x: x.split('_')[0])
unify.to_csv('unify.csv')
print(unify(head())

#Set index to cell line names
#create dictionary after slightly changing dataframe structure
kras_dictionary=unify.set_index('Name').T.to_dict('list')
print(type(kras_dictionary))

#Test run for a specific cell line
print(kras_dictionary['LOVO'])





#Create a list from the dataframe column names and delete the first member 'Name'
#columns_names=list(unify.columns.values)
print(unify.columns_names)
del columns_names[0]
print(unify.columns_names)

plt.hist(list(kras_dictionary.keys()), kras_dictionary.values(), color='g')
plt.show()
