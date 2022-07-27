
f=open("address.txt",'r')
a=f.read()

i=0
y=""
n=0
for x in a:
    
    if x!='\n':
        if x.isdigit():
            y+=f"{x}"
            i+=1
            
        else:
            if len(y)==6:
                print(y)
                f2=open("pincodes.txt",'a')
                f2.write(f"{y}\n")
                f2.close()
                count=True
            i=0
            y=""
    elif x=='\n':
        # print(count)
        if count!=True:
            print("NA")
            f2=open("pincodes.txt",'a')
            f2.write("NA\n")
            f2.close()
        count=False
f.close()
            










                

                
