import cadquery as cq

# パラメータ
desk_length = 1200    # 机の長さ (mm)
desk_width = 600      # 机の幅 (mm)
desk_height = 720     # 机の高さ (mm)
top_thickness = 25    # 天板の厚さ (mm)
leg_size = 60         # 脚の断面サイズ (mm)
wall_thickness = 4    # 脚の肉厚 (mm)

# フィレットとエッジのパラメータ
top_fillet = 10       # 天板のフィレット半径
leg_fillet = 5        # 脚のフィレット半径
edge_fillet = 2       # 細かいエッジのフィレット

# ガラス板用パラメータ
glass_thickness = 8   # ガラス板の厚さ
glass_margin = 20     # ガラス板を載せる縁の幅
glass_depth = 5       # ガラス板を埋め込む深さ

def create_hollow_leg(x, y):
    """中空構造の脚を作成する"""
    # 外側の脚
    outer_leg = (cq.Workplane("XY")
                .box(leg_size, leg_size, desk_height - top_thickness))
    
    # 脚の垂直エッジにフィレット
    outer_leg = (outer_leg.edges("|Z")
                .fillet(leg_fillet))
    
    # 内側の空洞
    inner_size = leg_size - (wall_thickness * 2)
    inner_height = desk_height - top_thickness - wall_thickness
    inner_void = (cq.Workplane("XY")
                 .box(inner_size, inner_size, inner_height)
                 .translate((0, 0, wall_thickness/2)))
    
    # 補強リブ（十字型）
    rib_thickness = 3
    rib_v = (cq.Workplane("XY")
             .box(rib_thickness, inner_size, inner_height)
             .translate((0, 0, wall_thickness/2)))
    rib_h = (cq.Workplane("XY")
             .box(inner_size, rib_thickness, inner_height)
             .translate((0, 0, wall_thickness/2)))
    
    # 脚を組み立て
    leg = (outer_leg
           .cut(inner_void)
           .union(rib_v)
           .union(rib_h))
    
    # 位置に移動
    leg = leg.translate((x, y, (desk_height - top_thickness)/2))
    
    return leg

def create_top_with_glass_recess():
    """ガラス板用の凹みを持つ天板を作成する"""
    # 基本の天板
    base_top = (cq.Workplane("XY")
               .box(desk_length, desk_width, top_thickness))
    
    # 天板の上面と下面のエッジにフィレット
    base_top = (base_top.edges("|Z")
               .fillet(top_fillet))
    
    # ガラス用の凹み
    glass_length = desk_length - (glass_margin * 2)
    glass_width = desk_width - (glass_margin * 2)
    glass_recess = (cq.Workplane("XY")
                   .box(glass_length, glass_width, glass_depth * 2)
                   .translate((0, 0, top_thickness/2)))
    
    # ガラス収納部のエッジにフィレット
    glass_recess = (glass_recess.edges("|Z")
                   .fillet(edge_fillet))
    
    # 天板を組み立て
    desktop = (base_top
              .cut(glass_recess)
              .translate((0, 0, desk_height - top_thickness/2)))
    
    return desktop

# メインの組み立て処理
def create_desk():
    """改良版デスクを作成する"""
    # 天板の作成
    desktop = create_top_with_glass_recess()
    
    # 脚の配置を計算
    leg_x_offset = desk_length/2 - leg_size
    leg_y_offset = desk_width/2 - leg_size
    
    # 4本の脚を作成
    legs = []
    for x in [-leg_x_offset, leg_x_offset]:
        for y in [-leg_y_offset, leg_y_offset]:
            legs.append(create_hollow_leg(x, y))
    
    # すべてのパーツを組み合わせる
    desk = desktop
    for leg in legs:
        desk = desk.union(leg)
    
    return desk

# メイン処理
if __name__ == "__main__":
    # デスクを作成
    final_desk = create_desk()
    
    # STLファイルとしてエクスポート
    cq.exporters.export(final_desk, "example/desk_improved.stl")
