import json
import boto3

class Control_Json:
    def __init__(self, file_path):
        self.json_data = None

        self.file_path = file_path

    def file_load(self):
        with open(self.file_path, "r", encoding='utf-8') as file:
            self.json_data = json.load(file)

    def get_key_data(self):
        key_path = "./config/key.json"
        with open(key_path, "r", encoding='utf-8') as file:
            data = json.load(file)

        return data
    
    def save_json_file(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(self.json_data, ensure_ascii=False, indent=4))

    def write_json(self, file_data):
        #파일경로 그냥 self에서 끌어다 쓰기
        pass

    def get_s3_obj(self):
        data = self.get_key_data()
        aws_access_key_id = data["aws"]["aws_access_key_id"]
        aws_secret_access_key = data["aws"]["aws_secret_access_key"]
        region_name = data["aws"]["region_name"]

        s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
        
        return s3

    def upload_json(self, s3_file_path):
        s3 = self.get_s3_obj()
        bucket_name = self.get_key_data()["aws"]["bucket_name"]

        s3.put_object(Body=open(self.file_path, 'rb'), Bucket=bucket_name, Key=s3_file_path)

    def load_json(self, s3_file_path):
        s3 = self.get_s3_obj()
        bucket_name = self.get_key_data()["aws"]["bucket_name"]

        file_obj = s3.get_object(Bucket=bucket_name, Key=s3_file_path)
        file_content = file_obj['Body'].read().decode('utf-8')
        self.json_data = json.loads(file_content)
