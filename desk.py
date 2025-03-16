import cadquery as cq

# パラメータ
desk_length = 1200  # 机の長さ (mm)
desk_width = 600    # 机の幅 (mm)
desk_height = 720   # 机の高さ (mm)
top_thickness = 25  # 天板の厚さ (mm)
leg_size = 50       # 脚の断面サイズ (mm)

# 天板を作成
desktop = (cq.Workplane("XY")
          .box(desk_length, desk_width, top_thickness)
          .translate((0, 0, desk_height - top_thickness/2)))

# 脚を作成する関数
def create_leg(x, y):
    return (cq.Workplane("XY")
            .box(leg_size, leg_size, desk_height - top_thickness)
            .translate((x, y, (desk_height - top_thickness)/2)))

# 4本の脚を作成し配置
leg_x_offset = desk_length/2 - leg_size
leg_y_offset = desk_width/2 - leg_size

leg1 = create_leg(-leg_x_offset, -leg_y_offset)
leg2 = create_leg(-leg_x_offset, leg_y_offset)
leg3 = create_leg(leg_x_offset, -leg_y_offset)
leg4 = create_leg(leg_x_offset, leg_y_offset)

# すべてのパーツを組み合わせる
desk = desktop.union(leg1).union(leg2).union(leg3).union(leg4)

# STLファイルとしてエクスポート
cq.exporters.export(desk, "desk.stl")
