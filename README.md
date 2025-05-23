# 📦 cola_rabbitmq

This is a simple architecture demo project using **RabbitMQ** and **Python** to simulate order processing and logistics notifications.

---

## 🧠 Purpose

The goal of this project is to demonstrate how to use a queue-based messaging system to decouple the components of an application, using **RabbitMQ** as the message broker and **pika** as the Python client.

---

## 🏗️ Project Structure
```
cola_rabbitmq/
│
├── productor_pedidos.py # Publishes new orders to the queue
├── procesador_pedidos.py # Consumes orders and simulates processing
├── notificador_logistica.py # Listens to notifications and simulates logistics actions
└── README.md # Project documentation
```


---
## 🐳 Docker - RabbitMQ Setup

If you don't have RabbitMQ installed, you can run it quickly with Docker:

```bash
docker run -d --hostname rabbitmq-host --name hospital-rabbitmq -p 5672:5672 -p 15672:15672 -e RABBITMQ_DEFAULT_USER=guest -e RABBITMQ_DEFAULT_PASS=guest rabbitmq:3-management
```
---
## 🚀 Requirements

- Python 3.x
- RabbitMQ installed and running on `localhost`
- `pika` library installed:

```
pip install pika
⚙️ How to Run
Make sure RabbitMQ is running locally on port 5672.

Start the order processor:


python procesador_pedidos.py
Start the logistics notifier:


python notificador_logistica.py
Publish a new order:


python productor_pedidos.py
📬 Message Flow
productor_pedidos.py sends a message to the pedido_nuevo queue.

procesador_pedidos.py receives and processes the order.

Then it sends a notification to the notificaciones_logistica queue.

notificador_logistica.py listens to that queue and simulates a logistics task.

📸 Example Output


✅ Processing order: {'product': 'Laptop', 'quantity': 2, 'customer': 'Juan'}
📦 Notifying logistics: {'product': 'Laptop', 'quantity': 2}

```
## 🧑‍💻 Author

**Justin Gomezcoello**  
Software Engineering Student at **Universidad de Las Américas (UDLA)** – Quito, Ecuador  
GitHub: [@JustinGomezcoello](https://github.com/JustinGomezcoello)


