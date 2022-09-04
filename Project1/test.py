# Write a for loop that uses range() to iterate over the positions in usernames to modify the list. Like you did in the previous quiz, change each name to be lowercase and replace spaces with underscores. After running your loop, this lis
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for idx in range(len(usernames)):
    usernames[idx] = usernames[idx].lower().replace(" ", "_")

print(usernames)

# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for key in basket_items:
    #if the key is in the list of fruits, add the value (number of fruits) to result
    if key in fruits:
        result += basket_items[key]
#if the key is in the list of fruits, add the value (number of fruits) to result


print(result)