import flet as ft


def main(page: ft.Page):
  # タイトル設定
  page.title = 'Sample'
  page.padding = 10

  # UI定義
  ui_text      = ft.Text('ダミーテキスト')
  ui_textfield = ft.TextField(label='テキストラベル', value='')
  ui_checkbox  = ft.Checkbox(label='チェックラベル', value=False)
  ui_dropdown  = ft.Dropdown(
     label='ドロップダウンラベル',
     width=300,
     options=[
      ft.dropdown.Option(key='OK', text='良い'),
      ft.dropdown.Option(key='NG', text='悪い'),
      ft.dropdown.Option(key='OTHER', text='その他'),
     ]
  )
  ui_radiogroup = ft.RadioGroup(
     value='ラジオグループ',
     content=ft.Row([
      ft.Radio(label='良い', value='OK'),
      ft.Radio(label='悪い', value='NG'),
      ft.Radio(label='その他', value='OTHER'),
     ])
  )
  ui_switch = ft.Switch(label="スイッチラベル", value=True)
  ui_slider = ft.Slider(label="{value}", value=50, min=0, max=100, divisions=10)
  ui_elevatedbutton = ft.ElevatedButton("登録", icon=ft.icons.ADD)
  ui_iconbutton     = ft.IconButton(icon=ft.icons.ADD)


  # ページに追加
  page.add (
     ft.Card (
      content=ft.Container (
        content=ft.Column (
          controls=[
            ui_text,
            ui_textfield,
            ui_checkbox,
            ui_dropdown,
            ui_radiogroup,
            ui_switch,
            ui_slider,
            ui_elevatedbutton,
            ui_iconbutton
          ]
        ),
        padding=10
      )
    )
  )


if __name__ == '__main__':
  ft.app(target=main)
