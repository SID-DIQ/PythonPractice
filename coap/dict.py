
#TASK 1
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
sampleDict["class"]['student']['marks']['history']

print("------------------------------------------------------------------------------------")
#MOHAMED SIDDIQ M (KONGUNADU COLLEGE OF ENGINEERING AND TECHNOLOGY)
#TASK 1

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1=set1|set2 
print(set1)
#By Using Union Operator we can Reject the Duplicate Elements
print("------------------------------------------------------------------------------------")

#TASK 2
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])
#By using splicing operator 
print("------------------------------------------------------------------------------------")

#create a list by picking an odd-index items from the first list and even index items from the second
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
print(l1[1::2]+l2[0::2])
print("------------------------------------------------------------------------------------")

#TASK 2
Dict={'a': 100, 'b': 200, 'c': 300} #200 present or not

if 200 in Dict.values():
    print("200 is present in the dictionary values.")
else:
    print("200 is not present in the dictionary values.")
    
#Another Method 

if Dict.get('b')==200:
    print("200 is present in the dictionary values")
else:
    print("200 is not present in the dictionary values")

