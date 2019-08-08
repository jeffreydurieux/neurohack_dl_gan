

# CycleGAN and pix2pix in PyTorch

This is the copy of PyTorch implementations  by [Jun-Yan Zhu](https://github.com/junyanz) and [Taesung Park](https://github.com/taesung), and supported by [Tongzhou Wang](https://ssnl.github.io/).



**CycleGAN: [Project](https://junyanz.github.io/CycleGAN/) |  [Paper](https://arxiv.org/pdf/1703.10593.pdf) |  [Torch](https://github.com/junyanz/CycleGAN)**


**Pix2pix:  [Project](https://phillipi.github.io/pix2pix/) |  [Paper](https://arxiv.org/pdf/1611.07004.pdf) |  [Torch](https://github.com/phillipi/pix2pix)**


## Prerequisites,   Getting Started Installation
- same as original repo
- base_options.py chenged...
-- chenges: batch norm instead of instance norm
-- edited the channel model
-- generator network has 32 input filters instead of 64 to make the model smaller
-- discriminator is n_layered model it has 6 layered CNN instead of PatchGAN discriminator, we want to use the model as basic as possible PatchGAN may have some clever tricks worth trying.
-- kaiming initialization selected.


### CycleGAN train/test custom data with costumized settings instead of changing the default parsing of the base_options
- assuming the dataset is named as data

- To view training results and loss plots, run `python -m visdom.server` and click the URL http://localhost:8097.
- Train a model:
```bash
#!./scripts/train_cyclegan.sh
python train.py --dataroot ./datasets/data --name mydata --model cycle_gan --input_nc 1 --output_nc 1 --netD n_layers --n_layers_D 6 --norm batch --init_type kaiming --load_size 128 --crop_size 128 --no_flip
```
To see more intermediate results, check out `./checkpoints/maps_cyclegan/web/index.html`.
- Test the model:
```bash
#!./scripts/test_cyclegan.sh
python test.py --dataroot ./datasets/data --name mydata --model cycle_gan --input_nc 1 --no_dropout --output_nc 1 --netD n_layers --n_layers_D 6 --norm batch --init_type kaiming --load_size 128 --crop_size 128 --no_flip
```
- The test results will be saved to a html file here: `./results/maps_cyclegan/latest_test/index.html`.



## The rest is same as CycleGAN page...

That's all for now! :D

MA.

------ reminder from original README.md -----------------
- The option `--model test` is used for generating results of CycleGAN only for one side. This option will automatically set `--dataset_mode single`, which only loads the images from one set. On the contrary, using `--model cycle_gan` requires loading and generating results in both directions, which is sometimes unnecessary. The results will be saved at `./results/`. Use `--results_dir {directory_path_to_save_result}` to specify the results directory.

- For your own experiments, you might want to specify `--netG`, `--norm`, `--no_dropout` to match the generator architecture of the trained model.
----

## Citation
If you use this code for your research, please cite the papers.
```
@inproceedings{CycleGAN2017,
  title={Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networkss},
  author={Zhu, Jun-Yan and Park, Taesung and Isola, Phillip and Efros, Alexei A},
  booktitle={Computer Vision (ICCV), 2017 IEEE International Conference on},
  year={2017}
}


@inproceedings{isola2017image,
  title={Image-to-Image Translation with Conditional Adversarial Networks},
  author={Isola, Phillip and Zhu, Jun-Yan and Zhou, Tinghui and Efros, Alexei A},
  booktitle={Computer Vision and Pattern Recognition (CVPR), 2017 IEEE Conference on},
  year={2017}
}
```




## Acknowledgments
CycleGan code is "inspired" by [pytorch-DCGAN](https://github.com/pytorch/examples/tree/master/dcgan).
