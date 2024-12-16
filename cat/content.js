let img = null; // 이미지 요소
let imageShadow = null; // 그림자 요소
let animationFrameId = null; // 애니메이션 프레임 ID
let targetX = 0; // 목표 X 좌표
let targetY = 0; // 목표 Y 좌표
let speed = 10; // 이동 속도 (픽셀/프레임)
let imageSize = 150; // 이미지 크기
let flipped = false; // 좌우 반전 상태 (초기 값은 false, 즉 오른쪽을 보고 있음)

let isDragging = false; // 드래그 상태 체크
let offsetX = 0; // 마우스와 이미지의 X 오프셋
let offsetY = 0; // 마우스와 이미지의 Y 오프셋
let rotationAngle = 0; // 회전 각도
let rotationActive = false; // 회전 효과 활성화 여부

function createImage(url, size) {
  if (img) return; // 이미지가 이미 있으면 생성하지 않음

  img = document.createElement('img');
  img.src = url || 'https://via.placeholder.com/150'; // 기본 이미지 URL
  img.alt = 'Moving Image';
  img.style.position = 'fixed';
  img.style.top = '100px';
  img.style.left = '100px';
  img.style.zIndex = '9999'; // 이미지가 다른 요소보다 위에 표시되도록 설정
  img.style.width = `${size}px`; // 크기 적용
  img.style.height = `${size}px`; // 크기 적용
  img.style.transition = 'transform 0.2s ease'; // 부드러운 회전 효과
  document.body.appendChild(img);

  // 그림자 요소 생성
  imageShadow = document.createElement('div');
  imageShadow.style.position = 'absolute';
  imageShadow.style.top = '0';
  imageShadow.style.left = '0';
  imageShadow.style.width = `${size}px`;
  imageShadow.style.height = `${size / 3}px`; // 그림자를 더 납작하게 만듦
  imageShadow.style.background = 'rgba(0, 0, 0, 1)'; // 그림자 강도를 더 진하게
  imageShadow.style.borderRadius = '50%'; // 그림자를 둥글게 처리
  imageShadow.style.filter = 'blur(12px)'; // 더 강한 블러 효과로 그림자 처리
  imageShadow.style.zIndex = '9998'; // 그림자가 이미지 아래에 표시되도록 설정
  imageShadow.style.pointerEvents = 'none'; // 그림자가 클릭되지 않도록
  imageShadow.style.opacity = '0'; // 초기 상태에서 그림자는 보이지 않음
  document.body.appendChild(imageShadow);

  // 이미지 범위 내 클릭 시 드래그 시작
  img.addEventListener('mousedown', (e) => {
    const rect = img.getBoundingClientRect();
    if (e.clientX >= rect.left && e.clientX <= rect.right && e.clientY >= rect.top && e.clientY <= rect.bottom) {
      isDragging = true;
      rotationActive = true; // 드래그 시작 시 회전 효과 활성화
      offsetX = e.clientX - img.offsetLeft; // 마우스와 이미지의 X 오프셋
      offsetY = e.clientY - img.offsetTop;  // 마우스와 이미지의 Y 오프셋
      imageShadow.style.left = `${e.clientX - offsetX}px`;
      imageShadow.style.top = `${e.clientY - offsetY + size / 2}px`; // 그림자가 이미지 아래로 조금 내려가도록 설정
      img.style.transform = 'translateY(-15px)'; // 이미지를 살짝 위로 띄우기
      imageShadow.style.opacity = '1'; // 드래그할 때 그림자가 보이도록
      e.preventDefault(); // 기본 동작 방지 (다른 창 뜨는 문제 해결)
      startRotatingImage(); // 드래그 시작 시 회전 애니메이션 시작
    }
  });

  // 마우스 이동 이벤트 (드래그 중)
  document.addEventListener('mousemove', (e) => {
    if (isDragging) {
      img.style.left = `${e.clientX - offsetX}px`;
      img.style.top = `${e.clientY - offsetY}px`;

      // 그림자 위치 조정 (이미지와 동일하게 위치 조정)
      imageShadow.style.left = `${e.clientX - offsetX}px`;
      imageShadow.style.top = `${e.clientY - offsetY + size / 2}px`; // 그림자가 이미지 아래로 조금 내려가도록 설정
    }
  });

  // 마우스 놓기 이벤트
  document.addEventListener('mouseup', () => {
    isDragging = false;
    rotationActive = false; // 드래그 종료 시 회전 효과 비활성화
    img.style.transform = ''; // 이미지 원래 위치로 돌아가게 설정
    imageShadow.style.opacity = '0'; // 드래그 종료 시 그림자 숨기기
    stopRotatingImage(); // 회전 애니메이션 멈춤
  });
}

