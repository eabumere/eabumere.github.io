import pandas as pd
import requests as rq
import json
from io import StringIO
from pandas import json_normalize


try:
    from __config__ import __username__, __password__, __url__, __indicatorType__
except ImportError:
    from .__config__ import __username__, __password__, __url__, __indicatorType__


class main:
    numerator = ''

    def __init__(self, dhis_uname=None, dhis_pwd=None, url=None, inputFiles=None, outPutFileA=None):
        self.dhis_uname = dhis_uname
        self.dhis_pwd = dhis_pwd
        self.url = url
        self.inputFiles = inputFiles
        self.outPutFileA = outPutFileA


    def extractPI(self):
        uids = pd.read_csv('OPD Final PIs V2.2.2.csv')
        listofUuids = list(uids['programIndicators.id'].unique())
        f1 = open('Part 3.1a_Infolink PIs.json')  # open the json file
        data1 = json.load(f1)  # load as json
        f1list = []
        f1.close()
        f2 = open('Part 3.1b_Infolink PIs.json')  # open the json file
        data2 = json.load(f2)  # load as json
        f2list = []
        f2.close()
        f3 = open('Part 3.1c_Infolink PIs.json')  # open the json file
        data3 = json.load(f3)  # load as json
        f3list = []
        f3.close()
        f4 = open('Part 3.1d_Infolink PIs & PI groups.json')  # open the json file
        data4 = json.load(f4)  # load as json
        f4list = []
        f4.close()

        f5 = open('Part 3.2_MER PIs and PI groups.json')  # open the json file
        data5 = json.load(f5)  # load as json
        f5list = []
        f5.close()
        for n in data1['programIndicators']:
            if n['id'] in listofUuids:
                f1list.append(n)
        jsonready = {"programIndicators": f1list}
        with open('PI_1s.json', 'w') as fp:
            json.dump(jsonready, fp)

        for n in data2['programIndicators']:
            if n['id'] in listofUuids:
                f2list.append(n)
        jsonready = {"programIndicators": f2list}
        with open('PI_2s.json', 'w') as fp:
            json.dump(jsonready, fp)

        for n in data3['programIndicators']:
            if n['id'] in listofUuids:
                f3list.append(n)
        jsonready = {"programIndicators": f3list}
        with open('PI_3s.json', 'w') as fp:
            json.dump(jsonready, fp)

        for n in data4['programIndicators']:
            if n['id'] in listofUuids:
                f4list.append(n)
        jsonready = {"programIndicators": f4list}
        with open('PI_4s.json', 'w') as fp:
            json.dump(jsonready, fp)

        for n in data5['programIndicators']:
            if n['id'] in listofUuids:
                f5list.append(n)
        jsonready = {"programIndicators": f5list}
        with open('PI_5s.json', 'w') as fp:
            json.dump(jsonready, fp)

        flist = f1list + f2list + f3list + f4list + f5list
        print(flist)
        jsonready = {"programIndicators":  flist}
        with open('PIs.json', 'w') as fp:
            json.dump(jsonready, fp)

    def extractInd(self):
        uids = pd.read_csv('OPD Final Indicators V2.2.2.csv')
        listofUuids = list(uids['Column1.id'].unique())
        f1 = open('Part 4.1a_Infolink INDs.json')  # open the json file
        data1 = json.load(f1)  # load as json
        f1list = []
        f1.close()

        f2 = open('Part 4.1b_Infolink INDs and IND groups.json')  # open the json file
        data2 = json.load(f2)  # load as json
        f2list = []
        f2.close()

        f3 = open('Part 4.2_MER INDs and IND Groups.json')  # open the json file
        data3 = json.load(f3)  # load as json
        f3list = []
        f3.close()

        for n in data1['indicators']:
            if n['id'] in listofUuids:
                f1list.append(n)
        jsonready = {"indicators": f1list}
        with open('Ind1.json', 'w') as fp:
            json.dump(jsonready, fp)

        for n in data2['indicators']:
            if n['id'] in listofUuids:
                f2list.append(n)
        jsonready = {"indicators": f2list}
        with open('Ind2.json', 'w') as fp:
            json.dump(jsonready, fp)

        for n in data3['indicators']:
            if n['id'] in listofUuids:
                f3list.append(n)
        jsonready = {"indicators": f3list}
        with open('Ind3.json', 'w') as fp:
            json.dump(jsonready, fp)

        flist = f1list + f2list + f3list
        print(flist)
        jsonready = {"indicators":  flist}
        with open('indicators.json', 'w') as fp:
            json.dump(jsonready, fp)



    def extractPIGroup(self):
        uids = pd.read_csv('OPD Final PIs V2.2.2.csv')
        listofUuids = list(uids['programIndicators.id'].unique())
        f4 = open('Part 3.2_MER PIs and PI groups.json')  # open the json file
        data4 = json.load(f4)  # load as json
        f4list = []
        # Removing irrelevant PI Groups
        for PI_groups in data4['programIndicatorGroups']:
            for PIs in PI_groups['programIndicators']:
                if PIs['id'] in listofUuids:
                    if PI_groups not in f4list:
                        f4list.append(PI_groups)

        neededPIs = []
        individualPIsCreated = []
        extracted = []
        n = 0
        for cleanedPIGroup in f4list:
            print(n)
            for PIs in cleanedPIGroup['programIndicators']:
                if PIs['id'] in listofUuids:
                    if [d for d in f4list[n]['programIndicators'] if
                        d['id'] in listofUuids] not in individualPIsCreated:
                        neededPIs.append(
                            {
                                "access": f4list[n]['access'],
                                "externalAccess": f4list[n]['externalAccess'],
                                "favorite": f4list[n]['favorite'],
                                "id": f4list[n]['id'],
                                "name": f4list[n]['name'],
                                "programIndicators": [d for d in f4list[n]['programIndicators'] if
                                                      d['id'] in listofUuids],
                                "publicAccess": f4list[n]['publicAccess']
                            }
                        )
                        individualPIsCreated.append(
                            [d for d in f4list[n]['programIndicators'] if d['id'] in listofUuids])
            n = n + 1
        jsonready = {"programIndicatorGroups": neededPIs}
        with open('programIndicatorGroups_MER.json', 'w') as fp:
            json.dump(jsonready, fp)

    def extractIndGroup(self):
        uids = pd.read_csv('OPD Final Indicators V2.2.2.csv')
        listofUuids = list(uids['Column1.id'].unique())
        f4 = open('Part 4.2_MER INDs and IND Groups.json')  # open the json file
        data4 = json.load(f4)  # load as json
        f4list = []
        #Removing irrelevant PI Groups
        for PI_groups in data4['indicatorGroups']:
            for PIs in PI_groups['indicators']:
                if PIs['id'] in listofUuids:
                    if PI_groups not in f4list:
                        f4list.append(PI_groups)



        neededPIs = []
        individualPIsCreated = []
        n = 0
        for cleanedPIGroup in f4list:
            print(n)
            for PIs in cleanedPIGroup['indicators']:
                    if PIs['id'] in listofUuids:
                        if [d for d in f4list[n]['indicators'] if d['id'] in listofUuids] not in individualPIsCreated:
                            neededPIs.append(
                                {
                                    "access": f4list[n]['access'],
                                    "externalAccess": f4list[n]['externalAccess'],
                                    "favorite": f4list[n]['favorite'],
                                    "id": f4list[n]['id'],
                                    "name": f4list[n]['name'],
                                    "indicators": [d for d in f4list[n]['indicators'] if
                                                          d['id'] in listofUuids],
                                    "publicAccess": f4list[n]['publicAccess']
                                }
                            )
                            individualPIsCreated.append(
                                [d for d in f4list[n]['indicators'] if d['id'] in listofUuids])
            n = n + 1
        jsonready = {"indicatorGroups": neededPIs}
        with open('IndicatorGroups_MER.json', 'w') as fp:
            json.dump(jsonready, fp)


if __name__ == "__main__":
    push = main()
    # push.extractPI()
    # push.extractPIGroup()
    # push.extractIndGroup()
    push.extractInd()