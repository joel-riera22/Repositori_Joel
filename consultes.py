from ciutats import ciutats

def consultar_ciutat(codi_postal):
    for ciutat, info in ciutats.items():
        if info["codi_postal"] == codi_postal:
            return ciutat
    return None

def main():
    codi_postal = input("Introdueix un codi postal per saber la ciutat: ")
    ciutat = consultar_ciutat(codi_postal)
    
    if ciutat:
        info = ciutats[ciutat]
        print(f"La ciutat amb el codi postal {codi_postal} és {ciutat}.")
        print(f"Número d'habitants: {info['habitants']}, Altura sobre el nivell del mar: {info['altura_sobre_nivell_mar']} m.")
    else:
        print("Codi postal no trobat. Si us plau, intenta-ho de nou.")

if __name__ == "__main__":
    main()