# ASR

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
cd init_task
pip3 install -r requirements.txt
```

### 1.2 **推荐！！！**Anaconda安装python虚拟环境
```
git clone https://github.com/luuuyi/init_task

# 安装基础环境
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.6 -c pytorch -c nvidia

# 安装依赖
cd init_task
pip3 install -r requirements.txt
```

## 2. 数据准备**（一定要做！即便只是推理）**
相关内容参考[数据准备](./docs/dataset.md)
```
cd init_task
cd download_data && python3 thchs_30.py && cd ../
python3 create_data.py
```
执行完后会生成`manifest.test、manifest.train、manifest.noise`三个文件用于训练，`vocabulary.txt`则用于训练和测试。

## 3. 推理
将ev_sdk文件夹拷贝到/usr/local/ev_sdk，工程代码均在/usr/local/ev_sdk目录

其中ji.py文件需要修改，更改文件line5的`PROJECT_PATH`为本项目的绝对路径

！！！测试过程中会自动下载预训练模型到`"~/.cache/masr"`路径，需要能联网；

## 4. 训练
以[thchs30](http://www.openslr.org/18/)数据集训练为例，按以下流程来执行

首先下载数据thchs30，**假定第二步的数据准备正常运行**

```
# 执行下面命令开始训练。
python3 train.py
# 相关的训练配置在`./configs/conformer.yml`，训练之后的模型会放在models/conformer_streaming_fbank/下
```

使用该模型评测之前，需要将模型转为torchscript格式，这样就能直接导入模型文件进行预测
```
# 导出模型
python3 export_model.py --resume_model=models/conformer_streaming_fbank/best_model/
# 预测音频文件
python3 infer_path.py --wav_path=./dataset/test.wav
```