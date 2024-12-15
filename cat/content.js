// 이미지 이동 애니메이션 관리
let img = null; // 이미지 요소
let animationFrameId = null; // 애니메이션 프레임 ID
let targetX = 0; // 목표 X 좌표
let targetY = 0; // 목표 Y 좌표
let speed = 10; // 이동 속도 (픽셀/프레임)
let imageSize = 150; // 이미지 크기

function createImage(url, size) {
  if (img) return; // 이미지가 이미 있으면 생성하지 않음

  img = document.createElement('img');
  img.src = url || 'https://via.placeholder.com/150'; // 기본 이미지 URL
  img.alt = 'Moving Image';
  img.style.position = 'fixed';
  img.style.top = '100px';
  img.style.left = '100px';
  img.style.zIndex = '1000';
  img.style.width = `${size}px`; // 크기 적용
  img.style.height = `${size}px`; // 크기 적용
  document.body.appendChild(img);
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
    img = null;
  }
}

// 마우스 클릭 이벤트 리스너
document.addEventListener('click', (event) => {
  if (img) {
    targetX = event.clientX - img.clientWidth / 2; // 이미지 중심 맞춤
    targetY = event.clientY - img.clientHeight / 2;
    startMovingImage();
  }
});

// 활성화 상태 확인 및 이미지 생성
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
    }
  }

  // 크기나 속도 변경시 반영
  if (changes.imageSize) {
    imageSize = changes.imageSize.newValue;
    if (img) {
      img.style.width = `${imageSize}px`;
      img.style.height = `${imageSize}px`;
    }
  }

  if (changes.speed) {
    speed = changes.speed.newValue;
  }
});
