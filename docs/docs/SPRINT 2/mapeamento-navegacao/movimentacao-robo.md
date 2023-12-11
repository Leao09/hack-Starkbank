# Movimentação do robô

Quando se trata de um robô autônomo, precisa-se entender as duas primeiras, e mais cruciais, etapas para que a movimentação corresponda ao desejado. 

A primeira delas é o mapeamento. O mapeamento nada mais é que o desbravamento do território realizado pelo robô. É quando ele se move livremente para fazer a detecção de ambientes livres e ocupados, através do seu sensor LIDAR, o qual emite luzes infravermelhas, e, com o tempo de retorno de cada emissão, calcula a distância que as luzes viajaram. Com isso, é possível salvar o mapa criado pelo robô para facilitar a segunda etapa.<br/>
A segunda etapa é a navegação. Para completar essa tarefa, foi utilizado a API Simple Commander, que gerencia todas as tarefas relacionadas ao ROS2 e ao servidor de Ações, para que seja possível focar nas funcionalidades do NAV2 e na criação da movimentação de fato.


O primeiro passo é criar uma classe que representa o robô. Ela comportará todas as funções relacionadas a ele, desde a configuração inicial do próprio navegador até os pontos que ele deve seguir no mapa.
```python showLineNumbers title="main.py"
    def __init__(self):
        rclpy.init()
        self.nav = BasicNavigator()
        self.q_x, self.q_y, self.q_z, self.q_w = quaternion_from_euler(0.0, 0.0, 0.0)
        self.initial_pose = self.create_pose_stamped()
        self.nav.setInitialPose(self.initial_pose)
        self.nav.waitUntilNav2Active()
        self.regex = r'.*?(ponto|prateleira|estante|local|peça|lugar|posi[çc][aã]o|[áa]rea|arm[áa]rio)?\s?([123])'
```
Esta classe inicializa e define que o Turtlebot será o navegador. Então, obtém-se os valores do quaternion correspondentes a uma orientação inicial de rotação zero. A função quaternion_from_euler converte ângulos de Euler para um quaternion. Após isso, ela configura a posição inicial usando a função `setInitialPose` e passando uma variável que armazena a função `create_pose_stamped()` como argumento. Ela também garante que o sistema de navegação esteja ativo antes de continuar a execução das demais operações. Por fim, define-se as expressões regulares, que serão o padrão de busca na entrada que refere a localização, dada pelo usuário.


A função `create_pose_stamped()`, citada acima, configura a posição inicial do robô para que ele consiga se achar no mapa:
```python showLineNumbers title="main.py"
    def create_initial_pose(self):
        initial_pose = PoseStamped()
        initial_pose.header.frame_id = 'map'
        initial_pose.header.stamp = self.nav.get_clock().now().to_msg()
        initial_pose.pose.position.x = 0.0
        initial_pose.pose.position.y = 0.0
        initial_pose.pose.position.z = 0.0
        initial_pose.pose.orientation.x = self.q_x
        initial_pose.pose.orientation.y = self.q_y
        initial_pose.pose.orientation.z = self.q_z
        initial_pose.pose.orientation.w = self.q_w
        return initial_pose
```
Nessa função, nota-se alguns pontos: <br/>
Primeiramente, ela cria uma instância de PoseStamped, que nada mais é que um tipo de mensagem em ROS2 que representa a posição e orientação do objeto em um espaço tridimensional. Após isso, ela define o quadro de referência, ou seja, o mapa que será utilizado. Depois, essencialmente, define as posições e orientações iniciais do objeto e retorna a mensagem.

Pronto! a posição inicial está configurada.

O último passo é criar uma lista de pontos para o robô percorrer, simulando a movimentação em diferentes setores da empresa parceira. Para isso, cria-se um dicionário que comporta e classifica todos os pontos com base nas expressões regulares:

```python showLineNumbers title="main.py"
    self.coordenadas_dict = {
        "1": self.create_pose_stamped(self.nav, 1.0, 0.0, 0.0),
        "2": self.create_pose_stamped(self.nav, 1.3, 1.3, 0.0),
        "3": self.create_pose_stamped(self.nav, 1.5, -1.0, 0.0)
    }
```
E a função `create_waypoints()` fará o processamento:
```python showLineNumbers title="main.py"
    def create_waypoints(self):
        while True:
            local = input("Para onde deseja ir? (Digite q para sair) ")
            match = re.search(self.regex, local, re.IGNORECASE)
            if local == 'q':
                self.nav.followWaypoints([self.create_pose_stamped(self.nav, 0.0, 0.0, 0.0)])
                print("Vontando para a posição inicial...")
                rclpy.shutdown()
                break
            if match:
                print("Indo...")
                numero_encontrado = match.group(2)  
                self.nav.followWaypoints([self.coordenadas_destino(numero_encontrado)])
                while not self.nav.isTaskComplete():
                    print(self.nav.getFeedback())
            else:
                print("Local indicado não mapeado.")
```
Esta função inicia solicitando a entrada do usuário, que será a localização desejada e sugere a alternativa de saída. Se o usuário optar pela altenartiva de saída, o sistema reiniciará o navegador para a posição de origem. Caso o usuário entre com uma localização presente no dicionário, o robô se movimentará até a posição atribuída a ela. Por fim, caso nenhum desses requisitos sejam atendidos, o sistema retorna que o local não foi previamente mapeado.