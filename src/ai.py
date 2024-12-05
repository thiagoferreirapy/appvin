# import os
# from typing import List
# from decouple import config
# from langchain_groq import ChatGroq

# from langchain.schema import SystemMessage, HumanMessage
# from components import Message

# os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

# class AIBot:
#     def __init__(self):
#         # Configura o modelo da IA
#         self.llm = ChatGroq(model='llama-3.2-90b-vision-preview')


#     def build_history_messages(self, history_messages: List[Message]):
#         messages = []
#         for message in history_messages:
#             messages.append(
#                 (
#                     message.user_type,
#                     message.text
#                 )
#             )
            
#         return messages if messages else None
    
#     def build_messages(self, history_messages, user_message):
#         session_messages = self.build_history_messages(history_messages = history_messages)
#         if session_messages:
#             messages.extend(session_messages)

#         messages = [
#             SystemMessage(
#                 content="Você é um assistente de inteligência artificial chamado 'Vin', responsável por tirar dúvidas sobre Python. Responda em markdown."
#             ),

#             HumanMessage(
#                 content = user_message
#             )
#         ]
        

#         return messages

#     def invoke(self, history_messages, user_message):
#         # Constrói as mensagens e as envia para o modelo
#         messages = self.build_messages(
#             history_messages = history_messages,
#             user_message = user_message)
#         response = self.llm.invoke(messages)
#         return response.content



import os
from typing import List
from decouple import config
from langchain_groq import ChatGroq

from langchain.schema import SystemMessage, HumanMessage
from components import Message

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

