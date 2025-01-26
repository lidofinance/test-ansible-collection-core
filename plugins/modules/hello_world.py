from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec={}
    )
    result = {
        'changed': False,
        'message': 'hello world'
    }
    module.exit_json(**result)

if __name__ == '__main__':
    main()
