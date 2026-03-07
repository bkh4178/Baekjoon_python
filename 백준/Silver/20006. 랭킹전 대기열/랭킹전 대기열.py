import sys
input = sys.stdin.readline

def main():
    p, max_room = map(int, input().split())
    room_list = []
    for _ in range(p):
        level, nickname = input().split()
        level = int(level)
        
        add = False
        for room in room_list:
            base_level = room[0][0]
            if len(room) < max_room and base_level-10 <= level <= base_level+10:
                room.append((level,nickname))
                add = True
                break
            else:
                continue
        if add == False:
            room_list.append([(level,nickname)])

    for room in room_list:
        if len(room) == max_room: print('Started!')
        else: print('Waiting!')
        room.sort(key=lambda x: x[1])
        for l, n in room:
            print(l, n)

if __name__ == '__main__':
    main()