from fastapi import FastAPI, Form
import pika

app = FastAPI()




@app.get("/")
async def root():
    return {"message": "This is the user interface."}


@app.post("/acquire-page")
async def acquire_page(target_url: str = Form()):
    with pika.BlockingConnection(pika.ConnectionParameters('rabbitmq')) as connection:
        channel = connection.channel()

        channel.queue_declare(queue='hello')
        channel.basic_publish(exchange='',
                              routing_key='hello',
                              body=f'{target_url}')
        print(f" [x] Asking scraper to acquire '{target_url}'")
    return {"target_url": target_url}
