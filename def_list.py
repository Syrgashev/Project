def my_len_queue(queue):
    duration = len(queue)
    return duration

def my_print_queue(queue):
    i = 0
    for x in queue:
        i += 1
        print('%s:%s' % (i, x))

def my_add_queue(queue, item):
    new_queue = queue[:]
    new_queue.append(item)
    return new_queue

def my_exit_queue(queue):
    a = queue.pop(0)
    return a

def main():
    queue = [1, 22, 35, 76, 12]
    #print(my_len_queue(queue))
    my_print_queue(queue)
    print('*' * 80)
    queue = my_add_queue(queue, 6)
    my_print_queue(queue)
    print('*' * 80)
    print('Удаленный элемент', my_exit_queue(queue))
    my_print_queue(queue)

if __name__ == '__main__':
    main()