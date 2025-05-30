_base_ = [
    '_base_/models/faster-rcnn_r50_fpn.py',
    '_base_/datasets/voc0712.py',
    '_base_/schedules/schedule_1x.py', 
    '_base_/default_runtime.py'
]

train_cfg = dict(max_epochs=100, val_interval=7)
device = 'cuda'