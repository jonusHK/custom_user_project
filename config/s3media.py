from storages.backends.s3boto3 import S3Boto3Storage
class MediaStorage(S3Boto3Storage):
    location = 'media'
    bucket_name = 'customuserimage.wpsshool.site'
    custom_domain = 'customuserimage.wpsshool.site'
    file_overwrite = False
