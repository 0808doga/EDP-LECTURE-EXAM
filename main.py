
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
        if "error" in data.lower():
            print(f"Processor encountered an error with: {data}")
            self.emit("data_error", data)
        else:
            print(f"Processor processed: {data}")
            self.emit("data_processed", data)


class Logger(EventEmitter):
    def log(self, message):
        print(f"Logger logged: {message}")


class Notifier(EventEmitter):
    def notify(self, message):
        print(f"Notifier sent notification: {message}")


if __name__ == "__main__":
    sensor = Sensor()
    processor = Processor()
    logger = Logger()
    notifier = Notifier()

    sensor.on("data_detected", processor.process)
    processor.on("data_processed", logger.log)
    processor.on("data_error", notifier.notify)

    sensor.detect("Temperature: 25°C")
    sensor.detect("Error: Sensor malfunction")
