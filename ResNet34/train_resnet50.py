from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import zipfile
import tqdm
import glob
import os
os.environ["CUDA_VISIBLE_DEVICES"]="0,1,2"
import sys
import shutil
from fastai.vision import *
import fastai
#from gradcam import *

from fastprogress.fastprogress import force_console_behavior

#import fastprogress
#fastprogress.fastprogress.NO_BAR = True
master_bar, progress_bar = force_console_behavior()
fastai.basic_train.master_bar, fastai.basic_train.progress_bar = master_bar, progress_bar


path2zip = '/home/tako/Chloe_test/kfood2/'
path2classes = 'train_classes.csv'
batch_size = 32
stage1_epochs = 30
stage2_epochs = 10

def get_parent_dir(f):
  return os.path.split(os.path.split(f)[0])[-1]
            
def train():
    cls_df = pd.read_csv(path2classes, index_col=0)
    train_classes = sorted(list(cls_df.query('use > 0').class_name))
    print('number of train_classes', len(train_classes))
        
    np.random.seed(42)
    tfms = get_transforms(do_flip=True, flip_vert=True, max_rotate=0.20, max_zoom=1.3, max_warp=0.0, max_lighting=0.2)
    il = (ImageList.from_folder(path2zip)
          .filter_by_func(lambda f: get_parent_dir(f) in train_classes)
          .split_by_rand_pct(valid_pct=0.2, seed=42)
          .label_from_func(lambda f: get_parent_dir(f))
          .transform(tfms=tfms)
          )
    data = (ImageDataBunch.create_from_ll(il, bs=batch_size,
                                         size=224,
                                         num_workers=4)
            .normalize(imagenet_stats)
            )
    print(len(data.classes), data.c, len(data.train_ds), len(data.valid_ds))

    
    learn = (cnn_learner(data, models.resnet34, metrics=accuracy)
             .mixup(alpha=0.2)
             )
    learn.loss_func = LabelSmoothingCrossEntropy()
    learn.fit_one_cycle(stage1_epochs, max_lr=1e-3)
    #learn.save('stage-1')
    learn.unfreeze()
    learn.fit_one_cycle(stage2_epochs, max_lr=slice(1e-6,3e-6))
    #learn.save('stage-2')
    # learn.export('210206_model.pkl')
    learn.export(os.path.abspath('/home/tako/Chloe_test/211213_model_resnet50_100epochs.pkl'))
    interp = ClassificationInterpretation.from_learner(learn)
    df_cm = pd.DataFrame(interp.confusion_matrix(), index=data.classes,
                         columns=data.classes)
    df_cm.to_csv('conf_matrix_211213_resnet50_100epochs.csv',encoding='utf-8-sig')
if __name__ == '__main__':
    train()
    
    
    
