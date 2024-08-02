import numpy as np

from sympy import symbols, Eq, solve

# 定義された変数
x, y, z, t = symbols('x y z t')

# 球の方程式のパラメータ
x0, y0, z0, r = 0, 0, 8, 4  # 球の中心 (0, 0, 8) と半径 4


# 交点の座標
intersection_point = np.array([0, 12/5, 24/5])

# 球の中心座標
sphere_center = np.array([x0, y0, z0])

# 法線ベクトルの計算 (交点の座標 - 球の中心座標)
normal_vector = intersection_point - sphere_center
print("normal_vector:",normal_vector)

# 法線ベクトルの正規化
normal_vector_normalized = normal_vector / np.linalg.norm(normal_vector)
print("normal_vector_normalized",normal_vector_normalized)

# 拡散反射係数ベクトル
kd = np.array([2/3, 3/4, 0])

# 入力光の強さ
I = 1/2

# 光の方向ベクトル
l = np.array([0, 1, 0])

# 拡散反射光のカラーベクトルの計算 (ランバートの反射モデル)
v = kd * I
print(v)
diffuse_reflection_color = kd * I * np.dot(normal_vector_normalized, l)

