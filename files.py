count = 0
with open('text.txt','r') as file:

    for l in file:
        for char in l:
            if char == '1':
                count += 1


with open('text.txt','r') as file:
    lines = file.readlines()
    res = lines[13].split(' ')
    print(res[7])
count = 0
with open('text.txt','r') as file:
    lines = file.readlines()
    for line in lines:
        numbers = line.split(' ')
        for n in numbers:
            count = count + int(n)

print(count)



        