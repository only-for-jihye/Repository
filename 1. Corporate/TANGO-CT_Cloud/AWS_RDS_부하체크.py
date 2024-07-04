# 2023.04.06

import boto3
import pandas as pd
from datetime import datetime, timedelta

# AWS 인증 정보 설정
session = boto3.Session(
    aws_access_key_id='ACCESS_KEY',
    aws_secret_access_key='SECRET_KEY',
    region_name='REGION'
)

# CloudWatch Logs Insights 클라이언트 생성
insights_client = session.client('logs')

# 조회 대상 로그 그룹 및 쿼리
log_group_name = 'your-log-group-name'
query_string = 'fields @timestamp, @message | sort @timestamp desc | limit 100'

# 조회 기간 설정
end_time = datetime.now()
start_time = end_time - timedelta(days=7)

# CloudWatch Logs Insights 쿼리 실행
response = insights_client.start_query(
    logGroupName=log_group_name,
    queryString=query_string,
    startTime=int(start_time.timestamp() * 1000),
    endTime=int(end_time.timestamp() * 1000)
)

# 쿼리 실행 결과 확인
query_id = response['queryId']
query_status = insights_client.get_query_results(
    queryId=query_id
)

while query_status['status'] == 'Running':
    query_status = insights_client.get_query_results(
        queryId=query_id
    )

if query_status['status'] == 'Complete':
    query_results = query_status['results']
    data = []

    for result in query_results:
        timestamp = result[0]['value']
        query_time = result[1]['value']
        data.append([timestamp, query_time])

    # 결과 데이터를 pandas DataFrame으로 변환
    df = pd.DataFrame(data, columns=['Timestamp', 'QueryTime'])
    df['QueryTime'] = pd.to_numeric(df['QueryTime'])
    df = df.nlargest(10, 'QueryTime')

    # 결과 데이터를 엑셀 파일로 출력
    writer = pd.ExcelWriter('query_times_top10.xlsx')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()
else:
    print("Query status is not 'Complete'.")