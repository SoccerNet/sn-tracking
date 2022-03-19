import glob
import os.path as osp


def gen_image_list(dataPath, datType, image_list_root='./image_lists'):
    inputPath = f'{dataPath}/images/{datType}'
    pathList = glob.glob(inputPath + '/*')
    pathList = sorted(pathList)
    allImageList = []
    for pathSingle in pathList:
        imgList = sorted(glob.glob(osp.join(pathSingle, 'img1', '*.jpg')))
        for imgPath in imgList:
            allImageList.append(imgPath)
    image_list_fname = osp.join(image_list_root, f'{dataPath}.{datType}'.lower())
    with open(image_list_fname, 'w') as image_list_file:
        allImageListStr = str.join('\n', allImageList)
        image_list_file.write(allImageListStr)


if __name__ == '__main__':
    dataPath = 'SN'
    datType = 'train'
    gen_image_list(dataPath, datType)
    datType = 'test'
    gen_image_list(dataPath, datType)
