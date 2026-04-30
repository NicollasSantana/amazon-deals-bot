# Amazon Deals Bot

[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)

Bot que busca promoções da Amazon e envia os melhores produtos diariamente via **Telegram** e **WhatsApp**.

## ✨ Funcionalidades

- 🔍 Busca promoções na Amazon usando Product Advertising API
- 🎯 Filtra apenas os melhores descontos (desconto, preço, avaliação)
- 📨 Envia 2+ produtos por dia via Telegram
- 📱 Suporte para WhatsApp (em desenvolvimento)
- ⏰ Agendamento automático diário

## 🛠️ Tecnologias

- **Python 3.14+**
- **python-telegram-bot** — Para integração com Telegram
- **amazon-paapi** — Para buscar produtos da Amazon
- **APScheduler** — Para agendamento diário
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

## 📁 Estrutura do projeto

\`\`\`
amazon-deals-bot/
├── src/
│   ├── scrapers/
│   │   └── amazon_scraper.py          # Busca produtos da Amazon
│   ├── notifiers/
│   │   ├── telegram_notifier.py       # Envia pelo Telegram ✅
│   │   └── whatsapp_notifier.py       # Envia pelo WhatsApp (em desenvolvimento)
│   ├── filters/
│   │   └── deal_filter.py             # Filtra promoções ✅
│   └── main.py                        # Orquestra tudo
├── tests/                              # Testes unitários
├── venv/                               # Ambiente virtual
├── .env                                # Variáveis de ambiente (não sobe no Git)
├── .env.example                        # Exemplo de .env
├── .gitignore                          # Arquivos a ignorar
├── requirements.txt                    # Dependências
├── scheduler.py                        # Agendamento diário
└── README.md                           # Este arquivo
\`\`\`

## 🔄 Status do projeto

- [x] Estrutura do projeto
- [x] Telegram Notifier funcionando
- [x] Deal Filter funcionando
- [ ] Amazon Scraper (em desenvolvimento)
- [ ] WhatsApp Notifier
- [ ] Main orchestrator
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
4. Gere suas chaves

## 🤝 Contribuições

Sinta-se livre para fazer fork e enviar pull requests!

## 📄 Licença

Este projeto está sob licença MIT.

## 👨‍💻 Autor

Nicollas Santana - [@NicollasSantana](https://github.com/NicollasSantana)

---
