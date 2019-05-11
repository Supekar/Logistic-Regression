import csv
import numpy as np
import math
import sys
import copy

indexvalue=1

def model1(infile,outfile,dict1):

	outputdata1=[]

	my_dict = {}
	with open(dict1) as fileobj:
		for line in fileobj:
			key, value = line.split()
			my_dict[key] = value
	  

#print(len(inputdata))
	with open(infile, mode='r') as input:
		rd=csv.reader(input, delimiter="\t", quotechar='"')
		inputdata=[]
	
		for row in rd:
			inputdata.append(row)
	
		for i in range(len(inputdata)):
			outputdata=[]
			outputdata.append(inputdata[i][0])
		
			line1=inputdata[i][1]
			line2=line1.split()
			outputdata2=[]
			for word in range(len(line2)):
				if line2[word] in my_dict:
				#print(line2[word])
				#print(my_dict.get(line2[word]))
				#outputdata2.append(str(my_dict.keys().index(line2[word]))+ ":1")
					outputdata2.append(str(my_dict.get(line2[word]))+ ":1")
				outputdata2 = list(set(outputdata2))
			#print(outputdata2)
		   
		#outputdata2 = list(set(outputdata2))
			for i in range(len(outputdata2)):
				outputdata.append(outputdata2[i])
		
		#outputdata.append(outputdata2)
			outputdata1.append(outputdata)


		
	#print(outputdata1)        #print(len(outputdata1))
	with open(outfile, mode='w') as output:
	
		tsv_writer=csv.writer(output, delimiter='\t')
		for i in outputdata1:
			tsv_writer.writerow(i)



def model2(infile1,outfile1,dict2):
	outputdata1=[]

	my_dict = {}
	with open(dict2) as fileobj:
		for line in fileobj:
			key, value = line.split()
			my_dict[key] = value
	  

#print(len(inputdata))
	with open(infile1, mode='r') as input:
		rd=csv.reader(input, delimiter="\t", quotechar='"')
		inputdata=[]
	
		for row in rd:
			inputdata.append(row)
	
		for i in range(len(inputdata)):
			outputdata=[]
			outputdata.append(inputdata[i][0])
		
			line1=inputdata[i][1]
			line2=line1.split()
		
			outputdata2=[]
			for word in range(len(line2)):
				if line2[word] in my_dict:
					p=line2.count(line2[word])
				
					if p<4:
					#outputdata2.append(str(my_dict.keys().index(line2[word]))+ ":" +str(p))
						outputdata2.append(str(my_dict.get(line2[word]))+ ":1")
				outputdata2 = list(set(outputdata2))
			for i in range(len(outputdata2)):
				outputdata.append(outputdata2[i])     
			outputdata1.append(outputdata) 
		
	#print(outputdata1)        #print(len(outputdata1))
	with open(outfile1, mode='w') as output:
	
		tsv_writer=csv.writer(output, delimiter='\t')
		for i in outputdata1:
			tsv_writer.writerow(i)




train_file=sys.argv[1]
valid_file=sys.argv[2]
test_file=sys.argv[3]
dict_input=sys.argv[4]
train_out=sys.argv[5]
valid_out=sys.argv[6]
test_out=sys.argv[7]
flag=int(sys.argv[8])

if flag==1:
	model1(train_file,train_out,dict_input)
	model1(valid_file,valid_out,dict_input)
	model1(test_file,test_out,dict_input)

elif flag==2:
	model2(train_file,train_out,dict_input)
	model2(valid_file,valid_out,dict_input)
	model2(test_file,test_out,dict_input)
else:
	nono=1
