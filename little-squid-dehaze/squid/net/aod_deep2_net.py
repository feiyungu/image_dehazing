#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Implementation of AOD-Net in ICCV2017
# Created by Zhao Yuhang in Meitu.

import os 
import torch
import torch.nn as nn
from torch.autograd import Variable

class AOD_Deep2_Net(nn.Module):
	def __init__(self):
		super(AOD_Deep2_Net, self).__init__()
		self.conv1 = nn.Conv2d(3, 3, kernel_size=1, stride=1)
		self.relu1 = nn.ReLU(inplace=True)
		self.conv2 = nn.Conv2d(3, 3, kernel_size=3, stride=1, padding=1)
		self.relu2 = nn.ReLU(inplace=True)
		self.conv3 = nn.Conv2d(6, 3, kernel_size=3, stride=1, padding=1)
		self.relu3 = nn.ReLU(inplace=True)
		self.conv4 = nn.Conv2d(6, 3, kernel_size=5, stride=1, padding=2)
		self.relu4 = nn.ReLU(inplace=True)
		self.conv5 = nn.Conv2d(6, 3, kernel_size=5, stride=1, padding=2)
		self.relu5 = nn.ReLU(inplace=True)
		self.conv6 = nn.Conv2d(9, 3, kernel_size=7, stride=1, padding=3)
		self.relu6 = nn.ReLU(inplace=True)
		self.conv7 = nn.Conv2d(12, 3, kernel_size=7, stride=1, padding=3)
		self.relu7 = nn.ReLU(inplace=True)
		self.conv8 = nn.Conv2d(12, 3, kernel_size=5, stride=1, padding=2)
		self.relu8 = nn.ReLU(inplace=True)
		self.conv9 = nn.Conv2d(15, 3, kernel_size=5, stride=1, padding=2)
		self.relu9 = nn.ReLU(inplace=True)
		self.conv10 = nn.Conv2d(15, 3, kernel_size=3, stride=1, padding=1)
		self.relu10 = nn.ReLU(inplace=True)
		self.conv11 = nn.Conv2d(18, 3, kernel_size=3, stride=1, padding=1)
		self.relu11 = nn.ReLU(inplace=True)
		self.conv12 = nn.Conv2d(18, 3, kernel_size=3, stride=1, padding=1)
		self.relu12 = nn.ReLU(inplace=True)
		self.conv13 = nn.Conv2d(21, 3, kernel_size=3, stride=1, padding=1)
		self.relu13 = nn.ReLU(inplace=True)
		self.conv14 = nn.Conv2d(21, 3, kernel_size=3, stride=1, padding=1)
		self.relu14 = nn.ReLU(inplace=True)
		self.conv15 = nn.Conv2d(24, 3, kernel_size=3, stride=1, padding=1)
		self.relu15 = nn.ReLU(inplace=True)
		self.conv16 = nn.Conv2d(24, 3, kernel_size=3, stride=1, padding=1)
		self.relu16 = nn.ReLU(inplace=True)
		self.conv17 = nn.Conv2d(24, 3, kernel_size=3, stride=1, padding=1)
		self.relu17 = nn.ReLU(inplace=True)
		self.conv18 = nn.Conv2d(27, 3, kernel_size=3, stride=1, padding=1)
		self.relu18 = nn.ReLU(inplace=True)
		self.conv19 = nn.Conv2d(30, 3, kernel_size=3, stride=1, padding=1)
		self.relu19 = nn.ReLU(inplace=True)

		self.conv20 = nn.Conv2d(57, 3, kernel_size=3, stride=1, padding=1)
		self.relu20 = nn.ReLU()
		self.clip = nn.ReLU(inplace=True)

	def forward(self, x, target=None):
		x1_0 = x
		x1 = self.conv1(x1_0)
		x1 = self.relu1(x1)
		x2_0 = x1
		x2 = self.conv2(x2_0)
		x2 = self.relu2(x2)
		x3_0 = torch.cat((x1, x2), dim=1)
		x3 = self.conv3(x3_0)
		x3 = self.relu3(x3)
		x4_0 = torch.cat((x2, x3), dim=1)
		x4 = self.conv4(x4_0)
		x4 = self.relu4(x4)
		x5_0 = torch.cat((x3, x4), dim=1)
		x5 = self.conv5(x5_0)
		x5 = self.relu5(x5)
		x6_0 = torch.cat((x3, x4, x5), dim=1)
		x6 = self.conv6(x6_0)
		x6 = self.relu6(x6)
		x7_0 = torch.cat((x3, x4, x5, x6), dim=1)
		x7 = self.conv7(x7_0)
		x7 = self.relu7(x7)
		x8_0 = torch.cat((x4, x5, x6, x7), dim=1)
		x8 = self.conv8(x8_0)
		x8 = self.relu8(x8)
		x9_0 = torch.cat((x4, x5, x6, x7, x8), dim=1)
		x9 = self.conv9(x9_0)
		x9 = self.relu9(x9)
		x10_0 = torch.cat((x5, x6, x7, x8, x9), dim=1)
		x10 = self.conv10(x10_0)
		x10 = self.relu10(x10)
		x11_0 = torch.cat((x5, x6, x7, x8, x9, x10), dim=1)
		x11 = self.conv11(x11_0)
		x11 = self.relu11(x11)
		x12_0 = torch.cat((x6, x7, x8, x9, x10, x11), dim=1)
		x12 = self.conv12(x12_0)
		x12 = self.relu12(x12)
		x13_0 = torch.cat((x6, x7, x8, x9, x10, x11, x12), dim=1)
		x13 = self.conv13(x13_0)
		x13 = self.relu13(x13)
		x14_0 = torch.cat((x7, x8, x9, x10, x11, x12, x13), dim=1)
		x14 = self.conv14(x14_0)
		x14 = self.relu14(x14)
		x15_0 = torch.cat((x7, x8, x9, x10, x11, x12, x13, x14), dim=1)
		x15 = self.conv15(x15_0)
		x15 = self.relu15(x15)
		x16_0 = torch.cat((x8, x9, x10, x11, x12, x13, x14, x15), dim=1)
		x16 = self.conv16(x16_0)
		x16 = self.relu16(x16)
		x17_0 = torch.cat((x9, x10, x11, x12, x13, x14, x15, x16), dim=1)
		x17 = self.conv17(x17_0)
		x17 = self.relu17(x17)
		x18_0 = torch.cat((x9, x10, x11, x12, x13, x14, x15, x16, x17), dim=1)
		x18 = self.conv18(x18_0)
		x18 = self.relu18(x18)
		x19_0 = torch.cat((x9, x10, x11, x12, x13, x14, x15, x16, x17, x18), dim=1)
		x19 = self.conv19(x19_0)
		x19 = self.relu19(x19)

		x20_0 = torch.cat((x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19), dim=1)
		x20 = self.conv20(x20_0)
		x20 = self.relu20(x20)
		out = x20 * x - x20 + 1
		out = self.clip(out)
		
		if target is not None:
			pairs = {'out': (out, target)}
			return pairs, self.exports(x, out, target)
		else:
			return self.exports(x, out, target)

	def exports(self, x, output, target):
		result = {'input': x, 'output': output}
		if target is not None:
			result['target'] = target
		return result


if __name__ == '__main__':
	model = AOD_Deep2_Net()
	x = Variable(torch.ones(4, 3, 100, 100))
	y = Variable(torch.ones(4, 3, 100, 100))
	if torch.cuda.is_available():
		model.cuda()
		x = x.cuda()
		y = y.cuda()
	model.eval()

	out = model(x)
	for key, value in out.items():
		print(key + ':', value.size())

