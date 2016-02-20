import argparse
from snapshot import SnapshotRequest, get_all_packages
import pprint
from utils import logger, check_port
from tabulate import tabulate

parser = argparse.ArgumentParser(description="find package information in debian.snapshot.org")

parser.add_argument("package_name", help="write the binary package name you wish to find", type=str)
# optional
parser.add_argument('-v', '--version', nargs=1, type=str, help='set the target version of the package you wish you')
parser.add_argument('-l', '--all-binary-versions', help='find binary package versions and corresponding source names and versions', action='store_true')
parser.add_argument('-ls', '--all-source-versions', help='list all available source versions for this package', action='store_true')
parser.add_argument('-alsfpv', '--all-source-for-package-version', help='list all source files associated with this package at that version', action='store_true')
parser.add_argument('-albfpv', '--all-binpackages-for-package-version', help='list all binary packages associated with this source package at that version', action='store_true')
parser.add_argument('-af', '--all-files', help='list all files associated with this source package at that version', action='store_true')
parser.add_argument('-fs', '--info', help='get information e.x first_seen', action='store_true')
parser.add_argument('-arch', '--architecture', nargs=1, type=str, help='define system architecture')
parser.add_argument('-all-packages', help='all packages', action='store_true')
args = parser.parse_args()

# if args.all_binary_versions:
#     package = SnapshotRequest(args.package_name)
#     print args.package_name
#     print package.find_binary_package_versions_and_corresponding_source_names_and_versions(package)
#     package.close()
the_hash = ''
arch = ''
if args.all_source_versions:
    # python apt-snapshot.py -ls spacefm
    package = SnapshotRequest(args.package_name)
    # pprint.pprint(package.list_all_available_source_versions())
    result = package.list_all_available_source_versions()
    print tabulate([[i] for i in result], tablefmt='grid', headers=["version"])
elif args.all_source_for_package_version:
    print args
    # python apt-snapshot.py -alls 0.9.4-2 spacefm
    # python apt-snapshot.py -alsfpv -v 0.9.4-2   spacefm
    package = SnapshotRequest(args.package_name)
    # package.list_all_sources_for_this_package_at_version()
    version = getattr(args, 'all_source_for_package_version')
    # pprint.pprint(package.list_all_sources_for_this_package_at_version(args.version[0]), width=1)
    result = package.list_all_sources_for_this_package_at_version(args.version[0])
    print '\n'
    print result['package'], result['version']
    print tabulate(result['result'], tablefmt='grid', headers='keys')
elif args.all_binpackages_for_package_version:
    # python apt-snapshot.py -alb 0.9.4-2 spacefm
    print(args)
    package = SnapshotRequest(args.package_name)
    # version = getattr(args, 'all_binpackages_for_package_version')
    result = package.list_all_binary_packages_for_this_package_at_version(args.version[0])
    # pprint.pprint([i for i in package.list_all_binary_packages_for_this_package_at_version(args.version[0])])
    print '\n'
    print tabulate(result, tablefmt='grid',headers='keys')
elif args.all_files:
    # python apt-snapshot.py spacefm -af  0.9.4-2 amd64
    # python apt-snapshot.py spacefm -af  0.9.4-2 -arch amd64
    package = SnapshotRequest(args.package_name)
    print args
    print '---------------------------'
    # num_parameters = len(getattr(args, 'all_files'))
    # version = getattr(args, 'all_files')[0]
    if args.architecture is None:
        pprint.pprint(package.list_all_files_associated_with_this_source_package_at_that_version(args.version[0]))
        exit()
    # arch = getattr(args, 'all_files')[1]
    architecture = check_port(args.architecture[0])
    #pprint.pprint(package.list_all_files_associated_with_this_source_package_at_that_version(args.version[0], architecture), width=1)
    result = package.list_all_files_associated_with_this_source_package_at_that_version(args.version[0], architecture)
    print tabulate(result['binaries'][0]['files'],tablefmt='grid',headers='keys')
    # print getattr(args, 'all_files')[1]
elif args.info:
    # python apt-snapshot.py python-apt --info 0.7.8 amd64
    print args
    package = SnapshotRequest(args.package_name)
    # num_parameters = len(getattr(args, 'info'))
    # print (getattr(args, 'info'))
    # if num_parameters == 1:
    #     print 'you must set the arch parameter'
    #     exit()
    # version = getattr(args, 'info')[0]
    # arch = getattr(args, 'info')[1]
    architecture = check_port(args.architecture[0])
    result = package.info_from_hash(args.version[0], architecture)
    result['result'][0].setdefault('hash', result['hash'])
    # pprint.pprint(package.info_from_hash(args.version[0], architecture), width=1)
    # print tabulate(package.info_from_hash(args.version[0], architecture),headers='keys')
    print '\n\n'
    print tabulate(result['result'], headers='keys')
    print '\n\n'

else:
    # python apt-snapshot.py -l spacefm
    # should be printed as table with both source & binary vesion
    package = SnapshotRequest(args.package_name)
    print args.package_name
    result = package.find_binary_package_versions_and_corresponding_source_names_and_versions(package)
    # pprint.pprint(result)

    print tabulate(result['result'], tablefmt='grid', headers='keys')  # , tablefmt='simple')
    # print [str(i) for i in result]
    print '\nNumber of packages: %d' % len(result['result'])


    #br2684ctl ,make, xserver-xorg-input-wacom source names change
    #apt-get -o  Dir::Etc::sourcelist="sources.list.d/snapshot.list" -o Dir::Etc::sourceparts="-" -o APT::Get::List-Cleanup="0"  -o Acquire::Check-Valid-Until=false update