from file_utils import demo_operations
import pprint


def main():
    # Run the demo which creates sample files and performs operations
    result = demo_operations(base_dir='samples')

    print('\nDemo finished. Generated outputs:')
    pprint.pprint(result)

    print('\nYou can open the files to inspect:')
    for k in ('txt_out', 'csv_out'):
        print(f"- {k}: {result[k]}")


if __name__ == '__main__':
    main()
