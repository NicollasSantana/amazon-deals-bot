import logging
from scrapers.amazon_scraper import AmazonScraper
from filters.deal_filter import ProdutoPromo, filtrar_produtos
from notifiers.telegram_notifier import carregar_configuracao, enviar_mensagem
import asyncio

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

async def executar_busca_e_envio():
    logger.info("Iniciando busca de produtos...")
    
    scraper = AmazonScraper()
    produtos = scraper.buscar_promocoes("Monitor", quantidade=20)
    if not produtos:
        logger.warning("Nenhum produto encontrado")
        return
    
    produtos_promo = []
    for produto in produtos:
        promo = ProdutoPromo(
            nome=produto['titulo'],
            preco_original=produto['preco_original'],
            preco_atual=produto['preco_atual'],
            avaliacao=produto['avaliacao']
        )
        produtos_promo.append(promo)
    bons_deals = filtrar_produtos(produtos_promo, desconto_min=10, preco_max=2000, avaliacao_min=4.0)
    if not bons_deals:
        logger.warning("Nenhum bom deal encontrado")
        return
    for produto in bons_deals:
        mensagem = produto.formatar_produto_para_mensagem()
        token, chat_id = carregar_configuracao()
        sucesso = await enviar_mensagem(token, chat_id, mensagem)
        if sucesso:
            logger.info(f"Enviado: {produto.nome}")
        else:
            logger.error(f"Erro ao enviar: {produto.nome}")
        pass

if __name__ == "__main__":
    asyncio.run(executar_busca_e_envio())