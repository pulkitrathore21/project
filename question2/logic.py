


def grade(avg):
    #measure grade
    if avg>=90:
        return f"average score:{avg} and grade B"
    if 80<=avg and avg<90:
        return f"average score:{avg} and grade B"
    if 70<=avg<80:
        return f"average score:{avg} and grade C"
    if 60 <=avg<70:
        return f"average score:{avg} and grade D"
    if avg<60:
        return f"average score:{avg} and grade F"

def average(t1,t2,t3):
    # calculating average and pass to the grade 
    avg=(t1+t2+t3)//3
    r=grade(avg)
    return r