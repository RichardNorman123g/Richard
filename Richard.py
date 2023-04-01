def fake_bin(x):
    lst1 = []
    for i in x:
        if int(i) < 5:
            x = x.replace(i, "0")
    for i in x:
        if int(i) >= 5:
            x = x.replace(i, "1")
    
    print(x)

fake_bin( "45385593107843568")