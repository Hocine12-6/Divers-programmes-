#نماذج
import os
import  time 
#دوال
def clear_sccren():
   os.system("cls" if os.name == "nt" else "clear")

#متغيرات عامة 
Books_in_catalog={}
check_out =0
check_in = 0
#البرنامج
while True:
 print("==============")
 print(f"Books : {len(Books_in_catalog)} |Available : {len(Books_in_catalog)-check_out} |Check out : {check_out} |Check in : {check_in}")
 print("==============")
 print("________________")
 print("Menu:")
 print("1. Add book")
 print("2. Check out book")
 print("3. Check In book")
 print("4. List Books")
 print("5. Exit")
 print("________________")

 
 while True :#ضبط المدخلات 
  user_gues_1= input("-Enter your choice (1-5): ")
  if len(user_gues_1)==1 and (True if user_gues_1 in"12345" else False) :
   break 
  else :
   print("Enter a ccorect choice please...")
 
 if user_gues_1 == "1":#add a book
    clear_sccren()
    while True :
      ISBN =input("Enter ISBN:")
      title=input("Enter the title:")
      author=input ("Enter author:")
      while True:
         if ISBN in Books_in_catalog :
            clear_sccren()
            print (f"This ID {ISBN} is in your catalog")
            ISBN=input("-Choice an other ISBN :")
         else :
            break
            
      Books_in_catalog[ISBN]={"Title":title , "Author":author , "Available":True}
      print(f"-The book {title} is add in your catalog and author is {author} avec ID :{ISBN} ☑.")
      
      user_gues_2= input ("Do you want add an other book..[y/n]:").lower()
      if user_gues_2 != "y":
         break 
    
    
 elif user_gues_1 =="2":#استعارة كتاب 
  clear_sccren()
  while True :
    if len(Books_in_catalog)==0:
       print("soory,your catalog not have a books,please add a book for check out ")
       break
    elif check_out == len(Books_in_catalog):
      print("-All books are check out ")
      break
    ISBN =input("Enter ISBN:")
    if ISBN in Books_in_catalog:
       if Books_in_catalog[ISBN]["Available"] == True :
           Books_in_catalog[ISBN]["Available"]=False
           print(f'The book"{Books_in_catalog[ISBN]["Title"]}" cheack out ssecssesffoly." ')
           check_out+= 1
       else:
          print(f'Sorry,the book "{Books_in_catalog[ISBN]["Title"]}" is not available . ')
    else:
       print(f'The book que ISBN :"{ISBN}" is not in catalog .')
    
       
    user_gues_2=input("Do you want chek out an other book...[y/n]:").lower()
    if user_gues_2 != "y":
     break
    
 elif user_gues_1 == "3":#ارجاع كتاب 
   clear_sccren()
   while True :
     if len(Books_in_catalog)==0:
        print ("soory,your catalog not have a books,please add a book and checkvout for check in ")
        break
     elif check_out==0:
        print("no book for chick in ,all the books in catalog ")
        break 
     ISBN = input ("Enter the ISBN for check in:")
     if ISBN in Books_in_catalog:
       if Books_in_catalog[ISBN]["Available"] == False :
           Books_in_catalog[ISBN]["Available"]=True
           print(f'The book"{Books_in_catalog[ISBN]["Title"]}" cheack in ssecssesffoly." ')
           check_out -= 1
           check_in += 1
       else:
           print(f'** the book "{Books_in_catalog[ISBN]["Title"]}" is available اصلا **')
     else:
           print(f'The book que ISBN :"{ISBN}" is not in catalog .')
     user_gues_2=input("Do you want  check in an other book...[y/n]:")
     if user_gues_2 != "y":
        break
 elif user_gues_1 == "4":#show the list 
   while True:
    clear_sccren()
    if len(Books_in_catalog)==0:
        print("the catalog are not hase any book")
        break
    print("-----------------")
    for ISBN in Books_in_catalog:
       print(f"{'ISBN'.ljust(10)}:{ISBN}")
       print(f"{'Title'.ljust(10)}:{Books_in_catalog[ISBN]['Title']}")
       print(f"{'Author'.ljust(10)}:{Books_in_catalog[ISBN]['Author']}")
       print(f"{'Available'.ljust(10)}:{Books_in_catalog[ISBN]['Available']}")
       print("-----------------")
    input("Enter any key  for back ...")
    break 
       
 else:#for exit 
   for x in range (5):
      clear_sccren()
      print("Exiting"+("." *x))
      time.sleep(0.5)
   clear_sccren()
   print("Exiting....♻")
   break
   
  
