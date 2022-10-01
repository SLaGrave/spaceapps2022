import requests
import re
import zipfile
import io
import json
import logging

def request_juno_cam_img(share_link: str) -> dict:
    """
    Parameters
    ----------
    share_link: `str` for the share link from the juno cam database

    Returns
    -------
    `dict` of filenames including thumbnail, metadata, and images
    """
    try:
        raw_html = requests.get(share_link)
    except Exception as err:
        logging.warning(err)
        return
    if not raw_html.ok:
        logging.warning(f"Failed request with response: {raw_html.status_code}")
        return
    img_str = f'<a href="(.*?)" target'
    img_ids = re.findall(img_str, raw_html.text)
    if len(img_ids) < 3:
        logging.warning(f"Failed request: bad endpoint")
        return

    thumbnail_id = img_ids[0]
    metadata_id = img_ids[1]
    image_set_id = img_ids[2]
    database_url = "https://www.missionjuno.swri.edu/"
    
    # Metadata
    metadata_data = requests.get(database_url + metadata_id)
    metadata_zip = zipfile.ZipFile(io.BytesIO(metadata_data.content))

    with metadata_zip.open(metadata_zip.infolist()[0]) as m:
        metadata_json = json.loads(m.read())
        data_set_id = metadata_json["DATA_SET_ID"]

    output_dir = f"./tmp/{data_set_id}/"
    metadata_zip.extractall(output_dir)

    # Thumbnail
    thumbnail_data = requests.get(database_url + thumbnail_id)
    thumbnail_dir = f"{output_dir}Thumbnail.png"
    with open(thumbnail_dir, "wb") as f:
        f.write(thumbnail_data.content)

    # Image set
    image_set_data = requests.get(database_url + image_set_id)
    image_set_zip = zipfile.ZipFile(io.BytesIO(image_set_data.content))
    image_set_zip.extractall(output_dir)

    filenames = {
        "thumbnail": thumbnail_dir,
        "metadata": f"{output_dir}DataSet",
        "imageset": f"{output_dir}ImageSet",
    }

    return filenames