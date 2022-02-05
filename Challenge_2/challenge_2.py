import requests
from optparse import OptionParser


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
    aws_meta_link = "http://169.254.169.254/latest/meta-data/"
    valid_meta_data_keys = [u'scheduled', u'domain', u'configured', u'vpc-ipv4-cidr-blocks', u'vhostmd',
                            u'security-group-ids', u'instance-type', u'subnet-ipv4-cidr-block', u'instance-id',
                            u'local-hostname', u'availability-zone-id', u'public-ipv4s', u'hostname', u'ami-id',
                            u'instance-action', u'interface-id', u'vpc-id', u'ami', u'reservation-id',
                            u'security-groups', u'instance-life-cycle', u'subnet-id', u'mac', u'profile',
                            u'public-ipv4', u'owner-id', u'ami-manifest-path', u'signer-cert', u'vpc-ipv4-cidr-block',
                            u'info', u'local-ipv4', u'ami-launch-index', u'public-hostname', u'region', u'partition',
                            u'availability-zone', u'ec2-instance', u'local-ipv4s', u'root', u'device-number', u'history'
                            ]
    meta_data_key = None
    parser = OptionParser()
    parser.add_option("-k", "--key", dest="data_key", help="To get history of data", default=None)
    (options, args) = parser.parse_args()
    if options.data_key and options.data_key in valid_meta_data_keys:
        meta_data_key = options.data_key
    elif options.data_key:
        print("Requested key is not valid, Valid keys are", valid_meta_data_keys)
        exit()
    else:
        pass
    instance_meta_data = {}
    instance_meta_data_fetched = get_instance_meta_data(aws_meta_link, result=instance_meta_data)
    if meta_data_key:
        print(instance_meta_data_fetched[meta_data_key])
    else:
        print(instance_meta_data_fetched)



