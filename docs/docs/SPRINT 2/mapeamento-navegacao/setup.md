# Setup e configurações

Para o realização da prova de conceito do projeto foi escolhido o robô Turtlebot 3 Burger, dispositivo que já vem equipado com dois motores servos DYNAMIXEL XL-430-W350-T, uma placa Raspberry Pi, laser, sensor de distância, cartão microSD e bateria polímero de Lítio. 


<img src={require('/img/turtlebot3.png').default} width='90%'/>


## 1. Setup de configurações no robô

Abaixo é possível acompanhar os passos realizados para a configuração do robô utilizado.

<img src={require('/img/setup-robo.png').default} width='100%'/>


### 1.1 Instalação do Ubuntu Server 22.04

O Ubuntu Server 22.04 foi instalado utilizando o cartão SD proveniente do robô e o aplicativo [Raspberry Pi Imager](https://www.raspberrypi.com/software/). Durante a configuração, os seguintes passos foram realizados na seção "Operating System": "Other general-purpose OS" > "Ubuntu" > "Ubuntu Server 22.04". Na opção "Storage", o cartão SD destinado à instalação foi selecionado. Na seção de configurações, o hostname foi definido como `grupo5.local`, o nome de usuário como `inteli`, e a senha como `inteli`. Adicionalmente, foram configuradas as opções de rede e a senha do Wi-Fi.

### 1.2 Inserir cartão SD no robô para instalar imagem do sistema no Raspberry Pi

Após a configuração do cartão SD com o Ubuntu Server 22.04, o passo subsequente envolveu a inserção do cartão no robô. Posteriormente, o robô foi inicializado, e a instalação da imagem do sistema foi feita sem complicações.

### 1.3 Conexão ao Raspberry Pi por SSH

Depois da instalação do sistema é feita a conexão SSH com o Raspberrry Pi. Para isso é feito o seguinte comando:

```
ssh inteli@grupo5.local
```

É crucial destacar que esta abordagem será eficaz somente se o computador que executa o comando e o robô estiverem na mesma rede.


### 1.4 Instalação do ROS Humble

Para instalar o ROS Humble foi executado o seguinte comando:

```
sudo apt-get --with-new-pkgs upgrade dpkg
```

Após seu termino o Raspberry foi reiniciado.

### 1.5 Instação dos pacotes do Turtlebot3

O próximo passo foi a instalação dos pacotes do Turtlebot3 e para isso foi executado o seguinte comando:

```
sudo apt install ros-humble-turtlebot3*
```

### 1.6 Compilação do pacote do LIDAR LDS-02 e Setup do Open CR

Foram necessárias configurações específicas para compilar o pacote do LIDAR LDS-02 e realizar o setup do OpenCR a fim de garantir o funcionamento adequado do robô. A compilação do pacote do LIDAR LDS-02 é de importância crucial, uma vez que esse sensor desempenha um papel fundamental na condução do robô, evitando colisões com objetos ao redor e possibilitando a criação de mapas do ambiente. Por outro lado, o setup do OpenCR é igualmente essencial, pois essa placa controladora desempenha um papel vital no TurtleBot3, especialmente no que diz respeito ao controle da movimentação do robô.

Abaixo é destacado as peças que são configuradas nessa etapa:

<img src={require('/img/lidar-opencr.jpeg').default} width='40%'/>


A configuração desta etapa foi realizada seguindo os passos descritos nos links abaixo:

- [LIDAR LDS-02](https://rmnicola.github.io/m8-ec-encontros/sprint2/encontro4/turtlebot/#5-compilando-o-pacote-do-lidar-lds-02)
- [Setup do Open CR](https://rmnicola.github.io/m8-ec-encontros/sprint2/encontro4/turtlebot/#6-setup-do-opencr)

### 1.7 Comandando o Turtlebot3 para mapeamento 

No terminal, ainda conectado via SSH, para realizar o mapeamento e controlar o robô, é necessário configurar a variável de ambiente que define qual robô está sendo utilizado:
```
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc && source ~/.bashrc
```

Em seguido é executado o comando que inícia o robô:

```
ros2 launch turtlebot3_bringup robot.launch.py
```

Para operar o robô remotamente, é essencial uniformizar o `ROS_DOMAIN_ID` em todos os computadores envolvidos. Essa variável de ambiente determina as portas que o ROS utilizará para facilitar a comunicação em rede. Quando ambos os computadores compartilham a mesma rede e têm o mesmo ROS_DOMAIN_ID configurado, a comunicação entre seus nós ocorre automaticamente.

Sendo, assim, os seguinter comando devem ser feitos:

```
echo 'export ROS_DOMAIN_ID=51 #TURTLEBOT3' >> ~/.bashrc
```
```
source ~/.bashrc
```

É importante ressaltar que na configuração feita nesse projeto o `ROS_DOMAIN_ID` usado é o número 51.

Com as configurações do robô concluídas, é necessário proceder com a configuração da máquina destinada à comunicação com o robô. Como pré-requisito, a máquina deve operar com um sistema operacional Linux. Com isso em mente, a instalação do ROS2 na máquina é essencial, e é possível seguir as instruções detalhadas neste [tutorial](https://rmnicola.github.io/m8-ec-encontros/sprint1/encontro1/setup-ros). Após isso, também é necessário configurar o `ROS_DOMAIN_ID` na máquina de controle, sendo assim, os mesmo comando podem sem aplicados em um novo terminal utilizando o mesmo valor númerico definido no robô:

```
echo 'export ROS_DOMAIN_ID=51 #TURTLEBOT3' >> ~/.bashrc
```
```
source ~/.bashrc
```

Por fim é executado o comando abaixo para mover o robô a partir do teclado do computador de controle:

```
ros2 run turtlebot3_teleop teleop_keyboard
```

E, em um novo terminal é executado o comando abaixo. Ele irá abrir o RVIZ, software em que diversas informações do robô são demonstradas, dentre elas o mapa criado pelo cartographer.

```
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True 
```

Ao finalizar o mapeamento um novo terminal é aberto e o comando abaixo é executado para salvar o mapa:

```
ros2 run nav2_map_server map_saver_cli -f <nome-do-mapa>
```