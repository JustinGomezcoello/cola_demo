import pika
import json

conexion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
canal = conexion.channel()
canal.queue_declare(queue='pedido_nuevo')

pedido = {
    "id_pedido": 101,
    "cliente": "Juan Pérez",
    "producto": "Laptop",
    "cantidad": 1
}

canal.basic_publish(
    exchange='',
    routing_key='pedido_nuevo',
    body=json.dumps(pedido)
)

print("📦 Pedido enviado:", pedido)
conexion.close()
