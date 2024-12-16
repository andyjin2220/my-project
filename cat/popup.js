document.addEventListener('DOMContentLoaded', () => {
  const buttons = document.querySelectorAll('#header button');
  const content = document.getElementById('content');

  // 버튼 클릭 이벤트
  buttons.forEach((button) => {
    button.addEventListener('click', () => {
      // 모든 버튼에서 active 클래스 제거
      buttons.forEach((btn) => btn.classList.remove('active'));
      button.classList.add('active');

      // 버튼 ID에 따라 컨텐츠 변경
      if (button.id === 'btn-image') {
        showImageControls();
      } else {
        content.innerHTML = `<p>${button.textContent} 기능을 준비 중입니다.</p>`;
      }
    });
  });

  // 이미지 관련 컨트롤 표시
  function showImageControls() {
    content.innerHTML = `
      <div class="control-group">
        <label for="imageUrl">이미지 URL:</label>
        <input type="text" id="imageUrl" placeholder="이미지 URL 입력">
      </div>
      <div class="control-group">
        <label for="imageSizeSlider">이미지 크기:</label>
        <input type="range" id="imageSizeSlider" min="50" max="300" step="10">
      </div>
      <div class="control-group">
        <label for="speedSlider">속도:</label>
        <input type="range" id="speedSlider" min="1" max="20" step="1">
      </div>
      <button id="toggleButton">Activate</button>
    `;

    // 저장된 설정 불러오기
    chrome.storage.local.get(['imageUrl', 'imageSize', 'speed', 'imageActive'], (result) => {
      document.getElementById('imageUrl').value = result.imageUrl || '';
      document.getElementById('imageSizeSlider').value = result.imageSize || 150;
      document.getElementById('speedSlider').value = result.speed || 10;
      document.getElementById('toggleButton').textContent = result.imageActive ? 'Deactivate' : 'Activate';
    });

    // 설정 저장 이벤트
    document.getElementById('imageUrl').addEventListener('input', (event) => {
      chrome.storage.local.set({ imageUrl: event.target.value });
    });

    document.getElementById('imageSizeSlider').addEventListener('input', (event) => {
      chrome.storage.local.set({ imageSize: event.target.value });
    });

    document.getElementById('speedSlider').addEventListener('input', (event) => {
      chrome.storage.local.set({ speed: event.target.value });
    });

    document.getElementById('toggleButton').addEventListener('click', () => {
      chrome.storage.local.get('imageActive', (result) => {
        const newState = !result.imageActive;
        chrome.storage.local.set({ imageActive: newState });
        document.getElementById('toggleButton').textContent = newState ? 'Deactivate' : 'Activate';
      });
    });
  }

  // 초기 화면 설정
  content.innerHTML = '<p>기능을 선택하세요.</p>';
});
