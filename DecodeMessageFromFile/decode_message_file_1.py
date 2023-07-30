# Start of the decode function that will read in a text file using the parameter message_file.

def decode(message_file):
  
  # Create here the key function for use as a parameter in the Python sort method/function below. See https://www.w3schools.com/python/ref_list_sort.asp
  # Set the index to 0 to only access numbers from ln list.
  def sortfirst(ln):
     return int(ln[0]) # We employ the int type cast because the numbers in text file are stored as a string type. We need to convert to the integer type so that Python's sort method/function can properly sort the numbers in ascending order. 
                       # A number stored as a string isn't equal to the same number stored as an int.
                       # ln[0] accesses the number elements in the ln list.

  list =[] #Declare an empty list variable first which we use to append a list contains string data from our text file. 
           #Arrays aren't built-in Python data structures.Lists are employed instead which and are slicable.See: https://www.freecodecamp.org/news/python-array-tutorial-define-index-methods/#:~:text=Lists%20are%20built%20into%20the,in%20order%20to%20be%20used.
  
  # Enter a Python for loop that will go over each line of text in  message_file.
  for eachline in message_file:
    ln = eachline.split(" ")  #Call the Python split function for each line (x) in the text file by the whitespace separator. ln is a list of a list containing the numbers and text stored as string data type.
    list.append(ln)    #Call Python append with ln parameter which contains the two elements split from the string from a text line in the file. 
  
  # Call Python sort function using the key created eariler.
  list.sort(key=sortfirst) # We needed to create a sortfirst key function as a control parameter to sort the list we created.
  #print(list)

  '''As an example: 

  Let list= [1,2,3,4,5,6,7,8,9,10]
  
  #The following indices in the below slices,list([x:y]), prints out the numbers in a staircase pattern:
  #print(list[0:1]) -> 1
  #print(list[1:3]) -> 2 3
  #print(list[3:6]) -> 4 5 6
  #print(list[6:10])-> 7 8 9 10
  
  Python's list index starts at zero. Values before the ending index and on starting index onwards are printed.
  Taking as an example the ending indices in the above slices. It increases in following manner: 1 -> add 2 (initial val) -> 3 , 3 -> add 3(=2+1)-> 6, 6 -> add 4(=3+1) ->10 , ... (it's similar for our starting indices)
  Therefore each time a loop is completed we increase the interval between the indices by 1 in order to get slices that print the pyramid /staircase pattern.
  '''

  #Initalize variables for our list slices before entering for loop
  start=0 
  end=1
  interval=2

  str="" #Initialize string variable for code in below for loop.
  
  #Iterate through the list:
  for eachline in list:
    #print(list[start:end])
    #print(list[end-1][1])
    #print(type(list[end-1][1])) #See data type
    str = str +" "+list[end-1][1].rstrip('\n') #The strings/words associated with each of the ending numbers in the pyramid/staircase are concatenated by this line of code 
                                               #Applying the rstrip() method/function removes the newline character in the list. This allows printing of words on a single line.

    start=end # Move our start index up the list after concatenation by setting it to ending value after each iteration of the for loop.
    end=end+interval # The ending index is moved up at first by 2 places from its previous position, then by 3, 4, ... by incrementing the interval variable. 
    interval=interval+1  #Interval is increased by 2, then 3 , 4, ...

    if(list[start:end]==[]): #This code block breaks out of the for loop if no other elements are found while transversing the list.
       break

  return str.lstrip() #Need to apply lstrip() Python string method to remove the whitespace at the beginning of the concatenated string in our str variable.
    

#Beginning of program

message_file= open("input.txt","r") #Opens text file assuming it's in the same folder as the Python file. If any other issues try adding folder to workspace.

print(decode(message_file)) #Call decode function with file input parameter i.e message_file and print out the decoded string

message_file.close() #Closes our opened text file.


