
num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))
for number_line in num_pad:
    for num in number_line:
        print(num, end=" ")
    print()