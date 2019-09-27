

#Import the relevant libraries
import pandas as pd
import matplotlib.pyplot as plt

#Import the baseline file and label the columns
df = pd.read_fwf('baseline.txt', delimiter=" ", names = ['Class', "Count"])
df

#remove the column header that we do not need
df = df.dropna()
df

# add a new column with the sentiment values
df = df.copy()
df['Values'] = range(-5,6)
df


#Find the total number of sentiment counts
df['Count'].sum()

# Multiply the count by value to get the score
df['Score'] = df['Count']*df['Values']
#Normalize the count value and score value to total counts
df['Normalized Count']=df['Count']/df['Count'].sum()
df['Normalized Score']=abs(df['Normalized Count']*df['Values'])
df

#Average sentiment value
df['Score'].sum()/df['Count'].sum()

#Make a bar plot of the baseline tweet sentiment scores
plt.bar(df['Values'],abs(df['Score']))
plt.xlabel('Sentiment Value')
plt.ylabel('Tweet Score')
plt.title('Baseline Tweet Sentiment Scores')
plt.show()

#Make a bar plot of the baseline tweet sentiment normalized scores
plt.bar(df['Values'],df['Normalized Score'])
plt.xlabel('Sentiment Value')
plt.ylabel('Normalized Tweet Score')
plt.title('Baseline Tweet Sentiment Normalized Score')
plt.show()

#Bar plot of the baseline tweet sentiment count
plt.bar(df['Values'],df['Count'])
plt.xlabel('Sentiment Value')
plt.ylabel('Tweet Count')
plt.title('Baseline Tweet Sentiment Count')
plt.show()


#Bar plot of the baseline tweet sentiment normalized count
plt.bar(df['Values'],df['Normalized Count'])
plt.xlabel('Sentiment Value')
plt.ylabel('Tweet Normalized Count')
plt.title('Baseline Tweet Sentiment Normalized Count')
plt.show()

# # # # # #
# Import the search specific tweets and make the same columns as we did for the baseline tweets.
#Import the baseline file and label the columns
df2 = pd.read_fwf('buff_py.txt', delimiter=" ", names = ['Class', "Count"])
df2
#remove the column header that we do not need
df2 = df.dropna()
df2
# add a new column with the sentiment values
df2 = df.copy()
df2['Values'] = range(-5,6)
df2


# Find the 'total count' AND 'average sentiment value' of your specific tweets
df2['Count'].sum()

# Multiply the count by value to get the score
df2['Score'] = df['Count']*df['Values']
#Normalize the count value and score value to total counts
df2['Normalized Count']=df['Count']/df['Count'].sum()
df2['Normalized Score']=abs(df['Normalized Count']*df['Values'])
df2

#Average sentiment value
df2['Score'].sum()/df['Count'].sum()



# Make at least two graphs representing your specific tweet sentiment analysis.  They can be similar to the plots above
# but they can be different too. Makre sure you add titles and have labeled axis.

# Try making at least one graph that shows the difference in baseline tweet counts or scores to your tweet specific counts or scores.
# Remember, Google (LMGTFY) is a great resource.
##### find the graph and the writeup in the word doc