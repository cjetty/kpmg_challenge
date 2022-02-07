import requests
from optparse import OptionParser
import json

aws_meta_link = "http://169.254.169.254/latest/meta-data/"


def get_instance_meta_data(meta_link, result, meta_data_key_recursive=None):
    if meta_data_key_recursive:
        meta_link = meta_link + meta_data_key_recursive
    out_put = requests.get(meta_link)
    for each_meta_data in out_put.text.split('\n'):
        if not each_meta_data.endswith("/"):
            data_link = meta_link + each_meta_data
            data = requests.get(data_link)
            if data.status_code != 404:
                result[each_meta_data] = data.text
        else:
            get_instance_meta_data(meta_link, result, each_meta_data)
    return result


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-k", "--key", dest="data_key", help="Provide key to get individual meta data", default=None)
    instance_meta_data = dict()
    instance_meta_data_fetched = get_instance_meta_data(aws_meta_link, result=instance_meta_data)
    (options, args) = parser.parse_args()
    if options.data_key:
        print(instance_meta_data_fetched.get(options.data_key))
    else:
        print(json.dumps(instance_meta_data_fetched, indent=4, sort_keys=True))
