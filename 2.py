import string

def run():
    #traemos el archivo
    message = ""
    # leeemos
    with open("./message.txt", "r") as f: 
        message = f.read()

    #list comprehession
    message_list_uncrypted = [ch for ch in message if ch in string.ascii_letters]
    # for ch in message:
        # if (ch in string.ascii_letters):
            #message.append(ch)
    print("".join(message_list_uncrypted))




if __name__ == "__main__":
    run()