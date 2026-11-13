
from flask import Blueprint, send_file, abort, request
from io import BytesIO
from urllib.parse import quote

import qrcode

from database import get_token_by_number


qr_blueprint = Blueprint("qr", __name__)


@qr_blueprint.route("/qr/<token_number>")
def generate_qr(token_number):

    token = get_token_by_number(token_number)

    if not token:
        abort(404)

    host = request.host

    tracking_url = (
        f"http://{host}/track/"
        + quote(token_number)
    )

    qr_image = qrcode.make(tracking_url)

    image_buffer = BytesIO()

    qr_image.save(image_buffer, format="PNG")

    image_buffer.seek(0)

    return send_file(
        image_buffer,
        mimetype="image/png",
        download_name=f"{token_number}_QR.png"
    )
