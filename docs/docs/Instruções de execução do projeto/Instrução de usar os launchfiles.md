# Execução dos launchfiles

Quando as instalações previamentes mencionadas forem concluidas basta só rodar os seguintes comandos para rodar os launchfiles

Comando que executa o launchfile de mapeamento:

´´´
ros2 launch turtlebot3 launch.py
´´´
Quando isso for feito vai ser necesário usar as teclas w, a, s, d para fazer a movimentação do robô para realizar a mapeação

Para salvar o mapa é necesário rodar o comando a seguir:

´´´
ros2 run nav2_map_server map_saver_cli -f nome-do-mapa
´´´

Comando que executa o launch file de movimentação do robô:

´´´
ros2 launch turtlebot3 movementlaunch.py
´´´