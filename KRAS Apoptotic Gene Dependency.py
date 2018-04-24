#!
#Python Final Project
#Assessing Gene Dependency of Apoptotic Genes in KRAS Mutant Cancers
#By: Owen, Izzy, Izadjoo, Salman, Hussain, Imran, Gierlack, Steven, Bauman, Bradly

#import all the relevant packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#reading the csv files with pandas and checking data
#sample info sourced from Project Achilles Achilles, v2.4.3 data folder
#(https://portals.broadinstitute.org/achilles/datasets/5/download)
achilles=pd.read_csv('Achilles_v2.4_SampleInfo_small.csv')
achilles.head()
achilles.shape

#CRISPR gene dependency data sourced from Project Achilles avana_public_18Q1, v3 data folder
#(https://portals.broadinstitute.org/achilles/datasets/18/download)
gene_dependency=pd.read_csv('gene_dependency.csv')
gene_dependency.head()
gene_dependency.shape

#selecting only KRas mutant cell lines from csv
remove_WT=achilles.loc[(achilles['KRAS'] != 'WT') & (achilles['KRAS'] !='NA/WT')]
solamente=remove_WT.dropna(subset=['KRAS'])
solamente.head()

#truncate file to only cell lines and tumor type
trunc=solamente.truncate(before='Name', after='Type', axis=1)
trunc.shape
trunc.head()

#merge Dataframes based on KRas mutants and drop 'Line' column
match_column=trunc.merge(gene_dependency, how='inner', left_on='Name', right_on='line')
match_column.drop(['line'], axis=1, inplace=True)
match_column.shape
match_column.head()

#remove Entrez gene number from gene names in column headers
match_column.rename(columns=lambda x: x.split(' ')[0], inplace=True)
match_column['Name']=match_column['Name'].apply(lambda x: x.split('_')[0])
match_column.drop(['Type'], axis=1, inplace=True)
match_column.head()

#generating list of apoptotic genes
apoptotic_genes=pd.read_csv('mutation_ccle_cosmic', sep='\s+', names=['Gene', 'UniProt', 'Cancer', 'CDS Mutation', 'AA Mutation', 'Database'], header=None)
apoptotic_genes.head()
apoptotic_genes.shape
    #remove duplicate copies of gene names
apo_genes2=apoptotic_genes.drop_duplicates(subset='Gene')
apo_genes2.head()
    #generate list of genes from 'Gene' column
genes=list(apo_genes2.Gene)
