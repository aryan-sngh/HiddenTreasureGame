print('''
          ,           ,
   /             \
  ((__-^^-,-^^-__))
   `-_---' `---_-'
    <__|o` 'o|__>
       \  `  /
        ): :(
        :o_o:
         "-"  
 
 ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1=input("choose sleep or awake  as is depand your own luck:")

if choice1 == "sleep":
    print("go to next step ")
    choice2=input("choose phone or tv:")
    if choice2 == "tv":
        print("go to next step")
        choice3=input("choose movie type comedy ,romantic and fight:")
        if choice3 == 'comedy':
            print("galat answer game over")
        elif choice3 == 'fight':
            print("galat answer gane over")
        elif choice3 == 'romantic':
            print("win finally jeet geye aap ")
        else:
            print("sahi se likho")
    elif choice2 == 'phone':
        print("game over:")
    else:
        print("sahi se likho")
elif choice1 == 'awake':
    print("game over:")
else:
    print("fir se likh")