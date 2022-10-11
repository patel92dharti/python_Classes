def squre():
    try:
        X= int(input("Enter X:"))
        if X>0:
            print("Squre of ",X,"Is",X*X)
        else:
            raise Exception
    except Exception as e:
        print("Please Enter the Positive Value")
        squre()
    #finally:
        #print("Finally Called")
squre()