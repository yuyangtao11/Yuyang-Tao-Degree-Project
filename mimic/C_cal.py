import pandas as pd
import numpy as np
import datetime

icd = pd.read_csv('diagnoses_icd.csv', dtype={'icd_code': str})
print(icd.head(5))

charlson_map = {
    'Myocardial_infarction': {
        'icd9': ['410', '412'],
        'icd10': ['I21', 'I22', 'I252']
    },
    'Congestive_heart_failure': {
        'icd9': [
            '428', '40201', '40211', '40291',
            '40401', '40403', '40411', '40413', '40491', '40493'
        ],
        'icd10': [
            'I50', 'I099', 'I110', 'I130', 'I132', 'I255',
            'I420', 'I425', 'I426', 'I427', 'I428', 'I429', 'P290'
        ]
    },
    'Peripheral_vascular_disease': {
        'icd9': [
            '0930', '4373', '440', '441', '4431', '4432',
            '4433', '4434', '4438', '4439', '4471', '5571',
            '5579', 'V434'
        ],
        'icd10': [
            'I70', 'I71', 'I72', 'I73', 'I77', 'I79',
            'K551', 'K558', 'K559', 'Z958', 'Z959'
        ]
    },
    'Cerebrovascular_disease': {
        'icd9': [
            '430', '431', '432', '433', '434', '435',
            '438', '36234'
        ],
        'icd10': [
            'G45', 'G46', 'H340', 'I60', 'I61', 'I62',
            'I63', 'I65', 'I66', 'I67', 'I68', 'I69'
        ]
    },
    'Dementia': {
        'icd9': ['290', '2941', '3312'],
        'icd10': ['F00', 'F01', 'F02', 'F03', 'G30', 'F051']
    },
    'Chronic_pulmonary_disease': {
        'icd9': [
            '490', '491', '492', '493', '494', '495', '496',
            '500', '501', '502', '503', '504', '505', '5064',
            '5081', '5088'
        ],
        'icd10': [
            'J40', 'J41', 'J42', 'J43', 'J44', 'J45', 'J47',
            'P27', 'J60', 'J61', 'J62', 'J63', 'J64', 'J65',
            'J66', 'J67', 'J684', 'J701', 'J703'
        ]
    },
    'Rheumatologic_disease': {
        'icd9': [
            '4465', '7100', '7101', '7102', '7103', '7104',
            '7140', '7141', '7142', '7148', '725'
        ],
        'icd10': [
            'M05', 'M06', 'M315', 'M32', 'M33',
            'M34', 'M351', 'M353', 'M360'
        ]
    },
    'Peptic_ulcer_disease': {
        'icd9': ['531', '532', '533', '534'],
        'icd10': ['K25', 'K26', 'K27', 'K28']
    },
    'Mild_liver_disease': {
        'icd9': [
            '5712', '5714', '5715', '5716', '5718', '5719',
            '5733', '5734', '5738', '5739', 'V427'
        ],
        'icd10': [
            'B18', 'K73', 'K700', 'K701', 'K702', 'K703', 'K709',
            'K717', 'K713', 'K714', 'K715', 'K71', 'K760', 'K762',
            'K763', 'K764', 'K768', 'K769', 'Z944'
        ]
    },
    'Diabetes_without_cc': {
        'icd9': [
            '2500', '2501', '2502', '2503', '2507'
        ],
        'icd10': [
            'E100', 'E109', 'E110', 'E119', 'E120', 'E129',
            'E130', 'E139', 'E140', 'E149'
        ]
    },
    'Diabetes_with_cc': {
        'icd9': [
            '2504', '2505', '2506'
        ],
        'icd10': [
            'E102', 'E103', 'E104', 'E105', 'E106',
            'E107', 'E108', 'E112', 'E113', 'E114',
            'E115', 'E116', 'E117', 'E118', 'E132',
            'E133', 'E134', 'E135', 'E136', 'E137',
            'E138', 'E142', 'E143', 'E144', 'E145',
            'E146', 'E147', 'E148'
        ]
    },
    'Hemiplegia_paraplegia': {
        'icd9': [
            '3341', '342', '343', '3440', '3441', '3442',
            '3443', '3444', '3445', '3446', '3449'
        ],
        'icd10': [
            'G04', 'G81', 'G82', 'G83'
        ]
    },
    'Renal_disease': {
        'icd9': [
            '40301', '40311', '40391', '40402', '40403', '40412',
            '40413', '40492', '40493', '585', '586', '5880',
            'V420', 'V451', 'V56'
        ],
        'icd10': [
            'I12', 'I13', 'N03', 'N05', 'N18', 'N19', 'N25',
            'Z490', 'Z491', 'Z492', 'Z940', 'Z992'
        ]
    },
    'Any_malignancy': {
        'icd9': [
            '140', '141', '142', '143', '144', '145', '146',
            '147', '148', '149', '150', '151', '152', '153',
            '154', '155', '156', '157', '158', '159', '160',
            '161', '162', '163', '164', '165', '170', '171',
            '172', '174', '175', '176', '185', '188', '189',
            '190', '191', '192', '193', '194', '195',
            '200', '201', '202', '203', '204', '205', '206',
            '207', '208', '2386'
        ],
        'icd10': [
            'C00', 'C01', 'C02', 'C03', 'C04', 'C05', 'C06',
            'C07', 'C08', 'C09', 'C10', 'C11', 'C12', 'C13',
            'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20',
            'C21', 'C22', 'C23', 'C24', 'C25', 'C30', 'C31',
            'C32', 'C33', 'C34', 'C37', 'C38', 'C39', 'C40',
            'C41', 'C43', 'C45', 'C46', 'C47', 'C48', 'C49',
            'C50', 'C51', 'C52', 'C53', 'C54', 'C55', 'C56',
            'C57', 'C58', 'C60', 'C61', 'C62', 'C63', 'C64',
            'C65', 'C66', 'C67', 'C68', 'C69', 'C70', 'C71',
            'C72', 'C73', 'C74', 'C75', 'C76', 'C7A', 'C7B',
            'C80', 'C81', 'C82', 'C83', 'C84', 'C85', 'C88',
            'C90', 'C91', 'C92', 'C93', 'C94', 'C95', 'C96',
            'C97', 'D46'
        ]
    },
    'Moderate_severe_liver': {
        'icd9': [
            '4560', '4561', '4562', '5722', '5723', '5724', '5728'
        ],
        'icd10': [
            'I850', 'I859', 'I864', 'I982', 'K704', 'K711',
            'K721', 'K729', 'K765', 'K766', 'K767'
        ]
    },
    'Metastatic_solid_tumor': {
        'icd9': [
            '196', '197', '198', '199'
        ],
        'icd10': [
            'C77', 'C78', 'C79', 'C80'
        ]
    },
    'AIDS_HIV': {
        'icd9': ['042', '043', '044'],
        'icd10': ['B20', 'B21', 'B22', 'B24']
    }
}

