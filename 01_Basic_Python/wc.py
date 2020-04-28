import sys

count_line = 0
count_tokens = 1
count_char = 0
count_syl  = 0
content= sys.stdin.read()

for key in content:
    if key.lower() in "abcdefghijklmnopqrstuvwxyz":
        count_char =count_char + 1
    if key == " ":
        count_tokens += 1
    if key == '\n':
        count_line += 1
    if key in "aeiouáéíóúâêôãàõAEIOUÀÁÂÃÉÊÍÓÔÕÚÜ":
        count_syl += 1

print("count line: " , count_line)
print("count tokens: ", count_tokens)
print("count characters: ", count_char)
print("count syllables: ",count_syl)

