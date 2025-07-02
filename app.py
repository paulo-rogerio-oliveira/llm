import streamlit as st
from langchain_community.llms import HuggingFaceHub
import unicodedata


def remove_non_utf(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text) if ord(c) < 128)

st.set_page_config(page_title="Sumarizador de Artigos com LLM", layout="centered")
st.title("Sumarizador de Artigos com LLM (HuggingFace)")
st.write("Insira o texto de um artigo ou qualquer texto longo para obter um resumo gerado por IA.")

user_text = st.text_area("Cole o texto do artigo aqui:", height=300)
hf_token = st.text_input("Token HuggingFace (https://huggingface.co/settings/tokens)", type="password")
generate_summary = st.button("Resumir")

if generate_summary and user_text and hf_token:
    with st.spinner("Gerando resumo..."):
        safe_text = remove_non_utf(user_text)
        llm = HuggingFaceHub(
            repo_id="sshleifer/distilbart-cnn-12-6",
            huggingfacehub_api_token=hf_token,
            model_kwargs={"max_length":130, "min_length":30, "do_sample":False}
        )
        summary = llm(safe_text)
    st.subheader("Resumo gerado:")
    st.success(summary)

st.markdown("---")
st.markdown("Desenvolvido com [Streamlit](https://streamlit.io/), [LangChain](https://langchain.com/) e [HuggingFace](https://huggingface.co/)") 