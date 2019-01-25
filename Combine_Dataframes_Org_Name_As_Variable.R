appendme <- function(dfnames) {
  do.call(rbind, lapply(dfnames, function(x) {
    cbind(get(x), Hatch_Trial_ID = x)
  }))
}  # Append dataframe by row and create a new variable based on DF name
# Function is based on https://stackoverflow.com/questions/15162197