import boto3
import json
import schedule
import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# AWS Route 53 클라이언트 생성
client = boto3.client('route53')

def get_records_name_and_ip():
    # 모든 레코드의 RecordName과 IP를 가져오는 함수
    hosted_zones = client.list_hosted_zones().get('HostedZones', [])
    result = []

    for zone in hosted_zones:
        zone_id_raw = zone.get('Id')
        if not zone_id_raw:
            logging.warning(f"Zone missing ID: {zone}")
            continue  # 건너뜀
        zone_id = zone_id_raw.split('/')[-1]

        # 해당 호스팅 영역의 레코드 가져오기
        records = client.list_resource_record_sets(HostedZoneId=zone_id)['ResourceRecordSets']
        
        for record in records:
            # IP 주소 또는 레코드 값이 존재할 경우에만 추가
            if 'ResourceRecords' in record:
                result.append({
                    "RecordName": record['Name'],
                    "IP": [r['Value'] for r in record['ResourceRecords']]
                })
                
    logging.info("모든 레코드와 IP 가져오기")
    return result

def save_records_to_json():
    # 모든 레코드와 IP 가져오기
    all_records = get_records_name_and_ip()

    # JSON 파일로 저장
    with open("route53_records.json", "w") as f:
        json.dump(all_records, f, indent=4)
        logging.info("JSON 파일로 저장")
    
    print("Route 53 records saved to 'route53_records.json'")

if __name__ == "__main__":
    # 스케줄링: 매 시간마다 실행
    schedule.every(1).hours.do(save_records_to_json)
    logging.info("Scheduled task to run every hour.")
    
    # 스케줄 유지
    while True:
        schedule.run_pending()
        time.sleep(1)
