import pandas as pd
import os

def read_excel(file_path):
    df = pd.read_excel(file_path) # default로 첫번째 시트를 읽음
    # df = pd.read_excel(file_path, sheet_name="") # 시트이름 지정 필요 시 사용
    df_header = df.columns.tolist()
    df_value = df.values.tolist()
    # print(df)
    # print(df.__len__)
    # print(df_header)
    # print(df_value)
    return df_header, df_value

def search_keyword_index_from_df(df_header, keyword):
    # 해당 단어가 포함된 행의 인덱스를 리스트로 반환
    matching_indices = [index for index, row in enumerate(df_header) if keyword in row]
    # print(int(matching_indices[0]))
    return int(matching_indices[0])

def separate_region():
    """
    # 1. 원본 파일의 엑셀 파일을 배열로 읽는다.
    # 2. 배열 내 우편번호 코드를 찾아 수도권or수도권외곽or지방 구분하고 추가배송비 여부를 확인한다. -> 각 배열 마지막에 추가
    """
    org_header, org_value = read_excel(os.path.join('/', 'Users', 'wonjongsoo', 'Downloads', '20241125_주문서취합 개발요청서.xlsx'))
    std_region_header, std_region_value = read_excel(os.path.join('/', 'Users', 'wonjongsoo', 'Downloads', '수도권_지방_등_구분_기준파일.xlsx'))
    postcode = search_keyword_index_from_df(org_header, "우편번호")
    regioncode = search_keyword_index_from_df(std_region_header, "우편번호")
    for row in org_value:
        # print(row)
        matched = False 
        for std in std_region_value:
            # print(row[postcode])
            # print(std[regioncode])
            if row[postcode] == std[regioncode]:
                row.append(std[1])
                row.append(std[2])
                matched = True 
                break 
        if not matched:
            row.append("No matched postcode")
    org_header.append("배송지역구분")
    org_header.append("추가배송비")
    # print(org_value)
    # return org_header, org_value
    calc_fee(org_header, org_value)


def calc_fee(org_header, org_value):
    """
    # 3. 원본 상품코드와 배송비기준파일의 상품코드를 매칭한다.
    # 4. 수도건, 수도권외곽, 지방, 추가배송비 등을 매칭해야 한다.
    """
    std_fee_header, std_fee_value = read_excel(os.path.join('/', 'Users', 'wonjongsoo', 'Downloads', '배송비기준파일.xlsx'))
    org_productcode = search_keyword_index_from_df(org_header, "상품코드")
    std_productcode = search_keyword_index_from_df(std_fee_header, "상품코드")

    delivery_region_standard = search_keyword_index_from_df(org_header, "배송지역구분")
    delivery_add_fee = search_keyword_index_from_df(org_header, "추가배송비")

    std_add_fee = search_keyword_index_from_df(std_fee_header, "추가배송비")
    org_header.append("착불비 합계")
    # 1. 원본 데이터를 한줄씩 가져온다
    for row in org_value:
        matched = False
        # 2. 기준 데이터를 모두 가져와서 한줄씩 비교한다.
        for std_row in std_fee_value:
            # 3. 상품코드 매칭
            if row[org_productcode] == std_row[std_productcode]:
                # 4. 배송지역구분 값 찾아서 기준 데이터의 칼럼 인덱스 찾기
                aa = std_row[search_keyword_index_from_df(std_fee_header, row[delivery_region_standard])]
                # 5. 추가 배송비 칼럼 읽기
                bb = str(row[delivery_add_fee])
                # 6. 추가 배송비 컬럼에 O라고 체크되어 있을 경우, 추가배송비 합산
                if (bb.upper() == "O" or bb == "0"):
                    cc = std_row[std_add_fee]
                    row.append(aa+cc)
                    matched = True 
                    break
        if not matched:
            row.append("No matched 상품코드")    
    print(org_value)
    # return org_value
    make_excel_file(org_header, org_value)

def make_excel_file(org_header, org_value):
    print(org_header)
    print(len(org_value[0]))
    print(len(org_header))
    df = pd.DataFrame(org_value, columns=org_header)
    file_path = os.path.join('/', 'Users', 'wonjongsoo', 'Downloads', 'test.xlsx')
    df.to_excel(file_path, index=False)

if __name__ == '__main__':
    # org_header, org_value = read_excel(os.path.join('/', 'Users', 'wonjongsoo', 'Downloads', '20241125_주문서취합 개발요청서.xlsx'))
    # std_fee_header, std_fee_value = read_excel(os.path.join('/', 'Users', 'wonjongsoo', 'Downloads', '배송비기준파일.xlsx'))
    # std_region_header, std_region_value = read_excel(os.path.join('/', 'Users', 'wonjongsoo', 'Downloads', '수도권_지방_등_구분_기준파일.xlsx'))
    # search_keyword_index_from_df(header, "우편번호")
    # search_keyword_index_from_df(header, "상품코드")
    separate_region()
    # calc_fee()