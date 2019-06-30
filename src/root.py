from kotano import proxy
from static import env
from static import about
from static import sections
from static import cdnlink
from static import bucketname
from urllib.parse import parse_qs

from io import BytesIO

import boto3
import json
import hashlib
import time


@proxy("html")
def root(request):
    modal = False
    modaltext = ""
    if request.method.lower() == "post":
        ip = request.context.get("identity", {}).get("sourceIp", "")
        q = parse_qs(request.data)
        name = q.get("name", [""])[0]
        email = q.get("email", [""])[0]
        body = q.get("body", [""])[0]
        data = {
                "name": name,
                "email": email,
                "body": body,
                "ip": ip,
                "asctime": time.asctime(),
                "unixtime": time.time()}

        try:
            upload(data)
            modaltext = "Message stored successfully!"
        except Exception as e:
            modaltext = str(e)
        modal = True

    template = env.get_template("index.html")
    return template.render(
            about=about,
            sections=sections,
            cdnlink=cdnlink,
            modal=modal,
            modaltext=modaltext)


def upload(data):
    s3 = boto3.client('s3')
    s = json.dumps(data).encode()
    buf = BytesIO(s)
    key = hashlib.sha256(s).hexdigest()[:8]
    now = time.localtime()
    year = now.tm_year
    mon = now.tm_mon
    day = now.tm_mday
    stamp = f"{year}{mon:02}{day:02}"
    s3.upload_fileobj(buf, bucketname, f"emails/{stamp}/{key}")
