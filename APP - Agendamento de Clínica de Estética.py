import PySimpleGUI as sg

sg.theme('LightBrown1') #Tema de cor

# --- Layout do elemento Frame --- #
frame_layout = [
    [sg.Text("Nome do Cliente:")],
    [sg.InputText(key='-NOME-', do_not_clear=False)],
    
    [sg.Text("Horário:")],
    [sg.Spin([i for i in range(8,18)], initial_value="", s=(5,0), key='-HORA-'), sg.Text('horas'), sg.Push(), sg.Text('OBS: funcionamos de 8h às 17h.', text_color='red')],
    
    [sg.Text("Tipo de Procedimento:")],
    [sg.Combo(["", "Botox (Toxina Botulínica)", "Carboxiterapia", "Jet Skin", "Lipo de Papada", "Microagulhamento", "Preenchimento Facial", "Preenchimento Labial", "Skinbooster", "Outros Corporais"], key='-PROC-')],
    
    [sg.Text("Funcionário Responsável:")],
    [sg.InputText(key='-FUNC-', do_not_clear=False)]
]

# --- Layout da janela principal --- #
layout = [
    [sg.Titlebar("Estetic Soft", font='Calibri', text_color='white')],
    [sg.MenubarCustom([['Institucional', ['Sobre nós']], ['Help', ['Sobre', 'Sair',]]], p=0)],
    
    [sg.Image(sg.EMOJI_BASE64_HAPPY_THUMBS_UP, s=(50,50)), sg.Text("Bem-vindo(a) a Estetic Soft!", font='Any 12 bold', text_color='black', p=(0,10), justification='c', expand_x=True)],
    [sg.Text("Escolha seu melhor horário e faça seu agendamento conosco.", font='Calibri 10 bold', text_color='black', justification='c', expand_x=True)],

    [sg.HorizontalSeparator()],

    [sg.Push(), sg.Frame("Agendamento", frame_layout, font='Calibri 12', title_color='black', p=(10,10)), sg.Push()],

    [sg.HorizontalSeparator()],

    [sg.Text("Deseja criar, consultar ou excluir seu agendamento?", text_color='black')],

    [sg.Button("SALVAR"), sg.Button("CONSULTAR"), sg.Button("EXCLUIR"), sg.Push(), sg.Button("Sair")],
]

# --- Janela principal --- #
janela = sg.Window("Estetic Soft", layout, enable_close_attempted_event=True)

# --- Loop para processar "eventos" e obter os "valores" das entradas --- #
while True:
    evento, valores = janela.read()
 # type: ignore
    if (evento == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or evento == "Sair") and sg.popup_yes_no("Deseja realmente fechar a janela?", title='Fechar') == "Yes":
        break

    elif evento == 'Sobre nós': #Menu 'Sobre nós' da barra de menu 'Institucional'
        frame_layout2 = [
            [sg.Text("Bem-vindo(a) a Estetic Soft, sua melhor Clínica de Estética!")],
            [sg.Text("Há XX anos somos referência no mercado de estética do RN\ne oferecemos um serviço completo, com atendimento plane-\njado em Harmonização Facial ou Estética Corporal. Nossos\nprocedimentos são feitos com os melhores produtos.")],
            [sg.Text("Venha sentir-se ainda mais lindo(a) e levantar a autoestima ;)")],
            [sg.Text("\nFuncionamento:", font='Arial 11 bold'), sg.Text("\nDe segunda à sábado das 8h às 17h.", text_color='green')],
            [sg.Text("E-mail:", font='Arial 11 bold'), sg.Text("contato@esteticsoft.com.br", text_color='green')]
            ]

        frame2_layout2 = [
            [sg.Text("Av. da Miss Universo, s/n - Praia Nova, Natal - RN, 59001-010")]
            ]

        layout2 = [
            [sg.Text("ESTETIC SOFT", font='Any 14 italic bold', justification='c', expand_x=True)],
            [sg.Push(), sg.Text("Version: 3.0", font='Calibri 11')],
            [sg.Push(), sg.Frame("Quem Somos", frame_layout2, font='Calibri 12 bold', title_color='black', p=(0,10)), sg.Push()],
            [sg.Push(), sg.Frame("Endereço:", frame2_layout2, font='Calibri 12 bold', title_color='black', p=(0,10)), sg.Push()]
            ]
        
        jan2 = sg.Window("Sobre nós", layout2)
        
        while True:
            evento, valores = jan2.read()
            
            if evento == sg.WIN_CLOSED:
                break
            
        jan2.close()
        
    elif evento == 'Sobre':     #Menu 'Sobre' da barra de menu 'Help'
        sg.popup_no_buttons(" ===== EQUIPE RESPONSÁVEL ===== ",
                "Ikaro Franklin Silva de Medeiros\nJairo Muniz da Cruz\nJhony Ewerton Belarmino da Silva\nJoão Pedro Gomes Tindo de Andrade\nJoão Thiago Crisanto Ferreira dos Santos\nJoanne Angel (João Vitor de Carvalho)\nJulya Emanuelle Oliveira Costa\nKalyl Victor dos Santos Alves\n",
                "           2022 © Estetic Soft LTDA.\n Desenvolvido com ❤ no PySimpleGUI™", title='Sobre')
    
    elif evento == "SALVAR":    #Botão SALVAR
        cliente = {"nome":"", "horario":0, "tipo-proced":"", "func":""}
        cliente["nome"] = valores['-NOME-']
        cliente["horario"] = valores['-HORA-']
        cliente["tipo-proced"] = valores['-PROC-']
        cliente["func"] = valores['-FUNC-']
        sg.popup("Agendamento feito com sucesso!", title='Estetic Soft', auto_close = True, auto_close_duration=5)

    elif evento == "CONSULTAR": #Botão CONSULTAR
        sg.Popup(" ******** SEU AGENDAMENTO ******** \n", f"Nome: {cliente['nome']}", f"Horário: {cliente['horario']}h", f"Procedimento: {cliente['tipo-proced']}", f"Funcionário: {cliente['func']}\n", title='Estetic Soft')

    elif evento == "EXCLUIR":   #Botão EXCLUIR
        cliente["nome"] = ""
        cliente["horario"] = 0
        cliente["tipo-proced"] = ""
        cliente["func"] = ""
        sg.popup("Seu cadastro foi excluído!", title='Estetic Soft', auto_close = True, auto_close_duration=5)

janela.close()