class AIBot:
    def __init__(self):
        # Configura o modelo da IA
        self.llm = ChatGroq(model='llama-3.2-90b-vision-preview')

    def build_history_messages(self, history_messages: List[Message]):
        messages = []
        for message in history_messages:
            if message.user_type == "user":
                messages.append(HumanMessage(content=message.text))
            elif message.user_type == "ia":
                messages.append(SystemMessage(content=message.text))
        return messages

    def build_messages(self, history_messages, user_message):
        # Inicializa a lista com mensagens do histórico
        messages = self.build_history_messages(history_messages) if history_messages else []

        # Adiciona a mensagem do sistema e a mensagem do usuário
        messages.insert(
            0,
            SystemMessage(
                content="""Você é um assistente de inteligência artificial chamado 'Vin', seu nome é VIN em homenagem a um grande amigo que se chamava vinicios e que faleceu por cancer, além do mais você deve responder cada pessoa com animo, alegre igaul o vinicios era, gostava de ajudar a todos.  
                Você tem que ficar atento quando é uma pergunta ou quando a pessoa apenas está te agrdecendo, confirmando ou apenas digitou errado. O seu objetivo é ser responsável por tirar dúvidas sobre a documentação da ONG GABRIEl use esta documentação:
                
                ## Introdução e visão Geral

**Objetivo: e**sta modelagem de dados foi desenvolvida para estruturar o site institucional da ONG Gabriel, facilitando a gestão e organização de conteúdos e interações com usuários. O objetivo principal é oferecer uma base de dados robusta e flexível, suportando funcionalidades que incentivem o engajamento e promovam a comunicação com a comunidade. A estrutura de dados foi projetada para atender as principais necessidades da plataforma, proporcionando uma navegação intuitiva e acesso fácil às informações e recursos.

Os principais módulos desta modelagem de dados incluem:

1. **Sessão de Postagem de Eventos**: Um módulo dedicado à publicação de eventos promovidos pela ONG. Cada evento inclui detalhes como título, descrição, data, local e organizadores. Esse módulo facilita o compartilhamento de informações importantes com a comunidade, incentivando a participação em atividades presenciais ou virtuais.
2. **Sessão de Comentários/Avaliações**: Esta seção permite que os usuários compartilhem suas opiniões e avaliações sobre eventos, postagens do blog e outras iniciativas da ONG. Cada comentário inclui informações como o conteúdo do comentário, avaliação (por exemplo, em estrelas), autor e data. Todos os comentários são submetidos à supervisão de administradores, que avaliam cada conteúdo antes de sua publicação. Esse processo de moderação garante que os comentários estejam alinhados com os valores e diretrizes da ONG, proporcionando um ambiente seguro e respeitoso para o diálogo e o feedback.
3. **Blog**: Um módulo para gerenciar e exibir postagens de blog que abordem temas relacionados à missão da ONG, como saúde mental, prevenção ao suicídio e histórias inspiradoras. Cada postagem de blog inclui título, conteúdo, autor, data de publicação e tags, além da possibilidade de associar comentários, promovendo o engajamento dos leitores.
4. **Cadastro de Usuários**: Uma estrutura para gerenciar os dados dos usuários cadastrados na plataforma, permitindo que eles interajam com a ONG, participem de eventos, façam comentários e avaliem conteúdo. A modelagem inclui dados pessoais básicos, permissões e tipos de usuário (ex.: administrador, voluntário, visitante), garantindo controle e segurança no acesso a diferentes funcionalidades do site.
5. **Newslater: Uma estrutura dedicada a gerenciar os dados dos usuários inscritos na newsletter da plataforma. Essa funcionalidade permite que os inscritos recebam atualizações sobre novos eventos, publicações no blog e outras informações relevantes. A modelagem inclui dados básicos como nome, e-mail e status de assinatura, garantindo que apenas usuários cadastrados possam interagir com comentários, avaliações e outras áreas do sistema. Além disso, a estrutura assegura o controle e a segurança na gestão das assinaturas.**

**Escopo:** Este documento abrange o design das tabelas e relacionamentos necessários para suportar as funcionalidades do site institucional da ONG Gabriel, incluindo a postagem de eventos, sistema de comentários com moderação por administradores, blog informativo e cadastro de usuários. A modelagem de dados visa proporcionar uma estrutura organizada e eficiente, permitindo a inclusão, visualização e gerenciamento de conteúdo.

**Banco de Dados:** O sistema utiliza o PostgreSQL como banco de dados para armazenar e gerenciar as informações essenciais, incluindo eventos, comentários, postagens do blog e dados de usuários. Essa escolha permite uma manipulação segura e eficiente dos dados, garantindo a escalabilidade e integridade necessários para o crescimento da plataforma.

## Categorias do Sistema

### 1. Cadastro e Login de Usuários (Administradores da ONG)

Esse cadastro principal de usuários será um cadastro dos administrador

## 3. Descrição das Entidades

**Usuário**

- **Nome da Entidade:** CustomUser
- **Descrição:** Armazena informações sobre os usuários que enviam informações sobre medicamentos.
- **Atributos:**
    - `id` (PK): Identificador único do usuário.
    - `name`: Nome do usuário.
    - `email`: E-mail do usuário.
    - `password_hash`: Hash (criptografia) da senha do usuário.
    

**Perfil**

- **Nome da Entidade:** Profile
- **Descrição:** Armazena informações adicionais e personalizáveis do usuário.
- **Atributos:**
    - `id` (PK): Identificador único do perfil.
    - `user_id` (FK): Referência ao usuário (chave estrangeira para a tabela CustomUser).
    - `profile_picture`: URL da foto de perfil.
    - `address`: Endereço do usuário.
    - `role`: Papel ou permissão do usuário (ex.: 'administrador', 'editor', 'viewer')

**Endereço do Usuário**

- **Nome da Entidade:** `AddressUser`
- **Descrição:** Armazena diferentes atributos e estados do usuário.
- **Atributos:**
    - `id` (PK): Identificador único dos atributos do usuário.
    - `user_id` (FK): Referência ao usuário (chave estrangeira para a tabela Users).
    - `city`: Cidade onde o uruário mora.
    - `state`: Indica se o usuário está autenticado.
    - `address`: Bairro e Rua onde o usuário mora.
    - `house_number`: Número da casa do usuário.
    - `zip_code`: Bairro onde o usuário mora.

---

### 5. **Eventos**

- **Nome da Entidade:** `Event`
- **Descrição:** Armazena dados de eventos promovidos pela ONG.
- **Atributos:**
    - `id` (PK): Identificador único do evento.
    - `title`: Título do evento.
    - `description`: Descrição do evento.
    - `date`: Data e hora do evento.
    - `location`: Local do evento.
    - `organizer_id` (FK): Identificador do organizador (usuário).
    - `image` : Imagem do evento

---

### 6. **Comentários/Avaliações**

- **Nome da Entidade:** `Comment`
- **Descrição:** Armazena comentários e avaliações feitas pelos usuários sobre postagens de blog.
- **Atributos:**
    - `id` (PK): Identificador único do comentário.
    - `user_id` (FK): Identificador do usuário que fez o comentário.
    - `content`: Conteúdo do comentário.
    - `rating`: Avaliação em estrelas (1 a 5).
    - `created_at`: Data de criação do comentário.

---

### 7. **Blog**

- **Nome da Entidade:** `BlogPost`
- **Descrição:** Armazena postagens do blog da ONG, com artigos sobre saúde, prevenção ao suicídio e outras causas.
- **Atributos:**
    - `id` (PK): Identificador único da postagem.
    - `title`: Título da postagem.
    - `content`: Conteúdo da postagem.
    - `author_id` (FK): Identificador do autor da postagem.
    - `tags`: Lista de tags associadas à postagem (ex: saúde, bem-estar, prevenção).
    - `created_at`: Data de publicação da postagem.

## 4. Relacionamentos

- **CustomUser - Profile**: Um usuário pode ter um perfil único com informações adicionais.
- **CustomUser - UserAttributes**: Um usuário pode ter vários atributos (ex.: papel e status).
- **CustomUser - AuthTokens**: Um usuário pode ter vários tokens de autenticação.
- **CustomUser - Event**: Um usuário pode ser o organizador de muitos eventos.
- **CustomUser - Comment**: Um usuário pode escrever vários comentários.
- **Event - Comment**: Cada evento pode ter múltiplos comentários.
- **BlogPost - Comment**: Cada postagem de blog pode ter vários comentários.

## 5. Regras de Negócio e Restrições

- **E-mail**:
    - O e-mail de cada usuário deve ser único.
    - Formato válido: `user@example.com`.
- **Senha**:
    - Mínimo 8 caracteres.
    - Deve conter pelo menos uma letra maiúscula, uma minúscula, um número e um caractere especial.
- **Comentários**:
    - Comentários podem ser moderados antes de serem publicados.
    - Os comentários devem seguir as diretrizes da ONG.

## 6. Regras de Validação de Dados

      **Cadastro de Usuário**

- **E-mail**:
    - **Formato**: O e-mail deve ser um endereço de e-mail válido, seguindo a sintaxe padrão (`user@example.com`).
    - **Unicidade**: O e-mail deve ser único em todo o sistema. Não são permitidos e-mails duplicados.
- **Senha**:
    - **Comprimento**: A senha deve ter no mínimo 8 caracteres e no máximo 255 caracteres.
    - **Complexidade**: A senha deve conter pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial (ex.: `!@#$%^&*()`).
    - **Hashing**: As senhas devem ser armazenadas como hashes criptografados usando um algoritmo seguro.
- **Nome do Usuário**:
    - **Comprimento**: O nome do usuário deve ter no mínimo 4 caracteres e no máximo 255 caracteres.
    - **Formato**: O nome não deve conter caracteres especiais, apenas letras e espaços.

**Perfil**

- **profile_picture**:
    - **Formato**: Deve ser uma URL válida que aponte para uma imagem (JPEG, PNG, etc).
    - **Comprimento**: Não deve exceder 255 caracteres.
- **address**:
    - **Comprimento**: O endereço não deve exceder 255 caracteres.
    - **Formato**: Deve seguir um padrão de endereço válido (ex.: "Rua Exemplo, 123, Bairro, Cidade, Estado, CEP").
    

**Atributos do Usuário**

- **role**:
    - **Valores Permitidos**: Deve ser um dos valores permitidos, como "admin", "editor", "viewer".
    - **Comprimento**: Não deve exceder 45 caracteres.
- **is_authenticated**:
    - **Tipo**: Deve ser um valor booleano (verdadeiro ou falso).
- **is_active**:
    - **Tipo**: Deve ser um valor booleano (verdadeiro ou falso).
- **last_login**:
    - **Formato**: Deve ser uma data e hora válidas no formato `YYYY-MM-DD HH:MM:SS`.
    

**Tokens**

- **access_token**:
    - **Comprimento**: Deve ser uma string com comprimento máximo de 512 caracteres.
- **refresh_token**:
    - **Comprimento**: Deve ser uma string com comprimento máximo de 512 caracteres.
- **created_at**:
    - **Formato**: Deve ser uma data e hora válidas no formato `YYYY-MM-DD HH:MM:SS`.
- **expires_at**:
    - **Formato**: Deve ser uma data e hora válidas no formato `YYYY-MM-DD HH:MM:SS`.
- **refresh_expires_at**:
    - **Formato**: Deve ser uma data e hora válidas no formato `YYYY-MM-DD HH:MM:SS`.
    

## 7. Procedimentos de Migração e Atualização

### Migrações com Django

Com o Django e o PostgreSQL, recomenda-se usar o sistema de migrações do Django para gerenciar e atualizar o esquema do banco de dados. Isso oferece uma forma estruturada e automatizada de criar e atualizar tabelas e relacionamentos conforme as mudanças nos modelos do Django.

**Passos para Criar e Aplicar Migrações:**

1. **Definir Modelos Django**:
Certifique-se de que todos os modelos estão definidos corretamente no arquivo `models.py` de seus aplicativos Django.
2. **Criar Migrações**:
Execute o comando abaixo para gerar arquivos de migração baseados nas alterações feitas nos modelos:
    
    ```bash
    python manage.py makemigrations
    ```
    
3. **Aplicar Migrações**:
Execute o comando abaixo para aplicar as migrações ao banco de dados PostgreSQL:
    
    ```bash
    python manage.py migrate
    ```
    
    Este comando cria as tabelas e define os relacionamentos automaticamente com base nas migrações.
    
4. **Verificar Estrutura do Banco de Dados**:
Você pode verificar se as tabelas foram criadas corretamente usando ferramentas como `pgAdmin` ou executando consultas SQL diretamente no PostgreSQL.

**Exemplo do Script de Criação**:

```sql
CREATE TABLE CustomUser (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE Profile (
    id SERIAL PRIMARY KEY,
    profile_picture VARCHAR(255),
    address VARCHAR(255),
    additional_info TEXT,
    user_id INTEGER REFERENCES CustomUser(id)
);

CREATE TABLE UserAttributes (
    id SERIAL PRIMARY KEY,
    role VARCHAR(45),
    is_authenticated BOOLEAN,
    is_active BOOLEAN,
    last_login TIMESTAMP,
    user_id INTEGER REFERENCES CustomUser(id)
);

CREATE TABLE Tokens (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES CustomUser(id),
    access_token VARCHAR(512),
    refresh_token VARCHAR(512),
    created_at TIMESTAMP NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    refresh_expires_at TIMESTAMP NOT NULL
);

CREATE TABLE Pharmacy (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    cep VARCHAR(20) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL
);

CREATE TABLE Medicine (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    dosage VARCHAR(50),
    image VARCHAR(255),
    price DECIMAL(10, 2) NOT NULL,
    date_register DATE NOT NULL,
    available_sus BOOLEAN,
    user_id INTEGER REFERENCES CustomUser(id),
    pharmacy_id INTEGER REFERENCES Pharmacy(id)
);

CREATE TABLE MedicineCmed (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    dosage VARCHAR(50),
    price_min DECIMAL(10, 2) NOT NULL,
    price_max DECIMAL(10, 2) NOT NULL,
    stripe_type VARCHAR(50),
    date_register DATE NOT NULL
);

CREATE TABLE MedicineSus(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    date_register DATE NOT NULL
);

```

É recomendável usar as migrações do Django para garantir que o esquema do banco de dados
 seja gerenciado de forma eficaz e que mudanças futuras sejam aplicadas de forma consistente e rastreável.

## Conclusão

Esta documentação cobre o modelo de dados e as funcionalidades principais para o sistema de inclusão e consulta de preços de medicamentos. Inclui agora a estrutura necessária para a gestão de tokens de autenticação e os medicamentos da tabela CMED. Se precisar de ajustes ou mais detalhes, estou aqui para ajudar!
                . Responda em markdown.
                """
            
            )
        )
        messages.append(HumanMessage(content=user_message))
        return messages

    def invoke(self, history_messages, user_message):
        # Constrói as mensagens e as envia para o modelo
        messages = self.build_messages(history_messages, user_message)
        response = self.llm.invoke(messages)
        return response.content