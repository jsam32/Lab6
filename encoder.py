from decoder import Decoder


while True:
    print('Menu\n'
            '-------------\n'
            '1. Encode\n'
            '2. Decode\n'
            '3. Quit\n')
    option = int(input('Please enter an option: '))
    if option == 1:
        password = input('Please enter your password to encode: ')
        encoded = ''
        for val in password:
            encoded += str(int(val) + 3)
        print('Your password has been encoded and stored!\n')
    if option == 2:
        decoded = Decoder.decode(encoded)
        print(f'The encoded password is {encoded}, and then original password is {decoded}.\n')
    if option == 3:
        break
