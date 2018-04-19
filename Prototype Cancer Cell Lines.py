#import all the relevant packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#reading the csv files with pandas and checking data
achilles=pd.read_csv('Achilles_v2.4_SampleInfo_small.csv')
print(achilles(head())

gene_dependency=pd.read_csv('gene_dependency.csv')
print(gene_dependency(head())

#selecting only KRas mutant cell lines from csv
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

#generating list of apoptotic genes
apoptotic_genes= pandas.read_csv("Apo_Mutations.tar.gz", header=0)
genes = list(apoptotic_genes.Genes)

#Parsing apoptotic gene list from KRAS gene dependency csv
df1 = pd.Dataframe(match_column, columns=genes)
