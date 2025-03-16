import cadquery as cq

# パラメータ
desk_length = 1200  # 机の長さ (mm)
desk_width = 600    # 机の幅 (mm)
desk_height = 720   # 机の高さ (mm)
top_thickness = 25  # 天板の厚さ (mm)
leg_size = 50       # 脚の断面サイズ (mm)
corner_radius = 20  # 角の丸みの半径 (mm)
shell_thickness = 2 # 肉抜き後の壁厚 (mm)

# 天板を作成（角を丸くする）
desktop = (cq.Workplane("XY")
          .box(desk_length, desk_width, top_thickness)
          .edges("|Z")
          .fillet(corner_radius)
          .translate((0, 0, desk_height - top_thickness/2)))

# 天板の裏側に大きな肉抜きパターンを作成
desktop = (desktop
          .faces("<Z")
          .workplane(offset=-shell_thickness)
          .rect(desk_length-60, desk_width-60)  # より大きな肉抜き
          .cutBlind(top_thickness - 2*shell_thickness))

# さらに補強リブを残して追加の肉抜き
rib_width = 20  # リブの幅
for x in [-desk_length/4, 0, desk_length/4]:
    desktop = (desktop
              .faces("<Z")
              .workplane()
              .moveTo(x, 0)
              .rect(rib_width, desk_width-60)
              .extrude(top_thickness - 2*shell_thickness))

for y in [-desk_width/4, 0, desk_width/4]:
    desktop = (desktop
              .faces("<Z")
              .workplane()
              .moveTo(0, y)
              .rect(desk_length-60, rib_width)
              .extrude(top_thickness - 2*shell_thickness))

# 脚を作成する関数（肉抜きと丸み付き）
def create_leg(x, y):
    # 外側の脚
    outer_leg = (cq.Workplane("XY")
                .box(leg_size, leg_size, desk_height - top_thickness))
    
    # 角を丸くする
    outer_leg = (outer_leg
                .edges("|Z")
                .fillet(corner_radius/2))  # 天板の半分の丸み
    
    # 内側の大きな肉抜き
    inner_cut = (cq.Workplane("XY")
                .box(leg_size - 2*shell_thickness, 
                     leg_size - 2*shell_thickness, 
                     desk_height - top_thickness - 2*shell_thickness))
    
    # 追加の肉抜きパターン（四隅に穴）
    hole_size = 15
    hole_offset = leg_size/4
    
    holes = (cq.Workplane("XY")
            .pushPoints([
                (hole_offset, hole_offset),
                (-hole_offset, hole_offset),
                (hole_offset, -hole_offset),
                (-hole_offset, -hole_offset)
            ])
            .circle(hole_size/2)
            .extrude(desk_height - top_thickness - 2*shell_thickness))
    
    # 肉抜きを行った脚を作成
    leg = outer_leg.cut(inner_cut).cut(holes)
    
    # 位置を移動
    return leg.translate((x, y, (desk_height - top_thickness)/2))

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
cq.exporters.export(desk, "example/desk_improved.stl")
