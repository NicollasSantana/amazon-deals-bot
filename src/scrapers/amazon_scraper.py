import logging, os
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

class AmazonScraper:
    
    produtos_banco = [
        {
            'titulo': 'Notebook Dell',
            'preco_original': 3500.00,
            'preco_atual': 2800.00,
            'avaliacao': 4.5,
            'url': 'https://amazon.com.br/notebook-dell',
            'imagem': 'https://...'
        },
        {
            'titulo': 'Monitor LG 27 polegadas',
            'preco_original': 1200.00,
            'preco_atual': 900.00,
            'avaliacao': 4.8,
            'url': 'https://amazon.com.br/monitor-lg',
            'imagem': 'https://...'
        },
    ]
    
    def __init__(self):
        self.amazonApi = os.getenv("AMAZON_API_KEY")
        self.amazonSecretPay = os.getenv("AMAZON_SECRET_KEY")
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        pass
    
    def buscar_produtos(self, palavra_chave, quantidade=10):
        [
            {
                'titulo': 'Notebook Dell',
                'preco_original': 3500.00,
                'preco_atual': 2800.00,
                'avaliacao': 4.5,
                'url': 'https://amazon.com.br/...',
                'imagem': 'https://...'
            },
            ...
        ]
        
        return