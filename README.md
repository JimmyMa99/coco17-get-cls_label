# coco17-get-cls_label

Click [here](https://cocodataset.org/#download) to download COCO Dataset.
And you can see the [COCO API](https://github.com/cocodataset/cocoapi).

Get cls_label.npy to train [PSA](https://github.com/jiwoon-ahn/psa), [IRN](https://github.com/jiwoon-ahn/irn) and [EPS](https://github.com/halbielee/EPS).

Please fill in the path as required in the code.

You can use this code to get json information in any COCO dataset format and convert it to onehot labels.
## Installation
- Python
- numpy

## Some adaptation work
- [PSA](https://github.com/jiwoon-ahn/psa)
Please create a new folder named coco, like [psa/voc12/](https://github.com/jiwoon-ahn/psa/tree/master/voc12),
then put .npy in ./coco

- [IRN](https://github.com/jiwoon-ahn/irn)
Please create a new folder named coco, like [irn/voc12/](https://github.com/jiwoon-ahn/irn/tree/master/voc12),
then put .npy in ./coco

- [EPS](https://github.com/halbielee/EPS)
Please put .npy in [EPS/metadata/coco/](https://github.com/halbielee/EPS/tree/main/metadata/coco) to train.

## Download the result
If you want to use the cls_label.npy of coco17 with 80(thing)+90(stuff) classes, please click [here (Google drive)](https://drive.google.com/file/d/1B_Dlx7FqtohgWmHduiIY-qAIqcBT3-zt/view?usp=sharing).

