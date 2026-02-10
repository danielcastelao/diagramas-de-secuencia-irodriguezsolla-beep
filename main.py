from second import second
class main(second):
    print("Main: interaccion")
    second = second()
    respuesta = second.mensaje()
    print("Mein: Valor retornado -> ", respuesta)

if __name__ == "__main__":
    main()