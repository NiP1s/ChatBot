# ChatBot
 
### Sobre o projeto

Este projeto foi desenvolvido para um processo seletivo, que consiste na construção de um chatbot baseado em IA para responder dúvidas sobre o vestibular da Unicamp 2024. Tendo como objetivo a introdução ao RAG - Retrieval Augmented Generation e a utilização de APIs. 

### Como executar

Foi utilizado o anaconda para a criação de um ambiente virtual.
Para executar o programa, antes é necessario preparar seu ambiente para a utilização das bibliotecas. Portanto temos que instalar as seguintes bibliotecas:
- Langchain
- Openai
- tiktoken
- ChromaDB
- Streamlit

Para a instalações das biblitecas usadas, foram executados os seguintes comandos no terminal:
- pip install langchain openai
- pip install tiktoken chromadb 
- pip install streamlit
  
Agora que nosso ambiente foi preparado, após baixar o arquivo python e a pasta static, abra o arquivo .py e coloque sua chave da OpenAi no local indicado no código para seu funcionamneto, depois de salvar a alteração feita basta dar o comando no terminal, você deve estar na pasta do arquivo python, streamlit run myfile.py, substituir myfile pelo nome de como você salvou o arquivo python, e assim irá se abrir um localhost para a interação com o chatbot.

 ### Teste

 Seu teste foi feito com algumas perguntas que podem ser recorrentes, essas estão no arquivo [DataSet](./DataSet.txt). O chatGPT foi utilizado para a criação de algumas perguntas, para gerar essas perguntas foi pedido "Gere 10 perguntas que um estudante faria na buscas de informações sobre o vestibular da unicamp"

 #### Resultado

 Da forma como o bot foi criado, é sempre bom dar um contexto, no caso falarmos que é o vestibular da unicamp 2024 ou VU 2024, desta forma as chances de obter a resposta em vez de receber uma mensagem que não foi possivel encontrar a resposta são aumentadas.<br />
 As resposta levam em media 15 segundos para a resposta, algumas vezes elas são mais rápidas outras mais demoradas, foi percebido também que como a pergunta é feita influência nesse tempo de resposta, então se fazermos uma pergunta muito abrangente, pode ser que a resposta não seja encontrada ou que demore um tempo para a sua resposta. 
 
 
