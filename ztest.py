import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics
import csv
import random
import pandas as pd


df = pd.read_csv("csvfile.csv")   # put your csv file name here
data = df["Math_score"].tolist()







def randomMean(counter):
    
    arr1 = []
    for i in range(0, counter):
        
        randindex  = random.randint(0,len(data)-1)
        value = data[randindex]
        arr1.append(value)
    
    m = statistics.mean(arr1)
    return m



meanList = []
for i in range(0,1000):
    
    set_of_means = randomMean(100)
    meanList.append(set_of_means)



std_deviation = statistics.stdev(meanList)
mean = statistics.mean(meanList)
print("sampling distribution mean: ",mean)
print("std dev of sampling distributoin: ", std_deviation)



first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation

second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)

third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)





# math lab studets
df = pd.read_csv("School_1_Sample.csv")

data = df["Math_score"].tolist()
mean_of_sample1 = statistics.mean(data)



print("Mean of sample1:- ",mean_of_sample1)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD MATH LABS"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))

fig.show()




# math practice app students
df = pd.read_csv("School_2_Sample.csv")

data = df["Math_score"].tolist()
mean_of_sample2 = statistics.mean(data)

print("mean of sample 2:- ",mean_of_sample2)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO USED THE APP"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))

fig.show()


# register students
df = pd.read_csv("School_3_Sample.csv")

data = df["Math_score"].tolist()
mean_of_sample3 = statistics.mean(data)

print("mean of sample3:- ",mean_of_sample3)
fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample3, mean_of_sample3], y=[0, 0.17], mode="lines", name="MEAN OF STUDNETS WHO WERE ENFORCED WITH MATH REGISTERS"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))

fig.show()





z_score = (mean - mean_of_sample2)/std_deviation

print( "Our Z score is ", z_score)
