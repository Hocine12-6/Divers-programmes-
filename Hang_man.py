import random #استرحاع نموذج عشوتئية
import string
words = ['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar',
         'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat',
         'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt',
         'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven',
         'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider',
         'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf',
         'wombat', 'zebra']#قائمة كلمات ليختار عشوئيا
word = random.choice(words) #يختار كلمة عشوائية من القائمة السابقة 

espace =("_ "*len(word)).split() # عمل قائمة بمسافات نفس طول الكلمة العشوئية
print(" ".join(espace))#طباعة المسافات على شكل جملة بين كل شلطة مسافة لتوضيح المسافات للمستخدم

tries=7 #تعيين متغير كعداد محاولات 
false_guses=[]#قائمة نسجل فيها ما أدخله المستخدم 
tries1use = 0
print('''
  +---+
      |
      |
      |
      |
      |
=========''')
print ("***The tries are your attempts*** ")
print("   TRIES = 7")
while  ("_"  in espace ) and ( tries > 0 ) : #مدام في المتغير مسافات و عداد المحاولات أكبر من صفر فكرر
	user_gues=input("__________\nGues a carecter :").lower() #طلب من المستخدم توقع حرف
	
##########################
	punctuation=False
	if user_gues:
	 		 			for x in user_gues:
	 		 				if x in string.punctuation:
	 		 					punctuation=True
	 		 					break
 
		
	if user_gues == "ls logs":#طباعة قائمة الحروف الخطاطئة التي أدخلها المستخدم 
		if len(false_guses) !=0:
			print("-".join(false_guses))
		else:
			print("YOUR LOGS ARE NONE")
		continue
		
	elif user_gues == "exit":#خروج من اللعبة 
		exit()
		
	elif user_gues == "ls tries":#عرض المحاولات الباقية 
		print(tries)
		continue
		
	elif user_gues == "tries1" :#إظافة محاولة واحدة  للجولة 
		if tries1use==0:
			tries += 1
			tries1use += 1
		else :
			print ("YOU ARE USE THIS ")
		continue
		
	elif user_gues == "change()":#تغيير الكلمة  يدويا 
		new_word=input(">>>")
		if new_word:
			 for x in new_word:
	 		 		if x in string.punctuation:
	 		 			punctuation=True
	 		 			break
		if " " in new_word :
			print("dont enter espace in the new word ... ")
			continue
		elif not new_word:
			print("Empty input")
			continue
		elif punctuation:
			print("Don't enter punctuation")
			continue
		else:
			espace=("_ "*len(new_word)).split()
			word=new_word
			continue
			

	elif len(user_gues )>1:
		print("YOUR GUES ARE SO STRONG \n ---Do not exceed one letter ---")
		continue
#############################
	if punctuation:
		print ("Don't enter punctuation")#إذا أدخل المستخدم علامات ترقيم نطبع 
		continue#و نعود 
		
	if user_gues in word :#تحقق مما اذا كان اختيار المستخدم داخل الكلمة 
			if user_gues:#تحقق مما اذا كان مدخل المستخدم فارغ فالتحقق السابق لا يكشفه  إلا اذا أدخل مدخلا لا يوجد في الكلمة  ففي الثعبان لا شيء يوجد في كل نص
				for x  in range (len(word)) :#تعويض المسافات بالحروف الصحيحة في الأجزاء الصحيحة  باستعمال تكرار منطقي  (ركز على التكرار لتفهم )
					if word[x]  == user_gues:
						espace[x]=user_gues
			else:#اذا لم يدخل المستخدم شيء  ننفذ ما يلي 
					print("You did not enter anything")
					continue
	else:#اذا لم يكن اختيار المستخدم في الكلمة ننفذ الشرط التالي
	    if user_gues not in false_guses:#اذا لم يكن الإختيار في سجل ادخالاته الخاطئة فقم بخصم نقطة و أضف الإختيار لسجل أخطاءه 
	    	tries -= 1#خصم المحاولة 
	    	print("TRIES -1")
	    	false_guses.append(user_gues)#اضافة المدخل الخاطئ لقائمة الأخطاء 
	    	
	    	#طباعة الرسمة حسب عدد اامحاولات الباقية
	    	if tries ==7: 
	    		print('''
  +---+
      |
      |
      |
      |
      |
=========''')
	    	elif tries ==6: 
	    		print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')#حبل
	    	elif tries == 5:
	    		print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')#رأس
	    	elif tries == 4:
	    		print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')#جسد
	    	elif tries ==	3:
	    		print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')#ذراع أيمن 
	    	elif tries ==	2:
	    		print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')#ذراع أيسر 
	    	elif tries == 1:
	    		print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')#قدم أيمن
	    else:#و إلا فلا تخصم و قم بطباعة له ما يلي 
	    	print("you alse enter this .Try again...")

	print(" ".join(espace))#نطبع المسافات بعد تركيب الحروف في مكانها الصحيح راجع الشرط السابق اذا لم تفهم  في السطر 15
	print (f" You have {tries} more tries")#طباعة المحاولات 
	
if "_" not in espace :#اذا لم تبقى مساحة في قائمة المسافات فالمستخدم فاز 
	print(("(_________\n    *******\n    you win\n    *******").upper())
else:#و إلا فقد نفذت محاولاته و خسر 
	print("""_________
	  YOU LOSE !
   +**+
   |  |
   O  |
  /|\ |
  / \ |
      |
  =====""")#جسم كامل 
  
