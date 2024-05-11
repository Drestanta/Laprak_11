try:
    with open(input("Enter a file name: "), 'r') as file:
        hour_count = {}
        for line in file:
            if line.startswith('From '):
                hour = line.split()[5].split(':')[0]
                hour_count[hour] = hour_count.get(hour, 0) + 1
        for hour, count in sorted(hour_count.items()):
            print(hour, count)
except FileNotFoundError:
    print("File not found.")