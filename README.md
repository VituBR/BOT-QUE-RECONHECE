╔══════════════════════════════════════════════════════════════╗
║        🤖 DISCORD IMAGE RECOGNITION BOT                    ║
║        Teachable Machine + Python + Keras                   ║
╚══════════════════════════════════════════════════════════════╝

📌 SOBRE O PROJETO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Este projeto é um bot para Discord desenvolvido em Python capaz
de receber imagens enviadas pelos usuários e utilizar Inteligência
Artificial para reconhecer o conteúdo dessas imagens.

O reconhecimento é feito através de um modelo treinado no
Google Teachable Machine e exportado para o formato Keras.

O objetivo do projeto é criar uma integração simples entre um
bot do Discord e um modelo de Machine Learning capaz de analisar
imagens.

O bot recebe uma imagem, processa seus pixels, envia os dados
para o modelo de Inteligência Artificial e retorna no Discord
qual classe foi identificada.

✨ PRINCIPAIS RECURSOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Recebe imagens diretamente pelo Discord
• Verifica se o arquivo enviado é uma imagem
• Suporta PNG, JPG, JPEG e GIF
• Processa automaticamente a imagem
• Redimensiona a imagem para 224 × 224 pixels
• Utiliza um modelo treinado no Teachable Machine
• Identifica a classe com maior probabilidade
• Retorna o resultado diretamente no Discord
• Pode ser treinado para reconhecer diferentes tipos de objetos

🧠 INTELIGÊNCIA ARTIFICIAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A inteligência artificial utilizada pelo projeto é criada através
do Google Teachable Machine.

O Teachable Machine permite treinar modelos de Machine Learning
utilizando imagens fornecidas pelo próprio usuário.

Por exemplo, um modelo pode ser treinado para reconhecer:

```
🐱 Gatos
🐶 Cachorros
🚗 Carros
🍎 Frutas
🌳 Plantas
🎮 Objetos
👕 Roupas
🐦 Animais
```

O que o bot consegue reconhecer depende das classes utilizadas
durante o treinamento.

O código do bot não precisa ser alterado para cada novo tipo de
imagem. Basta treinar outro modelo e substituir os arquivos do
modelo.

⚙️ COMO O SISTEMA FUNCIONA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

O funcionamento do bot pode ser resumido em algumas etapas:

```
01. O usuário envia uma imagem no Discord
                ↓
02. O bot recebe o arquivo
                ↓
03. O bot verifica se o arquivo é uma imagem
                ↓
04. A imagem é salva temporariamente
                ↓
05. A imagem é redimensionada para 224 × 224
                ↓
06. Os pixels são convertidos para números
                ↓
07. Os valores são normalizados
                ↓
08. A imagem é enviada para o modelo
                ↓
09. A IA calcula as probabilidades
                ↓
10. A classe com maior probabilidade é selecionada
                ↓
11. O resultado é enviado ao Discord
```

📂 ESTRUTURA DO PROJETO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
bot-discord/
│
├── bot.py
├── keras_model.h5
├── labels.txt
│
└── images/
```

Cada arquivo possui uma função específica.

bot.py
→ Contém todo o código responsável pelo funcionamento do bot.

keras_model.h5
→ Contém o modelo de Inteligência Artificial treinado no
Teachable Machine.

labels.txt
→ Contém os nomes das classes que o modelo consegue reconhecer.

images/
→ Pasta utilizada para armazenar as imagens enviadas pelos
usuários.

🧩 ARQUIVO KERAS_MODEL.H5
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

O arquivo keras_model.h5 contém o modelo de Machine Learning
treinado pelo Teachable Machine.

Ele é responsável por analisar a imagem recebida e gerar as
probabilidades de cada classe.

Por exemplo, imagine um modelo treinado para reconhecer três
classes:

```
Cachorro
Gato
Coelho
```

Ao receber uma imagem, o modelo pode retornar algo parecido com:

```
Cachorro → 0.03
Gato     → 0.94
Coelho   → 0.03
```

Nesse caso, a maior probabilidade pertence à classe "Gato".

O bot então identifica essa classe e envia o resultado para
o usuário.

🏷️ ARQUIVO LABELS.TXT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

O arquivo labels.txt contém os nomes das classes utilizadas
pelo modelo.

Um exemplo seria:

```
0 Cachorro
1 Gato
2 Coelho
```

O modelo trabalha principalmente com valores numéricos e índices.
O arquivo labels.txt permite transformar esses índices nos nomes
das classes.

Por exemplo:

```
Índice retornado → 1

