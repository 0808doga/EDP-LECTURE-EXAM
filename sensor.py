from event_emitter import EventEmitter

class Sensor(EventEmitter):
    def detect(self, data):
        print(f"Sensor detected: {data}")
        self.emit("data_detected", data)
