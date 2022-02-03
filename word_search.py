
import pandas as pd

def word_search(report):
    path_to_file = "/Users/krishkapoor/Documents/radiopaedia_embedding_2020/data/articles.csv"
    data = pd.read_csv(path_to_file, encoding ='utf-8')
    report = report.lower()
    key_terms = []
    for index, title in data.title.iteritems():
        title = title.lower()
        title_length = len(title)
        title = title[:-1]
        if str(title) in str(report):
            key_terms.append(title)
    return key_terms

def label_search(report):
    path_to_file = "/Users/krishkapoor/Documents/radiopaedia_embedding_2020/data/label_for_title.csv"
    data = pd.read_csv(path_to_file, encoding ='utf-8')
    key_terms = word_search(report)
    key_labels = []
    for index, title in data.Title.iteritems():
        title = title.lower()
        title = title[:-1]
        if str(title) in key_terms:
            if data.Label[index] not in key_labels:
                key_labels.append(data.Label[index])
    return key_labels


#report = report.replace(title, title + " (" + data.loc[index].link + ")")
input1 = """CT ABDOMEN/PELVIS WITH CONTRAST - 2020-12-03
INDICATION:
CT ABDOMEN/PELVIS WITH CONTRAST 12/3/2020 2:20 AM
CLINICAL HISTORY: abd pain, sepsis, diarrhea, c/f intraabd source Locally advanced urothelial cancer on Pembro, new watery diarrhea
COMPARISON: CT abdomen/pelvis on 10/19/2020 and CT chest dated 9/23/2020
TECHNIQUE: Following the administration of 150 cc of Omnipaque 350, contiguous 1.25-mm collimation axial images were obtained through the abdomen and pelvis. Coronal and sagittal reformats were also obtained.
CONTRAST MEDIA: Intravenous iodinated contrast
FINDINGS:
Visualized lung bases: 4 mm right middle lung nodule (series 3 image 3) and cyst (3 image 1). Bibasilar atelectasis. Coronary artery atherosclerosis.
Liver: Mild intrahepatic biliary dilatation, progressed from prior exam. Unchanged hepatic dome hypodensity measuring up to 1.2 cm. No new lesions.
Gallbladder: Cholelithiasis without evidence of acute cholecystitis. Fundal adenomyomatosis.
Spleen: Unremarkable
Pancreas: Unremarkable
Adrenal Glands: Similar-appearing indeterminate left adrenal nodule measuring approximately 2.0 x 2.0 cm. Right adrenal gland is unremarkable.
Kidneys: Bilateral percutaneous nephrostomy tubes are noted to be in the bilateral inferior pole calyces. No hydronephrosis. Bilateral striated nephrograms. Interval resolution of the previously seen left urothelial enhancement. Masslike enhancement and thickening involving the entire extent of the right ureter.
GI Tract: Scattered colonic diverticula without evidence of diverticulitis.
Vasculature: Moderate atherosclerotic disease of the abdominal aorta and its branches. Similar-appearing right common iliac artery aneurysm status post endovascular aorta biiliac repair with extension into the right external iliac artery. Redemonstration of right internal iliac artery embolization coils.
Lymphadenopathy: Enlarged, hyperenhancing, centrally necrotic right inguinal lymph node measuring up to 2.0 cm in its shortest dimension, previously 1.4 cm. An additional hyperenhancing right inguinal lymph node measures up to 1.1 cm in short axis, previously 0.6 cm. Interval enlargement of multiple prominent retroperitoneal lymph nodes, for example a left periaortic lymph node measures up to 6 mm (3 image 81) previously 4 mm.
Peritoneum: Mesenteric edema and mild peritoneal thickening.
Bladder: Significant interval progression of patient's known urothelial carcinoma with markedly bladder wall circumferential nodular thickening and enhancement with extension along the entire extent of the right ureter and into the proximal left ureter. This mass is now noted to extend anteriorly to involve perineum and the penile cavernosa spongiosa, left more than right. Progressed extension of the mass posteriorly which is now noted to invade the prostate and the serosal surface of the anterior rectal wall. The mass also extends posteriorly along the bilateral pelvic sidewalls and invading the bilateral obturator internus and externus muscles, right greater than left, causing destruction of the bilateral inferior pubic rami, right greater than left, and extends through the right sciatic foramen. The right internal iliac artery and vein appear to be separate from this mass and are patent. Enhancing left scrotal nodule is new since prior exam and measures 1.4 x 1.0 cm (3 image 24).
Reproductive organs: The large bladder mass is noted to invade the prostate and proximal penis as detailed above. Prostatic brachytherapy seeds.
Bones: Interval increase in extent of invasion of the urothelial carcinoma to the pubic symphysis and bilateral inferior pubic rami, right greater than left. This is increased osseous destruction puts the patient at risk for pathological fracture. Degenerative changes of the spine with grade 1 retrolisthesis of L3 on L4.
Extraperitoneal soft tissues: Unremarkable
Lines/drains/medical devices: None
IMPRESSION:
1. Marked interval worsening of locoregional urothelial carcinoma with enlarging bladder mass extending into the right lesser and greater sciatic foramina, base of the penis and perineum. Soft tissue enhancement of the proximal right ureter suggestive of upper tract metastasis. Enlarging nodal metastases.
2. Increased osseous destruction of pubic symphysis and bilateral inferior pubic rami by the large bladder mass, right greater than left, at risk for pathological fracture.
3. Bilateral percutaneous nephrostomy tubes stable in position. No hydronephrosis."""
input2 = """CT ABDOMEN/PELVIS WITH AND WITHOUT CONTRAST - 2021-07-28
CLINICAL HISTORY: right renal cell carcinoma,
COMPARISON: External CT dated February 25, 2021 external MR dated June 22, 2020
TECHNIQUE: CT of the abdomen and pelvis was performed.
CONTRAST MEDIA: Yes
FINDINGS:
Visualized lung bases: Unremarkable
Liver: Unremarkable
Gallbladder: Not visualized.
Spleen: Unremarkable
Pancreas: Unremarkable
Adrenal Glands: Unremarkable
Kidneys: There is a 1.4 cm exophytic lesion arising from the upper pole of the right kidney which measures 60 Hounsfield units on precontrast images and 70 Hounsfield units on postcontrast images.
When compared to the prior MR this likely represents a hyperdense cyst.
There is a complex cystic mass in the upper pole of the right kidney which measures up to 4.4 cm on the current study compared to 3.8 cm on the MR dated June 22, 2020 and approximately 3.7 cm on the noncontrast CT dated February 25, 2021. This abuts the renal sinus. This demonstrates thick septations and enhancing components concerning for a cystic renal cell carcinoma, Bosniak 4.
GI Tract: Status post gastric bypass
Vasculature: Unremarkable
Lymphadenopathy: There are multiple borderline enlarged retroperitoneal lymph nodes which do not appear significantly changed in size since the MR dated June 22, 2020. The largest is just adjacent to the left renal vein measuring 1 cm in short axis, stable.
Peritoneum: No ascites
Bladder: Unremarkable
Reproductive organs: Unremarkable
Bones: No suspicious lesions. Degenerative disc disease in the spine.
Extraperitoneal soft tissues: Unremarkable
Lines/drains/medical devices: None
IMPRESSION:
1. There is a complex cystic mass in the upper pole of the right kidney which measures up to 4.4 cm on the current study compared to 3.8 cm on the previous studies.This demonstrates thick septations and enhancing components concerning for a cystic renal cell carcinoma, Bosniak 4.
2. Multiple borderline retroperitoneal lymph nodes are stable. No definite evidence of metastatic disease in the abdomen or pelvis. """
def label_match(input1, input2):
    input1_labels = label_search(input1)
    input2_labels = label_search(input2)
    matches = []
    for i in input1_labels:
        if i in input2_labels:
            matches.append(i)
    return matches
