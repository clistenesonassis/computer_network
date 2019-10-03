class Conversor:

    def bin_to_str(self, binario):

        binario = str(binario)
        caractere = ''
        string = ''
        tamanho = len(binario)
        k = 1

        for j in binario:
            if j != ' ':
                caractere += j
                if k == tamanho:
                    string += chr(int(caractere, 2))
            else:
                string += chr(int(caractere, 2))
                caractere = ''  # 0x101100110
            k += 1
        return string

    def str_to_bin(self, string):
        binario = ''
        for i in string:
            binario += bin(ord(i))[2::] + ' ' 
        return binario