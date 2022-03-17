from gooey import Gooey, GooeyParser
import yaml


def convert(data):
    print("Writing yaml...")
    with open(data.FileSaver, "w") as outfile:
        yaml.dump(vars(data), outfile, default_flow_style=False)
    print("...")
    print("Done!")
    print(f"Yaml available at {data.FileSaver}")


@Gooey(
    dump_build_config=True,
    program_name="Convert to YAML",
    show_success_modal=False,
    show_restart_button=False,
)
def main():
    desc = "Enter fields and convert to yaml"
    file_help_msg = "Name of the file you want to output"

    my_cool_parser = GooeyParser(description=desc)

    my_cool_parser.add_argument(
        "FileSaver",
        help=file_help_msg,
        widget="FileSaver",
        gooey_options={"full_width": True},
    )

    my_cool_parser.add_argument(
        "some_required_field", metavar="Some Data", help="Enter some text"
    )

    data = my_cool_parser.parse_args()
    convert(data)


def here_is_more():
    pass


if __name__ == "__main__":
    main()
