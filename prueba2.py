from multiprocessing import Process, Queue

from time import sleep

def producer(q):

    # Envia 5 mensajes
    for i in range(5):

        # Envia el mensaje número 1
        q.put(i)
        print(i, "Enviado")
        sleep(2)
    
    # Envia el mensaje None (!True)
    q.put(None)
    print("El productor ha acabado")

def consumer (q):
    while True:

        # Recibe el mensaje
        item = q.get()

        # No hay más elementos
        if item is None:
            break
        print(item, "Recibido")

        sleep(1)
    sleep(1)
    print("El consumidor ha acabado")

if __name__ == "__main__":
    
    # Crea una cola
    queue = Queue()

    # Se crean los procesos Productor y Consumidor
    proceso1 = Process (target=producer,args=(queue,))
    proceso2 = Process (target=consumer, args=(queue,))

    # Se inician los procesos
    proceso1.start()
    proceso2.start()

    # Se espera a que termine el proceso 1
    proceso1.join()
    print("Proceso 1 terminado")

    # Se espera a que termine el proceso 2
    proceso2.join()
    print("Proceso 2 terminado")