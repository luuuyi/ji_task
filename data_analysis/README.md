# Translation

## 1. 环境准备

**重要！！！勿忽略**
- Python 3.8
- Pytorch 1.13.1
- Cuda 11.6

### 1.1 执行dockerfile拉取基础镜像后安装项目依赖
```
# 构建基础环境
cd init_task
docker build -t init_task .

# 进入到环境中
git clone https://github.com/luuuyi/init_task
cd init_task/data_analysis
pip3 install -r requirements.txt
```

### 1.2 **推荐！！！**Anaconda安装python虚拟环境
```
git clone https://github.com/luuuyi/init_task

# 安装基础环境
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.6 -c pytorch -c nvidia

# 安装依赖
cd init_task/data_analysis
pip3 install -r requirements.txt
```

## 3. 推理

执行下列命令按顺序调用三种task，并且会在本地存下`xxx_result.json`的结果文件

需要注意修改`line153, line160, line166`部分的输入数据物料；

需要注意修改`line15, line75, line115`部分的是否开启相关处理操作的flag；

```
cd init_task/data_analysis
python3 main.py
```