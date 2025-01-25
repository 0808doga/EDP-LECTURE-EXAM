from event_emitter import EventEmitter

class Processor(EventEmitter):
    def process(self, data):
        """Algılanan veriyi işler."""
        if "error" in data.lower():
            print(f"Processor encountered an error with: {data}")
            self.emit("data_error", data)
        else:
            print(f"Processor processed: {data}")
            self.emit("data_processed", data)
