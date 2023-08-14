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
cd init_task/algo_analysis/nlp/
pip3 install -r requirements.txt
```

### 1.2 **推荐！！！**Anaconda安装python虚拟环境
```
git clone https://github.com/luuuyi/init_task

# 安装基础环境
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.6 -c pytorch -c nvidia

# 安装依赖
cd init_task/algo_analysis/nlp/
pip3 install -r requirements.txt
```

## 3. 推理

### en to zh

将en_zh/ev_sdk文件夹拷贝到/usr/local/ev_sdk，工程代码均在/usr/local/ev_sdk目录

```
# 执行下面命令开始推理。
cd /usr/local/ev_sdk
python3 ji.py
```

### zh to en

将zh_en/ev_sdk文件夹拷贝到/usr/local/ev_sdk，工程代码均在/usr/local/ev_sdk目录

```
# 执行下面命令开始推理。
cd /usr/local/ev_sdk
python3 ji.py
```

## 4. 训练

### 数据准备

需要简单自备训练物料，训练数据为json line格式，如下所示，最外围的key `translation` 必不可少，对应的value为字典类型的数据，key分别为 `en` `zh`，必须要有，然后各自的value对应相关语言类型下的文本。

```
{"translation": {"en": "I wanted Tom to apologize to Mary.", "zh": "我要汤姆想玛丽道歉"}}
```

数据集文件设置成本地文件tmp.json

### en to zh

相关的指令在ft.sh中

```
python3 run_translation.pyc \
    --model_name_or_path Helsinki-NLP/opus-mt-en-zh \
    --do_train \
    --do_eval \
    --source_lang en \
    --target_lang zh \
    --train_file tmp.json \
    --validation_file tmp.json \
    --output_dir ./tmp/en-zh \
    --per_device_train_batch_size=4 \
    --per_device_eval_batch_size=4 \
    --overwrite_output_dir \
    --predict_with_generate
```

### zh to en

相关的指令在ft.sh中

```
python3 run_translation.pyc \
    --model_name_or_path Helsinki-NLP/opus-mt-zh-en \
    --do_train \
    --do_eval \
    --source_lang zh \
    --target_lang en \
    --train_file tmp.json \
    --validation_file tmp.json \
    --output_dir ./tmp/zh-en \
    --per_device_train_batch_size=4 \
    --per_device_eval_batch_size=4 \
    --overwrite_output_dir \
    --predict_with_generate
```