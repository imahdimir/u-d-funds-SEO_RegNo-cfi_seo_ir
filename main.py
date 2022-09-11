"""

    """

import pandas as pd
import requests
from githubdata import GithubData
from mirutil.df_utils import save_as_prq_wo_index as sprq


class RepoUrls :
    targ = 'https://github.com/imahdimir/d-funds-SEO_RegNo-cfi_seo_ir'
    cur = 'https://github.com/imahdimir/u-d-funds-SEO_RegNo-cfi_seo_ir'

ru = RepoUrls()

class Urls :
    src = 'https://cfi.rbcapi.ir/institutes?lng=fa&name=&city=&province=&instituteType=6&instituteKind=&activityType=&licenseType=&licenseStatus='

url = Urls()

def main() :
    pass

    ##

    hdrs = {
            'User-Agent' : 'Mozilla/5.0'
            }
    res = requests.get(url.src , headers = hdrs , verify = False)
    ##
    df = pd.DataFrame(res.json())
    ##
    df1 = df.explode('data')
    sr1 = df1['data'].drop_duplicates()
    ##
    for el in sr1 :
        print('"' + el + '":None,')
    ##
    dc1 = {
            "InstituteTypeId" : None ,
            "InstituteType"   : None ,
            "InstituteKindId" : None ,
            "InstituteKind"   : None ,
            "SEORegisterNo"   : None ,
            "Website"         : None ,
            "Name"            : None ,
            "NationalId"      : None ,
            "CEO"             : None ,
            "CEOMobileNo"     : None ,
            "StateId"         : None ,
            "State"           : None ,
            "Id"              : None ,
            }

    ##
    for ky in dc1.keys() :
        df[ky] = df['data'].apply(lambda x : x[ky])

    ##
    df = df.drop(columns = ['data'])

    ##
    df['ObsDate'] = pd.to_datetime('today').date()
    ##
    cols_ord = {
            "SEORegisterNo"   : None ,
            "Name"            : None ,
            "CEO"             : None ,
            "InstituteTypeId" : None ,
            "InstituteType"   : None ,
            "InstituteKindId" : None ,
            "InstituteKind"   : None ,
            "Website"         : None ,
            "NationalId"      : None ,
            "CEOMobileNo"     : None ,
            "StateId"         : None ,
            "State"           : None ,
            "Id"              : None ,
            "ObsDate"         : None ,
            "total"           : None ,
            }

    df = df[cols_ord.keys()]
    ##
    rp_trg = GithubData(ru.targ)
    rp_trg.clone()
    ##
    dfpre = rp_trg.read_data()
    ##
    df = pd.concat([df , dfpre] , ignore_index = True)
    df = df.drop_duplicates()
    ##
    fp = rp_trg.data_fp
    sprq(df , fp)

    ##
    msg = 'updated by: '
    msg += ru.cur
    ##
    rp_trg.commit_and_push(msg)

    ##
    rp_trg.rmdir()

    ##

##
if __name__ == "__main__" :
    main()
