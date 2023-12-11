import ReactPlayer from 'react-player'

# Testes de Mapeamento e Navegação

Na fase inicial de testes da navegação autônoma do robô, foram estabelecidos critérios rigorosos para medir o desempenho do sistema, abrangendo requisitos funcionais e não funcionais. Para facilitar a avaliação, desenvolvemos um mapa detalhado no simulador Rviz, que foi também adaptado para uma representação física. Este mapa serviu como base para nossas simulações e testes práticos. A imagem abaixo ilustra a projeção realizada do mapa no simulador:

<img src={require('/img/space-map.png').default} width='100%'/>

## Teste de Mapeamento Automático

Conduzimos um teste crucial de mapeamento automático, avaliando a capacidade do robô de navegar e mapear o espaço de forma independente. Iniciamos cada teste com o robô no ponto marcado como "início" no mapa. Um critério chave para a aceitação do sistema foi a geração de um mapa detalhado, cobrindo todos os corredores e áreas relevantes do ambiente de teste.

## Interação com Obstáculos

Um aspecto significativo testado foi a interação do robô com obstáculos. Observamos desafios relacionados à capacidade do robô de evitar colisões e retomar sua rota após desvios, especialmente quando iniciava de posições não padronizadas. No entanto, o robô demonstrou eficiência notável ao navegar pelos pontos designados (1, 2, 3 e 4, conforme a imagem acima) e retornar ao ponto de início sem incidentes. Essa fase do teste enfatizou a precisão do sensor LIDAR na detecção e na manobra diante de obstáculos.

## Procedimentos de Comando e Movimentação

Para executar a movimentação, posicionamos o robô no local de início e utilizamos a interface de linha de comando (CLI) para abrir o mapa do ambiente no Rviz, com o comando "python3 main.py". A movimentação foi comandada através de instruções como "mova-se para..." ou "desloque-se para...", seguido do número do ponto de destino. Cada comando foi inserido após a conclusão do trajeto de um ponto a outro.

[![Watch the video](https://img.youtube.com/vi/ibJ_DnxXIIY/maxresdefault.jpg)](https://www.youtube.com/embed/ibJ_DnxXIIY)


## Avaliação de Tempo de Resposta

Durante os testes, notamos que o tempo de resposta do robô para iniciar as ações após o recebimento dos comandos foi de aproximadamente 10 segundos. Além disso, o tempo total para o mapeamento do percurso completo dentro da área demarcada foi de cerca de 1 minuto e 10 segundos. Ambos os tempos estão dentro dos parâmetros esperados conforme os requisitos estabelecidos.

## Conclusão

Realizamos múltiplas iterações dos testes para assegurar a consistência dos resultados e a conformidade com os requisitos estabelecidos, tanto funcionais (ex: R1, R3) quanto não funcionais (ex: RNF2, RNF3). Os resultados obtidos demonstram um avanço significativo no desenvolvimento e na precisão do sistema de navegação autônoma do robô.