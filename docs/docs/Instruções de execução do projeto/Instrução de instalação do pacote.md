# Instalação dos Pacotes do Turtlebot

Este guia detalha os passos necessários para instalar o pacote Turtlebot, assegurando a funcionalidade plena do dispositivo.

## Pré-requisitos
Antes de iniciar a instalação, certifique-se de que os seguintes pré-requisitos estão atendidos:

- Ubuntu
- ROS (Robot Operating System)
- Nav2

# Passo a Passo da Instalação

1. **Clonagem do Repositório**

Primeiro, clone o repositório do Turtlebot no GitHub. Este passo é essencial para obter os arquivos mais recentes necessários para a instalação:

```
git clone github.com/2023M8T2-Inteli/grupo5.git
```

2. **Instalação de Dependências**

Depois da clonagem, é necessário instalar as dependências requeridas para o funcionamento correto do pacote. Execute os seguintes comandos:

```
sudo apt install python3-rosdep
sudo rosdep init
rosdep update
pip install setuptools==58.2.0
```
**3. Instalação das Dependências do ROS**

Para instalar as dependências específicas do ROS, use o seguinte comando:

```
rosdep install -i --from-path src --rosdistro humble -y
```

**4. Compilação do Pacote**

Para garantir que o pacote esteja na sua versão mais recente e configurado corretamente, proceda com a compilação:

```
colcon build --packages-select turtlebot3
```

**5. Configuração das Variáveis de Ambiente**

Após a compilação, configure as variáveis de ambiente para que o ROS possa utilizar todas as funcionalidades do pacote Turtlebot. Dependendo do seu shell, execute um dos comandos a seguir:

Para Bash:

```
source install/local_setup.bash
```

Para SSH:
```
source install/local_setup.zsh
```
