import flet as ft


class SampleForm:
    def __init__(self, page: ft.Page) -> None:
        # ページの基本情報設定
        self.page = page
        self.page.title = "サンプルフォームアプリケーション"
        self.page.vertical_alignment = "left"

        # 入力用UI作成
        self.ui_name = ft.TextField(label="名前", icon=ft.icons.EDIT_NOTE)
        self.ui_mailaddress = ft.TextField(
            label="メールアドレス", icon=ft.icons.MAIL_OUTLINE
        )
        self.ui_inquiry = ft.TextField(
            label="お問い合わせ内容",
            icon=ft.icons.QUESTION_MARK,
            multiline=True,
            min_lines=1,
            max_lines=7,
        )

        # ボタン系UI作成
        self.ui_button_clear = ft.ElevatedButton(
            text="クリア", width=200, on_click=self.__onclick_clear
        )
        self.ui_button_send = ft.ElevatedButton(
            text="送信", width=200, on_click=self.__onclick_send
        )

        # ダイアログ作成
        self.ui_dialog = ft.AlertDialog(actions_alignment="left")

        # ページにUIを載せる
        self.page.add(
            self.ui_name,
            self.ui_mailaddress,
            self.ui_inquiry,
            ft.Row([self.ui_button_clear, self.ui_button_send]),
        )

        # ページの表示内容更新
        self.page.update()

    def __onclick_clear(self, e: ft.ControlEvent):
        """クリアボタン押下時処理

        Args:
            e (ft.ControlEvent): イベント
        """

        self.ui_name.value = ""
        self.ui_mailaddress.value = ""
        self.ui_inquiry.value = ""

        # ページの表示内容更新
        self.page.update()

    def __onclick_send(self, e: ft.ControlEvent):
        """送信ボタン押下時処理

        Args:
            e (ft.ControlEvent): イベント
        """

        txt = "送信しました。\n\n名前：{0}\nメールアドレス：{1}\nお問い合わせ内容：{2}\n"
        txt = txt.format(
            self.ui_name.value,
            self.ui_mailaddress.value,
            self.ui_inquiry.value,
        )
        self.ui_dialog.title = ft.Text(txt)

        self.page.dialog = self.ui_dialog
        self.ui_dialog.open = True
        self.page.update()


if __name__ == "__main__":
    ft.app(target=SampleForm)
