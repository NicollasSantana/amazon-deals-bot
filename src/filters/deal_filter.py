import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s" )

class ProdutoPromo:
    
    def __init__(self, nome, preco_original, preco_atual, avaliacao):
        self.nome = nome
        self.preco_original = preco_original
        self.preco_atual = preco_atual
        self.avaliacao = avaliacao
        pass
    
    def calcular_desconto(self):
        desconto = ((self.preco_original - self.preco_atual) / self.preco_original) * 100
        return (f"{desconto:.2f}%")
    
    def boa_promo(self, desconto_min=20, preco_max=500, avaliacao_min=4.0):
        desconto = float(self.calcular_desconto().replace("%", ""))
        if desconto >= desconto_min and self.preco_atual <= preco_max and self.avaliacao >= avaliacao_min:
            return True
        return False
            
    def formatar_produto_para_mensagem(self):
        desconto = self.calcular_desconto()
        mensagem = (
            f"📦 {self.nome}\n"
            f"💰 De: R$ {self.preco_original:.2f} → Por: R$ {self.preco_atual:.2f}\n"
            f"⭐ Avaliação: {self.avaliacao}\n"
            f"🎉 Desconto: {desconto}"
    )
        return mensagem
    
def filtrar_produtos(produtos,desconto_min=20, preco_max=500, avaliacao_min=4.0):
    bons = []
    for produto in produtos:
        if produto.boa_promo(desconto_min, preco_max, avaliacao_min):
             bons.append(produto)
    return bons
    
if __name__ == "__main__":
    produtos_teste = [
        ProdutoPromo("Notebook", 3000, 2400, 4.5),
        ProdutoPromo("Mouse", 50, 45, 3.0),
        ProdutoPromo("Teclado", 200, 150, 4.8),
    ]
    
    bons_produtos = filtrar_produtos(produtos_teste)
    
    print(f"Total de produtos: {len(produtos_teste)}")
    print(f"Produtos bons: {len(bons_produtos)}")
    print("\n--- Produtos que passaram no filtro ---\n")
    
    for produto in bons_produtos:
        print(produto.formatar_produto_para_mensagem())
        print()
    