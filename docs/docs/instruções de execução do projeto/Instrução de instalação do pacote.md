# Instação dos pacotes

Para instalar o pacote responsável pelas funcionalidades do Turtlebot, é necessário seguir as etapas a seguir: 

Temos 3 prérequisitos para o funcionamento correto: Ubuntu, ROS e Nav2. Posteriorment é preciso realizar o clone do repositório no GitHub e obter as dependências necessárias:

Se necessário, faça o download das seguintes dependências:

´´´
sudo apt install python3-rosdep
sudo rosdep init
rosdep update
pip install setuptools==58.2.0
´´´

Execute os seguintes comandos:

´´´
git clone https://github.com/LucaSarhan/modulo8.git
rosdep install -i --from-path src --rosdistro humble -y
´´´

A fim de garantir o funcionamento adequado do pacote, é crucial realizar a compilação para atualizá-lo à sua versão mais recente e configurar as variáveis correspondentes para que o ROS possa aproveitar plenamente suas funcionalidades, segue rodar os seguintes comandos no diretório do pacote:

´´´
colcon build --packages-select turtlebot3
source install/local_setup.bash #se estiver usando zsh, mude para setup.zsh
´´´