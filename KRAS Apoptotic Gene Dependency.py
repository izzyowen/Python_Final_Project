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
