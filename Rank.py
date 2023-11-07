###########  Regex Answer ###########


# import re

# Regex_Pattern = r'hackerrank'	# Do not delete 'r'.


# Test_String = input()

# match = re.findall(Regex_Pattern, Test_String)

# print("Number of matches :", len(match))




##################### Text wrap ###################



import textwrap


def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width) 
    word_list = wrapper.wrap(text=string) 
    for data in word_list:
        print(data)
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

