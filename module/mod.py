import random

from client.comm import BaseComm
from common.frame_enum import FrameType
from common.frames import FrameCommandId


class Module:
    def __init__(self, comm: BaseComm):
        self.comm = comm
        self.comm.listen_for([FrameType.COMMAND_LOG])

    def process(self):
        while self.comm.has_data():
            frame = self.comm.get_data()

            if not frame.request:
                continue

            frame = FrameCommandId()
            frame.set_data(random.randint())
            self.comm.send(frame)

    def stop(self):
        self.comm.stop()
