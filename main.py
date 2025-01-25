from sensor import Sensor
from processor import Processor
from logger import Logger
from notifier import Notifier

if __name__ == "__main__":
    
    sensor = Sensor()
    processor = Processor()
    logger = Logger()
    notifier = Notifier()

    
    sensor.on("data_detected", processor.process)
    processor.on("data_processed", logger.log)
    processor.on("data_error", notifier.notify)


    
    print("Simulating events...\n")
    sensor.detect("Temperature: 25°C")
    sensor.detect("Error: Sensor malfunction")
