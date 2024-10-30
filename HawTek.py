import customtkinter as ctk
import json
from PIL import Image
import os

# Nome do arquivo de configuração
config_file = "config.json"

# Função para carregar as configurações do arquivo JSON
def load_config():
    if os.path.exists(config_file):
        with open(config_file, "r") as file:
            return json.load(file)
    return {"color": "blue"}  # Cor padrão

# Função para salvar as configurações no arquivo JSON
def save_config(color):
    config = {
        "color": color
    }
    with open(config_file, "w") as file:
        json.dump(config, file)

# Função para atualizar as cores
def update_color(choice):
    output.configure(border_color=("dark", choice)) 
    output.configure(state="normal") 
    output.insert("end", f"Mudou a cor para: {choice}\n") 
    output.configure(state="disabled")  
    title.configure(text_color=("dark", choice))
    title2.configure(text_color=("dark", choice))
    title3.configure(text_color=("dark", choice))
    title4.configure(text_color=("dark", choice))
    title5.configure(text_color=("dark", choice))
    title6.configure(text_color=("dark", choice))
    text.configure(text_color=("dark", choice))  
    by.configure(text_color=("dark", choice))    
    themes.configure(fg_color=choice)  
    check_button.configure(border_color=("dark", choice))  
    check_button1.configure(border_color=("dark", choice))  
    check_button2.configure(border_color=("dark", choice))  
    check_button3.configure(border_color=("dark", choice))  
    check_button4.configure(border_color=("dark", choice))    
    run.configure(border_color=("dark", choice))  
    github.configure(border_color=("dark", choice))  
    save_config(choice)  # Salva a cor selecionada

def check_checkbox():
    if otim1.get():
        output.configure(state="normal")
        output.insert("end", "Checkbox está marcada.\n")
        output.configure(state="disabled")
    else:
        output.configure(state="normal")
        output.insert("end", "Checkbox está desmarcada.\n")
        output.configure(state="disabled")
    save_config(themes.get(), otim1.get())

def check_checkbox2():
    if otim2.get():
        output.configure(state="normal")
        output.insert("end", "Checkbox está marcada.\n")
        output.configure(state="disabled")
    else:
        output.configure(state="normal")
        output.insert("end", "Checkbox está desmarcada.\n")
        output.configure(state="disabled")
    save_config(themes.get(), otim2.get())

def check_checkbox3():
    if otim3.get():
        output.configure(state="normal")
        output.insert("end", "Checkbox está marcada.\n")
        output.configure(state="disabled")
    else:
        output.configure(state="normal")
        output.insert("end", "Checkbox está desmarcada.\n")
        output.configure(state="disabled")
    save_config(themes.get(), otim3.get())

def check_checkbox4():
    if otim4.get():
        output.configure(state="normal")
        output.insert("end", "Checkbox está marcada.\n")
        output.configure(state="disabled")
    else:
        output.configure(state="normal")
        output.insert("end", "Checkbox está desmarcada.\n")
        output.configure(state="disabled")
    save_config(themes.get(), otim4.get())

def check_checkbox5():
    if otim5.get():
        output.configure(state="normal")
        output.insert("end", "Checkbox está marcada.\n")
        output.configure(state="disabled")
    else:
        output.configure(state="normal")
        output.insert("end", "Checkbox está desmarcada.\n")
        output.configure(state="disabled")
    save_config(themes.get(), otim5.get())

def runcode():
    if otim1.get():
        #temp
        output.configure(state="normal")
        output.insert("end", "Arquivos temporários limpos!\n")
        output.configure(state="disabled")
        os.system(rf"cache.bat")
    if otim2.get():
        #transparencia
        output.configure(state="normal")
        output.insert("end", "Transparencia desativada!\n")
        output.configure(state="disabled")
        os.system(rf"trans.bat")
    if otim3.get():
        #processo
        output.configure(state="normal")
        output.insert("end", "Processos otimizados!\n")
        output.configure(state="disabled")
        os.system(rf"process.reg")
    if otim4.get():
        #prefetch
        output.configure(state="normal")
        output.insert("end", "Prefetch desativado!\n")
        output.configure(state="disabled")
        os.system(rf"pref.bat")
    if otim5.get():
        #cpu
        output.configure(state="normal")
        output.insert("end", "Cpu limpa e otimizada!\n")
        output.configure(state="disabled")
        os.system(rf"cpu.bat")
    output.configure(state="normal")
    output.insert("end", "Obrigado por usar nossos serviços de otimização!!!\n")
    output.configure(state="disabled")
def githube():
    os.system(rf"git.bat")

# Configuração da janela principal
root = ctk.CTk()
root.title("HawTek")
root.geometry("850x480")
root.resizable(False, False)

# Variáveis para checkboxes (exemplo, não são usadas neste código)
otim1 = ctk.BooleanVar()
otim2 = ctk.BooleanVar()
otim3 = ctk.BooleanVar()
otim4 = ctk.BooleanVar()
otim5 = ctk.BooleanVar()

