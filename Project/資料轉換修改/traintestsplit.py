#標籤0會消失 尚未找到原因


import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import random
from shutil import copyfile
 
classes = ['0_Chromis_fumea','1_Pomacentrus_coelestis','2_Dascyllus_trimaculatus','3_Chromis_notata','4_Chaetodon_auripes',
'5_Coradion_altivelis',
'6_Chaetodon_octofasciatus',
'7_Chaetodon_kleinii',
'8_Heniochus_singularius',
'9_Heniochus_acuminatus',
'10_Chaetodon_weibeli',
'11_Chaetodon_auriga',
'12_Chaetodon_lunula',
'13_Chaetodon_lunulatus',
'14_Scarus_ghobban',
'15_Chlorurus_japanensis',
'16_Scarus_schlegeli',
'17_Chlorurus_sordidus',
'18_Scarus_rivulatus',
'19_Cephalopholis_boenak',
'20_Diploprion_bifasciatum',
'21_Pseudanthias_squamipinnis',
'22',
'23_Cheilinus_chlorourus',
'24_Halichoeres_melanochir',
'25_Oxycheilinus_unifasciatus',
'26_Stethojulis_terina',
'27_Labroides_dimidiatus',
'28_Bodianus_diana',
'29_Hemigymnus_fasciatus',
'30_Thalassoma_lunare',
'31_Cirrhilabrus_cyanopleura',
'32_Pteragogus_aurigarius',
'33_Bodianus_mesothorax',
'34_Choerodon_azurio',
'35_Pseudolabrus_eoethinus',
'36_Choerodon_schoenleinii',
'37_Aulostomus_chinensis',
'38_Chelonia_mydas',
'39_Diodon_holocanthus',
'40_Diodon_liturosus',
'41_Diodon_eydouxi',
'42_Prionurus_scalprum',
'43_Acanthurus_dussumieri',
'44_Scolopsis_vosmeri',
'45_Centropyge_vrolikii',
'46_Chaetodontoplus_septentrionalis',
'47_Scorpaenopsis_diabolus',
'48_Dendrochirus_zebra',
'49_Pterocaesio_digramma',
'50_Lethrinus_nebulosus',
'51_Sufflamen_bursa',
'52_Canthigaster_axiologus',
'53_Gymnothorax_thyrsoideus',
'54_Lutjanus_russellii',
'55_Lutjanus_vitta',
'56_Pervagor_janthinosoma',
'57_Ostracion_cubicus',
'58_Octopus_cyanea',
'59_Sepia_pharaonis',
'60_Parupeneus_multifasciatus',
'61_Pomacanthus_semicirculatus',
'62_Oplegnathus_punctatus',
'63_Synodus_variegatus',
'64_Microcanthus_strigatus',
'65_Hybrid_Epinephelus',
'66_Other_Serranidae',
'67_Other_Lutjanidae',
'68_Other_Chaetodontidae',
'69_Other_Scaridae',
'70_Cromileptes_altivelis',
'71_Cheilinus_undulatus',
'72_Bolbometopon_muricatum',
'73_Heniochus_diphreutes',
'74_Petroscirtes_breviceps',
'75_Oxycheilinus_digramma',
'76_unknown',
'77_Lutjanus_lutjanus',
'78_Chaetodon_speculum',
'79_Stephanolepis_cirrhifer',
'80_Planiliza_macrolepis',
'81_Diagramma_pictum',
'82_Canthigaster_rivulata',
'83_Monacanthus_chinensis',
'84_Siganus_fuscescens',
'85_Gymnothorax_favagineus',
'86_Echeneis_naucrates',
'87_Mugil_cephalus',
'88_Plectropomus_leopardus',
'89_Parupeneus_indicus',
'90_Parupeneus_ciliatus',
'91_Amblygobius_phalaena',
'92_Thalassoma_jansenii',
'93_Thalassoma_lutescens',
'94_Abudefduf_sexfasciatus',
'95_Scarus_rubroviolaceus',
'96_Lethrinus_nebulosus',
'97_Lutjanus_kasmira',
'98_Lutjanus_quinquelineatus',]
#classes=["ball"]
 
TRAIN_RATIO = 90
 
def clear_hidden_files(path):
    dir_list = os.listdir(path)
    for i in dir_list:
        abspath = os.path.join(os.path.abspath(path), i)
        if os.path.isfile(abspath):
            if i.startswith("._"):
                os.remove(abspath)
        else:
            clear_hidden_files(abspath)
 
def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
 
