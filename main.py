import argparse
import progressbar as pb
import gnupg
import os


class color:    
    green = '\033[92m'
    END = '\033[0m'


def call_arguments():
    parser = argparse.ArgumentParser(
            description="Especifica fichero y diccionario")

    parser.add_argument('--version', action='version', 
            version='GPG Brute Force Tool v1.0')

    parser.add_argument('--file', required=True, 
            help="Ruta del fichero a descifrar")

    parser.add_argument('--wordlist', required=True, 
            help="Ruta del diccionario a utilizar")

    return parser.parse_args()


def cabecera():

    print('''
       ___  ___   ___    ___                 _     _____           _ 
      / __|| _ \ / __|  / __| _ _  __ _  __ | |__ |_   _|___  ___ | |
     | (_ ||  _/| (_ | | (__ | '_|/ _` |/ _|| / /   | | / _ \/ _ \| |
      \___||_|   \___|  \___||_|  \__,_|\__||_\_\   |_| \___/\___/|_|
                                        Made with <3 by KevinLiebergen
        ''')

outputfile = 'file_decrypted'

def decrypt_gpg(password, encrypted_path, gpg):

    with open(encrypted_path,'rb') as encrypt:

        return  gpg.decrypt_file(encrypt, passphrase=password, output=outputfile) 


def gpg_brute(ifile, wordlist):

    gpg = gnupg.GPG()

    i=0
    nlines = len(open(wordlist).readlines())
    
    #initialize widgets
    widgets = ['Time for loop of %s  iterations: '% nlines, pb.Percentage(), ' ',
            pb.Bar(marker=pb.RotatingMarker()), ' ', pb.ETA()]
    timer = pb.ProgressBar(widgets=widgets, maxval=nlines).start()

    with open(wordlist, 'r') as f:

        for passw in f:

            passw = passw.strip()
            result = decrypt_gpg(passw, ifile, gpg)
    
            if result.ok:
                print(color.green + "\n[*] ENCONTRADO! La contraseña es: %s" % passw , color.END)
                print("Fichero guardado en %s " % outputfile)
                os._exit(1)
            i += 1
            timer.update(i)



def main():
   
    args = call_arguments()

    cabecera()

    gpg_brute(args.file, args.wordlist)
    

if __name__ == '__main__':
    main()
