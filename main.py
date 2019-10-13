import argparse
import time
import progressbar
import os

def gpg_brute(ifile, wordlist):
    with open(wordlist, 'r') as f:

        for passw in f:
            time.sleep(1)

            passw = passw.strip()

            command = 'gpg --batch --passphrase %s -d %s' % (passw, ifile)
            
            result = os.popen(command).read()

            value_result = result.find("descifrado fallido")

            print(value_result)
            
            if (value_result == -1):
                #print(result)
                print(passw)
                print("Encontrado!!!")
                break


#    for i in progressbar.progressbar(range(100)):
    #        time.sleep(0.02)



def main():
    parser = argparse.ArgumentParser(
            description="Especifica fichero y diccionario")

    parser.add_argument('--version', action='version', 
            version='GPG Brute Force Tool v1.0')

    parser.add_argument('--file', required=True, 
            help="Ruta del fichero a descifrar")

    parser.add_argument('--wordlist', required=True, 
            help="Ruta del diccionario a utilizar")

    args = parser.parse_args()

    gpg_brute(args.file, args.wordlist)
    

if __name__ == '__main__':
    main()
