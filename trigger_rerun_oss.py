import argparse
import requests
import json


OSS_SERVER = r'https://bios-ci.intel.com'


def trigger_rerun_oss_task(task_id, rerun_all, user, password):
    res = b'{"msg": 157059, "code": 0}'
    print(res)
    url = r'{}/app/rest/rerun_auto_task/?auto_task_id={}&rerun_all={}&uads=1'.format(OSS_SERVER, task_id, rerun_all)
    print(url)
    # try:
    #     res = requests.get(url, auth=(user, password), verify=False)
    #     print(res.content)
    # except Exception as e:
    #     print('exception {} happens while request url {}'.format(e, url))


def main():
    parser = argparse.ArgumentParser(
        prog='trigger_rerun_oss.py',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='',
        epilog='')
    parser.add_argument('--task_id', required=True)
    parser.add_argument('--rerun_all', action='store_true')
    parser.add_argument('--user', required=True)
    parser.add_argument('--password', required=True)

    args = parser.parse_args()
    trigger_rerun_oss_task(args.task_id, args.rerun_all, args.user, args.password)


if __name__ == '__main__':
    main()
