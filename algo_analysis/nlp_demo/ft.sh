python3 run_translation.py \
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

python3 run_translation.py \
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