import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

class AmazonScraper:
    
    def __init__(self):
        # Lista de produtos de teste
        self.produtos = [
            {'titulo': 'Notebook Dell', 'preco_original': 3500, 'preco_atual': 2800, 'avaliacao': 4.5, 'url': 'url1', 'imagem': 'img1'},
            {'titulo': 'Monitor LG', 'preco_original': 1200, 'preco_atual': 900, 'avaliacao': 4.8, 'url': 'url2', 'imagem': 'img2'},
            {'titulo': 'Teclado Mecânico', 'preco_original': 400, 'preco_atual': 300, 'avaliacao': 4.3, 'url': 'url3', 'imagem': 'img3'},
            {'titulo': 'Mouse Logitech', 'preco_original': 150, 'preco_atual': 150, 'avaliacao': 4.7, 'url': 'url4', 'imagem': 'img4'},
            {'titulo': 'Mouse Pad', 'preco_original': 50, 'preco_atual': 45, 'avaliacao': 4.8, 'url': 'url5', 'imagem': 'img5'},
            {'titulo': 'Mouse Logitech', 'preco_original': 150, 'preco_atual': 150, 'avaliacao': 4.7, 'url': 'url6', 'imagem': 'img6'},
            {'titulo': 'Televisão Samsung', 'preco_original': 5200, 'preco_atual': 5000, 'avaliacao': 4.9, 'url': 'url7', 'imagem': 'img7'},
            {'titulo': 'Monitor Arzopa', 'preco_original': 1650, 'preco_atual': 1500, 'avaliacao': 4.7, 'url': 'url8', 'imagem': 'img8'},
            {'titulo': 'Teclado Logitech', 'preco_original': 250, 'preco_atual': 190, 'avaliacao': 4.6, 'url': 'url9', 'imagem': 'img9'},
            {'titulo': 'Cabo de fonte', 'preco_original': 90, 'preco_atual': 85, 'avaliacao': 4.2, 'url': 'url10', 'imagem': 'img10'},
            
        ]
        logger.info("Scraper inicializado com produtos de teste")
    
    def buscar_produtos(self, palavra_chave, quantidade=10):
        resultado = []
        for produto in self.produtos:
            if palavra_chave.lower() in produto['titulo'].lower():
                resultado.append(produto)
        logger.info(f"Encontrados {len(resultado)} produtos para '{palavra_chave}'")
        return resultado[:quantidade]
    
    def buscar_promocoes(self, palavra_chave="eletrônicos", quantidade=10):
        todos = self.buscar_produtos(palavra_chave, quantidade=100)
        com_desconto = []
        for produto in todos:
            if produto['preco_original'] > produto['preco_atual']:
                com_desconto.append(produto)
        logger.info(f"Encontrados {len(com_desconto)} promoções")
        return com_desconto[:quantidade]


if __name__ == "__main__":
    scraper = AmazonScraper()
    promos = scraper.buscar_promocoes("monitor", quantidade=5)
    
    print(f"Encontrados {len(promos)} produtos\n")
    for p in promos:
        print(f"- {p['titulo']}")
        print(f"  R$ {p['preco_original']:.2f} → R$ {p['preco_atual']:.2f}")