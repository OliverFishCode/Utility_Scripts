###### Call Packages ######
library(tidyverse) # Suite of packages for data manipulation
library(e1071) # Misc. Functions
#########User specified functions and values########## 
se =  function(x) sd(x)/(sqrt(length(x)))# calculates standard error 
percentile = c(0.05,0.95)# Percentiles of interest 
##########Basic descriptive statistics-my R equivalent to SAS proc univariate ######### 
Descriptive_stats = summarise(group_by(Data,Group),# applys following statistics by group 
                              Mean = mean(value), 
                              N = length(value),# number of observations
                              SD = sd(value),# standard deviation 
                              SE = se(value),# standard error 
                              Median = median(value), 
                              Skewness = skewness(value,
                              type = 2),# type 2 corresponds to the same estimations method used by sas 
                              Kurtosis = kurtosis(value,
                              type = 2),# type 2 corresponds to the same estimations method used by sas
                              Fifth_percentile= quantile(value,
                              probs = percentile[1], type = 2),# type 2 corrisponds to the same estimation method used in sas
                              Ninety_Fifth_percentile= quantile(value,
                              probs = percentile[2], type = 2))# type 2 corrisponds to the same estimation method used in sas 
remove(se, percentile)# cleans up work environment to point
