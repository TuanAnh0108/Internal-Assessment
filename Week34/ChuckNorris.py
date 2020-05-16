String = input()

binary = ''

for i in range(len(String)):
    charInBinary = str(bin(ord(String[i])))[2:]

    # Fill binary representation with zeroes to get 7 bit.
    charInBinary = charInBinary.zfill(7)

    binary += charInBinary

# Convert binary representation in "Chuck Norris Code".
lastChar = ' '
string_coded = ''
encodedBits = [' 00 0', ' 0 0']

for i in range(len(binary)):
    if binary[i] != lastChar:
        lastChar = binary[i]
        string_coded += encodedBits[ord(lastChar) - ord('0')]
    else:
        string_coded += '0'

# Print encoded message.
print(string_coded[1:])