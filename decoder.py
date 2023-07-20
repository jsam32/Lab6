class Decoder:
    def decode(password):
        string_pass = str(password)
        decoded_password = ""
        for i in string_pass:
            decoded_password = decoded_password + str(int(i) - 3)
        return decoded_password
