import os
import random
import string
import boto3
from botocore.exceptions import ClientError

from enum import Enum
from datetime import datetime
from app.core.config import  settings

class STRING_TYPES(Enum):
    def __str__(self):
        return str(self.value)

    NUMBER = string.digits
    ASCII = string.ascii_letters
    ASCII_LOWER = string.ascii_lowercase
    ASCII_UPPER = string.ascii_uppercase
    ASCII_LOWER_NUMBER = string.ascii_lowercase + string.digits
    ASCII_UPPER_NUMBER = string.ascii_uppercase + string.digits
    ALPHA_NUMBER = string.ascii_letters + string.digits
    ALL = string.ascii_letters + string.digits + "!#$%&()*+-;<=>?@^_`{|}~."


def nonce(str_length=6, ty=STRING_TYPES.NUMBER):
    """
    문자숫자형 nonce
    """
    chars = ty.value
    random.seed = (os.urandom(1024))
    return (''.join(random.choice(chars) for _ in range(str_length)))


def make_image_file_path(upload_path, file):
    now = datetime.now()
    upload_format = "%Y%m%d%H%M"
    extension = {"image/jpeg": ".jpeg", "image/jpg" : ".jpg", "image/gif" : ".gif", "image/png" : ".png" }

    file_extension = extension.get(file.content_type)

    if file_extension:
        # 업로드 경로
        filename = now.strftime(upload_format) + nonce(8) + extension.get(file.content_type)
        full_path = upload_path + "/" + filename
    else:
        filename = now.strftime(upload_format) + nonce(8)
        full_path = upload_path + "/" + filename
    return {
        "filename": filename,
        "full_path": full_path
    }


def s3_upload(obj, upload_path):
    """
    s3 파일 업로드
    """

    # S3 클라이언트 생성.
    s3 = boto3.client(
        "s3",
        aws_access_key_id=settings.S3_AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.S3_AWS_SECRET_ACCESS_KEY,
    )

    try:
        s3.upload_fileobj(
            obj.file,
            settings.S3_BUCKET,
            upload_path,
            ExtraArgs={
                "ContentType": obj.content_type,
                "ContentEncoding": "base64",
                "ACL": "public-read",
            },
        )
    except ClientError as e:
        raise e
        return False

    return True