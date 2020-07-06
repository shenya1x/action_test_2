import argparse
import requests
import json


OSS_SERVER = r'https://bios-ci.intel.com'


def trigger_rerun_oss_task(task_id, rerun_all):
    res = b'{"msg": 157059, "code": 0}'
    print(res)
    
    url = r'{}/app/rest/rerun_auto_task/?auto_task_id={}&rerun_all={}'.format(OSS_SERVER, task_id, rerun_all)
    print(url)
    # try:
    #     res = requests.get(url)
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
    args = parser.parse_args()
    trigger_rerun_oss_task(args.task_id, args.rerun_all)


if __name__ == '__main__':
    main()
