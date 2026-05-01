import os, telegram, asyncio, logging
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s" )  

def carregar_configuracao():
    load_dotenv()
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = int(os.getenv("TELEGRAM_CHAT_ID"))
    return token, chat_id

async def enviar_mensagem(token,chat_id, texto):
    try:
        bot = telegram.Bot(token)
        await bot.send_message(chat_id, text=texto)
        logging.info("Enviando mensagem para o telegram.")
        return True
    except Exception as e:
        logging.error("Deu erro ao tentar enviar a mensagem.")
        pass

async def main():
    token, chat_id = carregar_configuracao()
    await enviar_mensagem(token, chat_id, "Hi Im bot of Nicollas")
   
    
if __name__ == "__main__": 
    asyncio.run(main())
    
