_base_ = 'queryinst_swin_tiny_patch4_window7_fpn_100_proposals_crop_mstrain_480-800_3x_coco.py'

num_proposals = 300
model = dict(
    pretrained=None,
    backbone=dict(
        _delete_=True,
        type='SwinTransformer',
        embed_dim=192,
        depths=[2, 2, 18, 2],
        num_heads=[6, 12, 24, 48],
        window_size=7,
        mlp_ratio=4.,
        qkv_bias=True,
        qk_scale=None,
        drop_rate=0.,
        attn_drop_rate=0.,
        drop_path_rate=0.3,
        ape=False,
        patch_norm=True,
        out_indices=(0, 1, 2, 3),
        use_checkpoint=False),
    neck=dict(
        type='FPN',
        in_channels=[192, 384, 768, 1536],
        out_channels=256,
        num_outs=4),
    rpn_head=dict(num_proposals=num_proposals),
    test_cfg=dict(
        _delete_=True, rpn=None, rcnn=dict(max_per_img=num_proposals, mask_thr_binary=0.5)))
