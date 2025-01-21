
class EventEmitter:
    def __init__(self):
        self._events = {}

    def on(self, event_name, listener):
        """Register a listener for an event."""
        if event_name not in self._events:
            self._events[event_name] = []
        self._events[event_name].append(listener)

    def emit(self, event_name, *args, **kwargs):
        """Trigger an event and notify listeners."""
        if event_name in self._events:
            for listener in self._events[event_name]:
                listener(*args, **kwargs)



class Sensor(EventEmitter):
    def detect(self, data):
        print(f"Sensor detected: {data}")
        self.emit("data_detected", data)

class Processor(EventEmitter):
    def process(self, data):
        print(f"Processor processed: {data}")
        self.emit("data_processed", data)

class Logger(EventEmitter):
    def log(self, message):
        print(f"Logger logged: {message}")


if __name__ == "__main__":
    sensor = Sensor()
    processor = Processor()
    logger = Logger()

    sensor.on("data_detected", processor.process)
    processor.on("data_processed", logger.log)

    sensor.detect("Temperature: 25°C")