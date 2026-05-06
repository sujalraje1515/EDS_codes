n = int(input(""))
marks = [int(x) for x in input().split()]

fail = False
for mark in marks:
	if mark<40:
		fail = True
		break
if fail:
	print("Fail")
else:
	aggregate = sum(marks)/n
	print(f"Aggregate Percentage: {aggregate:.2f}")

	if aggregate>75:
		print("Grade: Distinction")
	elif aggregate >=60:
		print("Grade: First Division")
	elif aggregate >=50:
		print("Grade: Second Division")
	elif aggregate >=40:
		print("Grade: Third Division")