"""
File that contains the networking functions
"""

# so python doesn't cry about file not found
import sys
sys.path.append("src/proto/")

from proto.schema_pb2_grpc import *

import time
print(time.time())


class NodeNetwork():
    pass