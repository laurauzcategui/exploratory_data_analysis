# Obtain the working directory
getwd()

# Change working directory
setwd('/data')

# Check working dir has been changed
getwd()

# Load the dataset
reddit <- read.csv('./datasets/reddit.csv')

# Table reddit dataset
table(reddit$employment.status)

# Summary
summary(reddit)

# Examine levels of Variables 
levels(reddit$age.range)

# Let's plot to see age.range factor
qplot(data=reddit, x=age.range)

# order the age.range
reddit$age.range <- ordered(reddit$age.range,levels=c("Under 18", "18-24", "25-34", "35-44", "45-54", "55-64", "65 or Above"))

# Let's plot to see age.range factor
qplot(data=reddit, x=age.range)

