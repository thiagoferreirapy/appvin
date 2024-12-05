import flet as ft
from components import Message, ChatMessage
from ai import AIBot


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.title = "Flet IA"
    page.window.height = 800
    page.window.width = 400
    ai_bot = AIBot()

    def join_chat_click(e):
        if not join_user_name.value:
            join_user_name.error_text = "Nome é obrigatório!"
            join_user_name.update()
        else:
            page.session.set("user_name", join_user_name.value)
            page.dialog.open = False
            new_message.prefix = ft.Text(f"{join_user_name.value}: ")
            page.update()

    def add_message_on_history(message: Message):
        chat_message = ChatMessage(message)
        chat.controls.append(chat_message)
        history_messages = page.session.get("history_messages")  if page.session.get("history_messages") else []
        history_messages.append(message)
        page.session.set("history_messages", history_messages)
        page.update()

    def send_message_click(e):
        if new_message.value != "":
            user_message = new_message.value
            add_message_on_history(
                Message(
                    user_name = page.session.get("user_name"),
                    text = user_message,
                    user_type = "user",
                )
            )
            new_message.value = ""
            new_message.update()
            ai_response = ai_bot.invoke(
                history_messages = page.session.get("history_messages")  if page.session.get("history_messages") else [],
                user_message = user_message
            )
            add_message_on_history(
                Message(
                    user_name = "Vin",
                    text = ai_response,
                    user_type = "ia",
                )
            )
            new_message.focus()
            new_message.update()

    join_user_name = ft.TextField(
        label = "Informe seu nome para começar",
        autofocus = True,
    )

    page.dialog = ft.AlertDialog(
        open = True,
        modal = True,
        title = ft.Text("Bem-vindo(a)"),
        content = ft.Column([join_user_name], width=300, height=70, tight=True),
        actions = [ft.ElevatedButton(text="Começar", on_click=(join_chat_click))],
        actions_alignment = ft.MainAxisAlignment.END,
    )

    app_bar = ft.AppBar(
        leading = ft.Icon(ft.Icons.ASSISTANT),
        leading_width = 40,
        title = ft.Text("Vin Agent"),
        center_title = True,
        bgcolor = ft.Colors.SURFACE,
    )

    chat = ft.ListView(
        expand = True,
        spacing = 10,
        auto_scroll = True,
    )

    new_message = ft.TextField(
        hint_text = "No que posso ajudar?",
        autofocus = True,
        shift_enter = True,
        min_lines = 1,
        max_lines = 4,
        filled = True,
        expand = True,
        on_submit = send_message_click,
    )

    page.add(
        app_bar, 
        ft.Container(
            content = chat,
            border_radius = 5,
            padding = 10,
            expand =True,
            bgcolor = ft.Colors.SURFACE_CONTAINER_HIGHEST,
        ),
        ft.Row(
            [
                new_message,
                ft.IconButton(
                    icon = ft.Icons.SEND_ROUNDED,
                    tooltip = "Enviar",
                    on_click = send_message_click,
                )
            ]
        )
        
    )

    page.update()

ft.app(main)
