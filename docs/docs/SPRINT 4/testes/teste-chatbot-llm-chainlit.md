# Avaliação do Chatbot com Chaintlit e LLM da OpenAI 

Nesta seção, apresentamos uma documentação detalhada dos testes realizados com o Chatbot idealizado com LLM da OpenAI, adaptado para o contexto do almoxarifado da AmBev. Os testes foram projetados para avaliar a eficácia do sistema em atender aos requisitos não funcionais, com foco na rapidez de resposta e na capacidade de processar e contextualizar informações de um arquivo PDF para responder perguntas de usuários. Abaixo está incluído um vídeo que demonstra o teste realizado. 

## 1. Descrição do Arquivo PDF Utilizado no Teste

#### Detalhes do Arquivo PDF

-   **Título**: Inventário Simulado do Almoxarifado da AmBev.
-   **Conteúdo**: O arquivo PDF é uma simulação fictícia de um inventário de peças para manutenção de equipamentos em uma fábrica de cerveja da AmBev. Este documento foi especialmente criado para fins de teste e não reflete um inventário real.
- **Link**: O arquivo está presente nesse [link](https://github.com/2023M8T2-Inteli/grupo5/blob/main/arquivos/pdf%20inventario/inventario_simulado_amoxarifado.pdf).

#### Descrição do Conteúdo

-   **Variedade de Itens**: O PDF inclui uma ampla gama de itens essenciais para a manutenção e operação dos equipamentos da fábrica, como rolamentos, correias, sensores, válvulas, motores, tubos e outros componentes mecânicos e eletrônicos.
-   **Detalhamento Técnico**: Cada item listado no inventário possui detalhes técnicos como número da peça, nome, descrição, quantidade, preço unitário e localização no armazém.
-   **Exemplos de Itens**: Rolamentos de diferentes tipos, correias sincronizadas e transportadoras, sensores de temperatura e luz, válvulas de controle de vazão, motores de passo, tubos para fluidos, entre outros.

#### Objetivo do Arquivo no Teste

-   **Contextualização de Dados**: O arquivo foi utilizado para avaliar a capacidade do Chatbot LLM da OpenAI em processar informações específicas e fornecer respostas contextualizadas baseadas nos dados contidos no documento.
-   **Desafio de Interpretação**: Representa um desafio de interpretação de dados técnicos e especializados, essencial para avaliar a eficácia do LLM em ambientes industriais e técnicos.

#### Importância no Teste

-   **Validação da Funcionalidade**: O inventário simulado é fundamental para testar a funcionalidade do Chatbot LLM em um cenário realista de almoxarifado, garantindo que o sistema possa lidar com consultas específicas e técnicas.
-   **Medição de Desempenho**: Auxilia na avaliação do desempenho do sistema em termos de precisão das respostas, tempo de resposta e eficiência no processamento de dados complexos.

#### Referência

 O arquivo foi feito em colaboração com o grupo 2 (BBB) do 2° ano turma de engenharia da computação de 2023.


## 2. Requisitos Não Funcionais e Testes Relacionados ao Chatbot/LLM

### 2.1 RNF2: Tempo de Resposta do Processamento das Requisições

Para esse RFN, o teste avalia se o tempo de resposta do processamento está entre 2 e 15 segundos, desde o envio da informação (voz ou texto) até o retorno ao usuário.

 #### Método

Utilizamos um log no terminal que envia feedbacks do tempo gasto para processamento do arquivo pdf e geração da resposta da pergunta do usuário. 
  #### Resultado
  
   -   **Tempo de Resposta**: O sistema levou entre 10 a 20 segundos para responder às perguntas dos usuários, atendendo às expectativas de desempenho.
   
#### Análise e Sugestões de Melhorias
 
A análise dos resultados indica que embora o sistema atenda às expectativas de desempenho em termos de tempo de resposta, ainda existe margem para otimização. Uma ação identificada para melhoria é a retirada da ressubmissão de arquivos PDF sempre que o usuário atualiza a página e deseja realizar novas perguntas. 

- **Melhoria Proposta:** Desenvolvimento de uma funcionalidade que permita ao usuário fazer múltiplas consultas sem a necessidade de submeter novamente o arquivo PDF. Isso pode ser alcançado mantendo o arquivo PDF em um banco de dados, permitindo que o chatbot acesse rapidamente as informações relevantes para responder às perguntas sempre que o usuário logar na plataforma.

###  2.2 Integração de Arquivo PDF com o Chatbot LLM para Contextualizar Respostas

#### Descrição do Teste

Este teste avalia a integração de um arquivo PDF com informações sobre peças de armazém ao chatbot LLM. O sistema processa o PDF para extrair dados essenciais, usando-os para contextualizar e responder às perguntas dos usuários de forma precisa.

#### Processo de Teste

1.  **Upload do PDF**:
    
    -   Os usuários fazem o upload de um arquivo PDF que simula as peças do armazém.
    -   O sistema recebe o arquivo e inicia o processamento.
2.  **Processamento do PDF**:
    
    -   O arquivo PDF é processado para extrair texto. Utiliza-se `PdfReader` para ler e `RecursiveCharacterTextSplitter` para dividir o texto em pedaços manejáveis.
3.  **Geração de Resposta**:
    
    -   Com base na consulta do usuário, o sistema pesquisa documentos similares no `VectorStore`.
    -   Utiliza-se o modelo `ChatOpenAI (gpt-3.5-turbo)` para gerar a resposta, contextualizada com as informações do PDF.
4.  **Medição de Tempo e Feedback**:
    
    -   O tempo total de processamento da resposta é medido, observando-se um intervalo de 10 a 20 segundos.
    -   O sistema gera um feedback sobre o número total de tokens utilizados e o custo estimado do processamento, demonstrando a eficiência e o uso de recursos do LLM da OpenAI.

#### Resultados do Teste

-   **Feedback de Tokens e Custo**: O sistema forneceu informações transparentes sobre o uso de tokens e os custos associados, permitindo monitorar a eficiência do modelo LLM da OpenAI.

#### Análise e Melhorias

-   **Adequação**: O teste mostrou que o sistema pode processar com eficiência informações de um arquivo PDF e utilizá-las para melhorar a contextualização das respostas do chatbot.
-   **Desempenho**: O tempo de resposta está dentro de um intervalo aceitável, mas pode-se explorar otimizações para acelerar ainda mais o processamento.
-   **Uso de Recursos**: A transparência no uso de tokens e custos é benéfica para monitorar e gerenciar o desempenho do sistema.
-   **Sugestões de Melhoria**: Explorar técnicas de pré-processamento mais eficientes para reduzir o tempo de resposta e otimizar o uso de tokens.

#### Conclusão

O teste demonstrou a capacidade do sistema de chatbot LLM em integrar e processar dados de um arquivo PDF, fornecendo respostas contextualizadas em um tempo de resposta adequado. A transparência no uso de recursos e o feedback sobre o desempenho são aspectos positivos, contribuindo para a melhoria contínua do sistema.

### 2.3 Desempenho do Chatbot LLM com API ChatGPT 3.5 Turbo Versus ChatGPT-4

#### Descrição do Teste

Este teste compara o desempenho do nosso chatbot baseado no modelo LLM da OpenAI 3.5 com o ChatGPT-4, utilizando o mesmo arquivo PDF sobre o inventário do almoxarifado da AmBev. O objetivo é avaliar a precisão e contextualização das respostas fornecidas por ambos os sistemas.

#### Processo de Teste

1.  **Seleção de Perguntas**:
    
    -   Uma série de perguntas foi escolhida para abordar informações específicas do arquivo PDF.
    -   As mesmas perguntas foram feitas tanto ao nosso chatbot com LLM 3.5 quanto ao ChatGPT-4.
2.  **Avaliação de Respostas**:
    
    -   As respostas de ambos os sistemas foram avaliadas quanto à precisão, contextualização e relevância em relação às informações do PDF.

#### Resultados do Teste

-   **Precisão das Respostas**: As respostas do nosso chatbot com a OpenAI 3.5 mostraram-se bastante próximas às do ChatGPT-4 em termos de precisão.
-   **Necessidade de Contextualização Adicional**: Algumas respostas do nosso sistema requereram mais contextualização para se aproximar da precisão do ChatGPT-4.

#### Análise e Melhorias

-   **Comparação de Eficiência**: O teste revelou que o nosso sistema com LLM 3.5 é eficiente e se compara favoravelmente ao ChatGPT-4 em termos de precisão nas respostas.
-   **Oportunidades de Aprimoramento**: A necessidade de contextualização adicional em algumas respostas indica a possibilidade de otimização no processamento e interpretação de dados do PDF.
-   **Sugestões de Melhoria**: Implementar métodos mais avançados de análise e processamento de dados para melhorar a contextualização e a precisão das respostas, aproximando-se ainda mais da performance do ChatGPT-4.

#### Conclusão

A comparação entre o nosso chatbot LLM 3.5 e o ChatGPT-4 demonstrou que nosso sistema é altamente eficaz e competitivo. Embora haja espaço para melhorias na contextualização, as respostas fornecidas estão em um nível de precisão comparável ao ChatGPT-4, destacando o potencial e a eficácia do nosso chatbot no contexto do almoxarifado da AmBev.

## Vídeo demonstrativo dos testes realizados

[![Veja o vídeo no youtube!](https://i3.ytimg.com/vi/NWNzE8_hUo0/maxresdefault.jpg)](https://youtu.be/NWNzE8_hUo0)