# Amazon Deals Bot

[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)

Bot que busca promoções da Amazon e envia os melhores produtos diariamente via **Telegram** e **WhatsApp**.

> ⚠️ **Status:** Os dados de produtos usados atualmente são **simulados/fictícios** para fins de desenvolvimento. Em breve, será integrada a **Amazon Product Advertising API** oficial para dados reais.

## ✨ Funcionalidades

- 🔍 Busca promoções de eletrônicos (dados simulados por enquanto)
- 🎯 Filtra apenas os melhores deals (desconto, preço, avaliação)
- 📨 Envia 2+ produtos por dia via Telegram ✅
- 📱 Suporte para WhatsApp (em desenvolvimento)
- ⏰ Agendamento automático diário (em desenvolvimento)
- 📊 Análise inteligente de promoções

## 🛠️ Tecnologias

- **Python 3.14+**
- **python-telegram-bot** — Para integração com Telegram ✅
- **amazon-paapi** — Para integração futura com Amazon API
- **APScheduler** — Para agendamento diário (em desenvolvimento)
- **python-dotenv** — Para gerenciar variáveis de ambiente

## 📦 Instalação

### 1. Clone o repositório

\`\`\`bash
git clone https://github.com/NicollasSantana/amazon-deals-bot.git
cd amazon-deals-bot
\`\`\`

### 2. Crie um ambiente virtual

\`\`\`bash
python -m venv venv
venv\Scripts\activate  # No Windows
# ou
source venv/bin/activate  # No Mac/Linux
\`\`\`

### 3. Instale as dependências

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Configure as variáveis de ambiente

Copie o arquivo `.env.example` para `.env`:

\`\`\`bash
copy .env.example .env  # Windows
# ou
cp .env.example .env  # Mac/Linux
\`\`\`

Preencha as credenciais:

\`\`\`env
TELEGRAM_BOT_TOKEN=seu_token_aqui
TELEGRAM_CHAT_ID=seu_chat_id_aqui
AMAZON_ACCESS_KEY=sua_chave_aqui
AMAZON_SECRET_KEY=sua_chave_secreta_aqui
AMAZON_ASSOCIATE_TAG=seu_tag_aqui
\`\`\`

## 🚀 Como usar

### Teste o Telegram Notifier

\`\`\`bash
python src/notifiers/telegram_notifier.py
\`\`\`

### Teste o Deal Filter

\`\`\`bash
python src/filters/deal_filter.py
\`\`\`

## 🔄 Status do projeto

- [x] Estrutura do projeto
- [x] Telegram Notifier funcionando
- [x] Deal Filter funcionando
- [x] Amazon Scraper com dados simulados
- [x] Main orchestrator funcionando
- [ ] Integração com Amazon Product Advertising API (aguardando aprovação)
- [ ] WhatsApp Notifier
- [ ] Agendador diário
- [ ] Testes unitários
- [ ] Deploy em servidor

## 📚 Como conseguir suas credenciais

### Telegram

1. Procure por `@BotFather` no Telegram
2. Envie `/newbot`
3. Copie o token gerado

### Amazon PA API

1. Acesse: https://associates.amazon.com.br
2. Vá em "Ferramentas do Associado"
3. Procure por "Product Advertising API"
4. Gere suas chaves (requer conta de afiliado aprovada)

> **Nota:** Atualmente usando dados simulados. A integração com API real será feita após aprovação da conta de afiliado Amazon.

## 🧪 Teste o projeto

Para testar com dados simulados:

```bash
# Terminal 1: Ative o venv
venv\Scripts\activate

# Terminal 2: Execute o bot
python src/main.py
```

Você deve receber **2 mensagens no Telegram** com produtos filtrados! ✅

## 🤝 Contribuições

Sinta-se livre para fazer fork e enviar pull requests!

## 📄 Licença

Este projeto está sob licença MIT.

## 👨‍💻 Autor

Nicollas Santana - [@NicollasSantana](https://github.com/NicollasSantana)

---

## 📝 Roadmap futuro

- [ ] Integrar Amazon Product Advertising API (dados reais)
- [ ] Adicionar notificações via WhatsApp
- [ ] Criar agendador para executar diariamente
- [ ] Adicionar banco de dados para histórico de produtos
- [ ] Dashboard web para visualizar produtos
- [ ] Testes automatizados completos