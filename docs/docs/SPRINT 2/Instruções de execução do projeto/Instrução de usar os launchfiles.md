# Execução dos Launch Files do Turtlebot

Após a conclusão das instalações mencionadas anteriormente, você pode começar a utilizar os launch files do Turtlebot para diversas funções, como mapeamento e movimentação autônoma do robô. Siga os passos abaixo para executar cada um desses processos.

## Executando o Launch File de Mapeamento

Para iniciar o processo de mapeamento, use o seguinte comando:

```
ros2 launch turtlebot3 launch.py
```

## Controle do Robô Durante o Mapeamento

Após iniciar o launch file de mapeamento, utilize as teclas w, a, s, d para controlar o movimento do robô. Essa movimentação é essencial para realizar um mapeamento abrangente do ambiente.

## Salvando o Mapa

Uma vez que o mapeamento estiver completo, você pode salvar o mapa gerado com o seguinte comando:

```
ros2 run nav2_map_server map_saver_cli -f nome-do-mapa
```

Substitua nome-do-mapa pelo nome desejado para o arquivo do mapa. Esse passo é crucial para preservar os dados coletados durante o mapeamento.

## Executando o Launch File de Movimentação do Robô

Para operar o robô em um modo de movimentação, que pode incluir navegação autônoma ou seguimento de trajetórias pré-definidas, execute o comando a seguir:

```
ros2 launch turtlebot3 movementlaunch.py
```

Este comando ativa o launch file responsável por gerir os aspectos de movimentação do Turtlebot.