# Frame para organizar os widgets
frame = ctk.CTkFrame(master=root, border_width=2, width=200, height=480)
frame.pack()
frame.place(x=0, y=0)

frame2 = ctk.CTkFrame(master=root, border_width=2, width=250, height=480)
frame2.pack()
frame2.place(x=600, y=0)

# Carregar a imagem para o botão
image_path = "git.jpg"  # Substitua pelo caminho da sua imagem
button_image = Image.open(image_path)

button_image = button_image.resize((200, 200), Image.LANCZOS)

# Converter a imagem para CTkImage
button_image = ctk.CTkImage(light_image=button_image, dark_image=button_image)

# Botão "Meu GitHub" com a imagem
github = ctk.CTkButton(
    master=root,
    image=button_image,
    text="Meu github",  # Remover texto para que a imagem cubra todo o botão
    width=200,
    height=200,
    command=githube,
    border_color=("dark", "blue"),
    border_width=2,
    bg_color="transparent",
    fg_color="transparent"
)
github.pack()
github.place(x=625, y=130)

text = ctk.CTkLabel(master=root, text="Otimizações", width=0, height=0, font=("Arial", 30), bg_color="transparent", text_color=("dark", "blue"))
text.pack()
text.place(x=230, y=210)

run = ctk.CTkButton(master=root, text="Começar", command=runcode, border_color=("dark", "blue"), border_width=2, bg_color="transparent", fg_color="transparent")
run.pack()
run.place(x=430, y=215)

# Checkboxes
check_button = ctk.CTkCheckBox(master=root, text="Limpar arquivos temporários", command=check_checkbox, variable=otim1, border_color=("dark", "blue"), border_width=2)
check_button.pack()
check_button.place(x=230, y=250)

check_button1 = ctk.CTkCheckBox(master=root, text="Desativar transparencia", command=check_checkbox2, variable=otim2, border_color=("dark", "blue"), border_width=2)
check_button1.pack()
check_button1.place(x=230, y=280)

check_button2 = ctk.CTkCheckBox(master=root, text="Otimizar processos", command=check_checkbox3, variable=otim3, border_color=("dark", "blue"), border_width=2)
check_button2.pack()
check_button2.place(x=230, y=310)

check_button3 = ctk.CTkCheckBox(master=root, text="Desativar prefetch", command=check_checkbox4, variable=otim4, border_color=("dark", "blue"), border_width=2)
check_button3.pack()
check_button3.place(x=230, y=340)

check_button4 = ctk.CTkCheckBox(master=root, text="Otimizar CPU", command=check_checkbox5, variable=otim5, border_color=("dark", "blue"), border_width=2)
check_button4.pack()
check_button4.place(x=230, y=370)

# Textbox configurada
output = ctk.CTkTextbox(master=root, width=400, height=200, corner_radius=5, border_color=("dark", "blue"), border_width=2)
output.configure(state="disabled") 
output.pack()
output.place(x=200)

# Título com cor inicial
title = ctk.CTkLabel(master=frame, text="ꃅ", width=0, height=0, font=("Arial", 50), bg_color="transparent", text_color=("dark", "blue"))
title.pack()
title.place(x=80, y=20)

title2 = ctk.CTkLabel(master=frame, text="ꍏ", width=0, height=0, font=("Arial", 50), bg_color="transparent", text_color=("dark", "blue"))
title2.pack()
title2.place(x=80, y=70)

title3 = ctk.CTkLabel(master=frame, text="ꅏ", width=0, height=0, font=("Arial", 50), bg_color="transparent", text_color=("dark", "blue"))
title3.pack()
title3.place(x=80, y=120)

title4 = ctk.CTkLabel(master=frame, text="꓄", width=0, height=0, font=("Arial", 50), bg_color="transparent", text_color=("dark", "blue"))
title4.pack()
title4.place(x=80, y=170)

title5 = ctk.CTkLabel(master=frame, text="ꍟ", width=0, height=0, font=("Arial", 50), bg_color="transparent", text_color=("dark", "blue"))
title5.pack()
title5.place(x=80, y=220)

title6 = ctk.CTkLabel(master=frame, text="ꀘ", width=0, height=0, font=("Arial", 50), bg_color="transparent", text_color=("dark", "blue"))
title6.pack()
title6.place(x=80, y=270)

by = ctk.CTkLabel(master=root, text="by Mxlsc", width=0, height=0, font=("Arial", 20), bg_color="transparent", text_color=("dark", "blue"))
by.pack()
by.place(x=500, y=450)

# Opções de cores
options = ["blue", "green", "red", "yellow", "pink", "purple"]

# Carrega a configuração inicial
config = load_config()
initial_color = config["color"]

# Menu de opções
themes = ctk.CTkOptionMenu(master=frame, values=options, command=update_color)
themes.pack()
themes.place(x=25, y=440)

# Define a cor inicial
themes.set(initial_color)
update_color(initial_color)  # Atualiza a cor com a cor carregada

root.mainloop()