function startRotatingImage() {
  function animate() {
    if (!rotationActive) return; // 회전 효과가 활성화되지 않으면 종료

    rotationAngle = Math.sin(Date.now() / 200) * 15; // 시간에 따라 회전 각도 조정 (좌우로 흔드는 효과)
    img.style.transform = `translateY(-15px) rotate(${rotationAngle}deg)`; // 회전 효과 적용

    animationFrameId = requestAnimationFrame(animate); // 애니메이션 반복
  }

  if (!animationFrameId) {
    animationFrameId = requestAnimationFrame(animate); // 애니메이션 시작
  }
}

function stopRotatingImage() {
  cancelAnimationFrame(animationFrameId); // 애니메이션 종료
  animationFrameId = null; // 애니메이션 프레임 ID 초기화
}

function startMovingImage() {
  function animate() {
    if (!img) return;

    const currentX = parseInt(img.style.left, 10);
    const currentY = parseInt(img.style.top, 10);

    // 이동할 거리 계산
    const dx = targetX - currentX;
    const dy = targetY - currentY;

    // 목표에 도달하면 멈춤
    if (Math.abs(dx) <= speed && Math.abs(dy) <= speed) {
      img.style.left = `${targetX}px`;
      img.style.top = `${targetY}px`;
      cancelAnimationFrame(animationFrameId);
      animationFrameId = null;
      return;
    }

    // 새로운 위치 계산
    const angle = Math.atan2(dy, dx);
    const stepX = speed * Math.cos(angle);
    const stepY = speed * Math.sin(angle);

    img.style.left = `${currentX + stepX}px`;
    img.style.top = `${currentY + stepY}px`;

    // 이미지가 이동하는 방향에 따라 좌우 반전 적용
    if (dx > 0 && flipped) {
      flipped = false;
      img.style.transform = ''; // 정상 상태로 설정
    } else if (dx < 0 && !flipped) {
      flipped = true;
      img.style.transform = 'scaleX(-1)'; // 좌우 반전
    }

    animationFrameId = requestAnimationFrame(animate);
  }

  if (!animationFrameId) {
    animationFrameId = requestAnimationFrame(animate);
  }
}

function stopMovingImage() {
  if (animationFrameId) {
    cancelAnimationFrame(animationFrameId);
    animationFrameId = null;
  }
  if (img) {
    img.remove();
    imageShadow.remove(); // 그림자도 삭제
    img = null;
  }
}

// 클릭 시 이미지 이동
document.addEventListener('click', (event) => {
  if (img) {
    targetX = event.clientX - img.clientWidth / 2; // 이미지 중심 맞춤
    targetY = event.clientY - img.clientHeight / 2;
    startMovingImage();
  }
});

// 상태 변경 감지
chrome.storage.local.get(['imageActive', 'imageUrl', 'imageSize', 'speed'], (result) => {
  if (result.imageActive) {
    imageSize = result.imageSize || 150; // 크기 값 가져오기
    speed = result.speed || 10; // 속도 값 가져오기
    createImage(result.imageUrl, imageSize);
  }
});

// 상태 변경 감지
chrome.storage.onChanged.addListener((changes) => {
  if (changes.imageActive) {
    if (changes.imageActive.newValue) {
      chrome.storage.local.get('imageUrl', (result) => {
        createImage(result.imageUrl, imageSize);
      });
    } else {
      stopMovingImage();
      stopRotatingImage();
    }
  }

  if (changes.imageSize) {
    imageSize = changes.imageSize.newValue;
    if (img) {
      img.style.width = `${imageSize}px`;
      img.style.height = `${imageSize}px`;
      imageShadow.style.width = `${imageSize}px`;
      imageShadow.style.height = `${imageSize / 3}px`; // 그림자 크기 업데이트
    }
  }

  if (changes.speed) {
    speed = changes.speed.newValue;
  }
});
