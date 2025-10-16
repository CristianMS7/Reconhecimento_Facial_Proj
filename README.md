Sistema de Autenticação Facial


 Funcionalidades

Interface Gráfica Intuitiva: Criada com Tkinter para uma fácil interação.

Captura de Vídeo em Tempo Real: Utiliza a biblioteca OpenCV para acessar a webcam.

Reconhecimento Facial Avançado: Emprega o modelo Facenet da biblioteca DeepFace para uma identificação precisa.



Sistema de Permissão: Valida o acesso do usuário com base em níveis de permissão.

Estrutura do Projeto

.
├── Rostos_cadastrados/      # Pasta para armazenar as imagens de referência dos usuários.
├── app.py                   # Arquivo principal que executa a aplicação com interface gráfica.
├── autenticacao.py          # Módulo responsável pela lógica de autenticação.
├── dados_usuarios.py        # Módulo que simula o banco de dados de usuários.
├── reconhecimento.py        # Módulo que encapsula a lógica de reconhecimento facial.
├── requirements.txt         # Arquivo com as dependências do projeto.
└── .gitignore               # Arquivo que especifica o que o Git deve ignorar.


 Instalação e Execução

Siga os passos abaixo para configurar e executar o projeto no seu ambiente local.

Pré-requisitos

Python 3.8+

Git

Passos

Clone o repositório:

git clone [https://github.com/CristianMS7/Reconhecimento_Facial_Proj.git](https://github.com/CristianMS7/Reconhecimento_Facial_Proj.git)
cd Reconhecimento_Facial_Proj


Crie e ative um ambiente virtual:

# Criar o ambiente
python -m venv venv

# Ativar no Windows
.\venv\Scripts\activate




Instale as dependências:

pip install -r requirements.txt


Adicione as imagens de referência:

Certifique-se de que a pasta Rostos_cadastrados existe na raiz do projeto.

Adicione as fotos dos usuários autorizados dentro desta pasta (ex: Samuel.jpg, Alex.png). O nome do arquivo (sem a extensão) deve corresponder ao nome cadastrado em dados_usuarios.py.

Execute a aplicação:
No terminal:

python app.py


A janela da aplicação será iniciada, pronta para uso.