# YouTube Video Downloader

Este é um aplicativo GUI em Python que permite baixar vídeos do YouTube ou apenas o áudio no formato MP3. O aplicativo utiliza `tkinter` para a interface gráfica, `pytubefix` para baixar o conteúdo do YouTube e `pydub` para converter o áudio de `m4a` para `mp3`. 

## Pré-requisitos

1. **Python** (versão 3.6+)
2. **pytubefix** para baixar vídeos do YouTube
3. **pydub** para converter áudio para MP3
4. **ffmpeg** (necessário para o `pydub` realizar a conversão)

### Instalando as Dependências

1. **Instalar as bibliotecas Python necessárias**:
   ```bash
   pip install pytubefix pydub
   ```

2. **Instalar o ffmpeg**:
   - **Windows**: Baixe o executável [aqui](https://ffmpeg.org/download.html) e adicione-o ao PATH.
   - **macOS**: Instale com `brew install ffmpeg`.
   - **Linux**: Instale com `sudo apt install ffmpeg`.

## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/DerekWillyan/Youtube-Video-Downloader.git
   ```
   
2. Navegue até o diretório do projeto:
   ```bash
   cd Youtube-Video-Downloader
   ```
   
3. Execute o script:
   ```bash
   python downloader_gui.py
   ```

## Funcionalidades

- **Baixar Vídeo**: Insira a URL de um vídeo do YouTube e baixe o vídeo na melhor resolução disponível.
- **Baixar Apenas Áudio (MP3)**: Marque a opção "Baixar apenas o áudio" para baixar e converter o áudio para o formato MP3 automaticamente.
- **Seleção de Diretório**: Escolha a pasta de destino para salvar o arquivo baixado.
- **Barra de Progresso**: Acompanhe o progresso do download em tempo real.

## Interface

A interface consiste em:
- Campo de URL para inserir o link do YouTube.
- Botão para selecionar o diretório de destino.
- Caixa de seleção para baixar apenas o áudio.
- Barra de progresso do download.
- Mensagem de status indicando o progresso ou conclusão do download.

## Exemplo de Uso

1. Insira a URL do vídeo do YouTube.
2. Escolha o diretório de destino onde o arquivo será salvo.
3. Marque a opção "Baixar apenas o áudio" se quiser o áudio no formato MP3.
4. Clique em "Baixar". Aguarde até que o download seja concluído.

## Problemas Comuns

- **Erro 400**: Verifique se a URL do vídeo é válida.
- **Erro de dependência de `ffmpeg`**: Confirme que o `ffmpeg` está instalado e configurado no PATH do sistema.

## Tecnologias Utilizadas

- **Python** (tkinter, pytubefix, pydub)
- **ffmpeg** para conversão de áudio

---

### Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto.
2. Crie uma nova branch (`git checkout -b feature/MinhaNovaFuncionalidade`).
3. Commit suas alterações (`git commit -m 'Adiciona Minha Nova Funcionalidade'`).
4. Envie para a branch (`git push origin feature/MinhaNovaFuncionalidade`).
5. Abra um Pull Request.

---

### Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---

### Autor

Criado por [Derek Willyan](https://github.com/DerekWillyan/)
