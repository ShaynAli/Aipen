from activities import MachineLearningActivity
import quandl
from _datetime import date, timedelta
import pdb
import numpy as np
from datetime import date
from dateutil.relativedelta import relativedelta


# region All tickers

fse_tickers = [
    '1COV_X',
    '2HR_X',
    'AAD_X',
    'AB1_X',
    'ADS_X',
    'ADV_X',
    'AFX_X',
    'AIR_X',
    'AIXA_X',
    'ALV_X',
    'ANN_X',
    'AOX_X',
    'ARL_X',
    'B5A_X',
    'BAF_X',
    'BAS_X',
    'BAYN_X',
    'BBZA_X',
    'BC8_X',
    'BDT_X',
    'BEI_X',
    'BIO3_X',
    'BMW_X',
    'BNR_X',
    'BOSS_X',
    'BYW6_X',
    'CBK_X',
    'CEV_X',
    'CLS1_X',
    'COK_X',
    'COM_X',
    'CON_X',
    'COP_X',
    'CWC_X',
    'DAI_X',
    'DB1_X',
    'DBAN_X',
    'DBK_X',
    'DEQ_X',
    'DEX_X',
    'DEZ_X',
    'DIC_X',
    'DLG_X',
    'DPW_X',
    'DRI_X',
    'DRW3_X',
    'DTE_X',
    'DUE_X',
    'DWNI_X',
    'EOAN_X',
    'EON_X',
    'EVD_X',
    'EVK_X',
    'EVT_X',
    'FIE_X',
    'FME_X',
    'FNTN_X',
    'FPE3_X',
    'FRA_X',
    'FRE_X',
    'G1A_X',
    'GBF_X',
    'GFJ_X',
    'GFK_X',
    'GIL_X',
    'GLJ_X',
    'GMM_X',
    'GSC1_X',
    'GWI1_X',
    'GXI_X',
    'HAB_X',
    'HAW_X',
    'HBH3_X',
    'HDD_X',
    'HEI_X',
    'HEN3_X',
    'HHFA_X',
    'HNR1_X',
    'HOT_X',
    'IFX_X',
    'INH_X',
    'JEN_X',
    'JUN3_X',
    'KBC_X',
    'KCO_X',
    'KD8_X',
    'KGX_X',
    'KRN_X',
    'KU2_X',
    'KWS_X',
    'LEG_X',
    'LEO_X',
    'LHA_X',
    'LIN_X',
    'LPK_X',
    'LXS_X',
    'MAN_X',
    'MEO_X',
    'MLP_X',
    'MOR_X',
    'MRK_X',
    'MTX_X',
    'MUV2_X',
    'NDA_X',
    'NDX1_X',
    'NEM_X',
    'NOEJ_X',
    'O1BC_X',
    'O2C_X',
    'O2D_X',
    'OSR_X',
    'P1Z_X',
    'PFV_X',
    'PMOX_X',
    'PSAN_X',
    'PSM_X',
    'PUM_X',
    'QIA_X',
    'QSC_X',
    'RAA_X',
    'RHK_X',
    'RHM_X',
    'RRTL_X',
    'RWE_X',
    'S92_X',
    'SAP_X',
    'SAX_X',
    'SAZ_X',
    'SBS_X',
    'SDF_X',
    'SFQ_X',
    'SGL_X',
    'SIE_X',
    'SIX2_X',
    'SKB_X',
    'SKYD_X',
    'SLT_X',
    'SOW_X',
    'SPR_X',
    'SRT3_X',
    'SW1_X',
    'SY1_X',
    'SZG_X',
    'SZU_X',
    'TEG_X',
    'TIM_X',
    'TKA_X',
    'TLX_X',
    'TTI_X',
    'TTK_X',
    'TUI1_X',
    'UTDI_X',
    'VIB3_X',
    'VNA_X',
    'VOS_X',
    'VOW3_X',
    'VT9_X',
    'WAC_X',
    'WCH_X',
    'WDI_X',
    'WIN_X',
    'ZIL2_X',
    'ZO1_X'
]

# endregion


class FrankfurtStockPrediction(MachineLearningActivity):

    years = [year for year in range(2000, 2020)]
    months = [month for month in range(1, 13)]

    default_tickers = [
        'AIXA_X',
        'ALV_X',
        'BAS_X',
        'BAYN_X',
        'BEI_X',
        'BMW_X',
        'CBK_X'
    ]

    default_guess_tickers = ['CON_X']

    def __init__(self, tickers=default_tickers, guess_tickers=default_guess_tickers):
        quandl.ApiConfig.api_key = 'z3rsXS2rz9ZXCe76xozE'
        self.code = 'FSE'
        self.tickers = tickers
        self.guess_tickers = guess_tickers

    def x_shape(self):
        return len(self.tickers), None

    def y_shape(self):
        return len(self.guess_tickers), None

    def next_data(self):
        from random import choice
        year = choice(FrankfurtStockPrediction.years)
        month = choice(FrankfurtStockPrediction.months)
        day = 18
        date_format = '%Y-%m-%d'
        start_date = date(year=year, month=month, day=day)
        end_date = start_date + relativedelta(months=1)
        start_date_str = start_date.strftime(date_format)
        end_date_str = end_date.strftime(date_format)

        ticker_data = []
        for ticker in self.tickers:
            print(f'Getting stock data for {ticker}')
            ticker_data.append(self.get_ticker(ticker, start_date=start_date_str, end_date=end_date_str))

        guess_ticker_data = []
        for ticker in self.guess_tickers:
            print(f'Getting stock data for {ticker}')
            guess_ticker_data.append(self.get_ticker(ticker, start_date=start_date_str, end_date=end_date_str))

        tickers = np.vstack(ticker_data)
        guess_tickers = np.vstack(guess_ticker_data)

        return tickers, guess_tickers

    def get_ticker(self, ticker, start_date, end_date, field='Open'):
        return quandl.get(f'{self.code}/{ticker}', returns='numpy', start_date=start_date, end_date=end_date)[field]


if __name__ == '__main__':
    activity = FrankfurtStockPrediction()
    data = [activity.next_data() for _ in range(3)]
    pdb.set_trace()
