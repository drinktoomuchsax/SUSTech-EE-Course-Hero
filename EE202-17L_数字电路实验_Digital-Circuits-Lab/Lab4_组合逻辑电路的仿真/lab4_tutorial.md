[LAST4](https://send.cra.moe/file/C4zRyVhNzITzyc4v/VZ1zqbc0dzcXBYhZ/LAST4.rar)
https://send.cra.moe/file/o42QJ4BVn30zQyAf/hXc6UxuRwv0yHqR3/3-3C.ms14
https://send.cra.moe/file/o42QJ4BVn30zQyAf/GQHqYsN6MIHLu2aP/3.2_C3.ms14
https://send.cra.moe/file/o42QJ4BVn30zQyAf/n4gjUahTPl503ivy/3.3_A.ms14
https://send.cra.moe/file/o42QJ4BVn30zQyAf/rSCIfpqENbgFzNVI/3-3_B.ms14

有四种ic，一种需要供电，为了连线简洁，选择不需要供电的，另两种封装不同，随便选择即可


# 3.2-c_3
用一个3-8线译码器74LS138和必需的基本逻辑门电路设计一个全减器

*A-B=D，b_0为下借位，b_1为上借位*

A B b_0 b_1 D
0 0  0   0  0    
0 0  1   1  1   
0 1  0   1  1    
0 1  1   1  0    
1 0  0   0  1    
1 0  1   0  0    
1 1  0   0  0    
1 1  1   1  1    

D = A'B'b_0 + A'Bb_0' + AB'b_0' + ABb_0
b_1 = A'B'b_0 + A'Bb_0' + A'Bb_0 + ABb_0

# 3.3-A

A B C_0 min C_1 D
0 0 0   0    0  0
0 0 1   1    0  1
0 1 0   2    0  1
0 1 1   3    1  0
1 0 0   4    0  1
1 0 1   5    1  0
1 1 0   6    1  0
1 1 1   7    1  1

写出最小项为c_1(a, b, c_0) = a'bc_0 + ab'c_0 + ab1
d(a, b, c_0) = a'b'c_0 + a'bc_0' + ab'c_0' + abc_0

[74LS153](https://www.ti.com/lit/ds/symlink/sn74ls153.pdf?ts=1682319146544&ref_url=https%253A%252F%252Fwww.google.com%252F)



# 3.3-B
一个数能否被2和5整除，看这个数的末位。

能被2整除的数末位是0、2、4、6、8。

能被5整除的数末位是0、5。

能同时被2和5整除的数末位是0。

A B C D min X 
0 0 0 0   0 1
0 0 0 1   1 0
0 0 1 0   2 1 
0 0 1 1   3 0
0 1 0 0   4 1
0 1 0 1   5 1
0 1 1 0   6 1
0 1 1 1   7 0
1 0 0 0   8 1
1 0 0 1   9 0
1 0 1 0  10 1
1 0 1 1  11 0
1 1 0 0  12 1
1 1 0 1  13 0
1 1 1 0  14 1
1 1 1 1  15 1

用[网站](https://www.charlie-coleman.com/experiments/kmap/)化简最小项为f(a, b, c, d) = d' + a'bc' + abc

[74LS151 DATA SHEET](https://www.ti.com/lit/ds/symlink/sn54s151.pdf?ts=1682317387216&ref_url=https%253A%252F%252Fwww.google.com%252F)

# 3.3-C
课本上的原题，p