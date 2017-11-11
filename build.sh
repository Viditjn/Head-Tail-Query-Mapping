#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH --mem-per-cpu=2048
#SBATCH --partition=short
#SBATCH --mail-type=ALL

source ~/.bashrc
module add cuda/8.0
module add cudnn/6-cuda-8.0

python neuralNet.py newMedium.txt
