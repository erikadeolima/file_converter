#!/usr/bin/env python3
import os
import sys
import argparse
from moviepy.editor import VideoFileClip

def convert_video(name_file_to_convert, output_format):
    """
    Convert a MOV file to either GIF or MP4 format
    
    Args:
        name_file_to_convert (str): Path to the input MOV file
        output_format (str): Desired output format ('gif' or 'mp4')
    
    Returns:
        str: Path to the output file
    """

    films_path = "/Users/erikalima/Movies"
    file_name = str(name_file_to_convert)
    full_file_path = films_path + "/" + file_name + ".mov"

    if not os.path.exists(full_file_path):
        print(f"Erro: O arquivo '{full_file_path}' não existe.")
        sys.exit(1)
    
    _, ext = os.path.splitext(full_file_path)
    if ext.lower() != '.mov':
        print(f"Erro: O arquivo deve ser do formato MOV, não '{ext}'.")
        sys.exit(1)
    
    output_path = os.path.splitext(full_file_path)[0] + '.' + output_format.lower()
    
    try:
        print(f"Carregando o vídeo: {file_name}")
        video_clip = VideoFileClip(full_file_path)
        
        print(f"Convertendo para {output_format.upper()}...")
        
        if output_format.lower() == 'gif':
            video_clip.write_gif(output_path, fps=15)
        elif output_format.lower() == 'mp4':
            video_clip.write_videofile(
                output_path, 
                codec='libx264', 
                audio=True,
                audio_codec='aac',
                temp_audiofile=os.path.join(os.path.dirname(output_path), f"{file_name}_temp_audio.m4a"),
                remove_temp=True
            )
        else:
            print(f"Erro: Formato de saída '{output_format}' não suportado. Use 'gif' ou 'mp4'.")
            sys.exit(1)
        
        print(f"Conversão concluída! Arquivo salvo em: {output_path}")
        return output_path
    
    except Exception as e:
        print(f"Erro durante a conversão: {str(e)}")
        sys.exit(1)
    finally:
        if 'video_clip' in locals():
            video_clip.close()
            
        temp_files = []
        dir_path = os.path.dirname(full_file_path)
        
        for filename in os.listdir(dir_path):
            if filename.startswith(file_name) and ('_temp_' in filename or 'TEMP_MPY' in filename):
                temp_files.append(os.path.join(dir_path, filename))
                
        current_dir = os.getcwd()
        if current_dir != dir_path:
            for filename in os.listdir(current_dir):
                if filename.startswith(file_name) and ('_temp_' in filename or 'TEMP_MPY' in filename):
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
    parser.add_argument('name_file_to_convert', help='Caminho para o arquivo MOV de entrada')
    parser.add_argument('--output-format', '-o', choices=['gif', 'mp4'], 
                        help='Formato de saída (gif ou mp4)')
    
    args = parser.parse_args()
    
    output_format = args.output_format
    if not output_format:
        while True:
            output_format = input("Escolha o formato de saída (gif/mp4): ").lower()
            if output_format in ['gif', 'mp4']:
                break
            print("Formato inválido. Por favor, escolha 'gif' ou 'mp4'.")
    
    convert_video(args.name_file_to_convert, output_format)

if __name__ == "__main__":
    main()
