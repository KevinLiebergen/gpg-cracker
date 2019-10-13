import argparse
import time
import progressbar


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

    print(args.file)
    print(args.wordlist)


    for i in progressbar.progressbar(range(100)):
        time.sleep(0.02)



if __name__ == '__main__':
    main()