def term_match(input1, input2):
    input1_terms = word_search(input1)
    input2_terms = word_search(input2)
    matches = []
    for i in input1_terms:
        if i in input2_terms:
            matches.append(i)
    return matches
def main(input1, input2):
    terms_matched = term_match(input1, input2)
    labels_matched = label_match(input1, input2)
    distance = len(terms_matched) * 2 + len(labels_matched)
    return distance
print(main(input1, input2))




# This is the output
#{'aorta': 'https://radiopaedia.org/articles/aorta?lang=us', 'cancer': 'https://radiopaedia.org/articles/cancer?lang=us', 'cyst': 'https://radiopaedia.org/articles/cyst?lang=us', 'ear': 'https://radiopaedia.org/articles/ear?lang=us', 'exposure': 'https://radiopaedia.org/articles/exposure?lang=us', 'great vessels': 'https://radiopaedia.org/articles/great-vessels?lang=us', 'heart': 'https://radiopaedia.org/articles/heart?lang=us', 'images': 'https://radiopaedia.org/articles/images?lang=us', 'lung': 'https://radiopaedia.org/articles/lung?lang=us', 'lymph': 'https://radiopaedia.org/articles/lymph?lang=us', 'mediastinum': 'https://radiopaedia.org/articles/mediastinum-1?lang=us', 'pelvis': 'https://radiopaedia.org/articles/pelvis-1?lang=us', 'pericardial effusion': 'https://radiopaedia.org/articles/pericardial-effusion?lang=us', 'pleura': 'https://radiopaedia.org/articles/pleura?lang=us', 'pleural effusion': 'https://radiopaedia.org/articles/pleural-effusion?lang=us', 'pneumothorax': 'https://radiopaedia.org/articles/pneumothorax?lang=us', 'right middle lobe': 'https://radiopaedia.org/articles/right-middle-lobe?lang=us', 'right upper lobe': 'https://radiopaedia.org/articles/right-upper-lobe?lang=us', 'thoracic aorta': 'https://radiopaedia.org/articles/thoracic-aorta?lang=us', 'thorax': 'https://radiopaedia.org/articles/thorax-1?lang=us'}
