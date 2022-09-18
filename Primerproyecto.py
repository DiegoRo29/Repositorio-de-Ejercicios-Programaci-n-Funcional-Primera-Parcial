
#hints

def mensaje(msg):
    print("Fuera de la función",msg,id(msg))

x = "Hola mundo"
print("Fuera de la función",x,id(msg))

if __name__ == "__main__":
    mensaje("Hola Mundo")