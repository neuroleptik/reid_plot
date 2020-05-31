# Reid plot tool
## Code to transform two input images to reidentification pyplt PNG  
![210](https://user-images.githubusercontent.com/46196875/83356833-e90b9c80-a368-11ea-8e46-a167509204bf.png)
This is an example of what you can get as output.

# Installation

Python version : 3.7.6 (can works on older versions)

```
git clone https://github.com/neuroleptik/reid_plot.git
cd reid_plot/
pip install torch torchvision
pip install -r requirements.txt

```
# Execution

To execute the script, please specify the two input images as follows :

```
python ./reid_plot.py path/to/img1.xxx path/to/other/img.xxx

```

# Packages used

I mainly used [torchreid](https://github.com/KaiyangZhou/deep-person-reid) package to train and infer on test phase.
Model is trained with [Duke_MTMC](https://megapixels.cc/duke_mtmc/) dataset 

# Remerciements

Thanks to Kaiyang Zhou who built torchreid.
Thanks to Computer Science Department, Duke University, Durham, US for sharing their datasets
