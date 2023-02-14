#Exercise #1
#Reverse the list below in-place using an in-place algorithm.
#For extra credit: Reverse the strings at the same time.


words = ['this' , 'is', 'a', 'sentence', '.']

def swap(words, i, j):
    words[i], words[j]= words[j], words[i]
    sliced_words= words[::-1]
    
    return words


print(reverse(words))






#Exercise #2
#Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.
#Should output:
#{'a': 5,
#'abstract': 1,
#'an': 3,
#'array': 2, ... etc...

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
word_counts = word_count(a_text)
print(word_counts)



#Exercise #3
#Write a program to implement a Linear Search Algorithm.
#  Also in a comment, 
# write the Time Complexity of the 
# following algorithm.

nums_list = [10,23,45,70,11,15]
target = 70

def linear_search(nums_list, n, target):
        for i in range(0, n):
            if (nums_list[i] == target):
                return i

# If number is not present return -1
index = linear_search(nums_list, len(nums_list), target)
print(index)            