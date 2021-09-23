'''
Elevar error con raise ValueError()
'''

def environment_args(env):
    """ Define proper source and sink based on environment(development, production) """
    if env == "production":
        args = {"source_": "main_source_prod", "sink_": "SDC_sink_0_prod"}
    elif env == "development":
        args = {"source_": "main_source_prod", "sink_": "SDC_sink_0_dev"}
    else:
        raise ValueError("Define an environment variable first [production, development]")
    return args


if __name__ == '__main__':
    res = environment_args('')
    print(res)