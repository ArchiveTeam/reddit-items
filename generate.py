import argparse
import math


def main(start: int, stop: int, item_size: int, file_index: int, type_: str,
         items_per_file: int):
    items = [
        '{}:{}-{}'.format(type_, i*item_size, (i+1)*item_size-1)
        for i in range(math.floor(start/item_size), math.ceil(stop/item_size))
    ]
    print(items[-1])
    for i in range(0, len(items)+1, items_per_file):
        item_list = items[i:i+items_per_file]
        print(item_list[0], item_list[-1])
        with open('{}_{}_{}-{}'.format(
            str(int(i/items_per_file)+file_index).zfill(3),
            type_,
            item_list[0].split(':', 1)[1].split('-')[0],
            item_list[-1].split(':', 1)[1].split('-')[1]
        ), 'w') as f:
            f.write('\n'.join(item_list))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', type=int, required=True)
    parser.add_argument('--stop', type=int, required=True)
    parser.add_argument('--file-index', type=int, required=True)
    parser.add_argument('--item-size', type=int, default=100)
    parser.add_argument('--type', type=str, default='posts')
    parser.add_argument('--items-per-file', type=int, default=300000)
    args = parser.parse_args()
    main(args.start, args.stop, args.item_size, args.file_index, args.type,
         args.items_per_file)

