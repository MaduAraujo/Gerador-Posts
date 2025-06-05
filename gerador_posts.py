import streamlit as st
import os
import json # Importa a biblioteca json para parsear o retorno da API
import requests # Importa a biblioteca requests para fazer chamadas HTTP

st.title("Post Pronto 🚀")

# Campos de entrada para o usuário
conteudo  = st.text_input("Conteúdo")
publico  = st.text_input("Público-alvo")
tom = st.selectbox("Tom de voz", ["Amigável", "Profissional", "Urgente", "Divertido"])

# Template do prompt para o modelo
template = f"""
Você é um copywriter especialista. Gere:
1) Um carrossel de instagram. Me devolva uma resposta em Markdown, separando os slides do carrossel muito bem. 
2) Uma descrição ótima.
conteudo: {conteudo}
Público-alvo: {publico}
Tom de voz: {tom}
"""

# Botão para gerar o conteúdo
if st.button("Gerar Post"):
    if not conteudo or not publico:
        st.warning("Por favor, preencha o 'Conteúdo do Post' e o 'Público-alvo'.")
    else:
        with st.spinner("A gerar o seu post..."):
            try:
                api_key = os.getenv("GEMINI_API_KEY")

                if not api_key:
                    st.error("Chave da API do Gemini não encontrada. Por favor, defina a variável de ambiente 'GEMINI_API_KEY' ou insira-a diretamente no código para testes.")
                    st.stop()

                # Prepara o payload para a chamada da API do Gemini
                chat_history = []
                chat_history.append({"role": "user", "parts": [{"text": template}]})
                payload = {"contents": chat_history}
                api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

                # FAZ A CHAMADA REAL À API DO GEMINI USANDO 'requests'
                headers = {'Content-Type': 'application/json'}
                
                response = requests.post(api_url, headers=headers, data=json.dumps(payload))
                response.raise_for_status() 
                result = response.json() 
                if result and result.get("candidates") and len(result["candidates"]) > 0:
                    response_text = result["candidates"][0]["content"]["parts"][0]["text"]
                    # Divide o texto em carrossel e descrição
                    parts = response_text.split("---")
                    
                    st.subheader("Carrossel Instagram 📸")
                    # Exibe cada slide do carrossel em caixas separadas para melhor visualização
                    carousel_slides = []
                    description = ""
                    
                    if len(parts) > 1:
                        # As primeiras N-1 partes são os slides do carrossel
                        for i in range(len(parts) - 1):
                            if parts[i].strip(): 
                                carousel_slides.append(parts[i].strip())
                        # A última parte é a descrição (ou o que sobrou após o último '---')
                        description = parts[-1].strip()

                        for i, slide_content in enumerate(carousel_slides):
                            st.markdown(f"**Slide {i+1}**")
                            st.markdown(slide_content)
                            st.markdown("---")

                        st.subheader("Descrição do Post 📝")
                        st.markdown(description)
                    else:
                        # Se não houver "---" no resultado, exibe tudo como uma única resposta
                        st.markdown(response_text)
                else:
                    st.error("Não foi possível gerar o conteúdo. A resposta do modelo está vazia ou num formato inesperado. Tente novamente.")

            except requests.exceptions.RequestException as e:
                st.error(f"Ocorreu um erro ao comunicar com a API do Gemini: {e}")
                st.info("Por favor, verifique se a sua chave de API do Gemini está correta e se tem ligação à internet. Tente novamente.")
            except json.JSONDecodeError:
                st.error("A resposta da API não é um JSON válido. Tente novamente.")
            except Exception as e:
                st.error(f"Ocorreu um erro inesperado: {e}")
                st.info("Por favor, verifique se o 'Conteúdo do Post' e o 'Público-alvo' são claros e tente novamente.")