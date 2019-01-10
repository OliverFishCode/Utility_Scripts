library(tidyverse)

AppendMe <- function(dfNames) {
  do.call(rbind, lapply(dfNames, function(x) {
    cbind(get(x), Trial_ID = x)
  }))
}#Creates function to append by row and creat new variable based on DF name
 #Function is based on https://stackoverflow.com/questions/15162197


Trial_1 = data.frame(c(1,2,3,1,4,3),c("G","A","G","A","G","A"))
colnames(Trial_1)= c("mort", "group")# mort = Mortality

Trial_2 = data.frame(c(2,2,3,4,4,3),c("G","A","G","A","G","A"))
colnames(Trial_2)= c("mort", "group")

Trial_3 = data.frame(c(1,1,1,1,1,1),c("G","A","G","A","G","A"))
colnames(Trial_3)= c("mort", "group")


Trial_1 = data.frame(Trial_1%>%group_by(group)%>%mutate(cummort = cumsum(mort)))
Trial_2 = data.frame(Trial_2%>%group_by(group)%>%mutate(cummort = cumsum(mort)))
Trial_3 = data.frame(Trial_3%>%group_by(group)%>%mutate(cummort = cumsum(mort)))

Trial_all = AppendMe(c("Trial_1","Trial_2","Trial_3"))
Trial_all = data.frame(test_all%>%group_by(Trial_ID,group)%>%mutate(cummort2 = cumsum(mort)))

