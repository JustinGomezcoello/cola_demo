import pika
import json

conexion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
canal = conexion.channel()
canal.queue_declare(queue='notificaciones_logistica')

def mostrar_notificacion(ch, method, properties, body):
    mensaje = json.loads(body)
    print(f"📨 Notificación a logística: {mensaje['mensaje']}")

canal.basic_consume(
    queue='notificaciones_logistica',
    on_message_callback=mostrar_notificacion,
    auto_ack=True
)

print("📡 Esperando notificaciones de logística...")
canal.start_consuming()
