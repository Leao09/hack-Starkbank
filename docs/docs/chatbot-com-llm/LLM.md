# Documentação da utilização do LLM 
- Primeiramente, explicando de maneira sucinta o que é um LLM(Large Language Model) refere-se a um tipo avançado de software de inteligência artificial que foi treinado em grandes quantidades de dados de linguagem natural. Esse modelo é capaz de entender e gerar texto em linguagem humana de maneira sofisticada.

# Implementação 
- Sobre a implementação foi utilizado a api da Openai, que sincroniza o desenvolvimento da personalização do prompt com o LLM da openai, utilizamos o Chat-GPT 3-turbo para realizar as pesquisas e respostas considerando o input que foi utilizado no prompt. Alé disso, foi implementado a funcionalidade de leitura de documentos para embasar o cotexto da pergunta. Para exemplo do que será apresentado nos testes, utilizamos um pdf que simulava equipamentos e peças que poderiam estar no almoxarifado da Ambev e realizamos perguntas sobre qual tipo de peça ela possui e a onde ala se localizava. 
## Custos de implementação
- Devido a utilização da api para um modelo treinado por uma compania a realização de prompts de pesquisa possui um custo, entrentano esse custo é significativamente baixo além da própria plataforma oferecer 5 dólares iniciais que possuem validade de 6 meses, posterior a este periodo eles expiram. O pagamento deste custo não é um problema para a realização de teste e implementação de provas de conceito necessárias para a entrega do projeto. Os valores podem variar dependendo do tamanho da pergunta e do seu nivel de complexidade, mas os valores variam entre 0,001 cents e 0,020 cents.
## Principais bibliotecas utilizadas 
- Para implemetação deste recurso foram utilizados bibliotecas como o Langchain e Streamlit, sendo o langchain responsável por criar abstrações e facilidades entre as diversas features como encadeamento de modelos, carregamento de arquivos como pdf .txt google drive, vetorização do input fornecido possibilitando um melhro tratamento da pergunta. Além do uso do streamlit como interface provisório que posterior a teste foi mudado para o chainlit que possui adaptações e melhorias especificas para a aplicação de um chat-bot. Outras bibliotecas que foram utilizadas com funções auxiliares foram como a PYPDF2, para a leitura de arquivos pdf e a python-dotenv, utilizada para carregar e proteger a chave da api para uso da openai. 



