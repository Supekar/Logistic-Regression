import numpy as np
import csv
import numpy as np
import math
import sys
import copy
outputdata1=[]
my_dict = {}

train_file=sys.argv[1]
valid_file=sys.argv[2]
test_file=sys.argv[3]
dict_input=sys.argv[4]
train_out=sys.argv[5]
test_out=sys.argv[6]
mtest_out=sys.argv[7]
epoch=int(sys.argv[8])

with open(dict_input) as fileobj:
  for line in fileobj:
      key, value = line.split()
      my_dict[key] = value

with open(train_file, mode='r') as input:
    rd=csv.reader(input, delimiter="\t", quotechar='"')
    inputdata=[]
    for row in rd:
        inputdata.append(row)
input21=[]           
input21=inputdata

label=[]           
           
for i in range(len(input21)):
    label.append(input21[i][0])
#label=np.asarray(label)
#print(label)
array1=[]
array2=[]
input3=[]
train_label=[]
test_label=[]

for i in range(len(input21)):
    array1=[]
    array2=[]
    newarray=[]
    array1=input21[i]
    array2=array1[1:]
    newarray = [x[:-2] for x in array2]
    #input3=[1]
    input3.append(newarray)    #input3 is array of all indices ,rows 39176
#print(input3) 
#print(len(input3))
w=np.zeros((1,len(my_dict.values())+1))# weight matrix will be 39176+1 because of bias
#print(input3)
#input22= np.zeros((len(input3), len(my_dict.values())))
input22=np.zeros(shape=(len(input3),len(my_dict.values())+1))

#input22=np.asarray(input22)
#print(input22.shape)
for i in range(len(input3)):
    list4=[]
    list4=input3[i]
    for j in range(len(list4)):
        input22[i][0]=1
        input22[i][int(list4[j])+1]=1
#print(input22)  

#list4=np.asarray(input3[0])
#print(list4[0])
#input22[0][int(list4[0])]=1

#print(input22)
#for i in range(input22.shape[0]):
    #input4=[]
    
#print(input22.shape[1])
#print(label)
#print(input22)


#errort=0
value=int(epoch)
testing=0

for j in range(value):
    count=0
    for i in input22:
        input22T=i.T
        #print(i)
        wnew=np.dot(w,input22T)
        sigma=1.0/(1.0+np.exp(-wnew))
        #print(count)
        #testing+=1
        y1=float(label[count])
        #print(sigma)
        gradient=(sigma-y1)*input22T
        w=w-(0.1*gradient)
        #print(gradient)
        #print(w)
        count+=1
    errort=0    
    count1=0 
    outputlabel=[]
#print(input22)    
#print(w)

for k in input22:
    input22T=k.T
    ypred=np.dot(w,input22T)
    if ypred>=0:
        ycap=1
        
    else:
        ycap=0
        
    outputlabel.append(ycap)
        
    if ycap!=int(label[count1]):
        errort+=1
            
    count1+=1
    
numerator=errort
denominator=count1
err=(float(numerator)/float(denominator))
#print(err)
    #print(count1)
#print(input22.shape)
#print(w.shape)
#print(w)
#print(numerator)

with open(test_file, mode='r') as input:
    rd=csv.reader(input, delimiter="\t", quotechar='"')
    inputdata=[]
    for row in rd:
        inputdata.append(row)
input21=[]           
input21=inputdata

label=[]           
           
for i in range(len(input21)):
    label.append(input21[i][0])
#label=np.asarray(label)
#print(label)
array1=[]
array2=[]
input3=[]
train_label=[]
test_label=[]

for i in range(len(input21)):
    array1=[]
    array2=[]
    newarray=[]
    array1=input21[i]
    array2=array1[1:]
    newarray = [x[:-2] for x in array2]
    #input3=[1]
    input3.append(newarray)    #input3 is array of all indices ,rows 39176
#print(input3) 
#print(len(input3))
#w=np.zeros((1,len(my_dict.values())+1))# weight matrix will be 39176+1 because of bias
#print(input3)
#input22= np.zeros((len(input3), len(my_dict.values())))
input22=np.zeros(shape=(len(input3),len(my_dict.values())+1))

#input22=np.asarray(input22)
#print(input22.shape)
for i in range(len(input3)):
    list4=[]
    list4=input3[i]
    for j in range(len(list4)):
        input22[i][0]=1
        input22[i][int(list4[j])+1]=1

#print(input22)
#print(w)
#errort=0
value=60
testing=0

# for j in range(value):
#     count=0
#     for i in input22:
#         input22T=i.T
#         #print(i)
#         wnew=np.dot(w,input22T)
#         sigma=1.0/(1.0+np.exp(-wnew))
#         #print(count)
#         #testing+=1
#         y1=float(label[count])
#         #print(sigma)
#         gradient=(sigma-y1)*input22T
#         w=w-(0.1*gradient)
#         #print(gradient)
#         #print(w)
#         count+=1
#     errort=0    
#     count1=0 
#     outputlabel=[]
#print(w)
errort1=0
count2=0
testlabel=[]
for d in input22:
    input22T=d.T
    ypred1=np.dot(w,input22T)
    if ypred1>=0:
        ycap1=1
        
    else:
        ycap1=0
        
    testlabel.append(ycap1)
        
    if ycap1!=int(label[count2]):
        errort1+=1
            
    count2+=1
    
numerator1=errort1
denominator1=count2
err1=(float(numerator1)/float(denominator1))
#print(err)
    #print(count1)
#print(input22.shape)
#print(w.shape)
#print(numerator1)

with open(mtest_out, mode='w') as output:
    output.write("error(train): %f" %err)
    output.write("\n")
    output.write("error(test): %f" %err1)
    
with open(train_out, mode='w') as output:

    #tsv_writer=csv.writer(output, delimiter='\t')
    for i in outputlabel:
        output.write(str(i))
        output.write('\n')
        

with open(test_out, mode='w') as output:

    #tsv_writer=csv.writer(output, delimiter='\t')
    for i in testlabel:
        output.write(str(i))
        output.write('\n')
        