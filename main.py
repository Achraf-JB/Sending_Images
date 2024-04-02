from src.send_image.pipeline.final_stage import SendPipeline
from src.send_image import logger

#folder_path =r"C:\Users\HP\OneDrive\Bureau\pythonProject\Sending_Images\photo_back"
file_path =r"C:\Users\HP\OneDrive\Bureau\pythonProject\Sending_Images\reel_photo\istockphoto-1337256709-612x612.jpg"
#file_path  ="istockphoto-1337256709-612x612.jpg"
STAGE_NAME = " send stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   send = SendPipeline(file_path)
   send.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e 


   


