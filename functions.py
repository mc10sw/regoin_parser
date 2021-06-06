file_list = [
    "entrc_busan",
    "entrc_chungbuk",
    "entrc_chungnam",
    "entrc_daegu",
    "entrc_daejeon",
    "entrc_gangwon",
    "entrc_gwangju",
    "entrc_gyeongbuk",
    "entrc_gyeongnam",
    "entrc_gyunggi",
    "entrc_incheon",
    "entrc_jeju",
    "entrc_jeonbuk",
    "entrc_jeonnam",
    "entrc_sejong",
    "entrc_seoul",
    "entrc_ulsan",
]


def create_region_map():
    region_map_file = open("region_map.txt", "w")
    region_list_file = open("region_list.txt", "w")
    region1_list = []
    region2_list = []
    region3_list = []

    for file_name in file_list:
        axis_list = {}
        f = open("data/" + file_name + ".txt", "r", encoding="cp949")
        print("file_name: " + file_name)
        lines = f.readlines()
        for line in lines:
            code_array = line.split('|')
            code = code_array[2]
            region1 = code_array[3]
            region2 = code_array[4]
            region3 = code_array[5]
            x_axis = code_array[16]
            y_axis = code_array[17]

            # 추가되지 않은 지역 새로 추가
            if region1 not in region1_list:
                region1_list.append(region1)

            if region2 not in region2_list:
                region2_list.append(region2)

            if region3 not in region3_list:
                region3_list.append(region3)

            # 동일한 지역에 대해 좌표값 추출
            if code not in axis_list:
                try:
                    axis_list[code] = {
                        'region1': region1,
                        'region2': region2,
                        'region3': region3,
                        'x_axis': float(x_axis),
                        'y_axis': float(y_axis),
                        'count': 1,
                    }
                except:
                    axis_list[code] = {
                        'region1': region1,
                        'region2': region2,
                        'region3': region3,
                        'x_axis': 0.0,
                        'y_axis': 0.0,
                        'count': 1,
                    }
            else:
                try:
                    axis_list[code]['x_axis'] = axis_list[code]['x_axis'] + float(x_axis)
                    axis_list[code]['y_axis'] = axis_list[code]['y_axis'] + float(y_axis)
                    axis_list[code]['count'] = axis_list[code]['count'] + 1
                except:
                    axis_list[code]['count'] = axis_list[code]['count'] + 1

        # 좌표 평균값 추출
        for key in axis_list.keys():
            region1 = axis_list[key]['region1']
            region2 = axis_list[key]['region2']
            region3 = axis_list[key]['region3']
            count = axis_list[key]['count']
            x_axis = axis_list[key]['x_axis'] / count
            y_axis = axis_list[key]['y_axis'] / count
            region_map_file.write('\"' + key + '\": [\"' + region1 + '\", \"' + region2 + '\", \"' + region3 +
                                  '\", ' + x_axis.__str__() + ', ' + y_axis.__str__() + '],\n')

    # 모든 지역명 리스트 출력
    for region1 in region1_list:
        region_list_file.write('\"' + region1 + '\",')

    region_list_file.write('\n')

    for region2 in region2_list:
        region_list_file.write('\"' + region2 + '\",')

    region_list_file.write('\n')

    for region3 in region3_list:
        region_list_file.write('\"' + region3 + '\",')

    region_list_file.write('\n')
