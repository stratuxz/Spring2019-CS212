import sys
from collections import defaultdict
from numpy import dot

def multiplyBits(character, binary, key_codes):

   generation_matrix = [[1,1,0,1],
                        [1,0,1,1],
                        [1,0,0,0],
                        [0,1,1,1],
                        [0,1,0,0],
                        [0,0,1,0],
                        [0,0,0,1]]

   binary = [int(i) for i in binary]

   first_four_bits = binary[:len(binary)//2]
   last_four_bits = binary[len(binary)//2:]

   parity_bits = list(dot(generation_matrix, first_four_bits))
   parity_bits = [ bit % 2 for bit in parity_bits]

   next_parity_bits = list(dot(generation_matrix, last_four_bits))
   next_parity_bits = [bit % 2 for bit in next_parity_bits]

   key_codes[character].append(parity_bits + next_parity_bits) 

   return key_codes[character][1]


def errorCorrect(check_bits, parity_list):
   if (all(bit == 0 for bit in check_bits) == False):
      answer = input("Error detected, would you like to attempt to fix it? ('y', 'n')")

      if (answer == 'y'):
         rotate_bits = check_bits[::-1]
         index = 0
         # convert binary to decimal
         for bit in rotate_bits: 
            index = (index * 2) + bit

         value = parity_list[index] 
         parity_list[index] = not(value) #flip

   return parity_list

def multipleDecode(bit_list):

   parity_check_matrix = [[1,0,1,0,1,0,1],
                          [0,1,1,0,0,1,1],
                          [0,0,0,1,1,1,1]]

   for char_bytes in bit_list:
      first_parity_list = list(char_bytes[:7])
      # converting to int list to do math
      first_parity = [int(bit) for bit in first_parity_list]

      next_parity_list = list(char_bytes[8:15])
      # converting to int list to do math
      next_parity = [int(bit) for bit in next_parity_list]

      first_parity = dot(parity_check_matrix, first_parity)
      next_parity = dot(parity_check_matrix, next_parity)

      check_bits = first_parity % 2
      check_next_bits = next_parity % 2

      first_parity = list(errorCorrect(check_bits, first_parity_list))
      next_parity = list(errorCorrect(check_next_bits, next_parity_list))

      # need to turn back into str to concatenate

      first_parity = [str(i) for i in first_parity_list]
      next_parity = [str(i) for i in next_parity_list]

      bit_list[bit_list.index(char_bytes)] = first_parity + next_parity

   return bit_list   

def createByte(bit_values, key_codes, character): # adding the dummy bit
   middle = len(bit_values)//2
   first_byte = bit_values[:middle]
   second_byte = bit_values[middle:]


   while len(first_byte) < 8:
      first_byte.append(0)
   
   while len(second_byte) < 8:
      second_byte.append(0)

   total_parity_bits = first_byte + second_byte

   key_codes[character].append(total_parity_bits)
   
   return key_codes[character][2]

def encodeFile(file_name, key_codes = defaultdict(list)):
   #key_codes = defaultdict(list)
   encoded = open("{0}.coded".format(file_name), 'w')

   with open(file_name, 'r') as some_file:
      for word in some_file:
         for character in word:

            if character not in key_codes.keys():
               # convert each char into hex
               char_hex = ord(character) # -- built-in function
               # convert each hex into binary & strip b from binary (0b100)
               char_binary = str(format(char_hex, '08b')) # to pass as a iterable parameter, convert to str
               # store codes in hashtable -- for later lookup

               key_codes[character].append(char_binary)

               parity_bits = multiplyBits(character, char_binary, key_codes)

               byte = createByte(parity_bits, key_codes, character)

               for bit in byte:
                  encoded.write(str(bit))
            else:
               for bit in key_codes[character][2]:
                  encoded.write(str(bit))
   
   encoded.close()

   return key_codes # contains key and its binary value

def decodeFile(file_name, key_codes):

   decode_file = open("{0}.decoded".format(file_name), 'w')

   with open(file_name, 'r') as binary_file:
      n = 16
      for line in binary_file: # get every 8 characters

         character_byte = [ line[i:i+n] for i in range(0, len(line), n)]

         parity_bits = multipleDecode(character_byte)

         for bit_list in parity_bits:
            bit_list = list(map(int, bit_list)) 
            for key, items in key_codes.items():
               for i in items:
                  if i == bit_list:
                     decode_file.write(key)
   decode_file.close()

def main():
   if len(sys.argv) != 3:
      print("Expected format: PA6.py <encode / decode> <file_name>")
      return

   if sys.argv[1] == "encode":
      #encode ABC.txt to ABC.txt.coded
      codes = encodeFile(sys.argv[2])
      print("File", sys.argv[2], "encoded.")

   elif sys.argv[1] == "decode":
      #decode ABC.txt.coded to ABC.decoded.txt
      decodeFile(sys.argv[2], codes)
      print("File", sys.argv[2] , "decoded.")
   else:
      print("Unexpected command.")

if __name__ == '__main__':
   main()