Classe correspondente → Gato
```

O bot então consegue transformar o resultado numérico em uma
resposta compreensível.

🖼️ PROCESSAMENTO DA IMAGEM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Antes de enviar a imagem para a Inteligência Artificial, o bot
precisa preparar o arquivo.

O modelo utilizado espera receber imagens com tamanho específico.

Por isso, a imagem enviada pelo usuário é redimensionada para:

```
224 × 224 pixels
```

Depois disso, a imagem é convertida para uma estrutura numérica.

Cada pixel da imagem possui valores que representam suas cores.
Esses valores são transformados em números que podem ser
processados pela rede neural.

Os valores também são normalizados para facilitar o processamento
pelo modelo.

🔎 RECONHECIMENTO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Depois que a imagem é preparada, ela é enviada para o modelo.

A Inteligência Artificial analisa a imagem e retorna uma
probabilidade para cada classe disponível.

Por exemplo:

```
🐶 Cachorro     5%
🐱 Gato        92%
🐰 Coelho       3%
```

O sistema identifica o maior valor.

Nesse exemplo:

```
MAIOR PROBABILIDADE → Gato
```

O bot então responde:

```
🔎 Eu reconheci: Gato
```

💬 COMANDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Para utilizar o sistema, basta enviar uma imagem junto do comando:

```
?reconhecer
```

Exemplo:

```
Usuário:
?reconhecer
[imagem enviada]

Bot:
🔎 Eu reconheci: Gato
```

📸 FORMATOS ACEITOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

O bot aceita os seguintes formatos de imagem:

```
✓ PNG
✓ JPG
✓ JPEG
✓ GIF
```

Arquivos que não sejam imagens não serão enviados para o modelo.

🚀 COMO CONFIGURAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Primeiramente, é necessário possuir Python instalado no computador.

Depois, instale as bibliotecas necessárias para executar o projeto.

As principais dependências são:

```
discord.py
tensorflow
keras
numpy
pillow
```

Também é necessário possuir um bot criado no Discord Developer
Portal.

Depois de criar o bot, coloque o token dele no final do código.

O token deve permanecer privado.

🔐 SEGURANÇA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

O token do bot do Discord é uma informação extremamente
importante.

Nunca publique o token no GitHub, em vídeos, prints ou envie
para outras pessoas.

O token funciona como uma credencial para acessar o bot.

Caso ele seja exposto, é recomendado gerar um novo token através
do Discord Developer Portal.

🎓 TREINANDO UM NOVO MODELO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Uma das maiores vantagens deste projeto é que o modelo pode ser
alterado sem precisar reconstruir o bot.

Para criar um novo sistema de reconhecimento, basta utilizar o
Teachable Machine para treinar novas classes.

Por exemplo, você pode criar:

```
MODELO DE ANIMAIS

🐶 Cachorro
🐱 Gato
🐰 Coelho
```

Ou:

```
MODELO DE FRUTAS

🍎 Maçã
🍌 Banana
🍊 Laranja
🍋 Limão
```

Ou até:

```
MODELO DE JOGOS

