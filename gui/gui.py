
from gui.wave_crypt_page import Ui_MainWindow
from utils.util import play


class Gui(Ui_MainWindow):

    def __init__(self):
        # load parent constructor
        Ui_MainWindow.__init__(self)

    def start(self, main_window):
        # start loading the page components
        self.setupUi(main_window)
        self.add_functions()

    def add_functions(self):
        # add diferent functionalities
        self.send()

    def send(self):
        # button send functionality
        # This method pauses the gui, it should be async
        self.pushButton.clicked.connect(play)
