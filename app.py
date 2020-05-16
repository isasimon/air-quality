from framework.flask.app import app


if __name__ == '__main__':
    app.run()


"""def s3_read():
    bucket = S3("openaq-fetches")
    files = bucket.get_object_list('realtime/2013-11-26/')
    [print(i.key) for i in files]"""
