import pika
import json

conexion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
canal = conexion.channel()
canal.queue_declare(queue='pedido_nuevo')
canal.queue_declare(queue='notificaciones_logistica')

def procesar_pedido(ch, method, properties, body):
    pedido = json.loads(body)
    print(f"✅ Procesando pedido: {pedido}")

    # Simula guardar en DB y notificar a logística
    mensaje_logistica = {
        "mensaje": f"Preparar envío para pedido #{pedido['id_pedido']} de {pedido['cliente']}"
    }

    canal.basic_publish(
        exchange='',
        routing_key='notificaciones_logistica',
        body=json.dumps(mensaje_logistica)
    )

canal.basic_consume(
    queue='pedido_nuevo',
    on_message_callback=procesar_pedido,
    auto_ack=True
)

print("⌛ Esperando pedidos...")
canal.start_consuming()
