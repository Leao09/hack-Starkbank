# Documentação do uso do ChatBot LLM com Chainlit e API da OpenAI

## LLM (Large Language Model)

Um LLM é um software avançado de inteligência artificial, treinado em vastos volumes de dados textuais. Ele é projetado para compreender e gerar texto em linguagem humana de forma sofisticada, permitindo aplicações diversas em processamento de linguagem natural.

## Implementação com a API da OpenAI

Utilizamos a API da OpenAI, integrada com o Chat-GPT 3.5-turbo, para pesquisa e geração de respostas. Esta integração permite a personalização do prompt e a sincronização com o LLM da OpenAI. Também implementamos a leitura de documentos, como PDFs, para fornecer contexto às perguntas. Por exemplo, usamos um PDF simulando um inventário de almoxarifado para responder perguntas sobre tipos e localizações de itens.

## Custos de implementação

- Devido a utilização da api para um modelo treinado por uma compania a realização de prompts de pesquisa possui um custo, entrentano esse custo é significativamente baixo além da própria plataforma oferecer 5 dólares iniciais que possuem validade de 6 meses, posterior a este periodo eles expiram. O pagamento deste custo não é um problema para a realização de teste e implementação de provas de conceito necessárias para a entrega do projeto. Os valores podem variar dependendo do tamanho da pergunta e do seu nivel de complexidade, mas os valores variam entre 0,001 cents e 0,020 cents.

## Principais bibliotecas utilizadas 

Para implementar este recurso, utilizamos bibliotecas como Langchain e Chainlit. Langchain facilita a interação com várias funcionalidades, como encadeamento de modelos e carregamento de arquivos (PDF, .txt, Google Drive), e vetorização de inputs para melhor tratamento de perguntas. Inicialmente, usamos o Streamlit como interface, mas depois migramos para o Chainlit, que oferece adaptações específicas para aplicações de chatbot. Bibliotecas auxiliares como PyPDF2 (leitura de PDFs) e python-dotenv (gerenciamento de chaves de API) também foram utilizadas.




