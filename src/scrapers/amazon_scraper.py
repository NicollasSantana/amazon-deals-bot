import logging, os
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

class AmazonScraper:
    
    def __init__(self):
        self.amazonApi = os.getenv("AMAZON_API_KEY")
        self.amazonSecretPay = os.getenv("AMAZON_SECRET_KEY")
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        pass
    
    def buscar_produtos(self, palavra_chave, quantidade=10):
        return