charlson_weights = {
    'Myocardial_infarction': 1,
    'Congestive_heart_failure': 1,
    'Peripheral_vascular_disease': 1,
    'Cerebrovascular_disease': 1,
    'Dementia': 1,
    'Chronic_pulmonary_disease': 1,
    'Rheumatologic_disease': 1,
    'Peptic_ulcer_disease': 1,
    'Mild_liver_disease': 1,
    'Diabetes_without_cc': 1,
    'Diabetes_with_cc': 2,
    'Hemiplegia_paraplegia': 2,
    'Renal_disease': 2,
    'Any_malignancy': 2,
    'Moderate_severe_liver': 3,
    'Metastatic_solid_tumor': 6,
    'AIDS_HIV': 6
}


def map_icd_to_charlson(icd_code, icd_version):
    if pd.isnull(icd_code):
        return []

    # Remove extra characters, convert to uppercase for startswith matching
    icd_str = str(icd_code).replace('.', '').strip().upper()

    matched_conditions = []
    for cond_name, dict_code in charlson_map.items():
        if icd_version == 9:
            # Iterate over all icd9 prefixes
            for prefix in dict_code['icd9']:
                prefix_clean = prefix.replace('.', '').upper()
                if icd_str.startswith(prefix_clean):
                    matched_conditions.append(cond_name)
                    break
        elif icd_version == 10:
            # Iterate over all icd10 prefixes
            for prefix in dict_code['icd10']:
                prefix_clean = prefix.replace('.', '').upper()
                if icd_str.startswith(prefix_clean):
                    matched_conditions.append(cond_name)
                    break

    # de-duplication
    matched_conditions = list(set(matched_conditions))

    return matched_conditions


# Charlson Comorbidity Index
cci_results = []

# Collect comorbidity entries for all diagnoses, grouped by hadm_id
for hadm_id, subdf in icd.groupby('hadm_id'):
    comorbid_set = set()
    for idx, row in subdf.iterrows():
        icdcode = row['icd_code']
        icdver = row['icd_version']
        matched_conds = map_icd_to_charlson(icdcode, icdver)
        for cond_name in matched_conds:
            comorbid_set.add(cond_name)

    # Count the sum of weights corresponding to all comorbidity for hospitalization
    cci_score = 0
    for cond_name in comorbid_set:
        if cond_name in charlson_weights:
            cci_score += charlson_weights[cond_name]

    if cci_score >= 4:
        cci_score = 5

    cci_results.append({
        'hadm_id': hadm_id,
        'Comorbidity': cci_score
    })

# convert to DataFrame
df_cci = pd.DataFrame(cci_results)
print(df_cci.head(5))

# merge
df_lace = pd.read_csv('merged_with_readmission_with_LACE.csv')
merged = pd.merge(df_lace, df_cci, on='hadm_id', how='left')
cols = merged.columns.tolist()
if 'Comorbidity' in cols:
    cols.insert(5, cols.pop(cols.index('Comorbidity')))
df_merged = merged[cols]

df_merged.to_csv('merged_with_LACE.csv', index=False)

df = pd.read_csv("merged_with_LACE.csv")

# LACE
df["LACE"] = df["Length"] + df["Acuity"] + df["Comorbidity"] + df["E"]

cols = df.columns.tolist()
cols.remove("LACE")
cols.insert(7, "LACE")
df = df[cols]

df.to_csv("merged_with_LACE.csv", index=False)