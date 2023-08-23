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

测试demo的推理入口为main_for_all.py，调用方传入`dict`类型的`EV_AUTO_TEST_CONFIG_PARAMS`配置信息，调用`process_interface`方法

```python
args = {
    "input_path": "./tmp/input_dataset.zip",
    "output_path":"./tmp/output_dataset.zip",
    "data_set_type":"SPEECH",
    "data_set_format":"plain text",
    "pretreatment_flag":1,
    "pretreatment": {
        "fill_flag": 1,
        "fill_args": {"roi": [500, 500]},
        "hist_equa_flag": 1,
        "white_balance_flag": 1,
        "automatic_color_enhancement_flag": 1,
        "blur_flag": 1,

        "remove_number_flag": 1,
        "remove_space_flag": 1,
        "remove_url_flag": 1,
        "remove_duplicate_str_flag": 1,
        "remove_words_flag": 1,
        "remove_words_args": {"words": ["hello", ]},


        "denoise_flag": 1,
        "remove_silence_flag": 1,
        "increase_sound_flag": 1,
        "increase_sound_args": {"inc": 10}
    }
}
ret_file = process_interface(args)
with open(ret_file, "r", encoding="utf-8") as fin:
    infos = json.load(fin)
print(infos)
```

全局参数解释如下：

- input_path：必填，zip结尾的存在文件；
- output_path：必填，输出文件
- data_set_type：必填，SPEECH CV NLP三选一
- pretreatment：必填，子函数配置信息

**pretreatment为dict类型数据，具体字段解释如下**

flag代表处理开关，1表示打开，0表示关闭

CV任务

- fill_flag：填充，fill_args.roi 表示宽高；
- hist_equa_flag：直方图均衡化；
- white_balance_flag：自动白平衡；
- automatic_color_enhancement_flag：自动色彩均衡
- blur_flag：平滑滤波

NLP任务

- remove_number_flag：去除数字；
- remove_space_flag：去除多余空格；
- remove_url_flag：去除url链接；
- remove_duplicate_str_flag：去除重复文本（多行！）
- remove_words_flag：敏感词开关，remove_words_flag.words为list类型的敏感词数组

SPEECH任务

- denoise_flag：降噪开关
- remove_silence_flag：消除静音段
- increase_sound_flag：增强/减弱音量，increase_sound_args.inc表示变量