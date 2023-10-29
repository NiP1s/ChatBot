from dataclasses import dataclass
from typing import Literal
import streamlit as st
import os

from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

# Define uma classe chamada Message usando o decorador @dataclass, que simplifica a criação de classes de dados imutáveis.
# Essa classe é usada para representar uma mensagem em uma conversa, mantendo a origem da mensagem (humana ou de IA) e o texto da mensagem.
@dataclass
class Message:
    """Class for keeping track of a chat message."""
    origin: Literal["human", "ai"]
    message: str

#Função para importar o css
def load_css():
    with open("static/style.css", "r") as f:
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)
    
#Função inicializa a sessão do Streamlit para manter o estado entre as interações do usuário.
def initialize_session_state():
    # Verifica se o histórico de mensagens está presente na sessão, e se não estiver, cria uma lista vazia para armazená-lo.
    if "history" not in st.session_state:
        st.session_state.history = []
    # Verifica se o objeto qa_with_source está presente na sessão.
    # Caso não esteja, executa uma sequência de operações para configurar um sistema de pergunta e resposta usando a OpenAI.
    if "qa_with_source" not in st.session_state:
        #ChatBot-langchain
        # Configura a chave da API da OpenAI usando um segredo do Streamlit.
        os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
        # Carrega documentos HTML da URL fornecida.
        loader = WebBaseLoader("https://www.pg.unicamp.br/norma/31594/0")
        docs = loader.load()
        # Divide o texto em pedaços menores usando um método específico.
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,  #Define o tamanho máximo de cada pedaço (chunk) do texto. No caso, cada chunk terá no máximo 1000 caracteres.
            chunk_overlap=200, #Especifica o tamanho da sobreposição entre chunks consecutivos. 
            length_function = len, #Indica a função utilizada para calcular o comprimento do texto.
            is_separator_regex= False #Determina se o parâmetro fornecido como is_separator é uma expressão regular.
        )
        # Faz a divisão do documento gerado anteriromente e salva na variavel data.
        data = text_splitter.split_documents(docs)
        # Calcula embeddings para os documentos usando OpenAI.
        embeddings = OpenAIEmbeddings()
        # Armazena os embeddings e documentos no Chroma para recuperação.
        store = Chroma.from_documents(
            data,
            embeddings,
            collection_name = "ResolucaoUnicamp",
            persist_directory = 'db',
        )
        #Esse método é responsável por persistir (ou salvar) os dados armazenados no objeto store
        store.persist()
        # Define um modelo de linguagem com uma temperatura zero.
        template = """You are a bot that answers questions about Unicamp entrance exam, using only the context provided.
        If you dont't know the answer, simply state that you don't know.

        {context}

        question: {question}"""
        # Cria um objeto PROMPT utilizando a classe PromptTemplate, que serve como um modelo para a geração de prompts para a OpenAI.
        # O template especifica a estrutura da pergunta, incluindo variáveis de entrada como 'context' e 'question'.
        PROMPT =  PromptTemplate(
            template=template, input_variables=["context", "question"]
        )
        # Inicializa um modelo de linguagem de chat da OpenAI (ChatOpenAI).
        # O parâmetro 'temperature=0' significa que as saídas geradas pelo modelo serão determinísticas, sem variação aleatória.
        # O parâmetro 'model_name='gpt-3.5-turbo'' especifica o modelo específico a ser utilizado (GPT-3.5-turbo).
        llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
        # Configura um sistema de pergunta e resposta usando a cadeia de documentos previamente armazenados.
        st.session_state.qa_with_source = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever = store.as_retriever(),
            chain_type_kwargs = {"prompt": PROMPT, },
            return_source_documents = False,
        )
        
# Função que é chamada quando o botão 'Enviar' é clicado, realizando interações na conversa entre o usuário e o modelo de linguagem.
def on_click_callback():
    # Obtém a última mensagem inserida pelo usuário armazenada na sessão.
    human_prompt = st.session_state.human_prompt
    # Chama o modelo de pergunta e resposta (qa_with_source) para obter uma resposta com base na mensagem do usuário.
    llm_response = st.session_state.qa_with_source(
        human_prompt
    )
    # Adiciona a mensagem do usuário ao histórico com a marca "human".
    st.session_state.history.append(
        Message("human", human_prompt)
    )
    # Adiciona a resposta do modelo ao histórico com a marca "ai".
    st.session_state.history.append(
        Message("ai", llm_response['result'])
    )

load_css()
initialize_session_state()

st.title("VU 2024 ChatBot")

#chatbot-streamlit
# Cria um container para exibir a conversa, um formulário para a entrada do usuário e uma área vazia para exibir mensagens.
chat_placeholder = st.container()
prompt_placeholder = st.form("chat-form")
entry = st.empty()

# Dentro do container de conversa, itera sobre as mensagens no histórico e exibe cada uma formatada em bolhas de chat.
with chat_placeholder:
    for chat in st.session_state.history:
        # Cria uma bolha de chat formatada em HTML, ajustando a aparência com base na origem (ai ou humano) da mensagem.
        div = f"""
<div class="chat-row 
    {'' if chat.origin == 'ai' else 'row-reverse'}">
    <img class="chat-icon" src="app/static/{
        'ai.png' if chat.origin == 'ai' 
                      else 'user.png'}"
         width=32 height=32>
    <div class="chat-bubble
    {'ai-bubble' if chat.origin == 'ai' else 'human-bubble'}">
        &#8203;{chat.message}
    </div>
</div>
        """
        # Exibe a bolha de chat na interface do Streamlit.
        st.markdown(div, unsafe_allow_html=True)

# Dentro do formulário de entrada, cria campos de entrada de texto e um botão de envio.
with prompt_placeholder:
    # Adiciona campos de entrada de texto para o usuário inserir sua mensagem.
    colunas = st.columns((6,1))
    colunas[0].text_input(
        "Chat",
        value="",
        label_visibility="collapsed",
        key="human_prompt",
    )
    # Adiciona um botão de envio que chama a função on_click_callback quando pressionado.
    colunas[1].form_submit_button(
        "Enviar",
        type="primary",
        on_click=on_click_callback,
    )
