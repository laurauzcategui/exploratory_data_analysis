# Obtain the working directory
getwd()

# Change working directory
setwd('/data')

# Check working dir has been changed
getwd()

# Load the dataset
statesInfo <- read.csv('./datasets/stateData.csv')

# Let's subset the dataset
subset(statesInfo, state.region == 1)

# Another way to subset
statesInfo[statesInfo$state.region == 1, ]
