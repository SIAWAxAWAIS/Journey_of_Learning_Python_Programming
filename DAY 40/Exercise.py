# st = input("Enter String Value: ")
# words = st.split(" ")
# coding = input("Enter 0 for Coding or Enter 1 for Decoding: ")
# coding == True if (coding=="0") else False
# print(coding)
# if(coding):
#     newword = []
#     for word in words:
#         if(len(word)>=3):
#             d1 = "hty"
#             d2 = "xnt"
#             stnew = d1+ word[1:] + word[0] +d2
#             newword.append(stnew)
#         else:
#             newword.append(word[::-1])
#     print(" ".join(newword))
    
# else:
#     newword = []
#     for word in words:
#             if(len(word)>=3):
#                 stnew = word[3:-3]
#                 stnew = stnew[-1] + stnew[:-1]
#                 newword.append(stnew)
#             else:
#                 newword.append(word[::-1])
#     print(" ".join(newword))



    # For Random 


import random
import string

st = input("Enter String Value: ")
words = st.split(" ")
user_choice = input("Enter 0 for Coding or Enter 1 for Decoding: ")


is_coding = True if user_choice == "0" else False

if is_coding:
    newword = []
    for word in words:
        if len(word) >= 3:
            d1 = "".join(random.choices(string.ascii_lowercase, k=3))
            d2 = "".join(random.choices(string.ascii_lowercase, k=3))

            stnew = d1 + word[1:] + word[0] + d2
            newword.append(stnew)
        else:
            newword.append(word[::-1])
    print(" ".join(newword))

else:
    newword = []
    for word in words:
        if len(word) >= 3:
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            newword.append(stnew)
        else:
            newword.append(word[::-1])
    print(" ".join(newword))