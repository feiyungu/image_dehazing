# inference config file
# Created by zyh in Meitu.

from squid.net import DnCnn
from squid.net import AODNet
from squid.net import DnCnn_AOD
from squid.net import Unet_AOD_Net
import torch.nn as nn

test_snapshot_path = '/root/zyh3/train_tasks/unet_aod_ntire_configv1/models/snapshot_40_G_model'

target_net = Unet_AOD_Net()
target_net = nn.DataParallel(target_net).cuda()

test_input_dir = '/root/zyh3/ntire/indoortest'

TEST_OUT_FOLDER = '/root/zyh3/ntire/indoortest_unet_aod_out'

GPU_ID = -1

vis = None

divided = True