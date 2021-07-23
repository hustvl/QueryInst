<div align="center">   

# Instances as Queries
</div>

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/queryinst-parallelly-supervised-mask-query/instance-segmentation-on-coco-minival)](https://paperswithcode.com/sota/instance-segmentation-on-coco-minival?p=queryinst-parallelly-supervised-mask-query)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/queryinst-parallelly-supervised-mask-query/instance-segmentation-on-coco)](https://paperswithcode.com/sota/instance-segmentation-on-coco?p=queryinst-parallelly-supervised-mask-query)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/queryinst-parallelly-supervised-mask-query/object-detection-on-coco-minival)](https://paperswithcode.com/sota/object-detection-on-coco-minival?p=queryinst-parallelly-supervised-mask-query)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/queryinst-parallelly-supervised-mask-query/object-detection-on-coco)](https://paperswithcode.com/sota/object-detection-on-coco?p=queryinst-parallelly-supervised-mask-query)

<div align="center">
  <img width="100%" alt="QueryInst-VIS Demo" src="https://user-images.githubusercontent.com/45201863/120617230-7d34a600-c48c-11eb-8a43-d61689a050be.gif">
</div>

* **TL;DR:** **QueryInst (Instances as Queries)** is a simple and effective query based instance segmentation method driven by parallel supervision on dynamic mask heads, which outperforms previous arts in terms of both accuracy and speed.


* Our QueryTrack (_i.e., Tracking Instances as Queries,_ [tech report](https://arxiv.org/abs/2106.11963)) based on QueryInst won [**the 2nd place** `(AP = 52.3 @ test set, AP = 54.3 @ val set)`](https://competitions.codalab.org/competitions/28988#results) in video instance segmentation (VIS) track with **single online end-to-end model, single scale testing & without using extra video training data** in the [3rd Large-scale Video Object Segmentation Challenge, CVPR 2021](https://youtube-vos.org/challenge/2021/). 


* For the first time, we demonstrate that an end-to-end query based framework driven by parallel supervision is competitive with well-established and highly-optimized methods in a wide range of instance-level recognition tasks ([object detection](https://paperswithcode.com/sota/object-detection-on-coco), [instance segmentation](https://paperswithcode.com/sota/instance-segmentation-on-coco) and video instance segmentation).

#

> [**Instances as Queries**](http://arxiv.org/abs/2105.01928)
>
> by [Yuxin Fang\*](https://scholar.google.com/citations?user=_Lk0-fQAAAAJ&hl=en), [Shusheng Yang\*](https://scholar.google.com/citations?hl=zh-CN&user=v6dmW5cntoMC&view_op=list_works&citft=1&email_for_op=2yuxinfang%40gmail.com&gmla=AJsN-F53CnxYBtSUBs91e_N7uL7139t5ufTWFZ-r8k5oNe1haqf_6f8AE0uyoqnVBPqNG8MGOPH_ep6k_-gMW9KmflOUalJPYu1VTaE2IVjNVn1k-lDjzMEN_oN_a7MySKPieyFEPwMfabczLcR4Qg14seBM3mx6QXUu9Hj5QMZrg9jbKDOGQxxeVX0DJtjiWCGr2ukQgSIR4VVetSaGei48SNUkO8zol-8hApyNYZcUBLD6n9FvTEeE94iLiIbFbNP0m59fh3_z), [Xinggang Wang†](https://xinggangw.info/), [Yu Li](http://yu-li.github.io), [Chen Fang](https://scholar.google.com/citations?hl=en&user=Vu1OqIsAAAAJ&view_op=list_works&citft=1&email_for_op=2yuxinfang%40gmail.com&gmla=AJsN-F5phq2a5UjdoNudoavuaCbem43ptau5cM8rWScWoxkUm0xFgCl6q49r-6MAWh-X9FVZCv9GuLk8D4u-ka0hVjKEWibox_kN9B346lA80Mrl4bUyDHBjwmbvsAfEBZ56neZ0D9p5neQBX8dBp8dD1I3248R0n0vVvzlfILA9oVpcn7xy6P0MQHUY-g0VT2g7sV6LJSPB7ZGyJFGqUk2SJ4MHRxG8U7Hz28WGuobOz-lrTnehfz5wsbwAaLETSZbP3vEMQ3Hc), [Ying Shan](https://scholar.google.com/citations?user=4oXBp9UAAAAJ&hl=en), Bin Feng, [Wenyu Liu](http://eic.hust.edu.cn/professor/liuwenyu/).
>
> (\*) equal contribution, (†) corresponding author.
> 
> *arXiv technical report ([arXiv 2105.01928](http://arxiv.org/abs/2105.01928))*

![QueryInst](resources/QueryInst.png)

* This repo serves as the official implementation for [QueryInst](http://arxiv.org/abs/2105.01928), based on [mmdetection](https://github.com/open-mmlab/mmdetection) and built upon [Sparse R-CNN](https://github.com/PeizeSun/SparseR-CNN) & [DETR](https://github.com/facebookresearch/detr). Implantations based on [Detectron2 ](https://github.com/facebookresearch/detectron2) will be released in the near future.

* This project is under active development, we will extend [QueryInst](http://arxiv.org/abs/2105.01928) to a wide range of instance-level recognition tasks.

#

### Main Results on COCO test-dev

|                            Configs                            |        Aug.         | Weights | Box AP | Mask AP |
| :----------------------------------------------------------: | :----------------: | :-----: | :----: | :-----: |
|              [QueryInst_Swin_L_300_queries (single scale testing)](configs/queryinst/queryinst_swin_large_patch4_window7_fpn_300_proposals_crop_mstrain_400-1200_50e_coco.py)               | 400 ~ 1200, w/ Crop |    [baidu](https://pan.baidu.com/s/1c-5A_XS1L79pBw5J0OlF9w) / [google](https://drive.google.com/file/d/1tqkpaArF0a0WVEolsCC8yrvgoydY7_Ha/view?usp=sharing)    |  [56.1](https://gist.github.com/Yuxin-CV/f477cb2a310e2db2b26112ae0f167baf)  |  [49.1](https://gist.github.com/Yuxin-CV/0e93ec9ab4c2d05be2d8a6cc61cd2f6b)   |


### Main Results on COCO val

|                            Configs                            |        Aug.         | Weights | Box AP | Mask AP |
| :----------------------------------------------------------: | :----------------: | :-----: | :----: | :-----: | 
| [QueryInst\_R50\_3x\_300_queries](configs/queryinst/queryinst_r50_fpn_300_proposals_crop_mstrain_480-800_3x_coco.py) | 480 ~ 800, w/ Crop |    [baidu](https://pan.baidu.com/s/1_WtTSVLLfWzKK7PAvHSylQ) / [google](https://drive.google.com/file/d/1D4Goiwb8BrDBVKkC35xm4ihUpSuF_tCF/view?usp=sharing)    |  46.9  |  41.4   | 
| [QueryInst\_R101\_3x\_300_queries](configs/queryinst/queryinst_r101_fpn_300_proposals_crop_mstrain_480-800_3x_coco.py) | 480 ~ 800, w/ Crop |    [baidu](https://pan.baidu.com/s/1upDlN8SEaTpXyOXWAc9hWg) / [google](https://drive.google.com/file/d/1EYFdoKfMt99uVL2z4hTcSIVA__Z04NKE/view?usp=sharing)    |  48.0  |  42.4   |
|              QueryInst_X101-DCN_3x_300_queries               | 480 ~ 800, w/ Crop |    -    |  50.3  |  44.2   | 
|              [QueryInst_Swin_L_300_queries (single scale testing)](configs/queryinst/queryinst_swin_large_patch4_window7_fpn_300_proposals_crop_mstrain_400-1200_50e_coco.py)          | 400 ~ 1200, w/ Crop |    [baidu](https://pan.baidu.com/s/1c-5A_XS1L79pBw5J0OlF9w) / [google](https://drive.google.com/file/d/1tqkpaArF0a0WVEolsCC8yrvgoydY7_Ha/view?usp=sharing)     |  56.1  |  48.9   |

Notes:
* Accesscode for ```baidu``` is ```QIst```.

### Getting Started

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

### Citation

If you find our paper and code useful in your research, please consider giving a star :star: and citation :pencil: :

```BibTeX
@article{QueryInst,
  title={Instances as Queries},
  author={Fang, Yuxin and Yang, Shusheng and Wang, Xinggang and Li, Yu and Fang, Chen and Shan, Ying and Feng, Bin and Liu, Wenyu},
  journal={arXiv preprint arXiv:2105.01928},
  year={2021}
}
```

```BibTeX
@article{QueryTrack,
  title={Tracking Instances as Queries},
  author={Yang, Shusheng and Fang, Yuxin and Wang, Xinggang and Li, Yu and Shan, Ying and Feng, Bin and Liu, Wenyu},
  journal={arXiv preprint arXiv:2106.11963},
  year={2021}
}
```

### TODO

- [x] QueryInst training and inference code.
- [x] QueryInst with Swin-Transformer and Test-Time-Augmentation.
- [ ] QueryInst based on [Detectron2 toolbox](https://github.com/facebookresearch/detectron2) will be released in the near future.
- [ ] QueryInst configurations for Cityscapes and YouTube-VIS.
- [x] QueryInst pretrain weights.
