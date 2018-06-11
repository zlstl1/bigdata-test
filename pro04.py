
def counter (split_rs,word) :
    count=0
    for i in split_rs :
        if i == word:
            count+=1
    return count

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
 in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

rs = s.replace(',', '').replace('.', '').replace('\n','')

split_rs = rs.split(" ")
split_rs.sort(key=str.lower)

temp = split_rs[0].upper()
for word in split_rs :
    if word != temp :
        print("%s : %d " % (word.upper(),counter(split_rs,word)) )
        temp = word
    else :
        temp = word



