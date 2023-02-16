print("___** THE USER MUST HAVE TO INPUT ONE UPPER CASE LETTER **____")
print("_______** But not more than one upper case letter **__________")
print()


txt1=input("For first row: ")
if len(txt1)>10:
  print("Invalid Input Size")
txt2=input("For second row: ")
if len(txt2)>10:
  print("Invalid Input Size")


counter_text1=0  
for i in txt1:
  if ord(i)>ord('@') and ord(i)<ord('['):
    counter_text1+=1
if counter_text1>1:
  print("Invalid Input!!","Upper case available:",counter_text1)


counter_text2=0  
for i in txt2:
  if ord(i)>ord('@') and ord(i)<ord('['):
    counter_text2+=1
if counter_text2>1 or counter_text1>1:
  print("Invalid Input!!","Upper case available:",counter_text1,"in first and", counter_text2,'in second')
elif counter_text1==0 or counter_text2==0:
  print("Invalid Input") 
else:
  #Builting the array
  array=[[0]*10,[1]*10]

  for i in range(len(txt1)):
    array[0][i]=txt1[i]
  for i in range(len(txt2)):
    array[1][i]=txt2[i]
  
  def Size(array):
   size=0

   for i in range(len(array)):
     if array[i]!=0:
       size+=1
   return size

  def Start(array):
   start=0
   for i in range(len(array)):
     if 65<=ord(array[i])<=90:
      start=array[i]
   return start

  def Index(array):
   idx=0
   for i in range(len(array)):
     if array[i]==Start(array):

       idx=i
   return idx
  print("The Array",array)
  print()
  print(array[0])
  print(array[1])
  print()
  print()
  print("Size of first row:",Size(array[0]))
  print("Size of second row:",Size(array[1]))
  print()
  print()
  print("---------------Initially--------------")
  print()
  print("Starting Character for second row:",Start(array[0]))
  print("Starting Character for second row:",Start(array[1]))
  print() 
  print("index of first:",Index(array[0]))
  print("index of second:",Index(array[1]))
  print()

  #Calling Functions
  def left(array,k,idx,size):

    i=(idx+k)%len(array[0])
    count=0
    while count<size:
      print(array[0][i],end='')
      i=(i+1)%len(array[0])
      count+=1

  def right(array,k,idx,size):
    i=(idx-k)%len(array[1])
    count=0
    while count<size:
      print(array[1][i],end='')
      i=(i+1)%len(array[0])
      count+=1
  print()
  print("-------------------------------------------------")
  print()
  k=1
  Enter=0
  while True:
    Enter=(input("Press any key to continue and Q/q to Exit: "))
    if Enter=='Q' or Enter=="q":
      break
    print("<<----Left Print--")
    left(array,k,Index(array[0]),Size(array[0]))
    print()
    print("--Right Print---->>")
    right(array,k,Index(array[1]),Size(array[1]))
    k+=1
    print()

  print()  
  print()
  print("---------------After Exiting the loop--------------")
  print()
  print("Starting Character for second row:",Start(array[0]))
  print("Starting Character for second row:",Start(array[1]))
  print() 
  print("index of first:",Index(array[0]))
  print("index of second:",Index(array[1]))
  print()
    


  
 
  


