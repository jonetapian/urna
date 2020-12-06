from views.Menu_view import Menu_view

menu_view = Menu_view()
while True:
    opcao = menu_view.tela_opcoes()
    if opcao == "SAIR":
        break


