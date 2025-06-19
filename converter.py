#!/usr/bin/env python3
import os
import sys
import argparse
from moviepy.editor import VideoFileClip

class VideoConverterError(Exception):
    pass

class VideoValidationError(VideoConverterError):
    pass

class VideoConverter:
    def __init__(self, input_name, output_format, films_path="/Users/erikalima/Movies"):
        self.input_name = input_name
        self.output_format = output_format.lower()
        self.films_path = films_path
        self.full_file_path = os.path.join(self.films_path, f"{self.input_name}.mov")
        self.output_path = os.path.splitext(self.full_file_path)[0] + f".{self.output_format}"

    def validar_arquivo(self):
        if not os.path.exists(self.full_file_path):
            raise VideoValidationError(f"O arquivo '{self.full_file_path}' não existe.")
        _, ext = os.path.splitext(self.full_file_path)
        if ext.lower() != '.mov':
            raise VideoValidationError(f"O arquivo deve ser do formato MOV, não '{ext}'.")

    def converter(self):
        self.validar_arquivo()
        try:
            print(f"Carregando o vídeo: {self.input_name}")
            video_clip = VideoFileClip(self.full_file_path)
            print(f"Convertendo para {self.output_format.upper()}...")
            if self.output_format == 'gif':
                video_clip.write_gif(self.output_path, fps=15)
            elif self.output_format == 'mp4':
                video_clip.write_videofile(
                    self.output_path,
                    codec='libx264',
                    audio=True,
                    audio_codec='aac',
                    temp_audiofile=os.path.join(os.path.dirname(self.output_path), f"{self.input_name}_temp_audio.m4a"),
                    remove_temp=True
                )
            else:
                raise VideoValidationError(f"Formato de saída '{self.output_format}' não suportado. Use 'gif' ou 'mp4'.")
            print(f"Conversão concluída! Arquivo salvo em: {self.output_path}")
        except Exception as e:
            raise VideoConverterError(f"Erro durante a conversão: {str(e)}")
        finally:
            if 'video_clip' in locals():
                video_clip.close()
            self.limpar_temporarios()

    def limpar_temporarios(self):
        temp_files = []
        dir_path = os.path.dirname(self.full_file_path)
        for filename in os.listdir(dir_path):
            if filename.startswith(self.input_name) and ('_temp_' in filename or 'TEMP_MPY' in filename):
                temp_files.append(os.path.join(dir_path, filename))
        current_dir = os.getcwd()
        if current_dir != dir_path:
            for filename in os.listdir(current_dir):
                if filename.startswith(self.input_name) and ('_temp_' in filename or 'TEMP_MPY' in filename):
                    temp_files.append(os.path.join(current_dir, filename))
        for temp_file in temp_files:
            try:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
                    print(f"Arquivo temporário removido: {temp_file}")
            except Exception as e:
                print(f"Não foi possível remover o arquivo temporário {temp_file}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Conversor de arquivos MOV para GIF ou MP4')
    parser.add_argument('name_file_to_convert', help='Nome do arquivo MOV de entrada (sem extensão)')
    parser.add_argument('--output-format', '-o', choices=['gif', 'mp4'], help='Formato de saída (gif ou mp4)')
    parser.add_argument('--films-path', default="/Users/erikalima/Movies", help='Caminho para a pasta dos vídeos')
    args = parser.parse_args()

    output_format = args.output_format
    if not output_format:
        while True:
            output_format = input("Escolha o formato de saída (gif/mp4): ").lower()
            if output_format in ['gif', 'mp4']:
                break
            print("Formato inválido. Por favor, escolha 'gif' ou 'mp4'.")

    try:
        converter = VideoConverter(args.name_file_to_convert, output_format, args.films_path)
        converter.converter()
    except VideoValidationError as ve:
        print(f"Erro de validação: {ve}")
    except VideoConverterError as ce:
        print(f"Erro de conversão: {ce}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
