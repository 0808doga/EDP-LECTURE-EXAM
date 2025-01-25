class EventEmitter:
    def __init__(self):
        self._events = {}

    def on(self, event_name, listener):
        if event_name not in self._events:
            self._events[event_name] = []
        self._events[event_name].append(listener)

    def emit(self, event_name, *args, **kwargs):
        if event_name in self._events:
            for listener in self._events[event_name]:
                listener(*args, **kwargs)
