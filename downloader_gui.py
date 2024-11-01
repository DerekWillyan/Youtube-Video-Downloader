import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pytubefix import YouTube

def selecionar_caminho():
    caminho = filedialog.askdirectory()
    if caminho:
        caminho_entry.delete(0, tk.END)
        caminho_entry.insert(0, caminho)

def baixar():
    url = url_entry.get()
    caminho = caminho_entry.get()
    audio_apenas = audio_var.get()

    if not url or url == "Digite a URL do vídeo":
        messagebox.showerror("Erro", "Por favor, insira uma URL válida.")
        return

    try:
        yt = YouTube(url)
        yt.register_on_progress_callback(atualizar_progresso)
        stream = yt.streams.filter(only_audio=True).first() if audio_apenas else yt.streams.get_highest_resolution()

        status_label.config(text="Baixando... Aguarde.")
        stream.download(output_path=caminho)
        status_label.config(text="Download concluído!")
        messagebox.showinfo("Sucesso", f"'{yt.title}' foi baixado com sucesso!")
        progress_bar['value'] = 0  # Reset da barra de progresso

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def atualizar_progresso(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentual = int((bytes_downloaded / total_size) * 100)
    progress_bar['value'] = percentual
    janela.update_idletasks()

# Funções para placeholders
def add_placeholder(entry, placeholder_text):
    entry.insert(0, placeholder_text)
    entry.config(fg="grey")

    def on_focus_in(event):
        if entry.get() == placeholder_text:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder_text)
            entry.config(fg="grey")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

# Configuração da janela principal
janela = tk.Tk()
janela.title("Baixar Vídeo do YouTube")
janela.geometry("450x200")
janela.resizable(False, False)

# Widgets da interface
url_entry = tk.Entry(janela, width=53)
url_entry.pack(pady=5, padx=5)
add_placeholder(url_entry, "Digite a URL do vídeo")

caminho_frame = tk.Frame(janela)
caminho_frame.pack(pady=5, padx=5)

caminho_entry = tk.Entry(caminho_frame, width=40)
caminho_entry.pack(side=tk.LEFT, padx=5)
caminho_button = tk.Button(caminho_frame, text="Selecionar", command=selecionar_caminho, 
                           fg="#ff0404",
                           activeforeground="#c50505",
                           font=("Helvetica", 10, "bold"))
caminho_button.pack(side=tk.LEFT, padx=5)
add_placeholder(caminho_entry, "Selecione o caminho")

audio_var = tk.BooleanVar()
audio_check = tk.Checkbutton(janela, text="Baixar apenas o áudio", variable=audio_var)
audio_check.pack(pady=5, padx=5)

# Barra de progresso
progress_bar = ttk.Progressbar(janela, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)

# Botão de download com hover
baixar_button = tk.Button(janela, text="Baixar", command=baixar, 
                          bg="#ff0404",         # Cor de fundo
                          fg="white",           # Cor do texto
                          activebackground="#c50505",  # Cor de fundo ao clicar
                          activeforeground="white", font=("Helvetica", 10, "bold"))    # Cor do texto ao clicar
baixar_button.pack(pady=5, padx=5)

status_label = tk.Label(janela, text="")
status_label.pack(pady=5, padx=5)

# Inicia a aplicação
janela.mainloop()
