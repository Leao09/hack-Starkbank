import ReactPlayer from 'react-player'

# Testes

### Teste realizados.

Para início de teste da navegação autônoma do robô foram realizados algumas metrificações de requisitos tanto funcionais quanto não funcionais para ter um bom desempenho nas precisões da robô. Além do mais, foi gerado o esboço do mapa no simulador Rviz e também projetado os perímetros do mapa para forma física. Veja a imagem a seguir de como foi feito a projeção do mapa:

<img src={require('/img/space-map.png').default} width='100%'/>


Em fase, foi realizado o teste de mapeamento automático, ou seja, foi verificado se o sistema é capaz de realizar esse mapeamento automático do espaço. Mas para isso, o robô deve ser iniciado no ponto inicial do percurso "início". Além disso, para critério de aceitação do sistema, até memsmo para fins de desempenho, é que o mapa gerado seja detalhado, abragendo todos os corredores e áreas do espaço de teste. 

Outra situação importante a ser destacado foi a interatividade com  obstáculos, o robô tinha desafios e possibilidades grandes de bater nos obstáculos e paredes do espaço, sendo assim dificuldades em voltar para o início ou até mesmo continuar o caminho de onde parou, isso se deve principalmente na posição de início que ele foi colocado, se caso estiver fora do ângulo de partida, até mesmo por intervalos de espaços e bases curtas, ele possivelmente dará problemas em desviar dos obstáculos. Entretanto, ao dar o comando de início de partida do percurso, o robô, ao ser observado, mostrou grande enficácia nos desvios, passando pelos pontos 1, 2, 3 e 4 (como mostrado na imagem a cima) e depois voltando para seu inicio de partida sem interrupção. Nessa parte, foi testado o quão preciso estava o sensor LIDAR, esse sensor é o que detecta cada parte do obstáculo em sua frente por uma curta distância de raio.

Para realizar essa movimentação, você deve colocar o robô na posição inicial. Logo em seguida, na interface de linha de comando (CLI), abra o mapa do ambiente (Rviz) usando "python3 main.py". Será iniciado. Após isso, colocando a inserção de comandos como "mova-se para..." ou "desloque-se para...", por exemplo, acrescentado com o número da posição seguinte, ele se moverá para o ponto especificado. Vale lembrar que a inserção dos comandos com seus pontos deverá ser realizado a cada final de trajeto de um ponto ao outro.

Veja o vídeo a seguir sobre a execução e desvios:

<video width="320" height="240" controls>
  <source src="./static/video/teste-video.mp4" type="video/mp4">
</video>


Em seguida, foi identificado que o tempo de resposta do envio de informações para execução do rôbo foi aproximadamente 10 segundos. Além disso, o teste de tempo de mapeamento do percurso completo dentro da área do perímetro foi de cerca de 1 minuto e 10 segundos. Nesse sentido, ambos tempos foram esperado como requisito.

Portanto, alguns testes foram feitos várias vezes até mostrar o resultado esperados contidos nos requisitos tanto funcionais quanto os requisitos não funcionais, como, por exemplo, R1 e R3 (funcionais) e RNF2 e RNF3 (não funcionais). 
