## Post Pronto 🚀
Gere posts de Instagram e descrições impactantes em segundos com a ajuda da inteligência artificial!

## Sobre o Projeto
O Post Pronto é uma ferramenta intuitiva que utiliza a poderosa API do Gemini para atuar como seu copywriter pessoal. 
Com apenas algumas informações básicas sobre o conteúdo, público-alvo e tom de voz desejado, a aplicação gera automaticamente 
um carrossel completo para Instagram e uma descrição otimizada, pronta para ser usada.

Ideal para criadores de conteúdo e qualquer pessoa que precise de posts de alta qualidade de forma rápida e eficiente.

### ✨ Funcionalidades
**Geração de Carrossel:** Cria automaticamente múltiplos slides para posts de carrossel no Instagram, formatados em Markdown.
<br>**Descrição Otimizada:** Gera uma descrição atrativa e relevante para o seu post.
<br>**Personalização Fácil:** Defina o Conteúdo, Público-alvo e Tom de Voz para resultados sob medida.
<br>**Integração com Gemini API:** Aproveita o poder da inteligência artificial avançada para criar textos criativos e coerentes.

### 🛠️ Tecnologias Utilizadas
- Python
- Streamlit
- Google Gemini API

## Como Rodar Localmente?
Siga estes passos para configurar e executar o Post Pronto em sua máquina.

1. Pré-requisitos
Certifique-se de ter o Python 3.8+ instalado.

2. Clone o Repositório
```bash
git clone https://github.com/MaduAraujo/Gerador-Posts.git
```

3. Navegue até a pasta
```bash
cd Gerador-Posts
```
4. Crie e Ative um Ambiente Virtual (Altamente Recomendado)

Snippet de código
```bash
python -m venv .venv
```

No Windows:
```bash
Bash
.venv\Scripts\activate
```

No macOS/Linux:
```bash
Bash
source .venv/bin/activate
```

5. Instale as Dependências
```bash
Bash
pip install
```

6. Configure sua Chave de API do Gemini
   
A aplicação requer uma chave de API do Gemini. A forma mais segura e recomendada é usar uma variável de ambiente.
Crie um arquivo chamado .env na raiz do seu projeto (na mesma pasta do app.py e do .gitignore) e adicione sua chave de API:

Snippet de código
```bash
GEMINI_API_KEY="SUA_CHAVE_DE_API_DO_GEMINI_AQUI"
```
Atenção: Nunca compartilhe sua chave de API publicamente! O arquivo .env já está configurado para ser ignorado pelo Git, garantindo que sua chave não seja enviada para o GitHub.

7. Execute a Aplicação
```bash
Bash
streamlit run seu_script.py
```
Nota: Substitua seu_script.py pelo nome do seu arquivo Python principal.
A aplicação será aberta automaticamente no seu navegador padrão, geralmente em http://localhost:8501.

## Projeto Funcionando

https://github.com/user-attachments/assets/eedf816a-01b1-437d-a0c8-12e975790d19
