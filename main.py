from src.send_image.pipeline.final_stage import SendPipeline
from src.send_image import logger
from folder import file_path

STAGE_NAME = " send stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   send = SendPipeline(file_path)
   send.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e 


   


