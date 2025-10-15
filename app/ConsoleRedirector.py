class ConsoleRedirector:
    def __init__(self, text_widget, queue):
        self.text_widget = text_widget
        self.queue = queue

    def write(self, message):
        self.queue.put(message)

    def flush(self):
        pass
