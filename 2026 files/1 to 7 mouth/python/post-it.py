import tkinter as tk
from tkinter import font
import json
import os
from pathlib import Path

class PostIt:
    def __init__(self, root):
        self.root = root
        self.root.title("Post-it")
        self.root.geometry("350x400")
        self.root.resizable(True, True)
        
        # Configurar para sempre ficar no topo
        self.root.attributes('-topmost', True)
        
        # Cor de fundo estilo post-it amarelo
        self.bg_color = "#FFEB3B"
        self.root.configure(bg=self.bg_color)
        
        # Arquivo para salvar notas
        self.notes_file = Path.home() / ".post_it_notes.json"
        
        # Fonte customizada
        self.text_font = font.Font(family="Arial", size=11)
        
        # Frame superior com botões
        self.top_frame = tk.Frame(self.root, bg=self.bg_color)
        self.top_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        
        # Botão salvar
        self.save_btn = tk.Button(
            self.top_frame,
            text="💾 Salvar",
            command=self.save_notes,
            bg="#4CAF50",
            fg="white",
            padx=10,
            pady=2,
            font=("Arial", 9, "bold")
        )
        self.save_btn.pack(side=tk.LEFT, padx=2)
        
        # Botão limpar
        self.clear_btn = tk.Button(
            self.top_frame,
            text="🗑️ Limpar",
            command=self.clear_notes,
            bg="#f44336",
            fg="white",
            padx=10,
            pady=2,
            font=("Arial", 9, "bold")
        )
        self.clear_btn.pack(side=tk.LEFT, padx=2)
        
        # Botão minimizar
        self.minimize_btn = tk.Button(
            self.top_frame,
            text="−",
            command=self.minimize_window,
            bg="#2196F3",
            fg="white",
            padx=8,
            pady=2,
            font=("Arial", 9, "bold")
        )
        self.minimize_btn.pack(side=tk.RIGHT, padx=2)
        
        # Botão fechar
        self.close_btn = tk.Button(
            self.top_frame,
            text="✕",
            command=self.close_window,
            bg="#999999",
            fg="white",
            padx=8,
            pady=2,
            font=("Arial", 9, "bold")
        )
        self.close_btn.pack(side=tk.RIGHT, padx=2)
        
        # Caixa de texto principal
        self.text_area = tk.Text(
            self.root,
            font=self.text_font,
            bg="white",
            fg="black",
            relief=tk.FLAT,
            wrap=tk.WORD,
            padx=10,
            pady=10
        )
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Carregar notas salvas
        self.load_notes()
        
        # Configurar close button da janela
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)
        
        # Auto-salvar a cada 30 segundos
        self.auto_save()
    
    def save_notes(self):
        """Salva as notas em um arquivo JSON"""
        notes = self.text_area.get("1.0", tk.END)
        try:
            with open(self.notes_file, 'w', encoding='utf-8') as f:
                json.dump({"notes": notes}, f, ensure_ascii=False, indent=2)
            self.show_status("✓ Salvo com sucesso!")
        except Exception as e:
            self.show_status(f"❌ Erro ao salvar: {e}")
    
    def load_notes(self):
        """Carrega as notas salvas"""
        try:
            if self.notes_file.exists():
                with open(self.notes_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.text_area.insert("1.0", data.get("notes", ""))
        except Exception as e:
            print(f"Erro ao carregar notas: {e}")
    
    def clear_notes(self):
        """Limpa todas as notas"""
        self.text_area.delete("1.0", tk.END)
        self.show_status("🗑️ Notas limpas!")
    
    def show_status(self, message):
        """Mostra mensagem de status temporária"""
        original_bg = self.root.cget('bg')
        self.root.configure(bg="#FFF59D")
        self.root.after(500, lambda: self.root.configure(bg=original_bg))
    
    def minimize_window(self):
        """Minimiza a janela"""
        self.save_notes()
        self.root.iconify()
    
    def close_window(self):
        """Fecha a janela"""
        self.save_notes()
        self.root.destroy()
    
    def auto_save(self):
        """Auto-salva as notas a cada 30 segundos"""
        self.save_notes()
        self.root.after(30000, self.auto_save)


def main():
    root = tk.Tk()
    app = PostIt(root)
    root.mainloop()


if __name__ == "__main__":
    main()
