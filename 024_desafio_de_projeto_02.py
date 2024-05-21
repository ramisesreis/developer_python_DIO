month = int(input())

months_dict = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
months_dict = [value.replace('\n','').strip('"') for value in months_dict]
# print(months_dict[0])
if month == 1: 
    print(months_dict[0])
elif month == 2: 
    print(months_dict[1])
elif month == 3: 
    print(months_dict[2])
elif month == 4: 
    print(months_dict[3])
elif month == 5: 
    print(months_dict[4])
elif month == 6: 
    print(months_dict[5])
elif month == 7: 
    print(months_dict[6])
elif month == 8: 
    print(months_dict[7])
elif month == 9: 
    print(months_dict[8])
elif month == 10: 
    print(months_dict[9])
elif month == 11: 
    print(months_dict[10])
elif month == 12: 
    print(months_dict[11])    