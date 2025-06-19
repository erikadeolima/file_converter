# Conversor de Arquivos MOV para GIF ou MP4

Este projeto permite converter arquivos de vídeo no formato `.mov` para `.gif` ou `.mp4` usando Python e MoviePy.

## Pré-requisitos

- Python 3 instalado (recomendado Python 3.8+)
- `pip` instalado

## Instalação

Clone o repositório:

```sh
git clone git@github.com:erikadeolima/file_converter.git
cd file_converter
```

Crie e ative um ambiente virtual:

```sh
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências:

```sh
pip install -r requirements.txt
```

## Uso

O script principal é o `converter.py`. Ele converte um arquivo `.mov` localizado na pasta padrão `/Users/erikalima/Movies` para `.gif` ou `.mp4`.

### Sintaxe

```sh
python converter.py NOME_DO_ARQUIVO_SEM_EXTENSAO [--output-format {gif,mp4}] [--films-path CAMINHO]
```

- `NOME_DO_ARQUIVO_SEM_EXTENSAO`: Nome do arquivo MOV (sem a extensão `.mov`).
- `--output-format` ou `-o`: Formato de saída desejado (`gif` ou `mp4`). Se não for informado, será solicitado interativamente.
- `--films-path`: Caminho para a pasta onde está o arquivo MOV. O padrão é `/Users/erikalima/Movies`.

### Exemplos

**Executando e escolhendo o formato interativamente:**

```sh
python converter.py teste
Escolha o formato de saída (gif/mp4): mp4
```

**Executando já informando o formato:**

```sh
python converter.py teste --output-format mp4
```

**Alterando o caminho da pasta de vídeos:**

```sh
python converter.py teste --output-format gif --films-path /caminho/para/sua/pasta
```

O arquivo convertido será salvo na mesma pasta do arquivo original.

## Observações

- O nome do arquivo deve ser passado **sem a extensão**.
- O script remove arquivos temporários gerados durante a conversão.
- Certifique-se de que o arquivo `.mov` existe no caminho especificado.

## Erros comuns

- Se aparecer `ModuleNotFoundError: No module named 'moviepy'`, verifique se o ambiente virtual está ativado e se as dependências foram instaladas corretamente.
- Se aparecer erro de permissão, execute o terminal com permissões adequadas ou ajuste as permissões da pasta de vídeos.

---

Qualquer dúvida, abra uma issue no repositório!
