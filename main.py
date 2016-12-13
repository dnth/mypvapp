import kivy
kivy.require('1.9.0')
 
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.tabbedpanel import TabbedPanel

import pymysql







# You can create your kv code in the Python file
Builder.load_string("""
<ScreenLogin>:
    canvas.before:
        Color:
            rgba: (1,1,1,1)
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            orientation: 'vertical'
            Label:
                id: login_label
                text: "MyProviApp Login"
                color: (0,0,0,1)
                font_size: 50

            Label:
                id: success
                color: (1,0,0,1)
                text: "Please Enter Credentials"

            GridLayout:
                rows:2
                cols:2
                padding:10
                spacing:10

                Label:
                    id: username_label
                    text: "Username"
                    color: (0,0,0,1)
                    font_size:30
                TextInput:
                    id: username_input
                    font_size: 20
                    color: (0,0,0,1)
                    multiline: False
                    cursor_color: (0,0,0,1)
                    write_tab: False
                Label:
                    id: password_label
                    text: "Password"
                    color: (0,0,0,1)
                    font_size:30
                TextInput:
                    id: password_input
                    font_size: 20
                    password: True
                    multiline: False
                    color: (0,0,0,1)
                    cursor_color: (0,0,0,1)
                    write_tab: False

        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: "Login"
                on_press:
                    # You can define the duration of the change
                    # and the direction of the slide
                    #root.manager.transition.direction = 'left'
                    #root.manager.transition.duration = 1
                    #root.manager.current = 'screen_two'
                    root.login()
            Button:
                text: "Exit"
                on_press: app.stop()
 
<ScreenTwo>:
    BoxLayout:
        orientation: 'vertical'
        

        TabbedPanel:
            do_default_tab: False

            TabbedPanelItem:
                text: "Lyrics"
                Label: 
                    text:"Content first"

            TabbedPanelItem:
                text: "Proverbs"
                Label: 
                    text:"Content Second"

            TabbedPanelItem:
                text: "Bible"
                Label: 
                    text:"Content third"

        Button:
            text: "Go to Screen 1"
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'screen_login'
""")
 
# Create a class for all screens in which you can include
# helpful methods specific to that screen



class ScreenLogin(Screen, Widget):
    def login(self):
        username = self.ids.username_input
        username_text = username.text

        password = self.ids.password_input
        password_text = password.text

        info_label = self.ids.success

        hostname = 'localhost'
        username = 'root'
        password = 'root'
        database = 'myprovi'

        print "Initiating Connection"
        myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
        print "Connected!"

        cursor = myConnection.cursor()

        try:
            with myConnection.cursor() as cursor:
                sql = "SELECT `username` FROM `user_pass` WHERE pass='%s' " % password_text
                cursor.execute(sql)
                result = cursor.fetchone()
                print result

                if result:
                    info_label.text = "Login Successful"
                    self.manager.transition.duration = 1
                    self.manager.transition.direction = 'left'
                    self.manager.current = 'screen_two'

                elif result is None:
                    info_label.text = "Wrong Credentials"

        except:
            print ("Error: unable to fetch data")
            info_label.text = "Check your internet connection"


        myConnection.close()
        print "Connection closed"

 
class ScreenTwo(Screen):
    pass


class MenuTabs(TabbedPanel):
    pass 
 
# The ScreenManager controls moving between screens
screen_manager = ScreenManager()

 
# Add the screens to the manager and then supply a name
# that is used to switch screens
screen_manager.add_widget(ScreenLogin(name="screen_login"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))

 
class MyProviApp(App):
    def build(self):
        return screen_manager

 
sample_app = MyProviApp()
sample_app.run()