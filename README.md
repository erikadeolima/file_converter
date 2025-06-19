# Conversor de Vídeo MOV

Este é um simples conversor de arquivos MOV para GIF ou MP4, desenvolvido em Python.

## Requisitos

- Python 3.6 ou superior
- Dependências listadas em `requirements.txt`

## Uso

1. Crie um ambiente virtual e ative-o:

```bash
python -m venv venv
source venv/bin/activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o script via terminal, fornecendo o caminho para o arquivo MOV que deseja converter:

```bash
python converter.py /caminho/para/seu/arquivo.mov
```

4. O programa solicitará o formato de saída desejado (GIF ou MP4).

   1. Alternativamente, você pode especificar o formato de saída diretamente:

    ```bash
    python converter.py /caminho/para/seu/arquivo.mov --output-format gif
    ```

    ou

    ```bash
    python converter.py /caminho/para/seu/arquivo.mov -o mp4
    ```

    #### Exemplo

    ```bash
    python converter.py ~/Videos/meu_video.mov -o gif
    ```

    O arquivo convertido será salvo no mesmo diretório do arquivo original, com o mesmo nome, mas com a extensão alterada.

5. Desativar o ambiente virtual

```bash
deactivate
```
