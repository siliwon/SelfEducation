first_apartment = int(input())
second_apartment = int(input())
entrance_amount = second_apartment - first_apartment + 1
previous_entrance_amount = first_apartment - 1

if first_apartment == 1:
    print("YES")
elif entrance_amount > previous_entrance_amount:
    print("NO")
elif previous_entrance_amount % entrance_amount == 0:
    print("YES")
else:
    print("NO")
