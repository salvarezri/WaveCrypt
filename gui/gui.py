
from gui.wave_crypt_window import Ui_MainWindow
from utils.util import play
from modules.cryptography_module import encrypt, decrypt


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
        self.send_function()
        self.receive_function()
        self.crypt_functions()

    def receive_function(self):
        self.button_recieve.clicked.connect(self.receive)

    def send_function(self):
        # button send functionality
        # This method pauses the gui, it should be async
        self.button_send.clicked.connect(self.send)

    def receive(self):
        self.field_recieve_text.setPlainText("")
        text = self.field_send_text.toPlainText()
        self.field_recieve_text.insertPlainText(text)

    def send(self):
        # obtains text to send and reproduce it
        text = self.field_send_text.toPlainText()
        play(text)

    def crypt_functions(self):
        # connect functions to encrypt and decrypt with corresponding buttons
        self.button_send_encrypt.clicked.connect(self.encrypt_text_send)
        self.button_send_decrypt.clicked.connect(self.decrypt_text_send)
        self.button_recieve_encrypt.clicked.connect(self.encrypt_text_receive)
        self.button_recieve_decrypt.clicked.connect(self.decrypt_text_receive)

    # next 4 functions are middle functions to call cryptography function
    def encrypt_text_send(self):
        return self.crypt_text(self.field_send_text, "encrypt", self.field_send_password)

    def decrypt_text_send(self):
        return self.crypt_text(self.field_send_text, "decrypt", self.field_send_password)

    def encrypt_text_receive(self):
        return self.crypt_text(self.field_recieve_text, "encrypt", self.field_recieve_password)

    def decrypt_text_receive(self):
        return self.crypt_text(self.field_recieve_text, "decrypt", self.field_recieve_password)

    def crypt_text(self, text_field, method, password_field):
        # obtains the text, the password and encrypt / decrypt acording what its needed
        text = text_field.toPlainText()
        password = password_field.text()
        crypt_text = encrypt(text, password) if method == "encrypt" else decrypt(text, password)
        text_field.setPlainText(crypt_text)