🎮 Minecraft
🎮 Roblox
🎮 Valorant
🎮 Fortnite
```

Depois de treinar o modelo, exporte-o para Keras e substitua:

```
keras_model.h5
labels.txt
```

O restante do bot pode continuar igual.

📊 QUALIDADE DO MODELO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A qualidade do reconhecimento depende principalmente da qualidade
do treinamento realizado no Teachable Machine.

É importante utilizar imagens variadas durante o treinamento.

Tente variar:

```
• Iluminação
• Ângulo
• Distância
• Fundo
• Posição
• Tamanho do objeto
• Aparência
```

Se todas as imagens utilizadas no treinamento forem muito
parecidas, o modelo pode ter dificuldades para reconhecer imagens
diferentes posteriormente.

⚠️ LIMITAÇÕES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Este bot não possui uma Inteligência Artificial capaz de entender
qualquer imagem existente.

Ele reconhece apenas as classes para as quais foi treinado.

Por exemplo, se o modelo foi treinado para reconhecer:

```
Cachorro
Gato
Coelho
```

ele não possui necessariamente conhecimento suficiente para
reconhecer corretamente:

```
Carro
Casa
Computador
Pessoa
```

Além disso, mesmo quando uma imagem não pertence a nenhuma das
classes treinadas, o modelo ainda pode escolher uma delas.

Por isso, a confiança e a qualidade do treinamento são muito
importantes.

⚡ POSSÍVEIS MELHORIAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

O projeto pode ser expandido futuramente com diversas funções.

Algumas possibilidades incluem:

```
• Mostrar a porcentagem de confiança
• Mostrar todas as probabilidades
• Criar respostas utilizando Embeds
• Adicionar mensagens de erro mais detalhadas
• Excluir automaticamente as imagens processadas
• Carregar o modelo apenas uma vez ao iniciar o bot
• Criar diferentes comandos para diferentes modelos
• Criar um sistema de histórico de reconhecimentos
• Adicionar suporte para mais formatos
• Criar um sistema de classificação mais avançado
```

🔄 FLUXO COMPLETO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

```
                     👤 USUÁRIO
                         │
                         ▼
                🖼️ ENVIA UMA IMAGEM
                         │
                         ▼
                   🤖 DISCORD BOT
                         │
                         ▼
                🔍 VERIFICA O ARQUIVO
                         │
                         ▼
                   💾 SALVA A IMAGEM
                         │
                         ▼
                 🖼️ REDIMENSIONA
                   224 × 224
                         │
                         ▼
                 🔢 CONVERTE PIXELS
                         │
                         ▼
                   📊 NORMALIZA
                         │
                         ▼
                 🧠 MODELO KERAS
                         │
                         ▼
                📈 FAZ A PREVISÃO
                         │
                         ▼
              🏆 PEGA A MAIOR CLASSE
                         │
                         ▼
                   🏷️ LABELS.TXT
                         │
                         ▼
                   💬 RESULTADO
                         │
                         ▼
              🔎 "Eu reconheci: Gato"
```

🛠️ TECNOLOGIAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🐍 Python
Linguagem utilizada para desenvolver o bot e controlar todo
o processo de reconhecimento.

💬 Discord.py
Biblioteca responsável pela comunicação entre o programa e
o Discord.

🧠 TensorFlow / Keras
Responsável por carregar e executar o modelo de Inteligência
Artificial.

🔢 NumPy
Utilizado para trabalhar com os dados numéricos das imagens.

🖼️ Pillow
Utilizado para carregar e preparar as imagens.

🎓 Google Teachable Machine
Utilizado para treinar o modelo de reconhecimento de imagens.

🎯 OBJETIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

O principal objetivo deste projeto é demonstrar como uma
Inteligência Artificial treinada através do Teachable Machine
pode ser integrada a um bot do Discord.

O projeto também serve como uma introdução prática aos conceitos
de:

```
• Python
• Bots do Discord
• Machine Learning
• Inteligência Artificial
• Visão computacional
• Processamento de imagens
• Redes neurais
• Classificação de imagens
```

╔══════════════════════════════════════════════════════════════╗
║                    🤖 FIM DO README                         ║
║                                                              ║
║       Discord + Python + Teachable Machine + IA              ║
╚══════════════════════════════════════════════════════════════╝
