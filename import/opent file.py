#print info from file
with open('file.txt', mode='w', encoding='iso-8859-1') as file_object:
    print('über naïve café', file=file_object)
