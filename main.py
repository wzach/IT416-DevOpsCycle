def openASCII(path):
    f = open(path, 'r')
    raw = f.read()
    f.close
    return f

def main():
    raw = openASCII(b"Pikachu.ascii")
    print(raw)

main()
