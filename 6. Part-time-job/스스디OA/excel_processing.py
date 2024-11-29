import pandas as pd

def read_excel(file_path):
    """엑셀 파일 읽기"""
    return pd.read_excel(file_path)

def add_shipping_fee(df, fee_data_path, region_data_path):
    """착불비 계산 및 추가"""
    print(df)
    # dfe = pd.read_excel(df)
    fee_data = pd.read_excel(fee_data_path)
    region_data = pd.read_excel(region_data_path)
    
    with open(df) as org:
        dfe = pd.read_csv(org)
        # 예시: 우편번호 기반 수도권/지방 구분
        dfe = dfe.merge(region_data, on='우편번호', how='left')
        dfe['착불비'] = dfe['지역'].map(lambda x: 3000 if x == '수도권' else 5000)

    # return dfe
    print("a")

def split_and_save(df, ssd_file, showbliss_file):
    """스스디/쇼블리스로 데이터 분리 후 저장"""
    ssd_df = df[df['카테고리'] == '스스디']
    showbliss_df = df[df['카테고리'] == '쇼블리스']

    ssd_df.to_excel(ssd_file, index=False)
    showbliss_df.to_excel(showbliss_file, index=False)
