import torch
from torch import nn


class CNN(nn.Module):
    def __init__(self):
        super().__init__()

        self.encoder = torch.nn.Sequential(

            nn.Conv2d(1, 3, kernel_size=4, stride=2, padding=1),
            nn.ReLU(True), #640 to 320 * 3
            nn.Conv2d(3, 3, kernel_size=4, stride=2, padding=1),
            nn.ReLU(True), #(320 to 160) *3
            nn.Conv2d(3, 3, kernel_size=4, stride=2, padding=1),
            nn.ReLU(True), #(160 to 80) * 3
            nn.Flatten(),
            nn.Linear(80 * 3, 128),
            nn.ReLU(True)
        )

    def forward(self, x):
        return self.encoder(x)