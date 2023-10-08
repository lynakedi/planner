from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.navigationdrawer import MDNavigationLayout, MDNavigationDrawer
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.toolbar import MDTopAppBar

from kivy.lang import Builder

KV = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#BABABA"
    text_color: "#124654"
    icon_color: "#124654"
    ripple_color: "#124654"
    selected_color: "#124654"

<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#124654"
    icon_color: "#124654"
    focus_behavior: False
    selected_color: "#124654"
    _no_ripple_effect: True

MDScreen:
    MDNavigationLayout:
        MDScreenManager:
            MDScreen:
                MDTopAppBar:
                    title: "Главная"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#00A08F"
                    specific_text_color: "#ffffff"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            MDNavigationDrawerMenu:
                MDNavigationDrawerHeader:
                    title: "Ежедневник"
                    title_color: "#124654"
                    text: "Ничего не забыть!"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

                MDNavigationDrawerLabel:
                    text: "Разделы"

                DrawerClickableItem:
                    icon: "home-outline"
                    text: "Главная"
                    text_color: "#124654"

                DrawerClickableItem:
                    icon: "pencil-outline"
                    text_right_color: "#124654"
                    text: "Записи"

                DrawerClickableItem:
                    icon: "order-bool-descending-variant"
                    text: "Список задач"
                    text_color: "#124654"

                DrawerClickableItem:
                    icon: "alarm"
                    text: "Напоминания"
                    text_color: "#124654"

                MDNavigationDrawerDivider:

                DrawerClickableItem:
                    text: "Другое"
                    icon: "information-outline"
                    text: "О нас"
'''


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def nav_drawer_open(self, *args):
        nav_drawer = self.root.children[0].ids.nav_drawer
        nav_drawer.set_state("open")


Example().run()
