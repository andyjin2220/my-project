Web VPython 3.2

from vpython import *



# 시점 이동 방지
scene.userzoom = False
scene.userspin = False



# 중력 및 속도 설정
velocity = vector(0, 0, 0)
g = vector(0, -100, 0) # 중력 가속도
up_force = vector(0, 23.123456789, 0) # 위쪽으로 순간 가속도




# 맵의 높이값을 저장할 리스트 (X좌표에 따른 Y좌표 값들)
map_heights      = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,2,2,2,2,0,0,3,3,3,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,0,2,2,0,0,3,3,0,0,4,4,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,1,1,1,1,1,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,2,0,0,0,3,0,0,0,4,0,0,0,5,0,4,0,3,0,2,0,0,0,2,2,2,2,0,0,2,2,2,2,2,2,0,0,0,3,0,0,5,0,0,1,0,0,0,2,0,1,0,0,0,2,0,1,0,0,0,2,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,1,2,0,0,4,0,0,0,0,0,4,0,0,4.5,0,3,0,0,0,4,0,0,0,0,0,0,2.5,2,2,2,0,0,3,0,0,0,4,4,4.3,4.3,4.6,4.6,4.9,4.9,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,  0,0,0,0,0,0,0,0,0,0, 0,0,0,3,0,0,0,0,0,0, 0,0,5,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,8,0,0, 0,0,0,8,0,0,0,0,0,0, 0,0,5,0,0,0,0,6,0,0, 0,5,0,0,0,0,4,0,0,0, 6,0,0,0,0,0,5,0,0,0, 0,6,0,0,0,0,0,8,0,0, 8,0,0,8,0,0,8,0,0,8, 0,0,8,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 12,12,12,12,12,12,12] 
obstacle_heights = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,2,0,0,0,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,   0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,  0,0,0,0,0,0,0,0,0,0,0,0,1,  0,0,1,0,0,0,0,0,0,0,0,0,  0,  0,  0,  0,  0,  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,  0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0, 0, 0, 0, 0, 0, 0 ] 
jumper_heights   = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,  0,0,0,0,0,0,0,0,1,0,0,0,0,  0,0,0,0,0,0,0,0,0,0,0,0,  0,  0,  0,  0,  0,  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,  0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0, 0, 0, 0, 0, 0, 0 ]
portal_height    = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,   0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,  0,0,0,0,0,0,0,0,0,0,0,0,0,  0,0,0,0,0,0,0,0,0,0,0,0,  0,  0,  0,  0,  0,  0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,  0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0, 0, 0, 0, 0, 0, 0 ]
map_ceiling      = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,   1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,  1,1,1,1,1,1,1,1,1,1,1,1,1,  1,1,1,1,1,1,1,1,1,1,1,1,  1,  1,  1,  1,  1,  1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,  1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1, 1, 1, 1, 1, 1, 1, 1 ]


#맵 색
phase1_color= vec(0, 1, 0)
phase2_color= vec(1.000, 0.421, 0.879)
phase3_color= vec(1.000, 1.000, 0.000)
phase4_color= vec(0.000, 0.890, 1.000)

print("phase4 부터는 스페이스바를 누르면 연속점프가 됩니다.")
print("ESC는 메뉴창")


