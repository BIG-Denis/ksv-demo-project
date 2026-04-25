import karavaisv as ksv
from copy import deepcopy

# default constants
PARAM_FILE = "config/default.yaml"
BUILD_DIR = "build/"
FILELIST = "filelist.klst"
FILES_TO_RENDER = {
    "rtl/smart_buffer.ksv"
}


# check correctness of given config
def check_parameters(parameters: dict) -> None:
    # module_id
    assert type(parameters["module_id"]) == str, \
        "module_id must be string"
    if parameters["module_id"]:
        assert parameters["module_id"][0] not in map(str, range(10)), \
            "module_id must not start with the number"
    # assertions
    assert type(parameters["assertions"]) == bool, \
        "assertions must be bool"
    # egress
    assert type(parameters["egress"]) == bool, \
        "egress must be bool"
    # arbiter
    assert parameters["arbiter"] in ("find_first", "round_robin"), \
        "arbiter must be either find_first or round_robin"
    # ports
    for port in parameters["ports"]:
        name  = port["name"]
        width = port["width"]
        assert type(name) == str, \
            "ports[name] must be string"
        assert name[0] not in map(str, range(10)), \
            "ports[name] must not start with the number"
        assert type(width) == int, \
            "ports[width] must be int"
        assert width > 0, \
            "ports[width] must be positive int"
    assert len(parameters["ports"]) == len(set(map(lambda port: port["name"], parameters["ports"]))), \
        "ports[name] must be unique"


# get derived parameters
def calculate_derived_parameters(parameters: dict) -> dict:
    parameters_drvd = deepcopy(parameters)
    # module_id
    parameters_drvd["module_id"] = parameters["module_id"] + '_'
    # max port width
    parameters_drvd["max_width"] = max(map(lambda port: port["width"], parameters["ports"]))
    # inbound ports number
    parameters_drvd["port_num"] = len(parameters["ports"])
    return parameters_drvd


# build project
def build(parameters: dict, build_dir: str) -> None:
    # check parameters
    check_parameters(parameters)
    # get derived parameters
    parameters = calculate_derived_parameters(parameters)
    # render sources
    for filename_src in FILES_TO_RENDER:
        filename_dst = build_dir + filename_src.replace(".ksv", ".sv")
        source_raw = ksv.read_source_from_file(filename_src)
        source_rendered = ksv.render(source_raw, parameters, filepath=filename_dst)
        ksv.write_rendered_to_file(source_rendered, filename_dst)
    # render filelist
    filename_dst = build_dir + "filelist.lst"
    source_raw = ksv.read_source_from_file(FILELIST)
    source_rendered = ksv.render(source_raw, parameters, filepath=filename_dst)
    ksv.write_rendered_to_file(source_rendered, filename_dst)


# default entry point
def main() -> None:
    parameters = ksv.read_params_from_yaml(PARAM_FILE)
    build_dir  = BUILD_DIR
    build(parameters, build_dir)


# get into entry point
if __name__ == "__main__":
    main()
