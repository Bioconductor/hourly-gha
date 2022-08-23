import sys
import argparse


def cloudbridge_objects_list(bucket, output_f):
    from cloudbridge.factory import CloudProviderFactory
    from cloudbridge.factory import ProviderList
    provider = CloudProviderFactory().create_provider('openstack', {})
    buck = provider.storage.buckets.get(bucket)
    objs = list(buck.objects)
    with open(output_f, 'w') as f:
        for o in objs:
            f.write(f'{o.size} {o.name}\n')


def main(arguments):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-o', '--output', dest='ls_output', type=str, help='Path where to save output list of all bucket objects')
    parser.add_argument('-b', '--bucket', dest='bucket', type=str, help='Name of bucket of which outputs to list')

    args = parser.parse_args()

    cloudbridge_objects_list(args.bucket, args.ls_output)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))



