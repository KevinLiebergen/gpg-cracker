# GPG Crack Tool

## Instalacion

```bash
$ virtualenv venv
$ source venv/bin/activate
$ pip3 install -r requirements
```

## Ejecución

```
usage: main.py [-h] [--version] --file FILE --wordlist WORDLIST

Especifica fichero y diccionario

optional arguments:
  -h, --help           show this help message and exit
  --version            show program's version number and exit
  --file FILE          Ruta del fichero a descifrar
  --wordlist WORDLIST  Ruta del diccionario a utilizar
```

`$ python3 main.py --file <file.gpg> --wordlist <rockyou.txt>`
