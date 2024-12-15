console.log("Content script loaded");

function handleKeydown(event) {
  console.log("키가 눌렸습니다:", event.key);

  // 랜덤 색상 생성
  const randomColor = `rgb(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)})`;
  console.log("변경된 색상:", randomColor);

  // 배경색 변경
  document.body.style.backgroundColor = randomColor;
  document.body.style.setProperty('background-color', randomColor, 'important');
}

// 활성화 상태 관리 함수
function updateState() {
  chrome.storage.local.get('extensionActive', (result) => {
    const isActive = result.extensionActive || false;
    console.log("Extension active state:", isActive);

    if (isActive) {
      // 활성화 상태: 키 이벤트 리스너 추가
      document.addEventListener('keydown', handleKeydown);
    } else {
      // 비활성화 상태: 기존 키 이벤트 리스너 제거
      document.removeEventListener('keydown', handleKeydown);
      document.body.style.backgroundColor = 'white'; // 배경색 초기화
    }
  });
}

// 상태 변경을 지속적으로 모니터링
chrome.storage.onChanged.addListener((changes) => {
  if (changes.extensionActive) {
    updateState();
  }
});

// 초기 상태 설정
updateState();
