#apps que uso de vez em nunca
awaysroot = tk.Tk()
awaysroot.geometry("800x600")
awaysroot.title("Abridor de aplicativos 2.0")
awaysroot.configure(bg='gray20')
button_style = {
    'bg': 'gray30',
    'fg': 'white',
    'activebackground': 'gray50',
    'activeforeground': 'white',
    'height': 3,
    'width': 20
}
#Titulo
title_text = tk.Text(awaysroot, height=1, bg='gray20', fg='white', font=('Helvetica', 16), bd=0)
title_text.pack(pady=20)
title_text.insert(tk.END, "Clique no app que deseja abrir abaixo:")
title_text.configure(state='disabled')