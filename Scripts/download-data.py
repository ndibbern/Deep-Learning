import torch
import torchvision
import torchvision.transforms as transforms
import os

os.system("mkdir data")

################
# MNIST
#################

print(" \n\n DOWNLOADING MNIST \n\n")
os.system("mkdir data/mnist")

trainset = torchvision.datasets.MNIST(root='./temp', train=True, download=True, transform=transforms.ToTensor())
testset = torchvision.datasets.MNIST(root='./temp', train=False, download=True, transform=transforms.ToTensor())

# train set
train_data=torch.Tensor(60000,28,28)
train_label=torch.LongTensor(60000)
for idx , example in enumerate(trainset):
    train_data[idx]=example[0].squeeze()
    train_label[idx]=example[1]
torch.save(train_data,'data/mnist/train_data.pt')
torch.save(train_label,'data/mnist/train_label.pt')

# test set
test_data=torch.Tensor(10000,28,28)
test_label=torch.LongTensor(10000)
for idx , example in enumerate(testset):
    test_data[idx]=example[0].squeeze()
    test_label[idx]=example[1]
torch.save(test_data,'data/mnist/test_data.pt')
torch.save(test_label,'data/mnist/test_label.pt')

os.system("rm -r temp")

################
# FASHION MNIST
#################

print("\n\n DOWNLOADING FASHION-MNIST \n\n")
os.system("mkdir data/fashion-mnist")

trainset = torchvision.datasets.FashionMNIST(root='./temp', train=True, download=True, transform=transforms.ToTensor())
testset = torchvision.datasets.FashionMNIST(root='./temp', train=False, download=True, transform=transforms.ToTensor())

# train set
train_data=torch.Tensor(60000,28,28)
train_label=torch.LongTensor(60000)
for idx , example in enumerate(trainset):
    train_data[idx]=example[0].squeeze()
    train_label[idx]=example[1]
torch.save(train_data,'data/fashion-mnist/train_data.pt')
torch.save(train_label,'data/fashion-mnist/train_label.pt')

# test set
test_data=torch.Tensor(10000,28,28)
test_label=torch.LongTensor(10000)
for idx , example in enumerate(testset):
    test_data[idx]=example[0].squeeze()
    test_label[idx]=example[1]
torch.save(test_data,'data/fashion-mnist/test_data.pt')
torch.save(test_label,'data/fashion-mnist/test_label.pt')

os.system("rm -r temp")


################
# CIFAR
#################

print("\n\n DOWNLOADING CIFAR \n\n")
os.system("mkdir data/cifar")

trainset = torchvision.datasets.CIFAR10(root='./temp', train=True, download=True, transform=transforms.ToTensor())
testset = torchvision.datasets.CIFAR10(root='./temp', train=False, download=True, transform=transforms.ToTensor())

# train set
train_data=torch.Tensor(50000,3,32,32)
train_label=torch.LongTensor(50000)
for idx , example in enumerate(trainset):
    train_data[idx]=example[0]
    train_label[idx]=example[1]
torch.save(train_data,'data/cifar/train_data.pt')
torch.save(train_label,'data/cifar/train_label.pt')

# test set
test_data=torch.Tensor(10000,3,32,32)
test_label=torch.LongTensor(10000)
for idx , example in enumerate(testset):
    test_data[idx]=example[0]
    test_label[idx]=example[1]
torch.save(test_data,'data/cifar/test_data.pt')
torch.save(test_label,'data/cifar/test_label.pt')

os.system("rm -r temp")



