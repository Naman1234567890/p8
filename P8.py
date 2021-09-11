import pandas as pd
data = pd.read_csv("SOCR-HeightWeight.csv")
data_weight = list(data['Weight(Pounds)'])

number_of_elements = len(data_weight)
sum= 0
for i in data_weight:
    sum = sum+i
mean= sum/number_of_elements
print(mean)


## calculation mode
range = {
    '50-60':0,
    '60-70':0,
    '70-80':0
}
for weight in data_weight:
    if(50<weight and weight<60):
        range['50-60']=range['50-60']+1
    elif (60<weight and weight<70):
        range['60-70']=range['60-70']+1
    elif (70<weight and weight<80):
        range["70-80"]=range["70-80"]+1
print(range)

##median
data_weight.sort() 
if(number_of_elements%2 == 0):
    median = data_weight[number_of_elements//2]+ data_weight[number_of_elements//2-1]
else:
    median = data_weight[number_of_elements//2]
print(median)