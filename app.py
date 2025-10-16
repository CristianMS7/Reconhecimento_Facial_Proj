import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import threading


from autenticacao import Autenticacao
from reconhecimento import Reconhecimento

class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        
      
        self.autenticacao = Autenticacao()
        self.reconhecimento = Reconhecimento()
        
        self.video = cv2.VideoCapture(0)
        self.recognition_active = False

       
        self._setup_ui()
        
       
        self.update()
        
        
        self.window.protocol("WM_DELETE_WINDOW", self._on_closing)
        
       
        self.window.mainloop()

    def _setup_ui(self):
        """Cria e organiza os widgets da interface."""
        input_frame = tk.Frame(self.window)
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Seu Nome:").pack(side=tk.LEFT, padx=5)
        self.entry_nome = tk.Entry(input_frame, width=20)
        self.entry_nome.pack(side=tk.LEFT)
        
        tk.Label(input_frame, text="Nível de Acesso:").pack(side=tk.LEFT, padx=5)
        self.entry_nivel = tk.Entry(input_frame, width=5)
        self.entry_nivel.pack(side=tk.LEFT)

        self.canvas = tk.Canvas(self.window, width=self.video.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()
        
        self.lbl_status = tk.Label(self.window, text="Aguardando verificação...", font=("Helvetica", 16))
        self.lbl_status.pack(pady=10)
        
        self.btn_start = tk.Button(self.window, text="Verificar Acesso", width=50, command=self.start_verification)
        self.btn_start.pack(pady=10)

    def start_verification(self):
        """Inicia o processo de verificação em uma nova thread."""
        if self.recognition_active:
            return

        nome_digitado = self.entry_nome.get()
        nivel_texto = self.entry_nivel.get()

        if not nome_digitado or not nivel_texto:
            messagebox.showerror("Erro", "Por favor, preencha o nome e o nível.")
            return

        try:
            self.nivel_desejado = int(nivel_texto)
        except ValueError:
            messagebox.showerror("Erro", "O nível de acesso deve ser um número.")
            return

        self.recognition_active = True
        self.lbl_status.config(text="Reconhecendo rosto...")
        
        thread = threading.Thread(target=self.run_recognition_logic, args=(nome_digitado,))
        thread.daemon = True
        thread.start()

    def run_recognition_logic(self, nome_digitado):
        """Executa a lógica de reconhecimento e autenticação."""
        ret, frame = self.video.read()
        if not ret:
            self.recognition_active = False
            self.lbl_status.config(text="Erro ao capturar imagem da câmera.")
            return

        nome_reconhecido = self.reconhecimento.reconhecer(frame)
        
       
        if nome_reconhecido.lower() != nome_digitado.strip().lower():
            status = f"Acesso Negado: O rosto não corresponde a '{nome_digitado}'."
        else:
            status = self.autenticacao.autenticar(nome_reconhecido, self.nivel_desejado)
        
        self.lbl_status.config(text=status)
        self.recognition_active = False
    
    def update(self):
        """Atualiza o frame do vídeo na tela."""
        ret, frame = self.video.read()
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        
        self.window.after(15, self.update)

    def _on_closing(self):
        """Libera a câmera e fecha a aplicação."""
        print("Fechando aplicação...")
        if self.video.isOpened():
            self.video.release()
        self.window.destroy()

if __name__ == "__main__":
    root = tk.Tk()  
    App(root, "Sistema de Autenticação Modular") 

