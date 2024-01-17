def avg(marks):
    assert len(marks) != 0,"List is empty"
    return sum(marks)/len(marks)

mark1 = []
print("Average of mark1:",avg(mark1))