def convert_annotation(image_id):
    in_file = open('VOCdevkit/VOC2007/Annotations/%s.xml' %image_id)
    out_file = open('VOCdevkit/VOC2007/YOLOLabels/%s.txt' %image_id, 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
 
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
    in_file.close()
    out_file.close()
 
wd = os.getcwd()
wd = os.getcwd()
data_base_dir = os.path.join(wd, "VOCdevkit/")
if not os.path.isdir(data_base_dir):
    os.mkdir(data_base_dir)
work_sapce_dir = os.path.join(data_base_dir, "VOC2007/")
if not os.path.isdir(work_sapce_dir):
    os.mkdir(work_sapce_dir)
annotation_dir = os.path.join(work_sapce_dir, "Annotations/")
if not os.path.isdir(annotation_dir):
        os.mkdir(annotation_dir)
clear_hidden_files(annotation_dir)
image_dir = os.path.join(work_sapce_dir, "JPEGImages/")
if not os.path.isdir(image_dir):
        os.mkdir(image_dir)
clear_hidden_files(image_dir)
yolo_labels_dir = os.path.join(work_sapce_dir, "YOLOLabels/")
if not os.path.isdir(yolo_labels_dir):
        os.mkdir(yolo_labels_dir)
clear_hidden_files(yolo_labels_dir)
yolov5_images_dir = os.path.join(data_base_dir, "images/")
if not os.path.isdir(yolov5_images_dir):
        os.mkdir(yolov5_images_dir)
clear_hidden_files(yolov5_images_dir)
yolov5_labels_dir = os.path.join(data_base_dir, "labels/")
if not os.path.isdir(yolov5_labels_dir):
        os.mkdir(yolov5_labels_dir)
clear_hidden_files(yolov5_labels_dir)
yolov5_images_train_dir = os.path.join(yolov5_images_dir, "train/")
if not os.path.isdir(yolov5_images_train_dir):
        os.mkdir(yolov5_images_train_dir)
clear_hidden_files(yolov5_images_train_dir)
yolov5_images_test_dir = os.path.join(yolov5_images_dir, "val/")
if not os.path.isdir(yolov5_images_test_dir):
        os.mkdir(yolov5_images_test_dir)
clear_hidden_files(yolov5_images_test_dir)
yolov5_labels_train_dir = os.path.join(yolov5_labels_dir, "train/")
if not os.path.isdir(yolov5_labels_train_dir):
        os.mkdir(yolov5_labels_train_dir)
clear_hidden_files(yolov5_labels_train_dir)
yolov5_labels_test_dir = os.path.join(yolov5_labels_dir, "val/")
if not os.path.isdir(yolov5_labels_test_dir):
        os.mkdir(yolov5_labels_test_dir)
clear_hidden_files(yolov5_labels_test_dir)
 
train_file = open(os.path.join(wd, "yolov5_train.txt"), 'w')
test_file = open(os.path.join(wd, "yolov5_val.txt"), 'w')
train_file.close()
test_file.close()
train_file = open(os.path.join(wd, "yolov5_train.txt"), 'a')
test_file = open(os.path.join(wd, "yolov5_val.txt"), 'a')
list_imgs = os.listdir(image_dir) # list image files
prob = random.randint(1, 100)
print("Probability: %d" % prob)
for i in range(0,len(list_imgs)):
    path = os.path.join(image_dir,list_imgs[i])
    if os.path.isfile(path):
        image_path = image_dir + list_imgs[i]
        voc_path = list_imgs[i]
        (nameWithoutExtention, extention) = os.path.splitext(os.path.basename(image_path))
        (voc_nameWithoutExtention, voc_extention) = os.path.splitext(os.path.basename(voc_path))
        annotation_name = nameWithoutExtention + '.xml'
        annotation_path = os.path.join(annotation_dir, annotation_name)
        label_name = nameWithoutExtention + '.txt'
        label_path = os.path.join(yolo_labels_dir, label_name)
    prob = random.randint(1, 100)
    print("Probability: %d" % prob)
    if(prob < TRAIN_RATIO): # train dataset
        if os.path.exists(annotation_path):
            train_file.write(image_path + '\n')
            convert_annotation(nameWithoutExtention) # convert label
            copyfile(image_path, yolov5_images_train_dir + voc_path)
            copyfile(label_path, yolov5_labels_train_dir + label_name)
    else: # test dataset
        if os.path.exists(annotation_path):
            test_file.write(image_path + '\n')
            convert_annotation(nameWithoutExtention) # convert label
            copyfile(image_path, yolov5_images_test_dir + voc_path)
            copyfile(label_path, yolov5_labels_test_dir + label_name)
train_file.close()
test_file.close()