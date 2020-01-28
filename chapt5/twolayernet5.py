import sys, os
sys.path.append(os.pardir)
import numpy as np
from layers import *
from master.common.gradient import numerical_gradient
from collections import OrderdDict
