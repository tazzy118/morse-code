# Author Name : tasnim
# Date: 25th/01/24
# Module: AIML-I
# Week 1
# File name: MorseCode.py 
# Progrm Title:Creating conversion table for converting text to their Morse code & vice-versa
# Morse_Code_Dictionary  : Morse Code Dictionary
# To_Encrypt()           : function to convert english text to morse code
# To_Decrypt()           : function to convert morse code to english text
# cipher                 : variable to store the morse translated form of the english text
# decipher               : variable to store the english translated form of the morse
# citext                 : variable to store morse code of a single english character
# i_space                : variable to keep track of spaces between morse characters
# message                : variable to store the string to be encoded or decoded

# Write your code to complete this Morse Code didctionary
Morse_Code_Dictionary = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...',
'T':'-', 'U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..',' ':'/',}


# Function to encrypt the english text according to the morse code chart

#morse_codeS = ("SOS it is an emergency")

def To_Encrypt(morse_codeS):

   cipher = ''
   for char in Morse_Code_Dictionary:
      if char in Morse_Code_Dictionary:
        morse_codeS += Morse_Code_Dictionary[char] + ' '
      else:
         print("Please try again!")

   return cipher

# Function to decrypt the morse code and return its equivalent English text
#message = ("... --- ... .. - .. ... .- -. . -- . .-. --. . -. -.-. -.—")

def To_Decrypt(morse_codeD):

   decipher = ''
   for char in Morse_Code_Dictionary:
      if char in Morse_Code_Dictionary:
         morse_codeD += Morse_Code_Dictionary[char] + ' '
      else:
         print("Please try again!")

   return decipher

# main() function of the python program   
def main():
   # Send morse code to Base station
   morse_codeS = input("Greetings Sailor, please enter your secret message for the base station:")
   output = To_Decrypt(str(morse_codeS))
   print("Message sent.....")
   print("Message decoded at the base station")
   print(output)

   # Send response from Base station
   morse_codeD = input("Type Base station response for encryption")
   output_ = To_Encrypt(str(morse_codeD.upper()))
   print ("Encrypted response to be sent is.")
   print(output_)

# Executes the main function
if __name__ == '__main__':
   main()