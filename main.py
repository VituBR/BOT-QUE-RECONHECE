```python
import discord
from discord.ext import commands
from keras.preprocessing import image
from keras.models import load_model
import numpy as np
import uuid
import os

# Configurações do bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix='?',
    intents=intents
)


# Função para reconhecer a imagem
def reconhecer_imagem(caminho_imagem):
    # Carregar o modelo do Teachable Machine
    modelo = load_model("keras_model.h5")

    # Carregar os nomes das classes
    with open("labels.txt", "r") as arquivo:
        rotulos = [linha.strip() for linha in arquivo.readlines()]

    # Carregar e preparar a imagem
    img = image.load_img(
        caminho_imagem,
        target_size=(224, 224)
    )

    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    # Fazer o reconhecimento
    previsao = modelo.predict(img_array, verbose=0)

    indice = np.argmax(previsao, axis=1)[0]
    resultado = rotulos[indice]

    return resultado


# Quando o bot iniciar
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')


# Comando para enviar uma imagem
@bot.command()
async def reconhecer(ctx):

    if not ctx.message.attachments:
        await ctx.send("Envie uma imagem junto com o comando!")
        return

    imagem = ctx.message.attachments[0]

    # Verificar se é uma imagem
    if not imagem.filename.lower().endswith(
        ('.png', '.jpg', '.jpeg', '.gif')
    ):
        await ctx.send("O arquivo enviado não é uma imagem!")
        return

    # Criar nome único para a imagem
    nome_arquivo = f"{uuid.uuid4()}_{imagem.filename}"
    caminho = f"images/{nome_arquivo}"

    # Criar a pasta caso ela não exista
    os.makedirs("images", exist_ok=True)

    # Salvar a imagem
    await imagem.save(caminho)

    # Reconhecer a imagem
    resultado = reconhecer_imagem(caminho)

    # Enviar o resultado
    await ctx.send(f"🔎 Eu reconheci: **{resultado}**")


bot.run("cola teu token aaquiii")
```
