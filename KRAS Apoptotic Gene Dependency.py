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
