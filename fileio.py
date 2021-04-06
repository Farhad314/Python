#we have to open file "with open", then filename and mode read, new filename for this program
#to read line, readlines() function
#strip() is a string function, it eliminate any space from front or end of any line
with open("paragraph.txt",mode="r") as nfile:
    for i in nfile.readlines():
        print(i.strip())

print('Finished')
#it will split any space between words
words_all=[]
with open("paragraph.txt",mode="r") as nfile:
    for i in nfile.readlines():
        words=i.strip().split(" ")
        words_all+=words
        print(words)

#we have added all strings in word_all in 14, then we created a new file and added all words in it 
#we can also sort it
with open("newparagraph.txt",mode="w") as wfile:
    for i in sorted(words_all):
        wfile.write(i)
        wfile.write(" ")

