#先用此程式進行yolo轉txt的格式,再用traintestsplit分割8:2 (不過class 0 會消失 所以要用產生的txt路徑檔回來抓標籤 不能用他自動產生好的標籤集)

from xml.dom.minidom import Document
import os
import cv2
import numpy as np

def cv_imread(filePath):
    cv_img=cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
    ## imdecode读取的是rgb，如果后续需要opencv处理的话，需要转换成bgr，转换后图片颜色会变化
    ##cv_img=cv2.cvtColor(cv_img,cv2.COLOR_RGB2BGR)
    return cv_img

# def makexml(txtPath, xmlPath, picPath):  # txt所在文件夹路径，xml文件保存路径，图片所在文件夹路径
def makexml(picPath, txtPath, xmlPath):  # txt所在文件夹路径，xml文件保存路径，图片所在文件夹路径
    """此函数用于将yolo格式txt标注文件转换为voc格式xml标注文件
    在自己的标注图片文件夹下建三个子文件夹分别命名为picture、txt、xml
    """
    dic = {'0':'0_Chromis_fumea',
    '1':'1_Pomacentrus_coelestis',
    '2':'2_Dascyllus_trimaculatus',
    '3':'3_Chromis_notata',
    '4':'4_Chaetodon_auripes',
    '5':'5_Coradion_altivelis',
    '6':'6_Chaetodon_octofasciatus',
    '7':'7_Chaetodon_kleinii',
    '8':'8_Heniochus_singularius',
    '9':'9_Heniochus_acuminatus',
    '10':'10_Chaetodon_weibeli',
    '11':'11_Chaetodon_auriga',
    '12':'12_Chaetodon_lunula',
    '13':'13_Chaetodon_lunulatus',
    '14':'14_Scarus_ghobban',
    '15':'15_Chlorurus_japanensis',
    '16':'16_Scarus_schlegeli',
    '17':'17_Chlorurus_sordidus',
    '18':'18_Scarus_rivulatus',
    '19':'19_Cephalopholis_boenak',
    '20':'20_Diploprion_bifasciatum',
    '21':'21_Pseudanthias_squamipinnis',
    '22':'22',
    '23':'23_Cheilinus_chlorourus',
    '24':'24_Halichoeres_melanochir',
    '25':'25_Oxycheilinus_unifasciatus',
    '26':'26_Stethojulis_terina',
    '27':'27_Labroides_dimidiatus',
    '28':'28_Bodianus_diana',
    '29':'29_Hemigymnus_fasciatus',
    '30':'30_Thalassoma_lunare',
    '31':'31_Cirrhilabrus_cyanopleura',
    '32':'32_Pteragogus_aurigarius',
    '33':'33_Bodianus_mesothorax',
    '34':'34_Choerodon_azurio',
    '35':'35_Pseudolabrus_eoethinus',
    '36':'36_Choerodon_schoenleinii',
    '37':'37_Aulostomus_chinensis',
    '38':'38_Chelonia_mydas',
    '39':'39_Diodon_holocanthus',
    '40':'40_Diodon_liturosus',
    '41':'41_Diodon_eydouxi',
    '42':'42_Prionurus_scalprum',
    '43':'43_Acanthurus_dussumieri',
    '44':'44_Scolopsis_vosmeri',
    '45':'45_Centropyge_vrolikii',
    '46':'46_Chaetodontoplus_septentrionalis',
    '47':'47_Scorpaenopsis_diabolus',
    '48':'48_Dendrochirus_zebra',
    '49':'49_Pterocaesio_digramma',
    '50':'50_Lethrinus_nebulosus',
    '51':'51_Sufflamen_bursa',
    '52':'52_Canthigaster_axiologus',
    '53':'53_Gymnothorax_thyrsoideus',
    '54':'54_Lutjanus_russellii',
    '55':'55_Lutjanus_vitta',
    '56':'56_Pervagor_janthinosoma',
    '57':'57_Ostracion_cubicus',
    '58':'58_Octopus_cyanea',
    '59':'59_Sepia_pharaonis',
    '60':'60_Parupeneus_multifasciatus',
    '61':'61_Pomacanthus_semicirculatus',
    '62':'62_Oplegnathus_punctatus',
    '63':'63_Synodus_variegatus',
    '64':'64_Microcanthus_strigatus',
    '65':'65_Hybrid_Epinephelus',
    '66':'66_Other_Serranidae',
    '67':'67_Other_Lutjanidae',
    '68':'68_Other_Chaetodontidae',
    '69':'69_Other_Scaridae',
    '70':'70_Cromileptes_altivelis',
    '71':'71_Cheilinus_undulatus',
    '72':'72_Bolbometopon_muricatum',
    '73':'73_Heniochus_diphreutes',
    '74':'74_Petroscirtes_breviceps',
    '75':'75_Oxycheilinus_digramma',
    '76':'76_unknown',
    '77':'77_Lutjanus_lutjanus',
    '78':'78_Chaetodon_speculum',
    '79':'79_Stephanolepis_cirrhifer',
    '80':'80_Planiliza_macrolepis',
    '81':'81_Diagramma_pictum',
    '82':'82_Canthigaster_rivulata',
    '83':'83_Monacanthus_chinensis',
    '84':'84_Siganus_fuscescens',
    '85':'85_Gymnothorax_favagineus',
    '86':'86_Echeneis_naucrates',
    '87':'87_Mugil_cephalus',
    '88':'88_Plectropomus_leopardus',
    '89':'89_Parupeneus_indicus',
    '90':'90_Parupeneus_ciliatus',
    '91':'91_Amblygobius_phalaena',
    '92':'92_Thalassoma_jansenii',
    '93':'93_Thalassoma_lutescens',
    '94':'94_Abudefduf_sexfasciatus',
    '95':'95_Scarus_rubroviolaceus',
    '96':'96_Lethrinus_nebulosus',
    '97':'97_Lutjanus_kasmira',
    '98':'98_Lutjanus_quinquelineatus',
    '99':'99_Gymnothorax_eurostus',
    '100':'100_Octopus_cyanea'
     }
    # if '0' in dic: #確認是否有抓到
    #     print(dic['0'])
    # else:
    #     print('not exist') 
        
        # '0': "0_EP",  # 创建字典用来对类型进行转换
        #    '1': "1_Lu",
        #     '2': "2_Pl",
        #     '3': "3_Sc",
        #     '4': "4_Cr",
        #     '5': "5_others",
        #     '6': "6_Pc",
        #     '7': "7_Cf",# 此处的字典要与自己的classes.txt文件中的类对应，且顺序要一致
           
           #0_Ep','1_Lu','2_Pl','3_Sc','4_Cr','5_others','6_Pc','7_Cf'
           
    files = os.listdir(txtPath)
    for i, name in enumerate(files):
        xmlBuilder = Document()
        annotation = xmlBuilder.createElement("annotation")  # 创建annotation标签
        xmlBuilder.appendChild(annotation)
        txtFile = open(txtPath + name)
        txtList = txtFile.readlines()
        img = cv_imread(picPath + name[0:-4] + ".jpg")
        Pheight, Pwidth, Pdepth = img.shape
 
        folder = xmlBuilder.createElement("folder")  # folder标签
        foldercontent = xmlBuilder.createTextNode("driving_annotation_dataset")
        folder.appendChild(foldercontent)
        annotation.appendChild(folder)  # folder标签结束
 
        filename = xmlBuilder.createElement("filename")  # filename标签
        filenamecontent = xmlBuilder.createTextNode(name[0:-4] + ".jpg")
        filename.appendChild(filenamecontent)
        annotation.appendChild(filename)  # filename标签结束
 
        size = xmlBuilder.createElement("size")  # size标签
        width = xmlBuilder.createElement("width")  # size子标签width
        widthcontent = xmlBuilder.createTextNode(str(Pwidth))
        width.appendChild(widthcontent)
        size.appendChild(width)  # size子标签width结束
 
        height = xmlBuilder.createElement("height")  # size子标签height
        heightcontent = xmlBuilder.createTextNode(str(Pheight))
        height.appendChild(heightcontent)
        size.appendChild(height)  # size子标签height结束
 
        depth = xmlBuilder.createElement("depth")  # size子标签depth
        depthcontent = xmlBuilder.createTextNode(str(Pdepth))
        depth.appendChild(depthcontent)
        size.appendChild(depth)  # size子标签depth结束
 
        annotation.appendChild(size)  # size标签结束
 
        for j in txtList:
            oneline = j.strip().split(" ")
            object = xmlBuilder.createElement("object")  # object 标签
            picname = xmlBuilder.createElement("name")  # name标签
            namecontent = xmlBuilder.createTextNode(dic[oneline[0]])
            picname.appendChild(namecontent)
            object.appendChild(picname)  # name标签结束
 
            pose = xmlBuilder.createElement("pose")  # pose标签
            posecontent = xmlBuilder.createTextNode("Unspecified")
            pose.appendChild(posecontent)
            object.appendChild(pose)  # pose标签结束
 
            truncated = xmlBuilder.createElement("truncated")  # truncated标签
            truncatedContent = xmlBuilder.createTextNode("0")
            truncated.appendChild(truncatedContent)
            object.appendChild(truncated)  # truncated标签结束
 
            difficult = xmlBuilder.createElement("difficult")  # difficult标签
            difficultcontent = xmlBuilder.createTextNode("0")
            difficult.appendChild(difficultcontent)
            object.appendChild(difficult)  # difficult标签结束
 
            bndbox = xmlBuilder.createElement("bndbox")  # bndbox标签
            xmin = xmlBuilder.createElement("xmin")  # xmin标签
            mathData = int(((float(oneline[1])) * Pwidth + 1) - (float(oneline[3])) * 0.5 * Pwidth)
            xminContent = xmlBuilder.createTextNode(str(mathData))
            xmin.appendChild(xminContent)
            bndbox.appendChild(xmin)  # xmin标签结束
 
            ymin = xmlBuilder.createElement("ymin")  # ymin标签
            mathData = int(((float(oneline[2])) * Pheight + 1) - (float(oneline[4])) * 0.5 * Pheight)
            yminContent = xmlBuilder.createTextNode(str(mathData))
            ymin.appendChild(yminContent)
            bndbox.appendChild(ymin)  # ymin标签结束
 
            xmax = xmlBuilder.createElement("xmax")  # xmax标签
            mathData = int(((float(oneline[1])) * Pwidth + 1) + (float(oneline[3])) * 0.5 * Pwidth)
            xmaxContent = xmlBuilder.createTextNode(str(mathData))
            xmax.appendChild(xmaxContent)
            bndbox.appendChild(xmax)  # xmax标签结束
 
            ymax = xmlBuilder.createElement("ymax")  # ymax标签
            mathData = int(((float(oneline[2])) * Pheight + 1) + (float(oneline[4])) * 0.5 * Pheight)
            ymaxContent = xmlBuilder.createTextNode(str(mathData))
            ymax.appendChild(ymaxContent)
            bndbox.appendChild(ymax)  # ymax标签结束
 
            object.appendChild(bndbox)  # bndbox标签结束
 
            annotation.appendChild(object)  # object标签结束
 
        f = open(xmlPath + name[0:-4] + ".xml", 'w')
        xmlBuilder.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')
        f.close()
 
if __name__ == "__main__":
    picPath = "C://Users//alana//Project//VOCdevkit//VOC2007//JPEGImages/"  # 图片所在文件夹路径，后面的/一定要带上
    txtPath = "C://Users//alana//Project//VOCdevkit//VOC2007//YOLO/"  # txt所在文件夹路径，后面的/一定要带上
    xmlPath = "C://Users//alana//Aigo//VOCdevkit//VOC2007//Annotations/"  # xml文件保存路径，后面的/一定要带上
    makexml(picPath, txtPath, xmlPath)

