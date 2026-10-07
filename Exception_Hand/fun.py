# exception handling
for i in range (10,-3,-1):
    try:
        print(i//2)
    except Exception as e:
        print(e)
    except ValueError:
        print("A ValueError occurred")
    except TypeError:
        print("A TypeError occurred")
    
    

