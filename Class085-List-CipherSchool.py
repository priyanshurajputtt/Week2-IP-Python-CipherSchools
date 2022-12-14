num=[1,2,3,4]
print(num[2])


word=["word1","word2","word3"]
print(word[:1])

mixed=[1,2,3,4,"five","six",2.3,None]
# print(mixed)

# mixed[1]='two'
# mixed[1:]='two'
mixed[:1]='two'
mixed[1:]=['two','three']
print(mixed)