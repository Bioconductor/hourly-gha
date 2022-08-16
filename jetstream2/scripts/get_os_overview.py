import sys
import argparse


def cloudbridge_instances_list(credid, credsecret, instances_file):
    from cloudbridge.factory import CloudProviderFactory
    from cloudbridge.factory import ProviderList
    from cloudbridge.interfaces.exceptions import DuplicateResourceException
    creds = {
        "os_application_credential_id": credid,
        "os_application_credential_secret": credsecret,
        "os_auth_url": f"https://js2.jetstream-cloud.org:5000/v3",
        "os_region_name": "IU",
    }
    provider = CloudProviderFactory().create_provider('openstack', creds)
    insts = list(provider.compute.instances)
    lines = []
    for i in insts:
        lines.append(f'Name: {i.label}')
        lines.append(f'State: {i.state}')
        vmtype = i.vm_type
        lines.append(f'Istance Type: {vmtype.name}')
        lines.append(f'RAM: {vmtype.ram}')
        lines.append(f'vCPUS: {vmtype.vcpus}')
        lines.append("---")
    with open(instances_file, 'w') as f:
        f.write('\n'.join(lines))


def main(arguments):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-i', '--credid', dest='os_cred_id', type=str, help='Application Credential ID used for OpenStack login')
    parser.add_argument('-s', '--credsecret', dest='os_cred_secret', type=str, help='Application Credential Secret used for OpenStack login')
    parser.add_argument('-r', '--report', dest='instances_report', type=str, help='Path where to save report of Openstack instances')

    args = parser.parse_args()

    cloudbridge_instances_list(args.os_cred_id, args.os_cred_secret, args.instances_report)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