# 박스(바닥) 생성 함수
def create_terrain(map_heights,obstacle_heights,jumper_heights):
    boxes1 = [] # 생성된 박스들을 저장할 리스트
    boxes2 = []
    pyramides=[] # 생성된 장애물들을 저장할 리스트
    spheres=[] 
    ringes=[]
    
    for i in range(len(map_heights)):
        # X좌표는 i, Y좌표는 map_heights[i]
        if 100<=i<=200:
            ground = box(pos=vector(i * 1.5, map_heights[i] / 2, 0), size=vector(1.5, map_heights[i], 10), color=phase2_color)
        else if 200<=i<=280:
            ground = box(pos=vector(i * 1.5, map_heights[i] / 2, 0), size=vector(1.5, map_heights[i], 10), color=phase3_color)
        else if i>=280:
            ground = box(pos=vector(i * 1.5, map_heights[i] / 2, 0), size=vector(1.5, map_heights[i], 10), color=phase4_color)
        else:
            ground = box(pos=vector(i * 1.5, map_heights[i] / 2, 0), size=vector(1.5, map_heights[i], 10), color=phase1_color)
            boxes1.append(ground)

    for i in range(len(map_ceiling)):
        # X좌표는 i, Y좌표는 map_ceiling[i]
        if map_ceiling[i]:
            ground = box(pos=vector(i * 1.5, 14, 0), size=vector(1.5, map_ceiling[i], 10),color = color.green,opacity=0)
            boxes2.append(ground)
            
    for i in range(len(obstacle_heights)):
        # X좌표는 i, Y좌표는 obstacle_heights[i]
        if  obstacle_heights[i]==1:
            ground = pyramid(pos=vector(i * 1.5, obstacle_heights[i] /8 + map_heights[i]-0.3, 0), size=vector(1.5, 1.5, 1.5), axis=vec(0,1,0),color=color.red)
            pyramides.append(ground)
            
    for i in range(len(jumper_heights)):
        # X좌표는 i, Y좌표는 jumper_heights[i]
        if  jumper_heights[i]==1:
            ground = sphere(pos=vector(i * 1.5, jumper_heights[i] /8 + map_heights[i]-0.3, 0), size=vector(1.5, 1.5, 1.5), axis=vec(0,1,0),color=color.yellow)
            spheres.append(ground)
    
    for i in range(len(portal_height)):
        # X좌표는 i, Y좌표는 jumper_heights[i]                
        if portal_height[i]==1:
            ground = ring(pos=vector(i * 1.5, portal_height[i] + map_heights[i]+1, 0),radius=1.5, color = color.white)
            ringes.append(ground)
            
    return boxes1,boxes2,pyramides,spheres,ringes



#레벨 나누기
text(text='Phase 1', pos=vec(5,8,0),align='center', color=phase1_color)
text(text='Phase 2', pos=vec(155,8,0),align='center', color=phase2_color)
text(text='Phase 3', pos=vec(300,8,0),align='center', color=phase3_color)
text(text='Phase 4', pos=vec(420,8,0),align='center', color=phase4_color)


# 바닥 생성
floor = box(pos=vector(0, 0, 0), size=vector(1500, 0.1, 10), color=phase1_color)

ceiling = box(pos=vec(0,14,0), size=vector(1000, 0.1, 10), color=phase1_color,opacity=0)


#천장 생성
#ceiling = box(pos=vec(0,0,0) size=vector(1000,10,10),color=color.green)

# 공 설정
ball = box(pos=vector(0, 0, 0), radius=0.5, make_trail=True,trail_radius=0.1,texture='https://i.imgur.com/GYkf8E1.png') 

#진행도바
jinhangdobar_base = box(pos=vec(0,12,0,) ,length=18,height=1,width=0.1,color=color.white)
jinhangdobar=box(pos=vec(0,12,0,) ,length=0,height=1,width=0.1,color=color.blue)
garimmack = box(pos=vec(0,12,0.01) ,length=5,height=1,width=0.1,color=color.black)

#메뉴창
menuchang=box(pos=vector(4, 5, 3),length=12, height=8, width=0.1,color=vec(0.000, 0.210, 0.746),opacity=0.9)

menuchang.visible=False



# 첫 번째 원뿔
cone1 = cone(pos=vector(0, 2, 0), axis=vector(0, -1, 0), radius=0.5)
# 두 번째 원뿔
cone2 = cone(pos=vector(0, 2, 0), axis=vector(0, 1, 0), radius=0.5)

# 두 원뿔을 하나로 합친 컴파운드 생성
checkpoint = compound([cone1, cone2])

cone1.visible = False
cone2.visible = False
checkpoint.visible =False


# 광원 위치 설정
local_light(pos=vec(0, 100, 50), color=color.white*0.1)
local_light(pos=vec(150, 100, 50), color=color.white*0.1)
local_light(pos=vec(300, 100, 50), color=color.white*0.1)


# 시간 설정
dt = 0.01

# 지형 생성
terrain = create_terrain(map_heights,obstacle_heights,jumper_heights,map_ceiling)

# 점프 상태
is_jumping = False



