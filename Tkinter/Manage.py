from Window import *
from DBConnect import *

start_window.Create_button(1600, 20, "Принт", dbconnect.ShowData())
# ____________ЗАПУСК_ОКНА____________
start_window.Run_window()