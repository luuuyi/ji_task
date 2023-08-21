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

需要注意修改`line148, line164, line176`部分的输入数据物料；

需要注意修改`line149, line165, line177`部分的是否开启相关处理操作的flag；

```
cd init_task/data_analysis
python3 main.py
```

flag代表处理开关，1表示打开，0表示关闭

CV任务

- fill_flag：填充，fill_args.roi 表示a图片中的roi区域；
- hist_equa_flag：直方图均衡化；
- white_balance_flag：自动白平衡；
- automatic_color_enhancement_flag：自动色彩均衡
- blur_flag：平滑滤波

NLP任务

- remove_number_flag：去除数字；
- remove_space_flag：去除多余空格；
- remove_url_flag：去除url链接；
- remove_duplicate_str_flag：去除重复文本（多行！）

SPEECH任务

- denoise_flag：降噪开关
- remove_silence_flag：消除静音段
- increase_sound_flag：增强/减弱音量，increase_sound_args.inc表示变量