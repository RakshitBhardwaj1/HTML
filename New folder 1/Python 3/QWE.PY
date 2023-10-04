# # str=input("Enter the alpha numeric tect\n")
# # count1=0
# # count2=0

# # for i in str:
# #     if str(i).isalpha():
# #         count1 +=1
# #     else:
# #         count2 +=2
# # print(count1)
# # print(count2)input
# # input_string=input("Enter the alpha numeric value")
# # num_alphabets=0
# # num_digits=0
# # num_specialcharacter=0
# # for entries in input_string:
# #     if entries.isalpha():
# #         num_alphabets+=1
# #     elif entries.isdigit():
# #         num_digits+=1
# #     else:
# #         num_specialcharacter+=1
# # print(f"Number of alphabets:-{num_alphabets}")
# # print(f"Number of digits:-{num_digits}")
# # print(f"Number of spacial charcters:-{num_specialcharacter}")

# # user_input=input("Enter the data")
# # reverse=user_input[::-1]
# # print(reverse)

# # str=input("Enter the alpha numeric value")
# # str1=" "
# # for i in str:
# #     if i.isalpha():
# #         str1=str1+i
        
# #     elif i.isdigit():
# #         print(i,end=" ")
# # print()
# # print("string",str1)

str=input("Enter the alpha numeric value")
str1=" "
str2=" "
for i in str:

    if i.isalpha():
        str1=str1+i
        
    elif i.isdigit():
         str2=str2+i
print()
print("string",str1)
print("digits",str2)



