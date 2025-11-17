📦 SGAE — Sistema de Gestão de Arquivos Empresariais
Sistema web desenvolvido em Django para gerenciar caixas de arquivos físicos por empresa, setor, localização e data de descarte.

🚀 Funcionalidades
- Cadastro de empresas e setores
- Registro de caixas com localização e descrição
- Filtro por data de descarte (caixas vencidas)
- Painel administrativo personalizado com Jazzmin
- Autenticação de usuários
- Tela de login customizada
🛠️ Tecnologias
- Python 3.10+
- Django 5.x
- SQLite (desenvolvimento)
- Jazzmin (admin estilizado)
- Bootstrap (interface)
- PythonAnywhere (deploy)


git clone https://github.com/emir-jr/sgae.git
cd sgae
python -m venv venv
source venv/bin/activate  #  venv/Scripts/Activate.ps1 no windows # venv\Scripts\activate no Windows

python manage.py migrate
python manage.py runserver

Acesse: http://127.0.0.1:8000/
