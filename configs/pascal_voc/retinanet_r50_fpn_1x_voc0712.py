_base_ = [
    '../_base_/models/retinanet_r50_fpn.py',
    '../_base_/datasets/voc0712.py',
    '../_base_/default_runtime.py',
]
model = dict(
    bbox_head=dict(num_classes=13)  # 13
)  # 20, doesn't overwrite well, overwrites to the one in the working_dir
# optimizer
# optimizer = dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.0001)
# # optimizer_config = dict(grad_clip=None)
# # Use Gradient Clipping
# optimizer_config = dict(grad_clip=dict(max_norm=25, norm_type=2))

# # learning policy
# # actual epoch = 3 * 3 = 9
# lr_config = dict(policy='step', step=[3])

# Use Adam
optimizer = dict(type='Adam', lr=0.005)
# Use Gradient Clipping
optimizer_config = dict(grad_clip=dict(max_norm=25, norm_type=2))
# # learning policy
lr_config = dict(
    policy='step', warmup='linear', warmup_iters=500, warmup_ratio=1.0 / 3, step=[180]
)

# runtime settings
total_epochs = 2
