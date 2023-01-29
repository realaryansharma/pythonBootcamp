studentMarks = input("Enter the set of marks : ").split()

for n in range(0, len(studentMarks)):
    studentMarks[n] = int(studentMarks[n])

avg = sum(studentMarks) // len(studentMarks);

print("Average marks of the class is : " + str(avg))