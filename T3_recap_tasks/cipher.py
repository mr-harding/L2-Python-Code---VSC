def find_letter(original, k):
  pos = alphabet.index(original)
  if pos + k > len(alphabet) - 1:
    return alphabet[pos + k - len(alphabet)]
  else:
    return alphabet[pos + k]

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

key = int(input("Please enter key: "))
msg = input("Enter message: ")

output_str = ""
for char in msg:
  output_str += find_letter(char, key)

print(output_str)

