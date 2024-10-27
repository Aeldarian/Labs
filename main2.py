# TODO Найдите количество книг, которое можно разместить на дискете
num_page=100
num_line=50
num_simb=25
size_simb=4
size_all_simb=num_page*num_line*num_simb*size_simb/1024
volume_hd=1.44
volume_in_kb=volume_hd*1024
aboba=int(volume_in_kb//size_all_simb)
print("Количество книг, помещающихся на дискету:", aboba)
