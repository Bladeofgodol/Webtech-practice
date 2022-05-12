list_of_name = ['alex','david','abel','hana']
list_of_nicknames = ['al','dave','ab','ha']
print(f'hello {list_of_name[0]}')

for single_element in list_of_name:
    print(f'hello {single_element}')

for single_element in range(len(list_of_name)):
        print(f'{list_of_name[single_element]} has a nickname {list_of_nicknames[single_element]}')

