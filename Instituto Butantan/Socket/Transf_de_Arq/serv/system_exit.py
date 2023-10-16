import tkinter as tk


class SistemaOutput:
    def __init__(self, root):
        self.root = root
        self.root.title("Saídas do Sistema")

        self.caixa_texto = tk.Text(self.root, height=15, width=50)
        self.caixa_texto.pack(padx=20, pady=20)

        self.botao_limpar = tk.Button(self.root, text="Limpar", command=self.limpar_caixa)
        self.botao_limpar.pack()

        # Redireciona a saída padrão para a caixa de texto
        self.orig_stdout = sys.stdout
        sys.stdout = self

    def __del__(self):
        # Restaura a saída padrão ao encerrar
        sys.stdout = self.orig_stdout

    def write(self, mensagem):
        self.caixa_texto.insert(tk.END, mensagem)
        self.caixa_texto.see(tk.END)  # Role a caixa de texto para o final

    def limpar_caixa(self):
        self.caixa_texto.delete("1.0", tk.END)

if __name__ == "__main__":
    import sys

    janela = tk.Tk()
    sistema_output = SistemaOutput(janela)
    janela.mainloop()