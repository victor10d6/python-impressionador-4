# criar o hashzap

# titulo: hashzap
# botão: iniciar chat
    # quando eu clicar no botão:
    # janela / dialog / modal / popup
        # titulo: bem vindo ao hashzap
        # CAMPO DE TEXTO: ESCREVA SEU NOME NO CHAT
        # BOTÃO : entrar no chat
            # clicou no botão:
            # fechar o dialog
                # criar o chat
                # criar o campo de mensagem : digite sua mensagemn
                # botão: eviar
                    # quando clicar no botão:
                    # enviar mensagem par ao chat

# importar o flet
import flet as ft 

# criar a função principao do seu app
def main(pagina):
    # criar os elementos
    titulo = ft.Text("Hashzap")

    titulo_janela = ft.Text("bem-vindo ao hashzap")
    campo_nome = ft.TextField(label="digite o seu nome", on_submit=entrar_chat)
    
    campo_mensagem = ft.TextField(label="escreva sua mensagem", on_submit=enviar_mensagem)
    
    def enviar_mensagem_tunel(mensagem):
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()

    # webscoket -> tunel de comunicação
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        mensagem = ft.Text(f"{campo_nome.value}: {campo_mensagem.value}")
        # enviar a mensagem no tunel
        pagina.pubsub.send_all(mensagem )
        campo_mensagem.value = ""
        pagina.update()
    
    botao_enviar = ft.ElevatedButton("enviar", on_click = enviar_mensagem)
    chat = ft.Column()
    linha_mensagem = ft.Row([campo_mensagem,botao_enviar])

    def entrar_chat(evento):
        pagina.pubsu.send_all(f"{campo_nome.value} entrou no chat")
        print("entrou no chat")
        # fechar a janela / dialog
        janela.open = False
        # tirar o titulo
        pagina.remove(titulo)
        # tirar o botão iniciar
        pagina.remove(botao_iniciar)

        
        # criar o chat
        # criar o campo digite sua mensagem
        # criar o botão enviar
        pagina.add(linha_mensagem)
        
        

        pagina.update()


    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click = entrar_chat )
   
    janela = ft.AlertDialog(
        title = titulo_janela,
        content = campo_nome,
        actions = [botao_entrar]        
    )

    def abrir_dialog(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()


    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_dialog)

    # colocar os elementos na pagina
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# rodar o seu app
ft.app(main, view= ft.WEB_BROWSER)

# sempre que você clica em qualquer botão -> flet ele cria um evento