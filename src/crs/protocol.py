from enum import Enum



class MessageType(Enum):
    ACKNOWLEDGE = b"\(^.^)/ - 0.0.1"
    REPLICATION_INFO = b"/(^.^)? - 0.0.1"
    


class CommandType(Enum):
    pass
