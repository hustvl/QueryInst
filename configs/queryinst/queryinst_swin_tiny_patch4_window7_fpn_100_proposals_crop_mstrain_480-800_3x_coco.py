_base_ = './queryinst_r50_fpn_300_proposals_crop_mstrain_480-800_3x_coco.py'

num_proposals = 100
model = dict(
    pretrained=None,
    backbone=dict(
        _delete_=True,
        type='SwinTransformer',
        embed_dim=96,
        depths=[2, 2, 6, 2],
        num_heads=[3, 6, 12, 24],
        window_size=7,
        mlp_ratio=4.,
        qkv_bias=True,
        qk_scale=None,
        drop_rate=0.,
        attn_drop_rate=0.,
        drop_path_rate=0.2,
        ape=False,
        patch_norm=True,
        out_indices=(0, 1, 2, 3),
        use_checkpoint=False),
    neck=dict(
        type='FPN',
        in_channels=[96, 192, 384, 768],
        out_channels=256,
        num_outs=4),
    rpn_head=dict(num_proposals=num_proposals),
    test_cfg=dict(
        _delete_=True, rpn=None, rcnn=dict(max_per_img=num_proposals, mask_thr_binary=0.5)))

lr_config = dict(policy='step', step=[27, 33])
total_epochs = 36
runner = dict(type='EpochBasedRunnerAmp', max_epochs=total_epochs)
optimizer = dict(paramwise_cfg=dict(custom_keys={'absolute_pos_embed': dict(decay_mult=0.),
                                                 'relative_position_bias_table': dict(decay_mult=0.),
                                                 'norm': dict(decay_mult=0.)}))
# do not use mmdet version fp16
fp16 = None
optimizer_config = dict(
    type="DistOptimizerHook",
    update_interval=1,
    grad_clip=dict(max_norm=1, norm_type=2),
    coalesce=True,
    bucket_size_mb=-1,
    use_fp16=False,
)
