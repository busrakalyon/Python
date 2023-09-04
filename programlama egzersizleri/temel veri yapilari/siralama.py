s1 = int(input("3 adet sayı girin:"))
s2 = int(input())
s3 = int(input())

if (s1<s3):
    if(s2<s3):
        if(s2<s1):
            print("{} < {} < {}".format(s2, s1, s3))
        else:
            print("{} < {} < {}".format(s1, s2, s3))
    else:
        print("{} < {} < {}".format(s1, s3, s2))
else:
    if (s2 > s3):
        if (s1 < s2):
            print("{} < {} < {}".format(s3, s1, s2))
        else:
            print("{} < {} < {}".format(s3, s2, s1))
    else:
        print("{} < {} < {}".format(s2, s3, s1))














