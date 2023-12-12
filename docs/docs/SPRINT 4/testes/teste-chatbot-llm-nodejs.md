# Avaliação do Chatbot com Node.js e LLM da OpenAI

Nesta seção, compartilhamos uma documentação abrangente referente aos testes conduzidos com o Chatbot concebido utilizando o LLM da OpenAI, agora integrado ao nosso frontend desenvolvido em Next.js e customizado para o ambiente específico do almoxarifado da AmBev. Os testes foram elaborados para avaliar a eficácia do sistema em atender aos requisitos não funcionais, com ênfase na rapidez de resposta e na habilidade de processar e contextualizar informações extraídas de um arquivo PDF para fornecer respostas precisas aos usuários. A seguir, apresentamos um vídeo que ilustra o processo e destaca as melhorias implementadas.

## 1. Alterações no PDF

Para os testes do chatbot integrado ao frontend, fizemos algumas alterações no arquivo de entrada do sistema. Essas alterações tiveram dois principais objetivos: facilitar o entendimento do modelo e possibilitar a movimentação do robô a partir do chatbot. Para isso, reduzimos a quantidade de itens do mesmo grupo (diferentes rolamentos, motores, etc.) e alteramos as coordenadas desses objetos para que façam sentido quando utilizadas em conjunto com o NAV2.

## 2. Requisitos Não Funcionais e Testes Relacionados ao Chatbot/LLM

### 2.1 RNF2: Tempo de Resposta do Processamento das Requisições

Para esse RFN, o teste avalia se o tempo de resposta do processamento está entre 2 e 15 segundos, desde o envio da informação (voz ou texto) até o retorno ao usuário.

 #### Método

Cronometramos o tempo de resposta do chatbot após receber uma entrada.
  #### Resultado
  
   -   **Tempo de Resposta**: O sistema levou entre 2 e 4 segundos para responder às perguntas dos usuários, atendendo às expectativas de desempenho.
   
#### Análise e Sugestões de Melhorias
 
A atualização do RFN trouxe melhorias significativas no tempo de resposta do chatbot, reduzindo-o de 10-20 segundos para 2-4 segundos. Contudo, ainda existem áreas de oportunidade que podem ser exploradas para aprimorar ainda mais a eficiência do sistema.

- **Melhorias Propostas:** 

#### 1. Avaliação Contínua do Desempenho: 
Realizar uma monitorização constante do desempenho do sistema para garantir que o tempo de resposta permanece consistente ao longo do tempo.
Implementar métricas automatizadas de desempenho para identificar possíveis degradações e agir proativamente.
Feedback Iterativo:

#### 2. Estabelecer um sistema de feedback contínuo com os usuários para capturar suas experiências em tempo real:
Utilizar os feedbacks dos usuários para realizar ajustes rápidos e atender às expectativas em constante evolução.
Otimização do Processo de Resposta:

#### 3. Analisar a eficiência do processamento interno do chatbot para identificar possíveis gargalos:
Investigar oportunidades de otimização no código-fonte, algoritmos ou infraestrutura para acelerar ainda mais o tempo de resposta.

#### 4. Expansão de Funcionalidades:
Desenvolver funcionalidades adicionais que possam enriquecer a experiência do usuário, como respostas mais contextuais, sugestões inteligentes, ou suporte a diferentes tipos de entrada, como imagens ou documentos.

### 2.2 Integração de Arquivo PDF com o Chatbot LLM para Contextualizar Respostas

#### Descrição do Teste

Este teste avalia a integração de um arquivo PDF com informações sobre peças de armazém ao chatbot LLM. O sistema processa o PDF para extrair dados essenciais, usando-os para contextualizar e responder às perguntas dos usuários de forma precisa.

#### Processo de Teste

Agora, o arquivo PDF já se encontra localizado acoplado com o chatbot, ou seja, ele está em um diretório específico dentro do próprio diretório do chatbot. Dessa forma, o usuário não precisa mais fazer o upload do arquivo e ele consegue responder múltiplas perguntas referentes a um mesmo arquivo. Portanto, realizamos 3 perguntas e comparamos a saída obtida com a saída esperada.

##### Primeira pergunta:

Oi! quem é você?

###### Resposta esperada: 

Sou um assistente de almoxarifado. O que posso ajudar?

###### Resposta obtida:

Não entendi a pergunta. Estou aqui para responder perguntas acerca da localização, descrição ou quantidade de peças do almoxarifado da Ambev.

##### Segunda pergunta:

Me dê a descrição da peça rolamento

###### Resposta esperada: 

Rolamento de esferas, vedação de borracha, diâmetro interno 20mm

###### Resposta obtida:

Rolamento de esferas, vedação de borracha, diâmetro interno 20mm, qtd 12, preço unitário 8.00.

##### Terceira pergunta:

Me diga onde está localizada a peça motor

###### Resposta esperada: 
[x:0.0, y:1.5]

###### Resposta obtida:

[x: 0.0, y: 1.5]

## Vídeo demonstrativo dos testes realizados
[Screencast from 12-12-2023 18:58:11.webm](https://github.com/2023M8T2-Inteli/grupo5/assets/99208114/549a7b39-3cd3-400a-9290-815633444fe8)

