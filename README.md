# QueryInst: Parallelly Supervised Mask Query for Instance Segmentation

* TL;DR: QueryInst is a simple and effective query based instance segmentation method driven by parallel supervision on dynamic mask heads, which outperforms previous arts in terms of both accuracy and speed.

> [QueryInst: Parallelly Supervised Mask Query for Instance Segmentation](http://arxiv.org/abs/2105.01928
),
>
> by [Yuxin Fang\*](https://scholar.google.com/citations?user=_Lk0-fQAAAAJ&hl=en), Shusheng Yang\*, [Xinggang Wang†](https://xinggangw.info/), [Yu Li](http://yu-li.github.io), [Chen Fang](https://scholar.google.com/citations?hl=en&user=Vu1OqIsAAAAJ&view_op=list_works&citft=1&email_for_op=2yuxinfang%40gmail.com&gmla=AJsN-F5phq2a5UjdoNudoavuaCbem43ptau5cM8rWScWoxkUm0xFgCl6q49r-6MAWh-X9FVZCv9GuLk8D4u-ka0hVjKEWibox_kN9B346lA80Mrl4bUyDHBjwmbvsAfEBZ56neZ0D9p5neQBX8dBp8dD1I3248R0n0vVvzlfILA9oVpcn7xy6P0MQHUY-g0VT2g7sV6LJSPB7ZGyJFGqUk2SJ4MHRxG8U7Hz28WGuobOz-lrTnehfz5wsbwAaLETSZbP3vEMQ3Hc), [Ying Shan](https://scholar.google.com/citations?user=4oXBp9UAAAAJ&hl=en), Bin Feng, [Wenyu Liu](http://eic.hust.edu.cn/professor/liuwenyu/).
>
> (\*) equal contribution, (†) corresponding author.

![QueryInst](resources/QueryInst.png)

This repo serves as an official implementation for QueryInst, based on [mmdetection](https://github.com/open-mmlab/mmdetection) and build upon [Sparse R-CNN](https://github.com/PeizeSun/SparseR-CNN) & [DETR](https://github.com/facebookresearch/detr).

## Updates
[06/05/2021] 🌟 QueryInst training and inference code has been released!

## Getting Started

* Our project is mainly developed on [mmdetection toolbox `(931d96)`](https://github.com/open-mmlab/mmdetection), please refer to the [mmdetection official installation](https://github.com/open-mmlab/mmdetection/blob/master/docs/get_started.md).
* Install `QueryInst` by:

```bash
python setup.py develop
```

* Prepare datasets:

```bash
mkdir data && cd data
ln -s /path/to/coco coco
```

* Training QueryInst with single GPU:

```bash
python tools/train.py configs/queryinst/queryinst_r50_fpn_1x_coco.py
```

* Training QueryInst with multi GPUs:

```bash
./tools/dist_train.sh configs/queryinst/queryinst_r50_fpn_1x_coco.py 8
```

* Test QueryInst on COCO val set with single GPU:

```bash
python tools/test.py configs/queryinst/queryinst_r50_fpn_1x_coco.py PATH/TO/CKPT.pth --eval bbox segm
```

* Test QueryInst on COCO val set with multi GPUs:

```bash
./tools/dist_test.sh configs/queryinst/queryinst_r50_fpn_1x_coco.py PATH/TO/CKPT.pth 8 --eval bbox segm
```

## Main Results on COCO val

|                            Method                            |        Aug         | Weights | Box AP | Mask AP |
| :----------------------------------------------------------: | :----------------: | :-----: | :----: | :-----: |
| [QueryInst\_R50\_3x\_300_queries](configs/queryinst/queryinst_r50_fpn_300_proposals_crop_mstrain_480-800_3x_coco.py) | 480 ~ 800, w/ Crop |    -    |  46.9  |  41.4   |
| [QueryInst\_R101\_3x\_300_queries](configs/queryinst/queryinst_r101_fpn_300_proposals_crop_mstrain_480-800_3x_coco.py) | 480 ~ 800, w/ Crop |    -    |  48.0  |  42.4   |
|              QueryInst_X101-DCN_3x_300_queries               | 480 ~ 800, w/ Crop |    -    |  50.3  |  44.2   |

## Citation

If you find our paper and code useful in your research, please consider giving a star :star: and citation :pencil: :

```BibTeX
@article{QueryInst,
  title={QueryInst: Parallelly Supervised Mask Query for Instance Segmentation},
  author={Fang, Yuxin and Yang, Shusheng and Wang, Xinggang and Li, Yu and Fang, Chen and Shan, Ying and Feng, Bin and Liu, Wenyu},
  journal={arXiv preprint arXiv:2105.01928},
  year={2021}
}
```

## TODO

- [x] QueryInst training and inference code.
- [ ] QueryInst based on Detectron2 toolbox will be released in the near future.
- [ ] QueryInst configurations for Cityscapes and YouTube-VIS.
- [ ] QueryInst pretrain weights.
