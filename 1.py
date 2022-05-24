def run():
    MESSAGE = "map"
    # MESSAGE = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
    message_modific = MESSAGE.replace(" ","*")
    message_list = list(MESSAGE)
    message_list_uncrypted = []
    # print(message_list)
    for i in range(len(message_list)):
        message_list_uncrypted.append(chr(ord(message_list[i]) + 2))
       
        message_uncrypted = "".join(message_list_uncrypted).replace("\"", " ").replace('{', "a").replace("|", "b")
    print(message_uncrypted)


if __name__ == "__main__":
    run()
