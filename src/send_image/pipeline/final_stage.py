from src.send_image.components.Back_Sel import BackgroundSelector
from src.send_image.components.image_process import ImageProcessor
from src.send_image.components.send import Send_Email


class SendPipeline:
    def __init__(self,file_path):
        #self.folder_path = folder_path
        self.file_path = file_path

    def main(self):
        selector = BackgroundSelector()
        selector.root.mainloop()
        selected_image_path = selector.get_selected_image_path()
        processor = ImageProcessor(self.file_path,selected_image_path)
        processor.process_image()
        email_to = input("give me your email address ")
        send_email = Send_Email(email_to)
        send_email.send_email()
