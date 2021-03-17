inFile = open('input.txt', 'r', encoding='utf8')
outFile = open("output.txt", "w", encoding="utf8")
parties = []
votes, prime, seats, tail = 0, 0, 0, 0
for i in inFile:
    line = i.split()
    parties.append([' '.join(line[:-1]), int(line[-1]), 0, 0])
    votes += int(line[-1])
inFile.close()
prime = votes / 450
for i in parties:
    i[2] = i[1] // prime
    i[3] = i[1] % prime
    seats += i[2]
tail = 450 - seats
for i in sorted(parties, key=lambda x: -x[3]):
    if tail > 0:
        i[2] += 1
        tail -= 1
for i in range(0, len(parties)):
    print(parties[i][0], int(parties[i][2]), file=outFile)
outFile.close()
