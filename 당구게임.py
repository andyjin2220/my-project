Web VPython 3.2
from vpython import *

# 캔버스 설정
scene = canvas(title='포켓볼 게임', width=800, height=600, center=vector(0,0,0), background=color.white)

# 당구대 크기 설정
table_length = 24
table_width = 12
table_height = 0.2

# 당구대 테이블
table = box(pos=vector(0, -table_height/2, 0), size=vector(table_length, table_height, table_width), color=color.blue)

# 당구대 벽(레일) 설정
wall_thickness = 0.2
wall_height = 0.5

# 당구대의 각 벽 생성
wall1 = box(pos=vector(0, wall_height/2, table_width/2 + wall_thickness/2), size=vector(table_length + wall_thickness*2, wall_height, wall_thickness), color=color.gray(0.5))
wall2 = box(pos=vector(0, wall_height/2, -table_width/2 - wall_thickness/2), size=vector(table_length + wall_thickness*2, wall_height, wall_thickness), color=color.gray(0.5))
wall3 = box(pos=vector(table_length/2 + wall_thickness/2, wall_height/2, 0), size=vector(wall_thickness, wall_height, table_width + wall_thickness*2), color=color.gray(0.5))
wall4 = box(pos=vector(-table_length/2 - wall_thickness/2, wall_height/2, 0), size=vector(wall_thickness, wall_height, table_width + wall_thickness*2), color=color.gray(0.5))

# 빛 설정 (옵션)
distant_light(direction=vector(0, -1, 0), color=color.white)

# 당구공 설정
ball_radius = 0.3


# 흰공(0)
ballW = sphere(pos=vector(0, ball_radius, 0), radius=ball_radius, color=color.white)
ballW.velocity = vector(0, 0, 0)
ballW.mass = 1
ballW.crash_count = 0

# 노랑 공
ballY = sphere(pos=vector(8, ball_radius, -3), radius=ball_radius, color=color.yellow)
ballY.velocity = vector(0, 0, 0)
ballY.mass = 1
ballY.crash_count = 0

# 빨간 공
ballR = sphere(pos=vector(8, ball_radius, 3), radius=ball_radius, color=color.red)
ballR.velocity = vector(0, 0, 0)
ballR.mass = 1
ballR.crash_count = 0

# 카메라 설정 (당구대 위에서 바라보게 설정)
scene.camera.up = vector(0, 0, -1)

# 마찰 계수
friction_coefficient = vector(0.42, 0, 0.42)
mass = 1  # 공의 질량

# 공 이동 함수
def move():
    dt = 0.01
    force = scene.mouse.pos - ballW.pos
    acceleration = force / mass
    ballW.velocity = acceleration
    ballW.velocity.y = 0
    loc = scene.mouse.pos
    while mag(ballW.velocity) > 0.1:
        rate(100)
        ballW.pos += ballW.velocity * dt
        friction_force = -vector(friction_coefficient.x * ballW.velocity.x,
                                 friction_coefficient.y * ballW.velocity.y,
                                 friction_coefficient.z * ballW.velocity.z)
        ballW.velocity += friction_force * dt
        if mag(ballW.velocity) < 0.1:
            ballW.velocity = vector(0, 0, 0)
    calculate_score()

# 충돌 처리 함수
def collision(b1, b2, e):
    c = b1.pos - b2.pos
    c_hat = norm(c)
    dist = mag(c)
    v_relm = dot(b1.velocity - b2.velocity, c_hat)
    if v_relm > 0:
        return False

    if dist < b1.radius + b2.radius:
        j = -(1 + e) * v_relm
        j = j / (1 / b1.mass + 1 / b2.mass)
        b1.velocity = b1.velocity + j * c_hat / b1.mass
        b2.velocity = b2.velocity - j * c_hat / b2.mass
        b1.crash_count += 1
        b2.crash_count += 1
    else:
        return False

# 마우스 클릭 이벤트 바인딩
scene.bind('click', move)

# 벽 충돌 함수
def crash(b):
    global wall_crash
    if b.pos.x >= 12 - ball_radius:
        b.velocity.x = -b.velocity.x
        wall_crash += 1
    elif b.pos.x <= -1 * (12 - ball_radius):
        b.velocity.x = -b.velocity.x
        wall_crash += 1

    if b.pos.z >= 6 - ball_radius:
        b.velocity.z = -b.velocity.z
        wall_crash += 1
    elif b.pos.z <= -1 * (6 - ball_radius):
        b.velocity.z = -b.velocity.z
        wall_crash += 1

# 점수 계산 함수
def calculate_score():
    global scoreA
    if ballW.crash_count == 2:
        scoreA += 1
    print("Score A: ", scoreA)

# 시뮬레이션 루프
def simulation():
    global wall_crash
    global scoreA
    t = 0
    dt = 0.01
    e = 0.99

    while True:
        rate(100)
        collision(ballW, ballY, e)
        collision(ballW, ballR, e)
        collision(ballR, ballY, e)

        ballW.pos += ballW.velocity * dt
        ballY.pos += ballY.velocity * dt
        ballR.pos += ballR.velocity * dt

        friction_forceY = -vector(friction_coefficient.x * ballY.velocity.x,
                                  friction_coefficient.y * ballY.velocity.y,
                                  friction_coefficient.z * ballY.velocity.z)
        ballY.velocity += friction_forceY * dt
        if mag(ballY.velocity) < 0.1:
            ballY.velocity = vector(0, 0, 0)

        friction_forceR = -vector(friction_coefficient.x * ballR.velocity.x,
                                  friction_coefficient.y * ballR.velocity.y,
                                  friction_coefficient.z * ballR.velocity.z)
        ballR.velocity += friction_forceR * dt
        if mag(ballR.velocity) < 0.1:
            ballR.velocity = vector(0, 0, 0)

        crash(ballW)
        crash(ballY)
        crash(ballR)

        if mag(ballW.velocity) == 0 and mag(ballY.velocity) == 0 and mag(ballR.velocity) == 0:
            wall_crash = 0
            ballW.crash_count = 0
            ballR.crash_count = 0
            ballY.crash_count = 0

        t += dt

scoreA = 0
scoreB = 0

# 시뮬레이션 실행
simulation()
