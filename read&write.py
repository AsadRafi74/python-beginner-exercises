# f =open("demo.txt","r")
# data = f.read()
# print(data)                    #for reading data from txt file 
# print(type(data))
# f.close()




# f =open("demo.txt","r")

# line1 = f.readline()
# print(line1)                     #for printing line 1 from txt

# f.close()


# f = open("demo.txt", "a")

# # f.write("i am doing paractice for python ")    #for write new data 

# f.write("\n i am doing coidung for the 1st time in python")
 
# f.close()

# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)                      #write  with synatx
    

# with open ("practice.txt","r") as f:
#     data = f.read()
# new_data = data.replace("java","pyhton")  
# print(new_data)                                 replacing java with python in practice.txt file


# with open ("practice.txt","w") as f:
#     f.write(new_data)

# def check_for_word():
#     word = "learning"
#     with open("practice.txt","r") as f:
#         data = f.read()
#         if (data.find(word) != -1):
#             print('found')                            #check for word 
#         else:
#             print("not found")

# check_for_word()
    
# def check_for_line():
#     word = "programming"
#     data = True
#     line_no =1
#     with open("practice.txt","r") as f:
#         while data:                             #check for lines with word
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#             line_no +=1
# check_for_line()
    


# with open("practice.txt","r") as f:
#     data = f.read()   
#     print(data)
#     num = ""
#     for i in range(len(data)):
#         if (data[i] ==","):        #for printing list of numbers 
#             print(int(num))
#             num = ""
#         else:
#             num += data[i]


count = 0
with open("practice.txt","r") as f:
    data = f.read()
    
    nums = data.split(",")
    for val in nums:                            # for checking even num in list 
        if(int(val)%2 ==0):
            count += 1
            
print(count)