import re

source = "Lorem ipsum doflor mitchell mccoll 8761950 szit ametß, consqecytetu$r adipibsching elit, sed do eiusmod tewmporα incid6kgidunt ut labq8ore et café dolore_ magna aliqua. Purus! sit{|}~ \t\n\r\x0b\x0c amet volutpat cons&jequat mau7ris. Penaxtibus e"

letters = re.findall("m", source)
nums = re.findall("[0-9]", source)
alphabet = re.findall("[a-zA-Z]", source)
nonalphanum = re.findall(r"[\W_]", source)
spaces = re.findall(" ", source)

print("The number of letters in the string is: ", len(letters))
print("The amount of numbers in the string is: ", len(nums))
print("The number of alphabetic characters in the string is: ", len(alphabet))
print("The number of non-alphanumeric characters in the string is: ", len(nonalphanum))
print("The number of spaces in the string is: ", len(spaces))