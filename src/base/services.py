
from django.core.exceptions import ValidationError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib




def get_path_upload_avatar(instance, file):
    return f'logo/{instance.id}/{file}'


def validate_size_image(file_obj):
    megabyte_limit = 2
    if file_obj.size > megabyte_limit*1024*1024:
        raise ValidationError(f"Максимальный размер файла {megabyte_limit}МВ")

