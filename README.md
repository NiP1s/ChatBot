# ChatBot
 
### Sobre o projeto

Este projeto foi desenvolvido para um processo seletivo, que consiste na construção de um chatbot baseado em IA para responder dúvidas sobre o vestibular da Unicamp 2024. Um dos objetivos é a introdução ao RAG - Retrieval Augmented Generation e a utilização de APIs.

### Como executar

Foi utilizado o Anaconda para a criação de um ambiente virtual. Para executar o programa, antes é necessário preparar seu ambiente para a utilização das bibliotecas. Portanto, temos que instalar as seguintes bibliotecas:
- Langchain
- Openai
- Tiktoken
- ChromaDB
- Streamlit

Para a instalações das biblitecas usadas, foram executados os seguintes comandos no terminal:
- pip install langchain openai
- pip install tiktoken chromadb 
- pip install streamlit
  
Agora que nosso ambiente foi preparado, após baixar o arquivo Python e a pasta "static", abra o arquivo .py e coloque sua chave da OpenAI no local indicado no código para o seu funcionamento. Depois de salvar a alteração feita, basta dar o comando no terminal (certifique-se de estar na pasta do arquivo Python): **streamlit run myfile.py**. Substitua "myfile" pelo nome como você salvou o arquivo Python. Assim, abrirá um localhost para a interação com o chatbot.

 ### Teste

 Seu teste foi feito com algumas perguntas que podem ser recorrentes, essas estão no arquivo [DataSet](./DataSet.txt). O chatGPT foi utilizado para a criação de algumas perguntas, para gera-las foi pedido "Gere 10 perguntas que um estudante faria na buscas de informações sobre o vestibular da unicamp".

 #### Resultado

 Da forma como o bot foi criado, é sempre bom fornecer um contexto, no caso falarmos que é o vestibular da unicamp 2024 ou VU 2024, desta forma as chances de obter a resposta em vez de receber uma mensagem que não foi possivel encontrar a resposta são aumentadas.<br />
 As respostas levam, em média, 15 segundos. Às vezes, são mais rápidas, outras vezes mais demoradas. Também foi percebido que a forma como a pergunta é feita influencia no tempo de resposta. Portanto, se fizermos uma pergunta muito abrangente, é possível que a resposta não seja encontrada ou que demore um tempo para ser fornecida.

 ## Código do ChatBot

 Temos que os comentários no [código](./Chatbot_streamlit_app.py) explicam de maneira sucinta o que cada função faz.<br />
 As bibliotecas utilizadas foram:

 - **Dataclasses:** Facilita a criação de classes de dados imutáveis em Python, reduzindo a quantidade de código necessário para definições de classes simples.
 - **Literal:** Introduz o tipo Literal para fornecer sugestões de tipo específicas para strings constantes, melhorando a segurança e a clareza do código.
 - **streamlit (st):** Uma biblioteca para criar aplicativos web interativos com Python, permitindo a fácil criação de interfaces do usuário para análise de dados e visualizações.
 - **os** : Fornece uma interface para interagir com funcionalidades dependentes do sistema operacional, como a manipulação de variáveis de ambiente.
 - **langchain.document_loaders:**  Módulo que oferece funcionalidades para carregar documentos, neste caso, carregar documentos HTML de uma URL.
 - **langchain.text_splitter:** Fornece ferramentas para dividir o texto em pedaços menores, usando métodos específicos, como a classe RecursiveCharacterTextSplitter usada aqui.
 - **langchain.embeddings:**  Implementa funcionalidades para calcular embeddings de documentos, com a classe OpenAIEmbeddings sendo utilizada para calcular embeddings usando a OpenAI.
 - **langchain.vectorstores:**  Oferece uma estrutura para armazenar e recuperar vetores, onde a classe Chroma é usada para armazenar embeddings e documentos para recuperação.
 - **langchain.chains:** Implementa cadeias de processamento de texto, e a classe RetrievalQA é utilizada para configurar um sistema de pergunta e resposta baseado em recuperação.
 - **langchain.prompts:** Fornece ferramentas para criar e manipular prompts, e a classe PromptTemplate é utilizada para criar modelos de prompts.
 - **langchain.chat_models:** Implementa modelos de chat, com a classe ChatOpenAI sendo utilizada para configurar um modelo de linguagem específico para chat da OpenAI.

## Bibliografia

Para o entendimento de RAG, langchain e como utiliza-los com o chatGPT foram vistos os seguintes videos:
- [What is Retrieval-Augmented Generation (RAG)?](https://www.youtube.com/watch?v=T-D1OfcDW1M&list=PLFCHBrHcKYsvSE4qgU7TNnb0_0-qYNcGv&index=1&t=6s)
- [Retrieval Augmented Generation with OpenAI/GPT and Chroma](https://www.youtube.com/watch?v=Cim1lNXvCzY&list=PLFCHBrHcKYsvSE4qgU7TNnb0_0-qYNcGv&index=2)
- [CHATGPT For WEBSITES: Custom ChatBOT: LangChain Tutorial](https://www.youtube.com/watch?v=RBnuhhmD21U&t=484s)

Videos para aprender o Streamlit:
- [Build a Streamlit Chatbot FAST ](https://www.youtube.com/watch?v=sBhK-2K9bUc)
- [Kickstart your Custom Streamlit Chatbot (ft. CSS & Langchain)](https://www.youtube.com/watch?v=6fs80o7Xm4I)

Também foi visto os sites :
- [Langchain - chatbot](https://python.langchain.com/docs/use_cases/chatbots/)
- [Langchain - web_scraping](https://python.langchain.com/docs/use_cases/web_scraping)
- [Streamlit](https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps)
 
 