# 키보드 입력 처리 함수
def key_input(evt):
    global velocity, is_jumping,spin
    s = evt.key
    if ball.pos.x <=420 or ball.pos.x>=620:
        if s == 'up' and ball.pos.y <= map_heights[int(ball.pos.x // 1.5)] + ball.radius + 0.01:
            velocity.y += up_force.y # 위쪽으로 속도 추가 (점프)
            is_jumping = True
            spin(2*up_force.y/(g.y*-1)) ##걸린시간을 구하는 식을 초기높이,최종높이,초기y속도, 중력가속도를 이용한 식으로 재구성 해야함//print((up_force.y+sqrt(up_force.y*up_force.y+2*g.y*h))/g.y*-1)#h는 변위
            #print(2*up_force.y/(g.y*-1))
    
    else:
        if s == 'up' and ball.pos.y <= map_heights[int(ball.pos.x // 1.5)] + ball.radius + 0.01 or s == ' ':
            velocity.y += up_force.y # 위쪽으로 속도 추가 (점프)
            is_jumping = True
            spin(2*up_force.y/(g.y*-1)) ##걸린시간을 구하는 식을 초기높이,최종높이,초기y속도, 중력가속도를 이용한 식으로 재구성 해야함//print((up_force.y+sqrt(up_force.y*up_force.y+2*g.y*h))/g.y*-1)#h는 변위
            #print(2*up_force.y/(g.y*-1))
            
     #체크포인트 설정
    if s == 'c':
        checkpoint.pos=ball.pos
        checkpoint.visible=True
        
    if s == 'esc':
        menuchang.visible=True
        menuchang.pos=vec(ball.pos.x,5,4)
        stop()
        
        
running = True

#일시정지
def stop():
    global running, last_dt, dt
    running = not running
    if running:
        dt = last_dt
    else:
        last_dt = dt
        dt = 0
    return
    

        
# 회전 함수 (공이 정확히 90도 회전)
def spin(time):
    # 회전 각도 설정 (90도 회전)
    target_angle = radians(90)
    
    # 회전 속도 계산 (총 시간 동안 90도 회전)
    angular_velocity = target_angle / time
    
    # 총 회전 각도 추적
    total_rotation = 0
    
    # 남은 시간 동안 회전하도록 설정
    t = 0
    while t < time:
        rate(100)
        
        
        # 각도 만큼 회전 (공이 z축을 기준으로 회전)
        rotation_angle = angular_velocity * dt
        
        # 남은 회전 각도를 넘지 않도록 보정
        if total_rotation + rotation_angle > target_angle:
            rotation_angle = target_angle - total_rotation # 남은 각도로 보정
        
        # 공을 회전
        ball.rotate(angle=-1*rotation_angle, axis=vector(0, 0, 1), origin=ball.pos)
        
        # 총 회전 각도 업데이트
        total_rotation += rotation_angle
        
        # 시간 업데이트
        t += dt
        
# 죽었을 시 터짐 표현
def explosion():
    global respawn_spot
    ball.visible = False  # 원래 공을 숨김

    # 공 조각 생성
    fragments = []
    for _ in range(30):  # 조각 수 조절 가능
        fragment = box(
            pos=ball.pos,
            size=vector(0.25, 0.25, 0.25),
            color=color.orange,
            velocity=vector((random() - 0.5) * 10, (random() - 0.5) * 10, (random() - 0.5) * 10),  # 퍼지는 속도를 작게 설정
        )
        fragments.append(fragment)

    t = 0
    ground_level = floor.pos.y + 0.1  # 바닥 높이 설정

    while t < 1:
        rate(100)
        for fragment in fragments:
            fragment.pos += fragment.velocity * dt
            fragment.velocity += vector(0, -9.8, 0) * dt  # 중력 적용
            
            # 조각이 바닥 아래로 내려가지 않도록 제한
            if fragment.pos.y < ground_level:
                fragment.pos.y = ground_level  # 바닥 위치에 고정
                fragment.velocity.y = 0
        t += dt

    # 파편 삭제 후 원래 공 다시 나타내기
    for fragment in fragments:
        fragment.visible = False  # 파편을 삭제합니다.
    fragments.clear()  # 파편 리스트 초기화
    ball.pos=checkpoint.pos
    ball.visible = True
    ball.clear_trail()



def ending(V):
    
    velocity = V
    g = vector(0, -60, 0) # 중력 가속도
    while mag(velocity) > 15:  # 속도가 거의 0에 가까워질 때까지 반복
        rate(30)
        velocity *= 0.8
        ball.pos += velocity * dt
    
    velocity = vector(0, 0, 0)
    g = vector(0, -60, 0) # 중력 가속도
    up_force = vector(0, 23.123456789, 0) # 위쪽으로 순간 가속도
    velocity.y += up_force.y
    
    # 회전 각도 설정 (270도 회전)
    target_angle = radians(270)
    
    # 회전 속도 계산 (총 시간 동안 270도 회전)
    angular_velocity = target_angle/(2*up_force.y/(g.y*-1))
    rotation_angle = angular_velocity * dt
    t=0
    while True:
        t+=0.05
        rate(50)
        ball.rotate(angle=-1*rotation_angle, axis=vector(0, 0, 1), origin=ball.pos)
        velocity.x = 15
        velocity += g * dt
        ball.pos += velocity * dt
        jinhangdobar.length= (ball.pos.x/((len(map_heights)-8)*1.5))*18*2
        scene.camera.pos = vector(ball.pos.x, 5, 15-t)
        if ball.pos.x>=len(map_heights)*1.5-12:
            text(text='GAME CLEAR', pos=vec(ball.pos.x,4,2.45),align='center', color=vec(1.000, 0.000, 0.000))
            explosion()
            break
        
count_end=0

# 키보드 입력 이벤트 설정
scene.bind('keydown', key_input)

# 카메라 고정
while True:

    rate(100)
    # x 방향 속도 증가
    if running:
        menuchang.visible=False
    
    velocity.x = 13.222125 # 일정한 속도로 이동하도록 설정
    
    # 위치 업데이트 (s = s + v * dt)
    ball.pos += velocity * dt
    jinhangdobar_base.pos.x=ball.pos.x
    jinhangdobar.pos.x=ball.pos.x-9
    garimmack.pos.x=ball.pos.x-11.5
    
    #진행도 업데이트
    jinhangdobar.length= (ball.pos.x/((len(map_heights)-6)*1.5))*18*2

    
    current_x_index = int(ball.pos.x // 1.5)
    
    if ball.pos.x>=(len(map_heights)*1.5)-22 and count_end==0:
        count_end =count_end+1
        ending(velocity)
        break
        
    
    if ball.pos.x <= 155:
        floor.color= phase1_color
    else if 155<=ball.pos.x <=300:
        floor.color= phase2_color
    else if 300<=ball.pos.x<=420:
        floor.color= phase3_color
    else if ball.pos.x>=420:
        floor.color= phase4_color
    
    # 바닥과 충돌 시
    if ball.pos.y <= floor.pos.y+ ball.radius:
        ball.pos.y = floor.pos.y+ ball.radius
        velocity.y=0
        
    elif ball.pos.y<=map_heights[current_x_index] + ball.radius:
       ball.pos.y= map_heights[current_x_index] + ball.radius
       velocity.y=0
    else:
        # 중력에 의한 속도 변화 (v = v + g * dt)
        velocity += g * dt
    #맵충돌
    if map_heights[current_x_index+1] != 0:
        if ball.pos.y < map_heights[current_x_index+1]:
            #text(text='GAME OVER', pos=vec(ball.pos.x,5,0),align='center', color=color.blue)
            #break
            ball.clear_trail()
            explosion()
            sleep(0.1)
            ball.clear_trail()
    #장애물충돌    
    if obstacle_heights[current_x_index]==1:
        if ball.pos.y <= obstacle_heights[current_x_index]+map_heights[current_x_index]-0.1:
            #text(text='GAME OVER', pos=vec(ball.pos.x,5,0),align='center', color=color.blue)
            #break
            ball.clear_trail()
            explosion()
            sleep(0.1)
            ball.clear_trail()
    #점프대충돌
    if jumper_heights[current_x_index]==1:
        if ball.pos.y <= jumper_heights[current_x_index]+map_heights[current_x_index]-0.5:
            velocity.y += up_force.y*sqrt(2) # 위쪽으로 속도 추가 (점프)
            count_spin=1
            #is_jumping = True
            #spin(2*up_force.y*1.5/(g.y*-1))            
            
    #천장 충돌
    if ball.pos.y >= 14-map_ceiling[current_x_index]:
        #text(text='GAME OVER', pos=vec(ball.pos.x,5,0),align='center', color=color.blue)
        #break
        ball.clear_trail()
        explosion()
        sleep(0.1)
        ball.clear_trail()
        
    # 카메라 설정
    scene.center = ball.pos
    if 300<=ball.pos.x<=420:
        scene.up=vec(0,-1,0)#상하좌우반전
    else:
        scene.up=vec(0,1,0)
    scene.camera.pos = vector(ball.pos.x, 5, 15)
"""
    if ball.pos.x >= len(map_heights)*1.5-10:
        scene.camera.pos=vector(len(map_heights)*1.5-10, 5, 15)
    else:
        scene.camera.pos = vector(ball.pos.x, 5, 15) # 카메라 위치 조정
"""

    
