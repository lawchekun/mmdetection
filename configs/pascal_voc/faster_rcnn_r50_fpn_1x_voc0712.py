_base_ = [
    '../_base_/models/faster_rcnn_r50_fpn.py',
    '../_base_/datasets/voc0712.py',
    '../_base_/default_runtime.py',
]
model = dict(roi_head=dict(bbox_head=dict(num_classes=13)))  # 20
# optimizer
optimizer = dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)
# learning policy
# actual epoch = 3 * 3 = 9
lr_config = dict(policy='step', step=[3])
# runtime settings
total_epochs = 8  # # # #  #  # actual epoch = 4 * 3 = 12
# load_from = "/home/chekun/vision/mmdetection/demo/work_dirs/faster_rcnn_r50_fpn_1x_voc0712/epoch_8.pth"
