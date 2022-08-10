from logging import Filter, LogRecord


class DuplicateFilter(Filter):
    def __init__(self):
        super().__init__()
        self.msgs = set()

    def filter(self, record: LogRecord) -> bool:
        is_duplicate = record.getMessage() in self.msgs
        self.msgs.add(record.getMessage())
        return not is_duplicate
